# OSMF Shared Evidence Graph — starter schema

Starter JSON Schema and **example** seed dump for the five MVP conditions:

- Long COVID
- PACVS
- ME/CFS
- POTS
- MCAS

## Files

| Path | Purpose |
|------|---------|
| `schemas/entity.schema.json` | Entity objects (`osmf:…` IDs) |
| `schemas/claim.schema.json` | Claim-centric knowledge units |
| `schemas/dump.schema.json` | Versioned public dump bundle |
| `examples/seed-dump.example.json` | Illustrative dataset (not curated truth) |

## Important

`examples/seed-dump.example.json` is **synthetic / illustrative**. Claims, tiers, and links are structural examples for engineering and product review. They are not OSMF-endorsed clinical statements. Replace with curated content before any public “published” use.

## ID scheme

`osmf:<type>:<slug>`

Types in MVP: `condition`, `phenotype`, `biomarker`, `agent`, `trial`, `paper`, `cohort`, `specimen-type`, `diagnostic-criterion`, `vaccine-lot`.

## Validate (optional)

```bash
npx --yes ajv-cli validate -s schemas/dump.schema.json -d examples/seed-dump.example.json --spec=draft2020
```

## License note

Schema is for OSMF network use. Attach your preferred data license on real dumps (`license` field on claims / dump meta).

## Validation

A bundled schema (inline entity/claim defs) is at `schemas/dump.bundled.schema.json` for offline validators that do not resolve remote `$ref`s.

```bash
python3 -m venv .venv && .venv/bin/pip install jsonschema
.venv/bin/python -c "import json; from jsonschema import Draft202012Validator; \
s=json.load(open('schemas/dump.bundled.schema.json')); \
d=json.load(open('examples/seed-dump.example.json')); \
Draft202012Validator(s).validate(d); print('ok')"
```

The example dump was validated successfully against the bundled schema on 2026-09-18.
