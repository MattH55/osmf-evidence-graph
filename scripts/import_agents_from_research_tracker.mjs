#!/usr/bin/env node
/**
 * Import therapeutic agents + treats_candidate_for claims from
 * osmf-research-tracker data/therapeutic_agents.json into the evidence graph.
 *
 * Usage:
 *   TRACKER_PATH=/path/to/osmf-research-tracker node scripts/import_agents_from_research_tracker.mjs
 *   npm run import:tracker:agents
 *
 * Idempotent: clears prior agent-* entity files and agent-*-treats-* claims, then rewrites.
 * Does NOT invent A/B evidence tiers or copy dosing/safety as clinical advice.
 * Does NOT import clinical_trials bulk JSON.
 */
"use strict";

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, "..");
const ENTITIES_DIR = path.join(ROOT, "data", "entities");
const CLAIMS_DIR = path.join(ROOT, "data", "claims");
const PROVENANCE_PATH = path.join(ROOT, "data", "import-provenance.json");

const TRACKER_BASE = "https://research.opensourcemed.info";

const CONDITION_MAP = {
  "long covid": "long-covid",
  pacvs: "pacvs",
  "me/cfs": "me-cfs",
  pots: "pots",
  mcas: "mcas",
  lyme: "lyme",
  "gulf war illness": "gulf-war-illness",
};

const EVIDENCE_TIER_MAP = {
  moderate: "C",
  preliminary: "D",
  anecdotal: "D",
};

const LIMITATIONS =
  "Auto-imported from OSMF Research Tracker therapeutic_agents.json. Evidence Level is tracker metadata, not an OSMF curator grade. Not medical advice; Desk does not provide dosing. Inclusion as a treats_candidate_for claim does not imply efficacy, safety, or clinical recommendation.";

const SUMMARY_DISCLAIMER =
  "See tracker agent page / linked studies; Desk does not provide dosing.";

