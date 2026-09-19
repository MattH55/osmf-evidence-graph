# OSMF Shared Evidence Graph

Shared evidence-graph schemas and **git-authored** data for post-viral / related conditions, populated from the OSMF Research Tracker (plus retained phenotype/biomarker seed nodes):

- Long COVID, PACVS, ME/CFS, POTS, MCAS
- Lyme / PTLDS, Gulf War Illness, Other post-viral

**schema_version:** `0.1.0` — see [SCHEMA.md](SCHEMA.md).

## Authoring decision (MVP)

**Git files are the source of truth** for MVP authoring (not a database). Edit JSON under `data/`, then compile a dump. A DB/CMS can be considered later.

## Layout

| Path | Purpose |
|------|---------|
| [`SCHEMA.md`](SCHEMA.md) | ID scheme, entity types, predicates, tiers A–D, claim status, git-for-MVP |
| `schemas/` | JSON Schema v0.1 (`entity`, `claim`, `dump`, bundled dump) |
| `data/entities/*.json` | One entity per file (named by ID slug) |
| `data/claims/*.json` | One claim per file (named by claim slug) |
| [`data/README.md`](data/README.md) | Data directory contract |
| [`IMPORT.md`](IMPORT.md) | Re-run tracker → graph import |
| `examples/seed-dump.example.json` | Checked-in compiled fixture (`is_example: true`); refreshed by `build:dump` |
| `dist/dump/latest.json` | Build output (gitignored; produced in CI / locally) |

## Build & validate

```bash
npm ci
npm run build:dump      # → dist/dump/latest.json (+ refreshes examples/seed-dump.example.json)
npm run validate:dump   # AJV vs schemas/dump.bundled.schema.json
```

CI: `.github/workflows/validate-dump.yml` runs build + schema validation on push/PR. Locally, `npm run validate:dump` **fails on an invalid dump**.

## Import from Research Tracker

```bash
export TRACKER_PATH=/path/to/osmf-research-tracker   # optional; auto-detects sibling /workspace
npm run import:tracker
npm run import:tracker:agents
npm run build:dump && npm run validate:dump
```

Details: [IMPORT.md](IMPORT.md).

## Important

`meta.is_example` remains **`true`**: paper PMIDs, condition pages, and therapeutic agent nodes come from the Research Tracker, but **claim grades are provisional auto-imports** (paper `related_to` tier C; agent `treats_candidate_for` C/D from tracker Evidence Level — never A/B), not human evidence review. They are **not** OSMF-endorsed clinical statements, **not medical advice**, and **not dosing guidance**.

See [IMPORT.md](IMPORT.md) to re-run tracker imports (`import:tracker` for papers; `import:tracker:agents` for therapeutic agents). Full clinical-trials JSON import remains deferred.

## ID scheme

`osmf:<type>:<slug>` — full rules in [SCHEMA.md](SCHEMA.md).

## License note

Schema is for OSMF network use. Dump `meta.license` / claim `license` carry the data license (seed uses `CC-BY-4.0`).
