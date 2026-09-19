#!/usr/bin/env node
/**
 * Import conditions + papers + provisional related_to claims from
 * osmf-research-tracker PubMed feed JSON into the evidence graph.
 *
 * Usage:
 *   TRACKER_PATH=/path/to/osmf-research-tracker node scripts/import_from_research_tracker.mjs
 *   npm run import:tracker
 *
 * Defaults TRACKER_PATH to sibling ../osmf-research-tracker or /workspace/osmf-research-tracker.
 *
 * Does NOT invent evidence tiers A/B or clinical recommendations.
 * All imported paper→condition claims are tier C / draft / provisional.
 * Therapeutic agents and clinical_trials JSON are intentionally out of scope.
 */
"use strict";

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, "..");
const ENTITIES_DIR = path.join(ROOT, "data", "entities");
const CLAIMS_DIR = path.join(ROOT, "data", "claims");

const CONDITION_SLUGS = [
  "long-covid",
  "pacvs",
  "me-cfs",
  "pots",
  "mcas",
  "lyme",
  "gulf-war-illness",
  "other-post-viral",
];

const PLACEHOLDER_ENTITY_FILES = [
  "example-repurposing-candidate.json",
  "example-nct-00000000.json",
  "example-review-001.json",
];

const PLACEHOLDER_CLAIM_FILES = [
  "ex-agent-candidate-long-covid.json",
  "ex-agent-studied-in-trial.json",
  "ex-paper-supports-pem-me-cfs.json",
];

const LIMITATIONS =
  "Auto-imported from OSMF Research Tracker PubMed feed; not human evidence-graded. Inclusion in the tracker query does not imply study quality or clinical applicability.";

const DEFAULT_ALIASES = {
  "long-covid": ["PASC", "post-COVID condition", "long COVID"],
  pacvs: ["post-acute COVID-19 vaccination syndrome"],
  "me-cfs": ["myalgic encephalomyelitis", "chronic fatigue syndrome", "CFS"],
  pots: ["postural orthostatic tachycardia syndrome"],
  mcas: ["mast cell activation syndrome"],
  lyme: ["PTLDS", "post-treatment Lyme disease syndrome", "chronic Lyme"],
  "gulf-war-illness": ["GWI", "Gulf War Syndrome"],
  "other-post-viral": ["post-viral syndrome", "post-infectious syndrome"],
};

function resolveTrackerPath() {
  if (process.env.TRACKER_PATH) {
    return path.resolve(process.env.TRACKER_PATH);
  }
  const candidates = [
    path.resolve(ROOT, "..", "osmf-research-tracker"),
    "/workspace/osmf-research-tracker",
  ];
  for (const c of candidates) {
    if (fs.existsSync(path.join(c, "data"))) return c;
  }
  throw new Error(
    "Could not find osmf-research-tracker. Set TRACKER_PATH to the repo root."
  );
}

function truncate(str, max) {
  const s = String(str || "").trim();
  if (s.length <= max) return s;
  return s.slice(0, max - 1).trimEnd() + "…";
}

function labelAndSummary(conditionField) {
  const full = String(conditionField || "").trim();
  const parts = full.split(/\s+[–—-]\s+/);
  const short = parts[0]?.trim() || full;
  return {
    label: truncate(short, 120) || "Unknown condition",
    summary: truncate(full, 500) || short,
  };
}

function pubmedUrl(pmid, fallback) {
  if (fallback && /^https?:\/\//i.test(fallback)) return fallback;
  return `https://pubmed.ncbi.nlm.nih.gov/${pmid}/`;
}

function writeJson(filePath, obj) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(obj, null, 2) + "\n");
}

function removeIfExists(filePath) {
  if (fs.existsSync(filePath)) {
    fs.unlinkSync(filePath);
    return true;
  }
  return false;
}

function isTrackerPaperFile(name) {
  return /^pmid-\d+\.json$/.test(name);
}

function isTrackerClaimFile(name) {
  return /^tracker-.+-pmid-\d+\.json$/.test(name);
}

