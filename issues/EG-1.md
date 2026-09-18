# EG-1: Freeze schema v0.1 and ID scheme

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
_Part of epic: Shared Evidence Graph MVP_
