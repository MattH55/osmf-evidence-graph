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

const SEED_CONDITIONS = [
  "osmf:condition:long-covid",
  "osmf:condition:pacvs",
  "osmf:condition:me-cfs",
  "osmf:condition:pots",
  "osmf:condition:mcas",
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

function main() {
  const entityFiles = readJsonFiles(ENTITIES_DIR);
  const claimFiles = readJsonFiles(CLAIMS_DIR);

  const entities = entityFiles.map((x) => x.obj).sort(byId);
  const claims = claimFiles.map((x) => x.obj).sort(byId);

  const dump = {
    meta: {
      schema_version: "0.1.0",
      generated_at: new Date().toISOString(),
      publisher: "Open Source Medicine Foundation (example seed)",
      is_example: true,
      license: "CC-BY-4.0",
      notes:
        "ILLUSTRATIVE ONLY. Entities and claims are structural examples for schema review. They are not curated OSMF clinical statements. Replace sources, tiers, and wording before any public published dump (set is_example to false).",
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