const PMID_RE =
  /(?:PMID[:\s]*|#?\s*|pubmed\.ncbi\.nlm\.nih\.gov\/)(\d{5,8})\b/gi;
const NCT_RE = /\b(NCT\d{8})\b/gi;

function resolveTrackerPath() {
  if (process.env.TRACKER_PATH) {
    return path.resolve(process.env.TRACKER_PATH);
  }
  const candidates = [
    path.resolve(ROOT, "..", "osmf-research-tracker"),
    "/workspace/osmf-research-tracker",
  ];
  for (const c of candidates) {
    if (fs.existsSync(path.join(c, "data", "therapeutic_agents.json"))) {
      return c;
    }
  }
  throw new Error(
    "Could not find osmf-research-tracker with data/therapeutic_agents.json. Set TRACKER_PATH."
  );
}

function truncate(str, max) {
  const s = String(str || "").trim();
  if (s.length <= max) return s;
  return s.slice(0, max - 1).trimEnd() + "…";
}

function slugify(text) {
  let s = String(text || "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();
  s = s.replace(/[^a-z0-9\s-]/g, "");
  s = s.replace(/[\s_]+/g, "-");
  s = s.replace(/-{2,}/g, "-");
  return s.replace(/^-+|-+$/g, "") || "unnamed";
}


function encodePubchemUrl(raw) {
  const s = String(raw || "").trim();
  if (!s || !/^https?:\/\//i.test(s)) return null;
  try {
    const u = new URL(s);
    // Rebuild search-style PubChem hash queries with full percent-encoding
    if (u.hash && u.hash.startsWith("#query=")) {
      const q = decodeURIComponent(u.hash.slice("#query=".length));
      u.hash = "#query=" + encodeURIComponent(q);
    }
    // Also encode path segments that may contain unsafe chars (rare)
    const href = u.toString();
    // Final ASCII-only check for ajv format:uri
    if (!/^[\x00-\x7F]*$/.test(href)) {
      // Fallback: encode each non-ASCII char
      return href.replace(/[^\x00-\x7F]/g, (ch) =>
        encodeURIComponent(ch)
      );
    }
    return href;
  } catch {
    try {
      return encodeURI(s);
    } catch {
      return null;
    }
  }
}

function writeJson(filePath, obj) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(obj, null, 2) + "\n");
}

function isAgentEntityFile(name) {
  return /^agent-.+\.json$/.test(name);
}

function isAgentClaimFile(name) {
  return /^agent-.+-treats-.+\.json$/.test(name);
}

function parseAliases(raw) {
  if (Array.isArray(raw)) {
    return [
      ...new Set(
        raw
          .map((a) => String(a || "").trim())
          .filter((a) => a.length > 0)
      ),
    ];
  }
  if (typeof raw === "string" && raw.trim()) {
    return [
      ...new Set(
        raw
          .split(/[;|,]/)
          .map((a) => a.trim())
          .filter(Boolean)
      ),
    ];
  }
  return [];
}

function mapCondition(raw) {
  const s = String(raw || "").trim();
  if (!s) return null;
  const lower = s.toLowerCase();
  if (CONDITION_MAP[lower]) return CONDITION_MAP[lower];
  if (lower.startsWith("other post-viral")) return "other-post-viral";
  // Prefix matches for slight wording drift
  for (const [key, slug] of Object.entries(CONDITION_MAP)) {
    if (lower === key || lower.startsWith(key + " ") || lower.startsWith(key + "–") || lower.startsWith(key + "-")) {
      return slug;
    }
  }
  return null;
}

function mapEvidenceTier(level) {
  const key = String(level || "")
    .trim()
    .toLowerCase();
  return EVIDENCE_TIER_MAP[key] || "D";
}

function looksLikeDosingOrSafetyAdvice(text) {
  const t = String(text || "");
  return /\b(dose|dosing|mg\/|ml\/|take\s+\d|prescrib|contraindicat|adverse event|side effect)\b/i.test(
    t
  );
}

function buildSummary(agent) {
  const mech = String(agent["Proposed Mechanism"] || "").trim();
  const notes = String(agent["Clinical Notes"] || "").trim();
  const parts = [];
  if (mech && !looksLikeDosingOrSafetyAdvice(mech)) {
    parts.push(mech);
  } else if (mech) {
    parts.push("Mechanism notes available on tracker page (neutral summary omitted).");
  }
  if (notes) {
    // Prefer high-level investigational framing; drop explicit dosing sentences
    const cleaned = notes
      .split(/(?<=[.!?])\s+/)
      .filter((sent) => !looksLikeDosingOrSafetyAdvice(sent))
      .join(" ")
      .trim();
    if (cleaned) parts.push(cleaned);
  }
  let summary = parts.join(" ").trim();
  if (!summary) {
    summary = `Therapeutic agent candidate listed in OSMF Research Tracker. ${SUMMARY_DISCLAIMER}`;
  } else {
    summary = `${summary} ${SUMMARY_DISCLAIMER}`;
  }
  return truncate(summary, 500);
}

function loadSlugMaps(trackerRoot) {
  const nameToSlug = new Map();
  const slugFiles = [
    path.join(trackerRoot, "data", "vocab", "agent-slugs.json"),
    path.join(trackerRoot, "data", "vocab", "agent-slugs-flagged.json"),
  ];
  for (const fp of slugFiles) {
    if (!fs.existsSync(fp)) continue;
    const rows = JSON.parse(fs.readFileSync(fp, "utf8"));
    for (const row of rows) {
      if (row.display_name && row.slug) {
        nameToSlug.set(row.display_name, row.slug);
      }
    }
  }
  return nameToSlug;
}

function allocateSlugs(agents, nameToSlug) {
  const used = new Map(); // slug -> name
  const result = new Map(); // name -> slug

  // Prefer vocab slugs first (stable)
  for (const agent of agents) {
    const name = agent["Therapeutic Agent"];
    if (!name) continue;
    const preferred = nameToSlug.get(name);
    if (preferred) {
      used.set(preferred, name);
      result.set(name, preferred);
    }
  }

  for (const agent of agents) {
    const name = agent["Therapeutic Agent"];
    if (!name || result.has(name)) continue;
    let base = slugify(name);
    let slug = base;
    let n = 2;
    while (used.has(slug) && used.get(slug) !== name) {
      slug = `${base}-${n}`;
      n++;
    }
    used.set(slug, name);
    result.set(name, slug);
  }

  return result;
}

function extractPmids(agent) {
  const found = new Set();
  const bags = [
    ...(agent["Key Studies / References"] || []),
    ...(agent.studies || []),
  ];
  for (const item of bags) {
    if (item && typeof item === "object") {
      const pmid = item.pmid || item.PMID || item.pubmed_id;
      if (pmid && /^\d+$/.test(String(pmid))) found.add(String(pmid));
      for (const v of Object.values(item)) {
        if (typeof v === "string") {
          for (const m of v.matchAll(PMID_RE)) found.add(m[1]);
        }
      }
    } else if (typeof item === "string") {
      for (const m of item.matchAll(PMID_RE)) found.add(m[1]);
    }
  }
  return [...found];
}

function extractNcts(agent) {
  const found = new Set();
  for (const t of agent.trials || []) {
    if (t && typeof t === "object" && t.nct_id) {
      const nct = String(t.nct_id).toUpperCase();
      if (/^NCT\d{8}$/.test(nct)) found.add(nct);
    } else if (typeof t === "string") {
      for (const m of t.matchAll(NCT_RE)) found.add(m[1].toUpperCase());
    }
  }
  const bags = [
    ...(agent["Key Studies / References"] || []),
    ...(agent.studies || []),
    agent["Ongoing Research"],
  ];
  for (const item of bags) {
    const text =
      typeof item === "string"
        ? item
        : item && typeof item === "object"
          ? JSON.stringify(item)
          : "";
    for (const m of String(text).matchAll(NCT_RE)) {
      found.add(m[1].toUpperCase());
    }
  }
  return [...found];
}

function agentPageExists(trackerRoot, slug) {
  const dir = path.join(trackerRoot, "agents", slug);
  return (
    fs.existsSync(path.join(dir, "index.html")) ||
    (fs.existsSync(dir) && fs.statSync(dir).isDirectory())
  );
}

function buildAgentUrl(trackerRoot, slug) {
  if (agentPageExists(trackerRoot, slug)) {
    return {
      rel: "tracker",
      href: `${TRACKER_BASE}/agents/${slug}/`,
    };
  }
  // Prefer candidate-therapeutics catalog, then agents hub
  const candidateLocal = path.join(trackerRoot, "candidate-therapeutics.html");
  if (fs.existsSync(candidateLocal)) {
    return {
      rel: "tracker",
      href: `${TRACKER_BASE}/candidate-therapeutics.html`,
    };
  }
  return {
    rel: "tracker",
    href: `${TRACKER_BASE}/agents.html`,
  };
}

function buildSources(trackerUrl, pmids, ncts) {
  const sources = [
    {
      type: "osmf_page",
      value: trackerUrl.href,
      label: "OSMF Research Tracker (therapeutic agent)",
    },
  ];
  for (const pmid of pmids.slice(0, 10)) {
    sources.push({ type: "pmid", value: pmid });
  }
  for (const nct of ncts.slice(0, 10)) {
    sources.push({ type: "nct", value: nct });
  }
  return sources;
}

function main() {
  const trackerRoot = resolveTrackerPath();
  const agentsPath = path.join(
    trackerRoot,
    "data",
    "therapeutic_agents.json"
  );
  const now = new Date().toISOString();
  const importDate = now.slice(0, 10);

  console.log(`Tracker path: ${trackerRoot}`);
  console.log(`Import timestamp: ${now}`);

  let removedEntities = 0;
  let removedClaims = 0;
  for (const f of fs.readdirSync(ENTITIES_DIR)) {
    if (isAgentEntityFile(f)) {
      fs.unlinkSync(path.join(ENTITIES_DIR, f));
      removedEntities++;
    }
  }
  for (const f of fs.readdirSync(CLAIMS_DIR)) {
    if (isAgentClaimFile(f)) {
      fs.unlinkSync(path.join(CLAIMS_DIR, f));
      removedClaims++;
    }
  }
  if (removedEntities || removedClaims) {
    console.log(
      `Cleared prior agent import: ${removedEntities} entities, ${removedClaims} claims`
    );
  }

  const payload = JSON.parse(fs.readFileSync(agentsPath, "utf8"));
  const agents = Array.isArray(payload.agents) ? payload.agents : [];
  console.log(`Source agents: ${agents.length}`);

  const nameToSlug = loadSlugMaps(trackerRoot);
  const allocated = allocateSlugs(agents, nameToSlug);

  let agentCount = 0;
  let claimCount = 0;
  let linkedPages = 0;
  let fallbackUrls = 0;
  const unknownConditions = new Map();
  const skippedNoName = [];

  for (const agent of agents) {
    const name = String(agent["Therapeutic Agent"] || "").trim();
    if (!name) {
      skippedNoName.push(agent);
      continue;
    }

    const slug = allocated.get(name);
    if (!slug || !/^[a-z0-9-]+$/.test(slug)) {
      console.warn(`SKIP agent with invalid slug: ${name} → ${slug}`);
      continue;
    }

    const aliases = parseAliases(agent.aliases).filter(
      (a) => a.toLowerCase() !== name.toLowerCase()
    );
    const trackerUrl = buildAgentUrl(trackerRoot, slug);
    if (trackerUrl.href.includes(`/agents/${slug}/`)) linkedPages++;
    else fallbackUrls++;

    const externalIds = [];
    const pubchemRaw = String(agent.PubChem || "").trim();
    const pubchem = encodePubchemUrl(pubchemRaw);
    if (pubchem) {
      externalIds.push({
        system: "other",
        value: pubchem,
        url: pubchem,
      });
    } else if (pubchemRaw) {
      // Keep non-URI strings as value-only (no url field — schema format:uri)
      externalIds.push({
        system: "other",
        value: truncate(pubchemRaw, 500),
      });
    }

    const entity = {
      id: `osmf:agent:${slug}`,
      type: "agent",
      label: name,
      aliases,
      summary: buildSummary(agent),
      external_ids: externalIds,
      urls: [trackerUrl],
      status: "active",
      updated_at: now,
    };

    writeJson(path.join(ENTITIES_DIR, `agent-${slug}.json`), entity);
    agentCount++;

    const pmids = extractPmids(agent);
    const ncts = extractNcts(agent);
    const sources = buildSources(trackerUrl, pmids, ncts);
    const tier = mapEvidenceTier(agent["Evidence Level"]);

    const conditions = Array.isArray(agent["Primary Conditions"])
      ? agent["Primary Conditions"]
      : agent["Primary Conditions"]
        ? [agent["Primary Conditions"]]
        : [];

    const seenCond = new Set();
    for (const rawCond of conditions) {
      const condSlug = mapCondition(rawCond);
      if (!condSlug) {
        const key = String(rawCond);
        unknownConditions.set(key, (unknownConditions.get(key) || 0) + 1);
        continue;
      }
      if (seenCond.has(condSlug)) continue;
      seenCond.add(condSlug);

      const claim = {
        id: `osmf:claim:agent-${slug}-treats-${condSlug}`,
        subject_id: `osmf:agent:${slug}`,
        predicate: "treats_candidate_for",
        object_id: `osmf:condition:${condSlug}`,
        evidence_tier: tier,
        sources,
        limitations: LIMITATIONS,
        status: "draft",
        reviewed_by: "tracker-import-bot",
        reviewed_at: now,
        license: "CC-BY-4.0",
      };

      writeJson(
        path.join(CLAIMS_DIR, `agent-${slug}-treats-${condSlug}.json`),
        claim
      );
      claimCount++;
    }
  }

  if (unknownConditions.size) {
    console.warn("Unknown Primary Conditions (skipped):");
    for (const [k, v] of [...unknownConditions.entries()].sort()) {
      console.warn(`  ${v}× ${k}`);
    }
  }
  if (skippedNoName.length) {
    console.warn(`Skipped ${skippedNoName.length} rows with empty Therapeutic Agent`);
  }

  // Merge agent counts into import-provenance.json
  let provenance = {};
  if (fs.existsSync(PROVENANCE_PATH)) {
    try {
      provenance = JSON.parse(fs.readFileSync(PROVENANCE_PATH, "utf8"));
    } catch (_) {
      provenance = {};
    }
  }
  provenance.agents_imported_at = now;
  provenance.agents_import_date = importDate;
  provenance.tracker_path = provenance.tracker_path || trackerRoot;
  provenance.counts = {
    ...(provenance.counts || {}),
    agents: agentCount,
    agent_claims: claimCount,
  };
  provenance.agent_import = {
    source: "data/therapeutic_agents.json",
    linked_agent_pages: linkedPages,
    fallback_urls: fallbackUrls,
    unknown_conditions: Object.fromEntries(unknownConditions),
    notes:
      "treats_candidate_for claims are draft; Evidence Level mapped Moderate→C, Preliminary/Anecdotal→D. No A/B. No dosing copied as advice. clinical_trials bulk JSON not imported.",
  };
  writeJson(PROVENANCE_PATH, provenance);

  console.log(
    `Wrote ${agentCount} agents, ${claimCount} treats_candidate_for claims`
  );
  console.log(
    `URLs: ${linkedPages} agent pages, ${fallbackUrls} catalog fallbacks`
  );
  console.log(`Provenance updated: data/import-provenance.json`);
}

main();
