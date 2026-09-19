#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const Ajv2020 = require("ajv/dist/2020");
const addFormats = require("ajv-formats");

const ROOT = path.join(__dirname, "..");
const SCHEMA_PATH = path.join(ROOT, "schemas", "dump.bundled.schema.json");
const DUMP_PATH = path.join(ROOT, "dist", "dump", "latest.json");

function main() {
  if (!fs.existsSync(DUMP_PATH)) {
    console.error(
      `Missing ${DUMP_PATH}. Run npm run build:dump first.`
    );
    process.exit(1);
  }

  const schema = JSON.parse(fs.readFileSync(SCHEMA_PATH, "utf8"));
  const dump = JSON.parse(fs.readFileSync(DUMP_PATH, "utf8"));

  const ajv = new Ajv2020({ allErrors: true, strict: false });
  addFormats(ajv);

  const validate = ajv.compile(schema);
  const ok = validate(dump);

  if (!ok) {
    console.error("Dump validation failed:");
    for (const err of validate.errors || []) {
      console.error(`  ${err.instancePath || "/"} ${err.message}`);
    }
    process.exit(1);
  }

  console.log(`OK: ${DUMP_PATH} validates against dump.bundled.schema.json`);
}

main();
