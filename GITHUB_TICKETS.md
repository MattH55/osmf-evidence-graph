# OSMF Shared Evidence Graph — MVP ticket list

Epic: **Shared Evidence Graph MVP**  
Depends on: product brief + starter schemas in this repo (`schemas/`, `examples/seed-dump.example.json`)  
Default labels: `evidence-graph`, `mvp`  
Suggested milestones: **EG-M1 Schema freeze** → **EG-M2 Seed + dump** → **EG-M3 Hub pages** → **EG-M4 Embeds + export** → **EG-M5 Harden**

---

## EG-1 — Freeze schema v0.1 and ID scheme
**Milestone:** EG-M1  
**Priority:** P0  
**Estimate:** S  

### Description
Adopt `entity` / `claim` / `dump` JSON Schemas as v0.1. Document `osmf:<type>:<slug>` IDs, evidence tiers A–D, and claim status (`draft` | `published` | `superseded`).

### Acceptance criteria
- [ ] Schemas committed as source of truth (start from starter package)
- [ ] Short `SCHEMA.md`: ID rules, predicates, tier definitions, required `limitations` for C/D
- [ ] `schema_version` set to `0.1.0` in dump meta
- [ ] Decision recorded: git files vs DB for authoring (can be “git for MVP”)

### Blocked by
—  

---

## EG-2 — Choose source-of-truth layout (git authoring)
**Milestone:** EG-M1  
**Priority:** P0  
**Estimate:** S  

### Description
For MVP, prefer versioned files (e.g. `data/entities/*.json`, `data/claims/*.json`) compiled into `dist/dump/latest.json`. Document the layout and compile script contract.

### Acceptance criteria
- [ ] Directory layout documented and created
- [ ] `npm run build:dump` (or equivalent) concatenates entities+claims → dump
- [ ] Dump `meta.generated_at` set at build time
- [ ] CI fails if dump is not valid against bundled schema

### Blocked by
EG-1  

---

## EG-3 — JSON Schema CI validation
**Milestone:** EG-M1  
**Priority:** P0  
**Estimate:** S  

### Description
Add CI step validating every entity/claim file and the built dump against schemas.

### Acceptance criteria
- [ ] PR CI runs schema validation
- [ ] Invalid ID pattern, missing C/D `limitations`, or both `object_id` + `object_literal` fails CI
- [ ] Example dump remains `is_example: true` and is validated in CI as a fixture

### Blocked by
EG-1, EG-2  

---

## EG-4 — Curator authoring conventions
**Milestone:** EG-M1  
**Priority:** P1  
**Estimate:** S  

### Description
Write a one-pager for curators: how to add an entity, draft a claim, publish, supersede; no clinical-advice language; provenance required.

### Acceptance criteria
- [ ] `CURATING.md` with examples (copy-paste templates)
- [ ] Checklist: sources, tier, limitations, review fields
- [ ] Explicit “not medical advice” rule

### Blocked by
EG-1  

---

## EG-5 — Seed five condition entities (real network URLs)
**Milestone:** EG-M2  
**Priority:** P0  
**Estimate:** M  

### Description
Replace illustrative condition stubs with curated **entity** records for Long COVID, PACVS, ME/CFS, POTS, MCAS. Link real OSMF tracker/hub/spikeprotein URLs. Keep claims draft until EG-6/EG-7.

### Acceptance criteria
- [ ] Five `osmf:condition:*` entities `status: active`
- [ ] Aliases + at least one external id where available (MeSH/MONDO/etc.)
- [ ] `urls` point at live OSMF pages (not placeholders)
- [ ] Still no false “published” clinical claims

### Blocked by
EG-2  

---

## EG-6 — Seed linking entities (phenotype, biomarker, specimen, criteria stub)
**Milestone:** EG-M2  
**Priority:** P0  
**Estimate:** M  

### Description
Add the minimum non-condition entities needed for embeds and demos: PEM, orthostatic intolerance, spike-persistence (research), plasma specimen type, PACVS criteria draft stub (clearly draft).

### Acceptance criteria
- [ ] ≥2 phenotypes, ≥1 biomarker, ≥1 specimen-type, ≥1 diagnostic-criterion (draft)
- [ ] Each has stable IDs and summaries that avoid advice language
- [ ] Spike entity links to https://spikeprotein.site/

