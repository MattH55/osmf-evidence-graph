#!/usr/bin/env node
/**
 * Import clinical trials + studied_in claims from
 * osmf-research-tracker clinical_trials/data/clinical_trials_current.json
 * into the evidence graph.
 *
 * Usage:
 *   TRACKER_PATH=/path/to/osmf-research-tracker node scripts/import_trials_from_research_tracker.mjs
 *   npm run import:tracker:trials
 *
 * Idempotent: clears prior trial-nct-* entities and trial/agent studied_in claim
 * files matching this importer's patterns, then rewrites.
 *
 * Does NOT invent efficacy outcomes or treats_candidate_for edges.
 * Structural studied_in only (tier C, draft, registration-link limitations).
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

const CTGOV = "https://clinicaltrials.gov/study";

const LIMITATIONS =
  "Auto-imported from OSMF Research Tracker clinical_trials JSON. Structural registration link only — not an efficacy grade. Inclusion does not imply study quality, enrollment completeness, or clinical applicability.";

/** mapped_conditions / text → condition slug */
const MAPPED_CONDITION = {
  "long covid / pasc": "long-covid",
  "long covid": "long-covid",
  pasc: "long-covid",
  "me/cfs": "me-cfs",
  "me-cfs": "me-cfs",
};

const TEXT_CONDITION_PATTERNS = [
  {
    slug: "long-covid",
    re: /\blong[\s-]?covid\b|\bpasc\b|post[\s-]?acute[\s-]?(covid|sequelae)|post[\s-]?covid/i,
  },
  {
    slug: "me-cfs",
    re: /\bme\/cfs\b|\bmyalgic encephalomyelitis\b|\bchronic fatigue syndrome\b|\bcfs\b/i,
  },
  {
    slug: "pots",
    re: /\bpots\b|postural orthostatic tachycardia|orthostatic tachycardia syndrome/i,
  },
  {
    slug: "mcas",
    re: /\bmcas\b|mast cell activation/i,
  },
  {
    slug: "lyme",
    re: /\blyme\b|borrelia|ptlds|post[\s-]?treatment lyme/i,
  },
  {
    slug: "pacvs",
    re: /\bpacvs\b|post[\s-]?acute covid[\s-]?19 vaccination|post[\s-]?vaccination syndrome/i,
  },
  {
    slug: "gulf-war-illness",
    re: /\bgulf war illness\b|\bgulf war syndrome\b|\bgwi\b/i,
  },
  {
    slug: "other-post-viral",
    re: /\bother post[\s-]?viral\b|\bpost[\s-]?viral syndrome\b|\bpost[\s-]?infectious syndrome\b/i,
  },
];

function resolveTrackerPath() {
  if (process.env.TRACKER_PATH) {
    return path.resolve(process.env.TRACKER_PATH);
  }
  const candidates = [
    path.resolve(ROOT, "..", "osmf-research-tracker"),
    "/workspace/osmf-research-tracker",
  ];
  for (const c of candidates) {
    if (
      fs.existsSync(
        path.join(c, "clinical_trials", "data", "clinical_trials_current.json")
      )
    ) {
      return c;
    }
  }
  throw new Error(
    "Could not find osmf-research-tracker with clinical_trials/data/clinical_trials_current.json. Set TRACKER_PATH."
  );
}

function truncate(str, max) {
  const s = String(str || "").trim();
  if (s.length <= max) return s;
  return s.slice(0, max - 1).trimEnd() + "…";
}

function slugify(text) {
  return (
    String(text || "")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .trim()
      .replace(/[/+,()]/g, "-")
      .replace(/[^a-z0-9\s-]/g, "")
      .replace(/[\s_]+/g, "-")
      .replace(/-{2,}/g, "-")
      .replace(/^-+|-+$/g, "") || "unnamed"
  );
}

function normalizeNct(raw) {
  const s = String(raw || "")
    .trim()
    .toUpperCase();
  const m = s.match(/^NCT(\d{8})$/);
  if (!m) return null;
  return `NCT${m[1]}`;
}

function nctSlug(nct) {
  // schema requires lowercase: osmf:trial:nct-05350774
  return `nct-${nct.slice(3).toLowerCase()}`;
}

