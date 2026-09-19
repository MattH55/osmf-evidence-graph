#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const ENTITIES_DIR = path.join(ROOT, "data", "entities");
const CLAIMS_DIR = path.join(ROOT, "data", "claims");
const DIST_DIR = path.join(ROOT, "dist", "dump");
const DIST_OUT = path.join(DIST_DIR, "latest.json");
const EXAMPLE_OUT = path.join(ROOT, "examples", "seed-dump.example.json");
const PROVENANCE_PATH = path.join(ROOT, "data", "import-provenance.json");

const SEED_CONDITIONS = [
  "osmf:condition:long-covid",
  "osmf:condition:pacvs",
  "osmf:condition:me-cfs",
  "osmf:condition:pots",
  "osmf:condition:mcas",
  "osmf:condition:lyme",
  "osmf:condition:gulf-war-illness",
  "osmf:condition:other-post-viral",
];

function readJsonFiles(dir) {
  if (!fs.existsSync(dir)) {
    throw new Error(`Missing directory: ${dir}`);
  }
  const files = fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .sort();
  return files.map((f) => {
    const full = path.join(dir, f);
    const obj = JSON.parse(fs.readFileSync(full, "utf8"));
    return { file: f, obj };
  });
}

function byId(a, b) {
  return a.id.localeCompare(b.id);
}

function buildNotes() {
  let importLine =
    "Papers/related_to and agents/treats_candidate_for were auto-imported from OSMF Research Tracker (provisional; status draft; no A/B tiers from this import).";
  if (fs.existsSync(PROVENANCE_PATH)) {
    try {
      const p = JSON.parse(fs.readFileSync(PROVENANCE_PATH, "utf8"));
      if (p.imported_at || p.agents_imported_at) {
        importLine += ` Last paper import: ${p.imported_at || "n/a"}; last agent import: ${p.agents_imported_at || "n/a"}.`;
      }
      if (p.counts) {
        importLine += ` Counts: ${p.counts.conditions || 0} conditions, ${p.counts.papers || 0} papers, ${p.counts.claims || 0} paper claims, ${p.counts.agents || 0} agents, ${p.counts.agent_claims || 0} agent claims.`;
      }
    } catch (_) {
      /* ignore */
    }
  }
  return [
    "ILLUSTRATIVE / PROVISIONAL DUMP (is_example: true).",
    "Condition entities, PubMed paper nodes, and therapeutic agent nodes are Tracker-backed, but claim grades are NOT human evidence-curated.",
    importLine,
    "Do not treat draft related_to or treats_candidate_for edges as clinical recommendations, efficacy endorsements, or dosing advice.",
    "Agent Evidence Level is tracker metadata mapped Moderate→C and Preliminary/Anecdotal→D only.",
    "Multi-MB clinical_trials JSON remains deferred to a follow-up import wave.",
    "Kept seed phenotypes/biomarkers (PEM, orthostatic intolerance, spike persistence, etc.) are structural examples pending curator re-grade.",
  ].join(" ");
}

function main() {
  const entityFiles = readJsonFiles(ENTITIES_DIR);
  const claimFiles = readJsonFiles(CLAIMS_DIR);

  const entities = entityFiles.map((x) => x.obj).sort(byId);
  const claims = claimFiles.map((x) => x.obj).sort(byId);

  const dump = {
    meta: {
      schema_version: "0.1.0",
      generated_at: new Date().toISOString(),
      publisher: "Open Source Medicine Foundation (provisional tracker import)",
      is_example: true,
      license: "CC-BY-4.0",
      notes: buildNotes(),
      seed_conditions: SEED_CONDITIONS,
    },
    entities,
    claims,
  };

  fs.mkdirSync(DIST_DIR, { recursive: true });
  const text = JSON.stringify(dump, null, 2) + "\n";
  fs.writeFileSync(DIST_OUT, text);
  fs.writeFileSync(EXAMPLE_OUT, text);

  console.log(
    `Wrote ${DIST_OUT} and ${EXAMPLE_OUT} (${entities.length} entities, ${claims.length} claims)`
  );
}

main();