### Blocked by
EG-5  

---

## EG-7 — First curated claim set (draft → published path)
**Milestone:** EG-M2  
**Priority:** P0  
**Estimate:** M  

### Description
Author a small real claim set (target ≥25) for the five conditions: phenotype_of, biomarker_of, related_to, with real DOIs/PMIDs where possible. Start as `draft`; publish only after human review.

### Acceptance criteria
- [ ] ≥25 claims with real sources (doi/pmid/nct/url)
- [ ] Every C/D claim has non-empty `limitations`
- [ ] At least 10 claims reach `published` after named reviewer
- [ ] Dump `meta.is_example` = `false` for the production dump artifact

### Blocked by
EG-5, EG-6, EG-4  

---

## EG-8 — Public dump artifact + versioning
**Milestone:** EG-M2  
**Priority:** P0  
**Estimate:** S  

### Description
Publish `latest.json` (and optional `latest.jsonld`) via static hosting / GitHub Releases / site path. Include license and schema version.

### Acceptance criteria
- [ ] Public URL for dump documented on hub
- [ ] Immutable dated snapshot also available (e.g. `dump-2026-09-18.json`)
- [ ] Changelog entry when schema or published claims change

### Blocked by
EG-3, EG-7  

---

## EG-9 — Hub Evidence Graph landing page
**Milestone:** EG-M3  
**Priority:** P0  
**Estimate:** M  

### Description
Add opensourcemed.info page explaining the graph, how to cite, link to dump, browse by entity type.

### Acceptance criteria
- [ ] Landing page live with plain-language explainer
- [ ] Links: schema docs, dump, curator guide, “not medical advice”
- [ ] Lists seed conditions with links to entity pages

### Blocked by
EG-8  

---

## EG-10 — Static entity pages
**Milestone:** EG-M3  
**Priority:** P0  
**Estimate:** M  

### Description
Generate static pages per entity: summary, claims in/out, linked OSMF tools, export buttons.

### Acceptance criteria
- [ ] One page per seed entity at stable paths (e.g. `/graph/condition/pacvs`)
- [ ] Shows evidence tier + sources + limitations inline
- [ ] Superseded claims visible but marked
- [ ] Works as static site (Vercel-friendly)

### Blocked by
EG-8  

---

## EG-11 — Minimal read API (or static query helpers)
**Milestone:** EG-M3  
**Priority:** P1  
**Estimate:** M  

### Description
Ship either thin API routes or prebuilt per-entity JSON: `GET /entities/:id`, `GET /entities/:id/claims`. Static JSON files are acceptable for MVP.

### Acceptance criteria
- [ ] Documented endpoints or file paths
- [ ] CORS-friendly for network site embeds
- [ ] 404 for unknown IDs; deprecated entities still returned with status

### Blocked by
EG-8  

---

## EG-12 — Related-evidence embed (Research Tracker)
**Milestone:** EG-M4  
**Priority:** P0  
**Estimate:** M  

### Description
Embeddable panel on Research Tracker pages: given `osmf:` ID (or mapped local slug), show top linked claims/entities with link-out to hub entity page.

### Acceptance criteria
- [ ] Embed live on ≥3 tracker pages covering different conditions
- [ ] Uses published claims only
- [ ] Graceful empty state when no graph links
- [ ] No advice language in embed chrome

### Blocked by
EG-10, EG-11  

---

## EG-13 — Related-evidence embed (spikeprotein.site)
**Milestone:** EG-M4  
**Priority:** P0  
**Estimate:** M  

### Description
Same embed pattern on spikeprotein.site for spike-persistence and related condition links.

### Acceptance criteria
- [ ] Embed live on hub or key article pages
- [ ] Uncertainty (C/D) visually distinct
- [ ] Links back to OSMF entity pages

### Blocked by
EG-10, EG-11  

---

## EG-14 — Citation / export pack
**Milestone:** EG-M4  
**Priority:** P1  
**Estimate:** S  

### Description
Export BibTeX + CSV for an entity subgraph or selected claims.

### Acceptance criteria
- [ ] CSV: claim id, subject, predicate, object, tier, sources, reviewed_at
- [ ] BibTeX generated from claim sources where DOI/PMID exist
- [ ] Available from entity pages

### Blocked by
EG-10  

---