function writeJson(filePath, obj) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(obj, null, 2) + "\n");
}

function isTrialEntityFile(name) {
  return /^trial-nct-\d+\.json$/.test(name);
}

function isTrialConditionClaimFile(name) {
  return /^trial-nct-\d+-studied-.+\.json$/.test(name);
}

function isAgentTrialClaimFile(name) {
  return /^agent-.+-studied-in-nct-\d+\.json$/.test(name);
}

function loadExistingAgents() {
  const bySlug = new Map(); // slug -> id
  const byNorm = new Map(); // slugify(label|alias) -> id
  const tokenKey = new Map(); // sorted-token key -> id

  for (const f of fs.readdirSync(ENTITIES_DIR)) {
    if (!f.startsWith("agent-") || !f.endsWith(".json")) continue;
    const e = JSON.parse(fs.readFileSync(path.join(ENTITIES_DIR, f), "utf8"));
    if (e.type !== "agent" || !e.id?.startsWith("osmf:agent:")) continue;
    const slug = e.id.slice("osmf:agent:".length);
    bySlug.set(slug, e.id);
    const norms = [e.label, ...(e.aliases || [])].filter(Boolean).map(slugify);
    for (const n of norms) {
      if (n && !byNorm.has(n)) byNorm.set(n, e.id);
      const tk = n.split("-").filter(Boolean).sort().join("-");
      if (tk && !tokenKey.has(tk)) tokenKey.set(tk, e.id);
    }
  }
  return { bySlug, byNorm, tokenKey };
}

function resolveAgentId(name, index) {
  const raw = String(name || "").trim();
  if (!raw) return null;
  const s = slugify(raw);
  if (index.bySlug.has(s)) return index.bySlug.get(s);
  if (index.byNorm.has(s)) return index.byNorm.get(s);

  // "Foo (Bar Baz)" → try inside/outside parens
  const paren = raw.match(/^(.+?)\s*\((.+)\)\s*$/);
  if (paren) {
    for (const part of [paren[1], paren[2]]) {
      const ps = slugify(part);
      if (index.bySlug.has(ps)) return index.bySlug.get(ps);
      if (index.byNorm.has(ps)) return index.byNorm.get(ps);
    }
  }

  const tk = s.split("-").filter(Boolean).sort().join("-");
  if (tk && index.tokenKey.has(tk)) return index.tokenKey.get(tk);

  return null;
}

function mapMappedCondition(raw) {
  const key = String(raw || "")
    .trim()
    .toLowerCase();
  if (!key) return null;
  if (/unspecified|overlap/i.test(key)) return null;
  if (MAPPED_CONDITION[key]) return MAPPED_CONDITION[key];
  for (const [k, slug] of Object.entries(MAPPED_CONDITION)) {
    if (key === k || key.startsWith(k + " ") || key.startsWith(k + "/")) {
      return slug;
    }
  }
  return null;
}

function detectConditions(trial) {
  const found = new Set();
  for (const raw of trial.mapped_conditions || []) {
    const slug = mapMappedCondition(raw);
    if (slug) found.add(slug);
  }
  const bag = [
    ...(trial.conditions_raw || []),
    trial.title || "",
    ...(trial.relevance_tags || []),
    ...(trial.mapped_conditions || []),
  ].join(" | ");
  for (const { slug, re } of TEXT_CONDITION_PATTERNS) {
    if (re.test(bag)) found.add(slug);
  }
  return [...found];
}

function trialMentionsSeed(trial) {
  return detectConditions(trial).length > 0;
}

