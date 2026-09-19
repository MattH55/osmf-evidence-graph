# Importing from OSMF Research Tracker

This repository can be populated from [osmf-research-tracker](https://github.com/MattH55/osmf-research-tracker) PubMed condition feeds under `data/*.json`.

## What the importer writes

| Kind | Rule |
|------|------|
| **Conditions** | One entity per feed key (`long-covid`, `pacvs`, `me-cfs`, `pots`, `mcas`, `lyme`, `gulf-war-illness`, `other-post-viral`) as `osmf:condition:<slug>` |
| **Papers** | One entity per PMID as `osmf:paper:pmid-<pmid>` (deduped across conditions) |
| **Claims** | Provisional `related_to` edges paper → condition: `osmf:claim:tracker-<slug>-pmid-<pmid>`, **evidence_tier C**, **status draft** |

The importer also removes known placeholder seed nodes (fake NCT / DOI / example agent) that would confuse Evidence Desk.

## What it does **not** do

- Does **not** invent A/B evidence grades or clinical recommendations
- Does **not** import the ~600 therapeutic agents catalog (follow-up PR)
- Does **not** import the multi-MB `clinical_trials` JSON (next wave)

## How to re-run

```bash
# Optional: point at a local tracker checkout
export TRACKER_PATH=/workspace/osmf-research-tracker   # or sibling ../osmf-research-tracker

npm run import:tracker
npm run build:dump
npm run validate:dump
```

`import:tracker` is idempotent: it clears prior `pmid-*.json` paper entities and `tracker-*-pmid-*.json` claims, then rewrites from the feeds.

Provenance is written to `data/import-provenance.json` (imported_at, counts). `build:dump` keeps `meta.is_example: true` so Desk banners stay honest while papers are real PMIDs.

## Required claim limitations text

Every auto-imported claim includes:

> Auto-imported from OSMF Research Tracker PubMed feed; not human evidence-graded. Inclusion in the tracker query does not imply study quality or clinical applicability.

## Tracker page URLs

Condition `urls` use `rel: tracker` → `https://research.opensourcemed.info/<slug>.html` (verified against local HTML pages when present).