## EG-15 — Local ID adapter map (tracker ↔ graph)
**Milestone:** EG-M4  
**Priority:** P1  
**Estimate:** M  

### Description
Mapping file from existing Research Tracker / spikeprotein slugs → `osmf:` IDs so embeds don’t require a full rewrite.

### Acceptance criteria
- [ ] `adapters/tracker.json` (and spikeprotein if needed) committed
- [ ] CI checks every adapter target ID exists in dump
- [ ] Documented how to add a mapping

### Blocked by
EG-5, EG-12  

---

## EG-16 — Provenance audit + publish gate
**Milestone:** EG-M5  
**Priority:** P0  
**Estimate:** S  

### Description
Audit all `published` A/B claims for source + review date; block publish in CI/scripts if missing.

### Acceptance criteria
- [ ] Automated check in build
- [ ] Audit report checked into PR or CI artifact
- [ ] Zero published A/B claims missing sources or `reviewed_at`

### Blocked by
EG-7, EG-3  

---

## EG-17 — Broken-reference CI
**Milestone:** EG-M5  
**Priority:** P0  
**Estimate:** S  

### Description
Fail build if any claim references a missing entity/claim id, or site embed maps to missing id.

### Acceptance criteria
- [ ] CI covers dump + adapters + embed config
- [ ] Clear error messages with offending ids

### Blocked by
EG-15  

---

## EG-18 — Docs: how to cite / how to extend
**Milestone:** EG-M5  
**Priority:** P1  
**Estimate:** S  

### Description
Public docs for external researchers: citing graph IDs, consuming the dump, proposing corrections.

### Acceptance criteria
- [ ] Cite guidelines on hub
- [ ] Correction / PR pathway documented
- [ ] License clarified on dump and pages

### Blocked by
EG-9  

---

## EG-19 — Success metrics instrumentation (lightweight)
**Milestone:** EG-M5  
**Priority:** P2  
**Estimate:** S  

### Description
Track dump downloads / entity page views / embed load counts (privacy-respecting).

### Acceptance criteria
- [ ] Basic analytics events defined
- [ ] Weekly snapshot note in changelog or internal doc
- [ ] Aligns with 30/90-day metrics from product brief

### Blocked by
EG-12, EG-13  

---

## Out of scope for this MVP (parked tickets — do not start)
- EG-X1 Full-text search over claims
- EG-X2 Auto PubMed edge suggestions
- EG-X3 Patient-facing symptom mapper
- EG-X4 Lot → phenotype paths in Vaccine Data Navigator
- EG-X5 Replacing spikeprotein or tracker UIs
- EG-X6 AI chat over the corpus

---

## Suggested first sprint (Week 1–2)
1. EG-1 Schema freeze  
2. EG-2 Git source layout  
3. EG-3 CI validation  
4. EG-4 Curator conventions  
5. EG-5 Seed conditions  

## Dependency graph (high level)
```
EG-1 → EG-2 → EG-3
EG-1 → EG-4
EG-2 → EG-5 → EG-6 → EG-7 → EG-8 → EG-9/10/11
EG-10+11 → EG-12/13
EG-10 → EG-14
EG-5+12 → EG-15 → EG-17
EG-7+3 → EG-16
EG-9 → EG-18
EG-12/13 → EG-19
```

## GitHub issue title paste list
```
EG-1: Freeze evidence graph schema v0.1 and ID scheme
EG-2: Git source-of-truth layout + dump build script
EG-3: CI validation for entities, claims, and dump
EG-4: Curator authoring conventions (CURATING.md)
EG-5: Seed five condition entities with real OSMF URLs
EG-6: Seed phenotypes, biomarkers, specimen, criteria stub
EG-7: First curated claim set with publish path
EG-8: Public dump artifact + dated snapshots
EG-9: Hub Evidence Graph landing page
EG-10: Static entity pages
EG-11: Minimal read API or per-entity JSON
EG-12: Related-evidence embed on Research Tracker
EG-13: Related-evidence embed on spikeprotein.site
EG-14: Citation export (CSV + BibTeX)
EG-15: Tracker/spikeprotein ↔ osmf ID adapter map
EG-16: Provenance audit + publish gate
EG-17: Broken-reference CI
EG-18: Docs — how to cite / how to extend
EG-19: Lightweight success metrics
```