function ctgovUrl(nct, fallback) {
  if (fallback && /^https?:\/\//i.test(fallback)) return fallback;
  return `${CTGOV}/${nct}`;
}

function buildSummary(trial) {
  const status = String(trial.status || "UNKNOWN").replace(/_/g, " ");
  const phase = String(trial.phase || "NA");
  const conds = [
    ...(trial.mapped_conditions || []),
    ...(trial.conditions_raw || []),
  ]
    .filter((c) => c && !/unspecified|overlap/i.test(c))
    .slice(0, 4);
  const condSnippet = conds.length
    ? conds.join("; ")
    : "conditions per ClinicalTrials.gov registration";
  const enroll =
    trial.enrollment != null && trial.enrollment !== ""
      ? ` Enrollment listed: ${trial.enrollment}.`
      : "";
  return truncate(
    `Status: ${status}. Phase: ${phase}. Conditions: ${condSnippet}.${enroll} Registration metadata only; not an efficacy assessment.`,
    500
  );
}

function main() {
  const trackerRoot = resolveTrackerPath();
  const trialsPath = path.join(
    trackerRoot,
    "clinical_trials",
    "data",
    "clinical_trials_current.json"
  );
  const now = new Date().toISOString();
  const importDate = now.slice(0, 10);

  console.log(`Tracker path: ${trackerRoot}`);
  console.log(`Import timestamp: ${now}`);

  let removedEntities = 0;
  let removedClaims = 0;
  for (const f of fs.readdirSync(ENTITIES_DIR)) {
    if (isTrialEntityFile(f)) {
      fs.unlinkSync(path.join(ENTITIES_DIR, f));
      removedEntities++;
    }
  }
  for (const f of fs.readdirSync(CLAIMS_DIR)) {
    if (isTrialConditionClaimFile(f) || isAgentTrialClaimFile(f)) {
      fs.unlinkSync(path.join(CLAIMS_DIR, f));
      removedClaims++;
    }
  }
  if (removedEntities || removedClaims) {
    console.log(
      `Cleared prior trial import: ${removedEntities} entities, ${removedClaims} claims`
    );
  }

  const payload = JSON.parse(fs.readFileSync(trialsPath, "utf8"));
  const trials = Array.isArray(payload.trials) ? payload.trials : [];
  console.log(`Source trials: ${trials.length} (last_run=${payload.last_run || "n/a"})`);

  const agentIndex = loadExistingAgents();
  console.log(`Existing agent entities: ${agentIndex.bySlug.size}`);

  // Optional filter via env for CI / oversized PRs
  const filterMode = (process.env.TRIALS_IMPORT_FILTER || "seed").toLowerCase();
  // seed = mention seed conditions (default)
  // large = recruiting/completed-ish + enrollment>=50 among seed
  // all-seed-mapped = only mapped Long COVID / ME/CFS

  let trialCount = 0;
  let conditionClaimCount = 0;
  let agentClaimCount = 0;
  let skippedNoNct = 0;
  let skippedFilter = 0;
  let agentLinkMisses = 0;
  const conditionHitCounts = new Map();
  const filterStats = {
    mode: filterMode,
    source_total: trials.length,
    seed_mention: 0,
    imported: 0,
  };

  for (const trial of trials) {
    const nct = normalizeNct(trial.nct_id);
    if (!nct) {
      skippedNoNct++;
      continue;
    }

    const conditions = detectConditions(trial);
    if (conditions.length === 0) {
      skippedFilter++;
      continue;
    }
    filterStats.seed_mention++;

    if (filterMode === "large") {
      const st = String(trial.status || "").toUpperCase();
      const okStatus =
        st.includes("RECRUIT") ||
        st === "COMPLETED" ||
        st === "ENROLLING_BY_INVITATION" ||
        st === "ACTIVE_NOT_RECRUITING";
      const enroll = Number(trial.enrollment) || 0;
      if (!okStatus || enroll < 50) {
        skippedFilter++;
        continue;
      }
    } else if (filterMode === "all-seed-mapped") {
      const mappedOnly = (trial.mapped_conditions || [])
        .map(mapMappedCondition)
        .filter(Boolean);
      if (mappedOnly.length === 0) {
        skippedFilter++;
        continue;
      }
    }

    const slug = nctSlug(nct);
    const href = ctgovUrl(nct, trial.link);
    const label =
      truncate(trial.title || nct, 200) || nct;

    const entity = {
      id: `osmf:trial:${slug}`,
      type: "trial",
      label,
      aliases: [],
      summary: buildSummary(trial),
      external_ids: [
        {
          system: "nct",
          value: nct,
          url: href,
        },
      ],
      urls: [
        {
          rel: "other",
          href,
        },
      ],
      status: "active",
      updated_at: now,
    };

    writeJson(path.join(ENTITIES_DIR, `trial-${slug}.json`), entity);
    trialCount++;
    filterStats.imported++;

    const sources = [
      { type: "nct", value: nct },
      { type: "url", value: href },
    ];

    // Prefer mapped conditions when present; still include text-detected seeds
    const claimConditions =
      filterMode === "all-seed-mapped"
        ? [
            ...new Set(
              (trial.mapped_conditions || [])
                .map(mapMappedCondition)
                .filter(Boolean)
            ),
          ]
        : conditions;

    for (const condSlug of claimConditions) {
      conditionHitCounts.set(
        condSlug,
        (conditionHitCounts.get(condSlug) || 0) + 1
      );
      const claim = {
        id: `osmf:claim:trial-${slug}-studied-${condSlug}`,
        subject_id: `osmf:trial:${slug}`,
        predicate: "studied_in",
        object_id: `osmf:condition:${condSlug}`,
        evidence_tier: "C",
        sources,
        limitations: LIMITATIONS,
        status: "draft",
        reviewed_by: "tracker-import-bot",
        reviewed_at: now,
        license: "CC-BY-4.0",
      };
      writeJson(
        path.join(CLAIMS_DIR, `trial-${slug}-studied-${condSlug}.json`),
        claim
      );
      conditionClaimCount++;
    }

    const seenAgents = new Set();
    for (const agentName of trial.agents || []) {
      const agentId = resolveAgentId(agentName, agentIndex);
      if (!agentId) {
        agentLinkMisses++;
        continue;
      }
      const agentSlug = agentId.slice("osmf:agent:".length);
      if (seenAgents.has(agentSlug)) continue;
      seenAgents.add(agentSlug);

      const claim = {
        id: `osmf:claim:agent-${agentSlug}-studied-in-${slug}`,
        subject_id: agentId,
        predicate: "studied_in",
        object_id: `osmf:trial:${slug}`,
        evidence_tier: "C",
        sources,
        limitations: LIMITATIONS,
        status: "draft",
        reviewed_by: "tracker-import-bot",
        reviewed_at: now,
        license: "CC-BY-4.0",
      };
      writeJson(
        path.join(
          CLAIMS_DIR,
          `agent-${agentSlug}-studied-in-${slug}.json`
        ),
        claim
      );
      agentClaimCount++;
    }
  }

  // Merge provenance
  let provenance = {};
  if (fs.existsSync(PROVENANCE_PATH)) {
    try {
      provenance = JSON.parse(fs.readFileSync(PROVENANCE_PATH, "utf8"));
    } catch (_) {
      provenance = {};
    }
  }
  provenance.trials_imported_at = now;
  provenance.trials_import_date = importDate;
  provenance.tracker_path = provenance.tracker_path || trackerRoot;
  provenance.counts = {
    ...(provenance.counts || {}),
    trials: trialCount,
    trial_condition_claims: conditionClaimCount,
    trial_agent_claims: agentClaimCount,
  };
  provenance.trial_import = {
    source: "clinical_trials/data/clinical_trials_current.json",
    filter: filterStats,
    condition_hits: Object.fromEntries(
      [...conditionHitCounts.entries()].sort()
    ),
    agent_link_misses: agentLinkMisses,
    notes:
      "studied_in only (trial→condition and agent→trial). Tier C draft; registration link only. No treats_candidate_for / no invented efficacy outcomes.",
  };
  writeJson(PROVENANCE_PATH, provenance);

  console.log(
    `Wrote ${trialCount} trials, ${conditionClaimCount} trial→condition studied_in, ${agentClaimCount} agent→trial studied_in`
  );
  console.log(
    `Filter: mode=${filterMode}, seed_mention=${filterStats.seed_mention}, skipped_filter=${skippedFilter}, skipped_no_nct=${skippedNoNct}, agent_link_misses=${agentLinkMisses}`
  );
  console.log("Condition hits:", Object.fromEntries(conditionHitCounts));
  console.log(`Provenance updated: data/import-provenance.json`);
}

main();
