# EG-3: JSON Schema CI validation

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
_Part of epic: Shared Evidence Graph MVP_