function main() {
  const trackerRoot = resolveTrackerPath();
  const dataDir = path.join(trackerRoot, "data");
  const now = new Date().toISOString();
  const importDate = now.slice(0, 10);

  console.log(`Tracker path: ${trackerRoot}`);
  console.log(`Import timestamp: ${now}`);

  // Remove prior tracker-import paper/claim files (idempotent re-run)
  let removedPapers = 0;
  let removedClaims = 0;
  for (const f of fs.readdirSync(ENTITIES_DIR)) {
    if (isTrackerPaperFile(f)) {
      fs.unlinkSync(path.join(ENTITIES_DIR, f));
      removedPapers++;
    }
  }
  for (const f of fs.readdirSync(CLAIMS_DIR)) {
    if (isTrackerClaimFile(f)) {
      fs.unlinkSync(path.join(CLAIMS_DIR, f));
      removedClaims++;
    }
  }
  if (removedPapers || removedClaims) {
    console.log(
      `Cleared prior import: ${removedPapers} papers, ${removedClaims} claims`
    );
  }

  // Remove confusing placeholders
  for (const f of PLACEHOLDER_ENTITY_FILES) {
    if (removeIfExists(path.join(ENTITIES_DIR, f))) {
      console.log(`Removed placeholder entity ${f}`);
    }
  }
  for (const f of PLACEHOLDER_CLAIM_FILES) {
    if (removeIfExists(path.join(CLAIMS_DIR, f))) {
      console.log(`Removed placeholder claim ${f}`);
    }
  }

  const papersByPmid = new Map();
  let conditionCount = 0;
  let claimCount = 0;
  const missingHtml = [];

  for (const slug of CONDITION_SLUGS) {
    const jsonPath = path.join(dataDir, `${slug}.json`);
    if (!fs.existsSync(jsonPath)) {
      console.warn(`SKIP missing feed: ${jsonPath}`);
      continue;
    }

    const htmlPath = path.join(trackerRoot, `${slug}.html`);
    const trackerHref = `https://research.opensourcemed.info/${slug}.html`;
    if (!fs.existsSync(htmlPath)) {
      missingHtml.push(slug);
      console.warn(`WARN: ${slug}.html not found locally; still using ${trackerHref}`);
    }

    const feed = JSON.parse(fs.readFileSync(jsonPath, "utf8"));
    const { label, summary } = labelAndSummary(feed.condition || slug);

    const conditionEntity = {
      id: `osmf:condition:${slug}`,
      type: "condition",
      label,
      aliases: DEFAULT_ALIASES[slug] || [],
      summary,
      external_ids: [],
      urls: [
        {
          rel: "tracker",
          href: trackerHref,
        },
      ],
      status: "active",
      updated_at: now,
    };

    // Preserve known MeSH for Long COVID if present in prior seed style
    if (slug === "long-covid") {
      conditionEntity.external_ids.push({
        system: "mesh",
        value: "D000094024",
      });
    }

    writeJson(path.join(ENTITIES_DIR, `${slug}.json`), conditionEntity);
    conditionCount++;

    const studies = Array.isArray(feed.studies) ? feed.studies : [];
    for (const study of studies) {
      const pmid = study.pmid != null ? String(study.pmid).trim() : "";
      if (!/^\d+$/.test(pmid)) {
        console.warn(`SKIP study without numeric pmid in ${slug}`);
        continue;
      }

      const href = pubmedUrl(pmid, study.url);
      const title = truncate(study.title || `PubMed ${pmid}`, 200) || `PubMed ${pmid}`;
      const abstractText = String(study.abstract || "").trim();
      const paperSummary = abstractText
        ? truncate(abstractText, 500)
        : truncate(`PubMed ${pmid}. No abstract in tracker feed.`, 500);

      if (!papersByPmid.has(pmid)) {
        papersByPmid.set(pmid, {
          id: `osmf:paper:pmid-${pmid}`,
          type: "paper",
          label: title,
          aliases: [],
          summary: paperSummary,
          external_ids: [
            {
              system: "pubmed",
              value: pmid,
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
        });
      }

      const claim = {
        id: `osmf:claim:tracker-${slug}-pmid-${pmid}`,
        subject_id: `osmf:paper:pmid-${pmid}`,
        predicate: "related_to",
        object_id: `osmf:condition:${slug}`,
        evidence_tier: "C",
        sources: [
          { type: "pmid", value: pmid },
          { type: "url", value: href },
        ],
        limitations: LIMITATIONS,
        status: "draft",
        reviewed_by: "tracker-import-bot",
        reviewed_at: now,
        license: "CC-BY-4.0",
      };

      writeJson(
        path.join(CLAIMS_DIR, `tracker-${slug}-pmid-${pmid}.json`),
        claim
      );
      claimCount++;
    }
  }

  for (const [pmid, entity] of papersByPmid) {
    writeJson(path.join(ENTITIES_DIR, `pmid-${pmid}.json`), entity);
  }

  // Write a small provenance sidecar for docs/build consumers
  const provenance = {
    imported_at: now,
    import_date: importDate,
    tracker_path: trackerRoot,
    conditions: CONDITION_SLUGS,
    counts: {
      conditions: conditionCount,
      papers: papersByPmid.size,
      claims: claimCount,
    },
    missing_html: missingHtml,
    notes:
      "Provisional auto-import from Research Tracker PubMed feeds. Grades are not human-curated. Agents and clinical_trials deferred.",
  };
  writeJson(path.join(ROOT, "data", "import-provenance.json"), provenance);

  console.log(
    `Wrote ${conditionCount} conditions, ${papersByPmid.size} papers, ${claimCount} claims`
  );
  console.log(`Provenance: data/import-provenance.json`);
}

main();
