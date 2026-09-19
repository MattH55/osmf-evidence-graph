# Data layout (git authoring)

For MVP, **versioned JSON files in git** are the source of truth. There is no authoring database.

## Directories

```
data/
  entities/     # one entity per file
  claims/       # one claim per file
```

### Entities — `data/entities/<slug>.json`

- Filename is the **ID slug** (final segment of `osmf:<type>:<slug>`)
- Example: `osmf:condition:long-covid` → `long-covid.json`
- File body is a single entity object matching `schemas/entity.schema.json`

### Claims — `data/claims/<slug>.json`

- Filename is the claim slug from `osmf:claim:<slug>`
- Example: `osmf:claim:ex-pem-of-me-cfs` → `ex-pem-of-me-cfs.json`
- File body is a single claim object matching `schemas/claim.schema.json`

## Compile

```bash
npm ci
npm run build:dump
```

`build:dump` reads all entity and claim files, writes:

1. `dist/dump/latest.json` — compiled dump (`meta.generated_at` = build time, UTC)
2. `examples/seed-dump.example.json` — same payload refreshed as a checked-in fixture (`is_example: true`)

Validate:

```bash
npm run validate:dump
```

## Notes

- Keep seed / example content with `meta.is_example: true` until curated for publication
- Do not invent clinical claims beyond illustrative structure
- See [SCHEMA.md](../SCHEMA.md) for IDs, tiers, predicates, and the git-for-MVP decision

