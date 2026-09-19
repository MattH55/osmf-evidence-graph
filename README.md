# OSMF Shared Evidence Graph

Shared evidence-graph schemas and **git-authored** seed data for five MVP conditions:

- Long COVID
- PACVS
- ME/CFS
- POTS
- MCAS

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
| `examples/seed-dump.example.json` | Checked-in compiled fixture (`is_example: true`); refreshed by `build:dump` |
| `dist/dump/latest.json` | Build output (gitignored; produced in CI / locally) |

## Build & validate

```bash
npm ci
npm run build:dump      # → dist/dump/latest.json (+ refreshes examples/seed-dump.example.json)
npm run validate:dump   # AJV vs schemas/dump.bundled.schema.json
```

CI: `.github/workflows/validate-dump.yml` runs build + schema validation on push/PR. Locally, `npm run validate:dump` **fails on an invalid dump**.

## Important

`examples/seed-dump.example.json` and the compiled dump are **synthetic / illustrative**. Claims, tiers, and links are structural examples for engineering and product review. They are **not** OSMF-endorsed clinical statements and are **not medical advice**. Keep `is_example: true` until curated content replaces the seed.

## ID scheme

`osmf:<type>:<slug>` — full rules in [SCHEMA.md](SCHEMA.md).

## License note

Schema is for OSMF network use. Dump `meta.license` / claim `license` carry the data license (seed uses `CC-BY-4.0`).
