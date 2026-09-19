# OSMF Evidence Graph Schema v0.1

**schema_version:** `0.1.0`

This document freezes the v0.1 contract for entities, claims, and public dumps. Machine-readable sources of truth live under [`schemas/`](schemas/).

## Not medical advice

Content in this repository describes structured research and product wiring. It is **not medical advice**, not a diagnosis, and not a treatment recommendation. Example seed data (`is_example: true`) is illustrative only.

## ID scheme

```
osmf:<type>:<slug>
```

- `type` — entity kind (see below) or `claim` for claims
- `slug` — lowercase kebab-case (`[a-z0-9-]+`)
- IDs are stable once published; do not reuse a slug for a different concept

Examples: `osmf:condition:pacvs`, `osmf:claim:ex-pem-of-me-cfs`

## Entity types (MVP)

| Type | Role |
|------|------|
| `condition` | Clinical / post-viral condition (e.g. Long COVID, ME/CFS) |
| `phenotype` | Observable trait or symptom cluster (e.g. PEM) |
| `biomarker` | Measured or research marker |
| `agent` | Drug, biologic, or other intervention candidate |
| `trial` | Clinical trial record |
| `paper` | Publication / review node |
| `cohort` | Study or patient cohort |
| `specimen-type` | Biobank specimen class (e.g. plasma) |
| `diagnostic-criterion` | Criteria set (may be draft) |
| `vaccine-lot` | Lot-level exposure entity when needed |

Entity `status`: `active` | `deprecated`.

## Predicates (claims)

| Predicate | Typical use |
|-----------|-------------|
| `biomarker_of` | Marker linked to a condition |
| `phenotype_of` | Phenotype linked to a condition |
| `treats_candidate_for` | Agent under study for a condition (not efficacy endorsement) |
| `studied_in` | Entity studied in a trial |
| `supported_by` | Claim or statement supported by a paper/source node |
| `conflicts_with` | Competing claim or finding |
| `supports_criterion` | Evidence contributing to a diagnostic criterion |
| `measured_in` | Marker/assay context in a specimen type |
| `associated_with_exposure` | Association with an exposure entity |
| `related_to` | Non-causal relatedness / comorbidity / theme link |
| `supersedes` | Newer claim replaces an older one |

Each claim must have exactly one of `object_id` or `object_literal` (not both).

## Evidence tiers A–D

| Tier | Meaning |
|------|---------|
| **A** | Strong clinical / consensus support |
| **B** | Solid clinical evidence or high-quality synthesis |
| **C** | Mechanistic, preclinical, case-level, or early signal |
| **D** | Contested, insufficient, or highly uncertain |

**Required `limitations`:** tiers **C** and **D** must include a non-empty `limitations` string. Limitations are strongly recommended for **B**.

## Claim status

| Status | Meaning |
|--------|---------|
| `draft` | Authoring / review in progress; not for public “published” presentation |
| `published` | Curator-reviewed for public dump use |
| `superseded` | Replaced by another claim (`supersedes_id` / `supersedes` as applicable) |

## Dump meta

Public dumps (`meta`) include at least:

- `schema_version` — semver string; **v0.1 uses `0.1.0`**
- `generated_at` — ISO-8601 UTC timestamp set at build time
- `publisher`, `is_example`, `license`
- optional `notes`, `seed_conditions`

## Authoring decision (MVP)

**Git files are the source of truth for MVP authoring** — not a database.

- Edit `data/entities/*.json` and `data/claims/*.json` in version control
- Compile with `npm run build:dump` → `dist/dump/latest.json`
- A database or CMS may be considered later; it is out of scope for MVP

## Schema files

| Path | Purpose |
|------|---------|
| `schemas/entity.schema.json` | Entity objects |
| `schemas/claim.schema.json` | Claims |
| `schemas/dump.schema.json` | Dump bundle (`$ref` to entity/claim) |
| `schemas/dump.bundled.schema.json` | Offline-friendly bundled dump schema |

