# Importing from OSMF Research Tracker

This repository can be populated from [osmf-research-tracker](https://github.com/MattH55/osmf-research-tracker):

1. PubMed condition feeds under `data/<condition>.json`
2. Therapeutic agents catalog `data/therapeutic_agents.json` (+ optional `data/vocab/agent-slugs.json`)
3. Clinical trials catalog `clinical_trials/data/clinical_trials_current.json`

## What the importers write

### Papers / conditions (`npm run import:tracker`)

| Kind | Rule |
|------|------|
| **Conditions** | One entity per feed key (`long-covid`, `pacvs`, `me-cfs`, `pots`, `mcas`, `lyme`, `gulf-war-illness`, `other-post-viral`) as `osmf:condition:<slug>` |
| **Papers** | One entity per PMID as `osmf:paper:pmid-<pmid>` (deduped across conditions) |
| **Claims** | Provisional `related_to` edges paper → condition: `osmf:claim:tracker-<slug>-pmid-<pmid>`, **evidence_tier C**, **status draft** |

Also removes known placeholder seed nodes (fake NCT / DOI / example agent) that would confuse Evidence Desk.

### Therapeutic agents (`npm run import:tracker:agents`)

| Kind | Rule |
|------|------|
| **Agents** | One entity per row in `therapeutic_agents.json` (~596) as `osmf:agent:<slug>` |
| **Claims** | `treats_candidate_for` agent → condition: `osmf:claim:agent-<slug>-treats-<condition-slug>`, **status draft** |

**Slug:** kebab-case from Therapeutic Agent name; prefer stable slugs from tracker `data/vocab/agent-slugs.json` (and flagged list). Collisions get numeric suffixes.

**Evidence Level → tier (never A/B from this import):**

| Tracker Evidence Level | evidence_tier |
|------------------------|---------------|
| Moderate | C |
| Preliminary | D |
| Anecdotal | D |

**Primary Conditions → condition IDs:**

| Tracker string | Condition ID |
|----------------|--------------|
| Long COVID | `osmf:condition:long-covid` |
| PACVS | `osmf:condition:pacvs` |
| ME/CFS | `osmf:condition:me-cfs` |
| POTS | `osmf:condition:pots` |
| MCAS | `osmf:condition:mcas` |
| Lyme | `osmf:condition:lyme` |
| Gulf War Illness | `osmf:condition:gulf-war-illness` |
| Other Post-Viral… | `osmf:condition:other-post-viral` |

Unknown condition strings are skipped and logged.

**URLs:** `https://research.opensourcemed.info/agents/<slug>/` when `agents/<slug>/` exists locally; otherwise `candidate-therapeutics.html` or `agents.html`.

**Summaries:** Proposed Mechanism + Clinical Notes (truncated), with neutral disclaimer. Dosing/Safety are **not** copied as recommendations (`See tracker agent page / linked studies; Desk does not provide dosing.`).

**Sources:** prefer `osmf_page` tracker URL; add PMIDs/NCTs when present in studies/trials/Key Studies.

**reviewed_by:** `tracker-import-bot`.

### Clinical trials (`npm run import:tracker:trials`)

| Kind | Rule |
|------|------|
| **Trials** | One entity per NCT as `osmf:trial:nct-<nctid>` (lowercase id slug; display NCT uppercased in `external_ids`) |
| **Claims** | `studied_in` trial → condition when mapped/text matches a seed condition; optional `studied_in` agent → trial when intervention slug/label matches an existing `osmf:agent:*` |
| **Filter** | Default: NCTs that mention seed conditions (Long COVID, PACVS, ME/CFS, POTS, MCAS, Lyme, GWI, other-post-viral). Set `TRIALS_IMPORT_FILTER=large` for recruiting/completed-ish + enrollment≥50, or `all-seed-mapped` for mapped Long COVID/ME/CFS only |

**Field mapping (tracker → graph):**

| Tracker field | Graph use |
|---------------|-----------|
| `nct_id` | Entity id slug + `external_ids.system=nct` + ClinicalTrials.gov URL |
| `title` | `label` (truncated) |
| `status`, `phase`, `mapped_conditions` / `conditions_raw`, `enrollment` | Neutral `summary` snippet |
| `link` | `urls[]` (`rel: other`); fallback `https://clinicaltrials.gov/study/<NCT>` |
| `mapped_conditions` | Prefer for trial→condition `studied_in` (`Long COVID / PASC`→`long-covid`, `ME/CFS`→`me-cfs`; skip Unspecified/Overlap) |
| `conditions_raw` / `title` / `relevance_tags` | Extra seed-condition detection (POTS, MCAS, Lyme, PACVS, GWI, other-post-viral, etc.) |
| `agents[]` | Optional agent→trial `studied_in` when slug/label matches existing agent entity |

**Tiers:** structural `studied_in` links are **evidence_tier C**, **status draft**, limitations = registration link only. No `treats_candidate_for` and no invented efficacy outcomes (results fields are not present in the tracker export).

**reviewed_by:** `tracker-import-bot`.

## What it does **not** do

- Does **not** invent A/B evidence grades or clinical recommendations
- Does **not** copy dosing instructions into summaries as advice
- Does **not** invent efficacy outcomes from ClinicalTrials.gov registrations

## How to re-run

```bash
# Optional: point at a local tracker checkout
export TRACKER_PATH=/workspace/osmf-research-tracker   # or sibling ../osmf-research-tracker

npm run import:tracker          # conditions + papers + related_to
npm run import:tracker:agents   # agents + treats_candidate_for
npm run import:tracker:trials   # trials + studied_in
# or: npm run import:tracker:all

npm run build:dump
npm run validate:dump
```

Importers are idempotent: they clear prior files matching their patterns, then rewrite.

- Papers: `pmid-*.json` entities and `tracker-*-pmid-*.json` claims
- Agents: `agent-*.json` entities and `agent-*-treats-*.json` claims
- Trials: `trial-nct-*.json` entities, `trial-nct-*-studied-*.json` claims, and `agent-*-studied-in-nct-*.json` claims

Provenance is written to `data/import-provenance.json` (imported_at / agents_imported_at / trials_imported_at, counts). `build:dump` keeps `meta.is_example: true` so Desk banners stay honest while nodes are real Tracker-backed IDs.

## Required claim limitations text

### Paper `related_to` claims

> Auto-imported from OSMF Research Tracker PubMed feed; not human evidence-graded. Inclusion in the tracker query does not imply study quality or clinical applicability.

### Agent `treats_candidate_for` claims

> Auto-imported from OSMF Research Tracker therapeutic_agents.json. Evidence Level is tracker metadata, not an OSMF curator grade. Not medical advice; Desk does not provide dosing. Inclusion as a treats_candidate_for claim does not imply efficacy, safety, or clinical recommendation.

### Trial / agent `studied_in` claims

> Auto-imported from OSMF Research Tracker clinical_trials JSON. Structural registration link only — not an efficacy grade. Inclusion does not imply study quality, enrollment completeness, or clinical applicability.

## Tracker page URLs

- Condition `urls` use `rel: tracker` → `https://research.opensourcemed.info/<slug>.html`
- Agent `urls` use `rel: tracker` → agent page or catalog fallback (see above)
