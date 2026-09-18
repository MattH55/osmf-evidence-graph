# EG-2: Choose source-of-truth layout (git authoring)

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
_Part of epic: Shared Evidence Graph MVP_
