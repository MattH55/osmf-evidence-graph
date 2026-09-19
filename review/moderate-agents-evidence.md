# Moderate agents — evidence evaluation report

**Date:** 2026-09-19 (America/Edmonton)
**Evaluator:** evidence-eval-bot
**Queue size:** 58 claims

## Counts by proposed tier

- **A**: 0 (published=0, draft=0)
- **B**: 0 (published=0, draft=0)
- **C**: 33 (published=9, draft=24)
- **D**: 25 (published=4, draft=21)

## Method

For each claim: ClinicalTrials.gov API v2 summaries for NCT IDs from tracker `trials[]`; PMIDs from tracker `studies[]` / Key Studies; Europe PMC search fallback (`agent` + condition terms, top cited, limit 5). Tiers follow OSMF A–D. Phase 3 without verified supportive results is **not** upgraded to B. Claims 1–2 (amphetamine-dextroamphetamine→Long COVID; Ampligen→ME/CFS) were human-graded C/published and retained.

## Notable upgrades / downgrades vs import default (C)

- No A/B upgrades (honest: no verified solid multi-trial supportive packages found in this pass).
- Downgrades to D: 25 claims (terminated/off-target/class/contested/insufficient).
- Example C retain/publish with new evidence notes: Fluvoxamine→Long COVID (posted CT.gov signal, still C); Metformin→Long COVID (prevention>treatment); Paxlovid→Long COVID (mixed).
- Example D: Rituximab→ME/CFS (negative Phase 3 program); Ivermectin (contested); ACEI/ARB class agents; CBT→ME/CFS (contested); terminated Baricitinib 4mg / Montelukast / IgPro20.

## Left draft due to missing / unverified results

- Angiotensin Converting Enzyme Inhibitor → Long COVID (tier D): Class-level agent (ACEI/ARB) without drug-specific supportive LC treatment results in extracted refs.
- Angiotensin Ii Receptor Blockers → Long COVID (tier D): Class-level agent (ACEI/ARB) without drug-specific supportive LC treatment results in extracted refs.
- Baricitinib → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Compound Ciwujia Granules, Guipi Granules → ME/CFS (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Dapagliflozin → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Fluvoxamine → ME/CFS (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Gcjbp Laennec Inj. → ME/CFS (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Hyperbaric Oxygen Therapy (HBOT) → ME/CFS (tier C): ME/CFS-specific HBOT trial is recruiting (NCT07621068); one prospective cohort PMID exists. No completed confirmatory RCT results → C draft,
- Hyperbaric Oxygen Therapy (HBOT) → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Immulina Tm → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Ivabradine → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Losartan → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Metformin → ME/CFS (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Pirfenidone → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Prednisolone → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Pycnogenol® → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Regenecyte → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Remdesivir → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Shengmai Liquid → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Sirolimus (low-dose Rapamycin) → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Solriamfetol Oral Tablet [Sunosi] → ME/CFS (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Testofen → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Thiamine (Vitamin B1) → Long COVID (tier C): Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- Upadacitinib → Long COVID (tier C): Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- Sildenafil → ME/CFS (tier C): Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- Sodium Oxybate → ME/CFS (tier C): Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.

## Human-locked claims (session prior)

- `osmf:claim:agent-amphetamine-dextroamphetamine-treats-long-covid` → **C/published** — Previously human-graded C/published by MattH55 (2026-09-19); retained after evidence check (terminated small Phase 4, n=7).
- `osmf:claim:agent-ampligen-treats-me-cfs` → **C/published** — Previously human-graded C/published by MattH55 (2026-09-19); retained (completed Phase 3 Ampligen CFS trial exists but results contested/not broadly approved).

## Tier C

### Amphetamine-Dextroamphetamine → Long COVID
- **claim_id:** `osmf:claim:agent-amphetamine-dextroamphetamine-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `high`
- **note:** human-locked (claims 1–2 session)
- **rationale:** Previously human-graded C/published by MattH55 (2026-09-19); retained after evidence check (terminated small Phase 4, n=7).
- **evidence_summary:** Human-locked claim retained as tier C. Linked trial(s): NCT05597722:TERMINATED. Literature search '(Amphetamine-Dextroamphetamine) AND ("long COVID" OR "post-COVID" OR PASC)' returned 33 Europe PMC hits. Evidence remains early/contested rather than consensus clinical support.
- **gaps:** Full systematic review of published outcomes not performed
- **references:**
  - [nct] NCT05597722 — Addressing Cognitive Fog in Long-COVID-19 Patients, TERMINATED, PHASE4
  - [pmid] 35673334 — 2022 Guidelines of the Taiwan Society of Cardiology and the Taiwan Hypertension Society for the Mana
  - [pmid] 36899952 — Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutic
  - [pmid] 37344737 — Long COVID and possible preventive options.
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 37655303 — Long COVID as a functional somatic symptom disorder caused by abnormally precise prior expectations 
  - [pubmed_search] (Amphetamine-Dextroamphetamine) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (33 hits)

### Ampligen → ME/CFS
- **claim_id:** `osmf:claim:agent-ampligen-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `high`
- **note:** human-locked (claims 1–2 session)
- **rationale:** Previously human-graded C/published by MattH55 (2026-09-19); retained (completed Phase 3 Ampligen CFS trial exists but results contested/not broadly approved).
- **evidence_summary:** Human-locked claim retained as tier C. Linked trial(s): NCT00215800:COMPLETED. Literature search '(Ampligen OR rintatolimod) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")' returned 136 Europe PMC hits. Evidence remains early/contested rather than consensus clinical support.
- **gaps:** Full systematic review of published outcomes not performed
- **references:**
  - [nct] NCT00215800 — The Study of the Safety and Efficacy of Ampligen in Chronic Fatigue Syndrome, COMPLETED, PHASE3
  - [pmid] 18202435 — Sensing of viral infection and activation of innate immunity by toll-like receptor 3.
  - [pmid] 20713100 — TLR-based immune adjuvants.
  - [pmid] 24316048 — Toll-like receptors in antiviral innate immunity.
  - [pmid] 29730580 — Toll-like receptors in immunity and inflammatory diseases: Past, present, and future.
  - [pmid] 34024217 — Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.
  - [pubmed_search] (Ampligen OR rintatolimod) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (136 hits)

### Baricitinib → Long COVID
- **claim_id:** `osmf:claim:agent-baricitinib-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Baricitinib → Long COVID: NCT06631287 (RECRUITING, phase=PHASE3, n=550, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 33743212: COVID-19 and the human innate immune system.; PMID 35216673: A blood atlas of COVID-19 defines hallmarks of disease severity and specificity.; PMID 35271343: The immunology and immunopathology of COVID-19.. Europe PMC query `(Baricitinib) AND ("long COVID" OR "post-COVID" OR PASC)` → 882 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT06631287 — Randomized Double-Blind Placebo-Controlled Trial EValuating Baricitinib on PERSistent NEurologic and, RECRUITING, PHASE3
  - [pmid] 33743212 — COVID-19 and the human innate immune system.
  - [pmid] 35216673 — A blood atlas of COVID-19 defines hallmarks of disease severity and specificity.
  - [pmid] 35271343 — The immunology and immunopathology of COVID-19.
  - [pmid] 36253560 — Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential t
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pubmed_search] (Baricitinib) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (882 hits)

### Compound Ciwujia Granules, Guipi Granules → ME/CFS
- **claim_id:** `osmf:claim:agent-compound-ciwujia-granules-guipi-granules-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Compound Ciwujia Granules, Guipi Granules → ME/CFS: NCT06245642 (COMPLETED, phase=PHASE4, n=235, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 42543377: [Compound Ciwujia Granules for chronic fatigue syndrome with syndrome of deficiency of both heart and spleen: a multicen. Europe PMC query `(Compound Ciwujia Granules, Guipi Granules) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 1 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT06245642 — Compound Ciwujia Granules Treat Chronic Fatigue Syndrome, COMPLETED, PHASE4
  - [pmid] 42543377 — [Compound Ciwujia Granules for chronic fatigue syndrome with syndrome of deficiency of both heart an
  - [pubmed_search] (Compound Ciwujia Granules, Guipi Granules) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (1 hits)

### Dapagliflozin → Long COVID
- **claim_id:** `osmf:claim:agent-dapagliflozin-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Dapagliflozin → Long COVID: NCT06907251 (NOT_YET_RECRUITING, phase=PHASE3, n=192, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 35176758: Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.; PMID 37076602: Therapeutic strategies for COVID-19: progress and lessons learned.. Europe PMC query `(Dapagliflozin) AND ("long COVID" OR "post-COVID" OR PASC)` → 154 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT06907251 — Dapagliflozin for Long COVID Syndrome, NOT_YET_RECRUITING, PHASE3
  - [pmid] 35176758 — Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Dapagliflozin) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (154 hits)

### Fluvoxamine → Long COVID
- **claim_id:** `osmf:claim:agent-fluvoxamine-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** Completed Long COVID fluvoxamine RCT (NCT05874037) has posted CT.gov results with larger mean symptom-score reduction vs placebo (-47.3 vs -31.1); still single-trial / early clinical without guideline consensus → C published, not B. Other linked trials include acute COVID (off-target) and additional LC work without fully curated endpoints.
- **evidence_summary:** NCT05874037 (Fluvoxamine for Long COVID-19; Phase 2/3, n=191 actual) posted primary outcome Change in Total Symptom Scores: fluvoxamine mean change -47.3 (SD 8.1) vs placebo -31.1 (SD 7.0). This is an early clinical efficacy signal but not multi-trial consensus. NCT06128967 (REVIVE; includes fluvoxamine/metformin arms) completed without results posted in this pass; NCT04510194 is acute COVID progression (off-target for established LC treatment). Europe PMC search returned additional literature. Limitations: single positive registry result package, symptom self-report primary, not a systematic review.
- **gaps:** Independent replication / peer-reviewed primary publication review; Statistical significance details and secondary endpoints curation
- **references:**
  - [nct] NCT05874037 — Fluvoxamine for Long COVID-19, COMPLETED, PHASE2,PHASE3
  - [nct] NCT07359482 — sElective Serotonin reuPtake inhibitoRs In posT-covid After COVID-19, RECRUITING, PHASE3
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [nct] NCT06128967 — A Multicenter, Adaptive, Randomized, doublE-blinded, Placebo-controlled Study in Participants With L, COMPLETED, PHASE3
  - [pmid] 33180097 — Fluvoxamine vs Placebo and Clinical Deterioration in Outpatients With Symptomatic COVID-19: A Random
  - [pmid] 35987197 — Neurological and psychiatric risk trajectories after SARS-CoV-2 infection: an analysis of 2-year ret
  - [pmid] 36253560 — Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential t
  - [pmid] 36631691 — Innate immune evasion strategies of SARS-CoV-2.

### Fluvoxamine → ME/CFS
- **claim_id:** `osmf:claim:agent-fluvoxamine-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 4 registry trial(s) for Fluvoxamine → ME/CFS: NCT05874037 (COMPLETED, phase=PHASE2,PHASE3, n=191, relevant=False); NCT07359482 (RECRUITING, phase=PHASE3, n=160, relevant=False); NCT04510194 (COMPLETED, phase=PHASE3, n=1323, relevant=False); NCT06128967 (COMPLETED, phase=PHASE3, n=399, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 19428959: 5-HT(1A) receptor function in major depressive disorder.; PMID 23459093: The Efficacy of Cognitive Behavioral Therapy: A Review of Meta-analyses.; PMID 33666147: Lessons learned 1 year after SARS-CoV-2 emergence leading to COVID-19 pandemic.. Europe PMC query `(Fluvoxamine) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 157 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05874037 — Fluvoxamine for Long COVID-19, COMPLETED, PHASE2,PHASE3
  - [nct] NCT07359482 — sElective Serotonin reuPtake inhibitoRs In posT-covid After COVID-19, RECRUITING, PHASE3
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [nct] NCT06128967 — A Multicenter, Adaptive, Randomized, doublE-blinded, Placebo-controlled Study in Participants With L, COMPLETED, PHASE3
  - [pmid] 19428959 — 5-HT(1A) receptor function in major depressive disorder.
  - [pmid] 23459093 — The Efficacy of Cognitive Behavioral Therapy: A Review of Meta-analyses.
  - [pmid] 33666147 — Lessons learned 1 year after SARS-CoV-2 emergence leading to COVID-19 pandemic.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.

### Gcjbp Laennec Inj. → ME/CFS
- **claim_id:** `osmf:claim:agent-gcjbp-laennec-inj-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Gcjbp Laennec Inj. → ME/CFS: NCT01742013 (COMPLETED, phase=PHASE3, n=78, relevant=True). No posted CT.gov results found in this pass. Europe PMC query `(Gcjbp Laennec Inj.) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 0 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT01742013 — Investigator Initiated Clinical Study to Explore the Efficacy and Safety of Human Placenta Hydrolysa, COMPLETED, PHASE3
  - [pubmed_search] (Gcjbp Laennec Inj.) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (0 hits)

### Hyperbaric Oxygen Therapy (HBOT) → ME/CFS
- **claim_id:** `osmf:claim:agent-hyperbaric-oxygen-therapy-hbot-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** ME/CFS-specific HBOT trial is recruiting (NCT07621068); one prospective cohort PMID exists. No completed confirmatory RCT results → C draft, not B/D.
- **evidence_summary:** HBOT for ME/CFS has a dedicated recruiting interventional trial (NCT07621068, n≈74, sham-controlled) and a small prospective cohort report in tracker literature (PMID 42249466). Other linked HBOT registry entries primarily target Long COVID/PASC rather than ME/CFS. Without completed positive confirmatory trials, evidence remains early clinical/mechanistic (tier C). Europe PMC search returned hits but does not establish consensus efficacy.
- **gaps:** Completed sham-controlled RCT results in ME/CFS; Not a systematic review
- **references:**
  - [nct] NCT06452095 — Recovering From COVID-19 Lingering Symptoms Adaptive Integrative Medicine Trial - Effect of Hyperbar, RECRUITING, NA
  - [nct] NCT04842448 — Safety and Efficacy of Hyperbaric Oxygen Therapy for Long COVID Syndrome, COMPLETED, PHASE2
  - [nct] NCT06267300 — Treatment of Post-COVID-19 With Hyperbaric Oxygen Therapy: a Randomized, Controlled Trial, UNKNOWN, PHASE3
  - [nct] NCT04905888 — Hyperbaric Oxygen for Long COVID-19 Pulmonary Sequela, WITHDRAWN, PHASE2
  - [nct] NCT07621068 — Hyperbaric Oxygen Therapy for Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS), RECRUITING, NA
  - [pmid] 24752591 — The glutathione system: a new drug target in neuroimmune disorders.
  - [pmid] 28506916 — 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement on catheter and surgical ablation of atr
  - [pmid] 34067776 — Post-COVID-19 Syndrome and the Potential Benefits of Exercise.

### Hyperbaric Oxygen Therapy (HBOT) → Long COVID
- **claim_id:** `osmf:claim:agent-hyperbaric-oxygen-therapy-hbot-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 5 registry trial(s) for Hyperbaric Oxygen Therapy (HBOT) → Long COVID: NCT06452095 (RECRUITING, phase=NA, n=120, relevant=True); NCT04842448 (COMPLETED, phase=PHASE2, n=80, relevant=True); NCT06267300 (UNKNOWN, phase=PHASE3, n=120, relevant=True); NCT04905888 (WITHDRAWN, phase=PHASE2, n=0, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 34067776: Post-COVID-19 Syndrome and the Potential Benefits of Exercise.; PMID 34163217: The Conundrum of 'Long-COVID-19': A Narrative Review.; PMID 35875883: Long COVID and the cardiovascular system-elucidating causes and cellular mechanisms in order to develop targeted diagnos. Europe PMC query `("hyperbaric oxygen" OR HBOT) AND ("long COVID" OR "post-COVID" OR PASC)` → 359 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT06452095 — Recovering From COVID-19 Lingering Symptoms Adaptive Integrative Medicine Trial - Effect of Hyperbar, RECRUITING, NA
  - [nct] NCT04842448 — Safety and Efficacy of Hyperbaric Oxygen Therapy for Long COVID Syndrome, COMPLETED, PHASE2
  - [nct] NCT06267300 — Treatment of Post-COVID-19 With Hyperbaric Oxygen Therapy: a Randomized, Controlled Trial, UNKNOWN, PHASE3
  - [nct] NCT04905888 — Hyperbaric Oxygen for Long COVID-19 Pulmonary Sequela, WITHDRAWN, PHASE2
  - [nct] NCT07621068 — Hyperbaric Oxygen Therapy for Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS), RECRUITING, NA
  - [pmid] 34067776 — Post-COVID-19 Syndrome and the Potential Benefits of Exercise.
  - [pmid] 34163217 — The Conundrum of 'Long-COVID-19': A Narrative Review.
  - [pmid] 35875883 — Long COVID and the cardiovascular system-elucidating causes and cellular mechanisms in order to deve

### Immulina Tm → Long COVID
- **claim_id:** `osmf:claim:agent-immulina-tm-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Immulina Tm → Long COVID: NCT05524532 (COMPLETED, phase=PHASE3, n=101, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 35204236: Cyanobacteria and Algae-Derived Bioactive Metabolites as Antiviral Agents: Evidence, Mode of Action, and Scope for Furth; PMID 37388814: The pathophysiology of postacute sequelae of COVID-19 (PASC): Possible role for persistent inflammation.; PMID 39179099: Inflammatory pathways in patients with post-acute sequelae of COVID-19: The role of the clinical immunologist.. Europe PMC query `(Immulina OR "Spirulina extract") AND ("long COVID" OR "post-COVID" OR PASC)` → 7 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05524532 — Effects of Immulina TM Supplements With PASC Patients, COMPLETED, PHASE3
  - [pmid] 35204236 — Cyanobacteria and Algae-Derived Bioactive Metabolites as Antiviral Agents: Evidence, Mode of Action,
  - [pmid] 37388814 — The pathophysiology of postacute sequelae of COVID-19 (PASC): Possible role for persistent inflammat
  - [pmid] 39179099 — Inflammatory pathways in patients with post-acute sequelae of COVID-19: The role of the clinical imm
  - [pmid] 40722944 — Post-COVID Condition and Neuroinflammation: Possible Management with Antioxidants.
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [pubmed_search] (Immulina OR "Spirulina extract") AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (7 hits)

### Intravenous Immunoglobulin (IVIG) → Long COVID
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- **evidence_summary:** Extracted 2 registry trial(s) for Intravenous Immunoglobulin (IVIG) → Long COVID: NCT06305793 (COMPLETED, phase=PHASE2, n=200, relevant=True); NCT06305780 (COMPLETED, phase=PHASE2, n=381, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33428867: 6-month consequences of COVID-19 in patients discharged from hospital: a cohort study.; PMID 33753937: Post-acute COVID-19 syndrome.; PMID 36639608: Long COVID: major findings, mechanisms and recommendations.. Europe PMC query `(IVIG OR "intravenous immunoglobulin") AND ("long COVID" OR "post-COVID" OR PASC)` → 1960 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06305793 — RECOVER-AUTONOMIC: Platform Protocol, Appendix A (IVIG), COMPLETED, PHASE2
  - [nct] NCT06305780 — RECOVER-AUTONOMIC Platform Protocol, COMPLETED, PHASE2
  - [pmid] 33428867 — 6-month consequences of COVID-19 in patients discharged from hospital: a cohort study.
  - [pmid] 33753937 — Post-acute COVID-19 syndrome.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 42137701 — Isolated Arterial Hypertension as a Rare Early Manifestation of Guillain-Barré Syndrome: A Case Repo

### Intravenous Immunoglobulin (IVIG) → POTS
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-pots`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- **evidence_summary:** Extracted 2 registry trial(s) for Intravenous Immunoglobulin (IVIG) → POTS: NCT06305793 (COMPLETED, phase=PHASE2, n=200, relevant=True); NCT06305780 (COMPLETED, phase=PHASE2, n=381, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33753937: Post-acute COVID-19 syndrome.; PMID 34144933: Postural orthostatic tachycardia syndrome (POTS): State of the science and clinical care from a 2019 National Institutes; PMID 34319569: Long COVID, a comprehensive systematic scoping review.. Europe PMC query `(IVIG OR "intravenous immunoglobulin") AND ("postural orthostatic tachycardia" OR POTS)` → 343 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06305793 — RECOVER-AUTONOMIC: Platform Protocol, Appendix A (IVIG), COMPLETED, PHASE2
  - [nct] NCT06305780 — RECOVER-AUTONOMIC Platform Protocol, COMPLETED, PHASE2
  - [pmid] 33753937 — Post-acute COVID-19 syndrome.
  - [pmid] 34144933 — Postural orthostatic tachycardia syndrome (POTS): State of the science and clinical care from a 2019
  - [pmid] 34319569 — Long COVID, a comprehensive systematic scoping review.
  - [pmid] 34817268 — Long-term complications of COVID-19.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 42137701 — Isolated Arterial Hypertension as a Rare Early Manifestation of Guillain-Barré Syndrome: A Case Repo

### Ivabradine → Long COVID
- **claim_id:** `osmf:claim:agent-ivabradine-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 2 registry trial(s) for Ivabradine → Long COVID: NCT06305806 (COMPLETED, phase=PHASE2, n=181, relevant=True); NCT05481177 (UNKNOWN, phase=PHASE4, n=250, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 32201335: Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID-19 Pandemic.; PMID 34024217: Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.; PMID 35176758: Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.. Europe PMC query `(Ivabradine) AND ("long COVID" OR "post-COVID" OR PASC)` → 264 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT06305806 — RECOVER-AUTONOMIC: Platform Protocol, Appendix B (Ivabradine), COMPLETED, PHASE2
  - [nct] NCT05481177 — Ivabradine for Long-Term Effects of COVID-19 With POTS Cohort, UNKNOWN, PHASE4
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 34024217 — Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.
  - [pmid] 35176758 — Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.
  - [pmid] 35307156 — 2022 ACC Expert Consensus Decision Pathway on Cardiovascular Sequelae of COVID-19 in Adults: Myocard
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pubmed_search] (Ivabradine) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (264 hits)

### Lisdexamfetamine Dimesylate → ME/CFS
- **claim_id:** `osmf:claim:agent-lisdexamfetamine-dimesylate-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- **evidence_summary:** Extracted 1 registry trial(s) for Lisdexamfetamine Dimesylate → ME/CFS: NCT01071044 (COMPLETED, phase=PHASE4, n=26, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 27189581: Activational and effort-related aspects of motivation: neural mechanisms and implications for psychopathology.; PMID 27480574: Inflammation Effects on Motivation and Motor Activity: Role of Dopamine.; PMID 27664125: Adult ADHD and Comorbid Somatic Disease: A Systematic Literature Review.. Europe PMC query `(lisdexamfetamine OR Vyvanse) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 36 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT01071044 — Efficacy and Safety of Lisdexamfetamine Dimesylate in Adults With Chronic Fatigue Syndrome, COMPLETED, PHASE4
  - [pmid] 27189581 — Activational and effort-related aspects of motivation: neural mechanisms and implications for psycho
  - [pmid] 27480574 — Inflammation Effects on Motivation and Motor Activity: Role of Dopamine.
  - [pmid] 27664125 — Adult ADHD and Comorbid Somatic Disease: A Systematic Literature Review.
  - [pmid] 29173175 — Imaging the Role of Inflammation in Mood and Anxiety-related Disorders.
  - [pmid] 31394725 — Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: A Comprehensive Review.
  - [pubmed_search] (lisdexamfetamine OR Vyvanse) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (36 hits)

### Losartan → Long COVID
- **claim_id:** `osmf:claim:agent-losartan-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Losartan → Long COVID: NCT05619653 (ACTIVE_NOT_RECRUITING, phase=PHASE3, n=279, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 32750108: Endothelial dysfunction in COVID-19: a position paper of the ESC Working Group for Atherosclerosis and Vascular Biology,; PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 36253560: Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential therapies.. Europe PMC query `(Losartan) AND ("long COVID" OR "post-COVID" OR PASC)` → 274 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT05619653 — Myocardial Protection in Patients With Post-acute Inflammatory Cardiac Involvement Due to COVID-19, ACTIVE_NOT_RECRUITING, PHASE3
  - [pmid] 32750108 — Endothelial dysfunction in COVID-19: a position paper of the ESC Working Group for Atherosclerosis a
  - [pmid] 33909761 — Brazilian Guidelines of Hypertension - 2020.
  - [pmid] 36253560 — Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential t
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 37518181 — Cellular mechanotransduction in health and diseases: from molecular mechanism to therapeutic targets
  - [pubmed_search] (Losartan) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (274 hits)

### Metformin → ME/CFS
- **claim_id:** `osmf:claim:agent-metformin-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 3 registry trial(s) for Metformin → ME/CFS: NCT04510194 (COMPLETED, phase=PHASE3, n=1323, relevant=False); NCT06128967 (COMPLETED, phase=PHASE3, n=399, relevant=True); NCT06147050 (UNKNOWN, phase=PHASE3, n=16, relevant=False). No posted CT.gov results found in this pass. Literature notes: PMID 18923511: The molecular neurobiology of depression.; PMID 23798298: Lack of exercise is a major cause of chronic diseases.; PMID 30317530: An insight into gut microbiota and its functionalities.. Europe PMC query `(Metformin) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 422 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [nct] NCT06128967 — A Multicenter, Adaptive, Randomized, doublE-blinded, Placebo-controlled Study in Participants With L, COMPLETED, PHASE3
  - [nct] NCT06147050 — Effect of Metformin in Reducing Fatigue in Long COVID in Adolescents, UNKNOWN, PHASE3
  - [pmid] 18923511 — The molecular neurobiology of depression.
  - [pmid] 23798298 — Lack of exercise is a major cause of chronic diseases.
  - [pmid] 30317530 — An insight into gut microbiota and its functionalities.
  - [pmid] 30496104 — Global, regional, and national incidence, prevalence, and years lived with disability for 354 diseas
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.

### Metformin → Long COVID
- **claim_id:** `osmf:claim:agent-metformin-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** COVID-OUT / related work supports a prevention signal for incident long COVID; treatment of established LC remains early/limited → C not B.
- **evidence_summary:** Metformin has a notable signal for reducing incidence of long COVID after acute infection in randomized data, but that is prevention rather than treatment of established Long COVID. Linked trials: NCT04510194:COMPLETED, NCT06128967:COMPLETED, NCT06147050:UNKNOWN. Literature includes preclinical GWI work and PACVS map notes. Search hits=1165.
- **gaps:** Dedicated large RCTs for treatment of established Long COVID with posted results
- **references:**
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [nct] NCT06128967 — A Multicenter, Adaptive, Randomized, doublE-blinded, Placebo-controlled Study in Participants With L, COMPLETED, PHASE3
  - [nct] NCT06147050 — Effect of Metformin in Reducing Fatigue in Long COVID in Adolescents, UNKNOWN, PHASE3
  - [pmid] 35668219 — The burden and risks of emerging complications of diabetes mellitus.
  - [pmid] 36050306 — Lactate metabolism in human health and disease.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass

### Paxlovid (Nirmatrelvir + Ritonavir) → Long COVID
- **claim_id:** `osmf:claim:agent-paxlovid-nirmatrelvir-ritonavir-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** Multiple Phase 2 LC trials exist; results mixed/limited for established PASC—early clinical signal tier C, not B.
- **evidence_summary:** Nirmatrelvir/ritonavir has been tested for post-COVID / long COVID in several trials; available public results are mixed and do not yet constitute solid consensus treatment evidence. Trial statuses: NOT_YET_RECRUITING, COMPLETED, COMPLETED, ACTIVE_NOT_RECRUITING, COMPLETED. Search hits=1525.
- **gaps:** Clear positive Phase 3 treatment results for established LC not confirmed in this pass
- **references:**
  - [nct] NCT07597902 — SARS-CoV-2 and Herpesvirus Inhibition for Ending Long COVID Dysfunction, NOT_YET_RECRUITING, PHASE2
  - [nct] NCT05965726 — RECOVER-VITAL: Platform Protocol, Appendix to Measure the Effects of Paxlovid on Long COVID Symptoms, COMPLETED, PHASE2
  - [nct] NCT05595369 — RECOVER-VITAL: Platform Protocol to Measure the Effects of Antiviral Therapies on Long COVID Symptom, COMPLETED, PHASE2
  - [nct] NCT05852873 — PAxlovid loNg cOvid-19 pRevention triAl With recruitMent In the Community in Norway, ACTIVE_NOT_RECRUITING, PHASE3
  - [nct] NCT05576662 — Paxlovid for Treatment of Long Covid, COMPLETED, PHASE2
  - [pmid] 35271343 — The immunology and immunopathology of COVID-19.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 36951832 — Risk Factors Associated With Post-COVID-19 Condition: A Systematic Review and Meta-analysis.

### Pirfenidone → Long COVID
- **claim_id:** `osmf:claim:agent-pirfenidone-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Pirfenidone → Long COVID: NCT06928272 (RECRUITING, phase=PHASE3, n=348, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 32201335: Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID-19 Pandemic.; PMID 32422178: Pulmonary fibrosis and COVID-19: the potential role for antifibrotic therapy.; PMID 33609255: A Review of Persistent Post-COVID Syndrome (PPCS).. Europe PMC query `(Pirfenidone) AND ("long COVID" OR "post-COVID" OR PASC)` → 407 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT06928272 — Long Covid (LC)-REVITALIZE - A Long Covid Repurposed Drug Study, RECRUITING, PHASE3
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 32422178 — Pulmonary fibrosis and COVID-19: the potential role for antifibrotic therapy.
  - [pmid] 33609255 — A Review of Persistent Post-COVID Syndrome (PPCS).
  - [pmid] 35176758 — Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pubmed_search] (Pirfenidone) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (407 hits)

### Prednisolone → Long COVID
- **claim_id:** `osmf:claim:agent-prednisolone-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Prednisolone → Long COVID: NCT05619653 (ACTIVE_NOT_RECRUITING, phase=PHASE3, n=279, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 32201335: Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID-19 Pandemic.; PMID 32637987: The emerging spectrum of COVID-19 neurology: clinical, radiological and laboratory findings.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.. Europe PMC query `(Prednisolone) AND ("long COVID" OR "post-COVID" OR PASC)` → 2547 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT05619653 — Myocardial Protection in Patients With Post-acute Inflammatory Cardiac Involvement Due to COVID-19, ACTIVE_NOT_RECRUITING, PHASE3
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 32637987 — The emerging spectrum of COVID-19 neurology: clinical, radiological and laboratory findings.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Prednisolone) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (2547 hits)

### Pycnogenol® → Long COVID
- **claim_id:** `osmf:claim:agent-pycnogenol-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Pycnogenol® → Long COVID: NCT05890534 (COMPLETED, phase=PHASE3, n=153, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 35566252: Flavonoids as Potential Anti-Inflammatory Molecules: A Review.; PMID 36043493: The potential role of ischaemia-reperfusion injury in chronic, relapsing diseases such as rheumatoid arthritis, Long COV; PMID 36364899: A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.. Europe PMC query `(Pycnogenol OR "French maritime pine") AND ("long COVID" OR "post-COVID" OR PASC)` → 29 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05890534 — Pycnogenol® in Post-COVID-19 Condition, COMPLETED, PHASE3
  - [pmid] 35566252 — Flavonoids as Potential Anti-Inflammatory Molecules: A Review.
  - [pmid] 36043493 — The potential role of ischaemia-reperfusion injury in chronic, relapsing diseases such as rheumatoid
  - [pmid] 36364899 — A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 37080828 — Long COVID: pathophysiological factors and abnormalities of coagulation.
  - [pubmed_search] (Pycnogenol OR "French maritime pine") AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (29 hits)

### Regenecyte → Long COVID
- **claim_id:** `osmf:claim:agent-regenecyte-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 2 registry trial(s) for Regenecyte → Long COVID: NCT07184385 (NOT_YET_RECRUITING, phase=PHASE3, n=60, relevant=True); NCT05682560 (COMPLETED, phase=PHASE2, n=30, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 41625963: REGENECYTE cord blood cell therapy in post-COVID syndrome: a phase IIa randomized, placebo-controlled trial.. Europe PMC query `(Regenecyte) AND ("long COVID" OR "post-COVID" OR PASC)` → 1 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT07184385 — A Study of Human Umbilical Cord Blood (REGENECYTE) Infusion in Patients With Post-COVID Condition, NOT_YET_RECRUITING, PHASE3
  - [nct] NCT05682560 — Human Umbilical Cord Blood (RegeneCyte) Infusion in Patients with Post-COVID Syndrome, COMPLETED, PHASE2
  - [pmid] 41625963 — REGENECYTE cord blood cell therapy in post-COVID syndrome: a phase IIa randomized, placebo-controlle
  - [pubmed_search] (Regenecyte) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1 hits)

### Remdesivir → Long COVID
- **claim_id:** `osmf:claim:agent-remdesivir-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Remdesivir → Long COVID: NCT05911906 (COMPLETED, phase=PHASE4, n=73, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 32201335: Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID-19 Pandemic.; PMID 33146552: Global Initiative for the Diagnosis, Management, and Prevention of Chronic Obstructive Lung Disease. The 2020 GOLD Scien; PMID 33892403: Long COVID: An overview.. Europe PMC query `(Remdesivir) AND ("long COVID" OR "post-COVID" OR PASC)` → 3586 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05911906 — An Open-label, Clinical Feasibility Study of the Efficacy of Remdesivir for Long-COVID., COMPLETED, PHASE4
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 33146552 — Global Initiative for the Diagnosis, Management, and Prevention of Chronic Obstructive Lung Disease.
  - [pmid] 33892403 — Long COVID: An overview.
  - [pmid] 35271343 — The immunology and immunopathology of COVID-19.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pubmed_search] (Remdesivir) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (3586 hits)

### Shengmai Liquid → Long COVID
- **claim_id:** `osmf:claim:agent-shengmai-liquid-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Shengmai Liquid → Long COVID: NCT06980636 (RECRUITING, phase=PHASE4, n=100, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 37810369: Expert consensus on the use of traditional Chinese medicine for the treatment of common symptoms of post-COVID-19 short-; PMID 38579075: Advances in the application of traditional Chinese medicine during the COVID-19 recovery period: A review.; PMID 40671020: Efficacy and safety of traditional Chinese medicine for post-COVID-19 syndrome: a systematic review and meta-analysis.. Europe PMC query `(Shengmai) AND ("long COVID" OR "post-COVID" OR PASC)` → 10 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT06980636 — A Trial of Shengmai Liquid for Long COVID Fatigue., RECRUITING, PHASE4
  - [pmid] 37810369 — Expert consensus on the use of traditional Chinese medicine for the treatment of common symptoms of 
  - [pmid] 38579075 — Advances in the application of traditional Chinese medicine during the COVID-19 recovery period: A r
  - [pmid] 40671020 — Efficacy and safety of traditional Chinese medicine for post-COVID-19 syndrome: a systematic review 
  - [pmid] 42296071 — Shengmai Liquid (Chinese Patent Medicine) for the Treatment of Post-COVID-19 Fatigue: A Protocol for
  - [pmid] 42719314 — Nrf2 as a therapeutic target of ginseng: A comprehensive review from preclinical evidence to clinica
  - [pubmed_search] (Shengmai) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (10 hits)

### Sildenafil → ME/CFS
- **claim_id:** `osmf:claim:agent-sildenafil-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- **evidence_summary:** Extracted 1 registry trial(s) for Sildenafil → ME/CFS: NCT00598585 (COMPLETED, phase=PHASE4, n=12, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 28506916: 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement on catheter and surgical ablation of atrial fibrillation.; PMID 34686843: Cardiac involvement in the long-term implications of COVID-19.; PMID 34991982: An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.. Europe PMC query `(Sildenafil) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 113 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT00598585 — Use of Sildenafil (Viagra) to Alter Fatigue, Functional Status and Impaired Cerebral Blood Flow in P, COMPLETED, PHASE4
  - [pmid] 28506916 — 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement on catheter and surgical ablation of atr
  - [pmid] 34686843 — Cardiac involvement in the long-term implications of COVID-19.
  - [pmid] 34991982 — An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - [pmid] 36364899 — A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.
  - [pmid] 39083764 — Long Covid Defined.
  - [pubmed_search] (Sildenafil) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (113 hits)

### Sirolimus (low-dose Rapamycin) → Long COVID
- **claim_id:** `osmf:claim:agent-sirolimus-low-dose-rapamycin-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 2 registry trial(s) for Sirolimus (low-dose Rapamycin) → Long COVID: NCT06960928 (RECRUITING, phase=PHASE3, n=80, relevant=True); NCT04948203 (ACTIVE_NOT_RECRUITING, phase=PHASE2,PHASE3, n=60, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 32422178: Pulmonary fibrosis and COVID-19: the potential role for antifibrotic therapy.; PMID 35668219: The burden and risks of emerging complications of diabetes mellitus.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.. Europe PMC query `(sirolimus OR rapamycin) AND ("long COVID" OR "post-COVID" OR PASC)` → 1157 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT06960928 — Low Dose Sirolimus in People With Post-Acute Sequelae of COVID-19 (PASC) Long COVID-19, RECRUITING, PHASE3
  - [nct] NCT04948203 — Assessing the Efficacy of Sirolimus in Patients With COVID-19 Pneumonia for Prevention of Post-COVID, ACTIVE_NOT_RECRUITING, PHASE2,PHASE3
  - [pmid] 32422178 — Pulmonary fibrosis and COVID-19: the potential role for antifibrotic therapy.
  - [pmid] 35668219 — The burden and risks of emerging complications of diabetes mellitus.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (sirolimus OR rapamycin) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1157 hits)

### Sodium Oxybate → ME/CFS
- **claim_id:** `osmf:claim:agent-sodium-oxybate-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- **evidence_summary:** Extracted 3 registry trial(s) for Sodium Oxybate → ME/CFS: NCT01584934 (WITHDRAWN, phase=PHASE4, n=0, relevant=True); NCT02055898 (COMPLETED, phase=PHASE4, n=13, relevant=True); NCT00498485 (TERMINATED, phase=PHASE4, n=17, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 19225604: Fibromyalgia: presentation and management with a focus on pharmacological treatment.; PMID 22802155: Peripheral and central mechanisms of fatigue in inflammatory and noninflammatory rheumatic diseases.; PMID 22811766: Fibromyalgia syndrome: an overview of pathophysiology, diagnosis and management.. Europe PMC query `("sodium oxybate" OR Xyrem) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 44 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT01584934 — Sodium Oxybate in Patients With Chronic Fatigue Syndrome., WITHDRAWN, PHASE4
  - [nct] NCT02055898 — SWS And Daytime Functioning in Chronic FatiguE Syndrome (SAFFE), COMPLETED, PHASE4
  - [nct] NCT00498485 — Use of Xyrem to Improve Sleep in Chronic Fatigue Syndrome, TERMINATED, PHASE4
  - [pmid] 19225604 — Fibromyalgia: presentation and management with a focus on pharmacological treatment.
  - [pmid] 22802155 — Peripheral and central mechanisms of fatigue in inflammatory and noninflammatory rheumatic diseases.
  - [pmid] 22811766 — Fibromyalgia syndrome: an overview of pathophysiology, diagnosis and management.
  - [pmid] 24289848 — Beyond pain in fibromyalgia: insights into the symptom of fatigue.
  - [pmid] 24348701 — Treatment of fibromyalgia syndrome: recommendations of recent evidence-based interdisciplinary guide

### Solriamfetol Oral Tablet [Sunosi] → ME/CFS
- **claim_id:** `osmf:claim:agent-solriamfetol-oral-tablet-sunosi-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Solriamfetol Oral Tablet [Sunosi] → ME/CFS: NCT04622293 (COMPLETED, phase=PHASE4, n=44, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 39125722: Comprehensive Review of COVID-19: Epidemiology, Pathogenesis, Advancement in Diagnostic and Detection Techniques, and Po; PMID 39150700: Insights from a 10-year Australasian idiopathic hypersomnia patient data registry study.; PMID 40046430: Neurological sequelae of long COVID: a comprehensive review of diagnostic imaging, underlying mechanisms, and potential . Europe PMC query `(solriamfetol OR Sunosi) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 15 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT04622293 — A Trial of Solriamfetol in the Treatment of Myalgic Encephalomyelitis/Chronic Fatigue Syndrome, COMPLETED, PHASE4
  - [pmid] 39125722 — Comprehensive Review of COVID-19: Epidemiology, Pathogenesis, Advancement in Diagnostic and Detectio
  - [pmid] 39150700 — Insights from a 10-year Australasian idiopathic hypersomnia patient data registry study.
  - [pmid] 40046430 — Neurological sequelae of long COVID: a comprehensive review of diagnostic imaging, underlying mechan
  - [pmid] 40261198 — Multidisciplinary collaborative guidance on the assessment and treatment of patients with Long COVID
  - [pmid] 41076550 — Orexin Deficiency in Narcolepsy: Molecular Mechanisms, Clinical Phenotypes, and Emerging Therapeutic
  - [pubmed_search] (solriamfetol OR Sunosi) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (15 hits)

### Somatropin → Long COVID
- **claim_id:** `osmf:claim:agent-somatropin-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`
- **rationale:** Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.
- **evidence_summary:** Extracted 1 registry trial(s) for Somatropin → Long COVID: NCT03554265 (COMPLETED, phase=PHASE3, n=72, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 36334362: An improved Fuzzy based GWO algorithm for predicting the potential host receptor of COVID-19 infection.; PMID 36969241: Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOVER initiative.; PMID 37680987: The current landscape of long COVID clinical trials: NIH's RECOVER to Stanford Medicine's STOP-PASC initiative.. Europe PMC query `(Somatropin) AND ("long COVID" OR "post-COVID" OR PASC)` → 9 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03554265 — Brain and Gut Plasticity in Mild TBI or Post-acute COVID Syndrome Following Growth Hormone Therapy, COMPLETED, PHASE3
  - [pmid] 36334362 — An improved Fuzzy based GWO algorithm for predicting the potential host receptor of COVID-19 infecti
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 37680987 — The current landscape of long COVID clinical trials: NIH's RECOVER to Stanford Medicine's STOP-PASC 
  - [pmid] 37759668 — Literature-Based Discovery to Elucidate the Biological Links between Resistant Hypertension and COVI
  - [pmid] 39382470 — Long COVID syndrome: An unfolding enigma.
  - [pubmed_search] (Somatropin) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (9 hits)

### Testofen → Long COVID
- **claim_id:** `osmf:claim:agent-testofen-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Testofen → Long COVID: NCT05795816 (COMPLETED, phase=PHASE3, n=150, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 39599909: Beyond Antivirals: Alternative Therapies for Long COVID.. Europe PMC query `(Testofen OR "Fenugreek extract") AND ("long COVID" OR "post-COVID" OR PASC)` → 1 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05795816 — Effectiveness of Testofen Compared to Placebo on Long COVID Symptoms, COMPLETED, PHASE3
  - [pmid] 39599909 — Beyond Antivirals: Alternative Therapies for Long COVID.
  - [pubmed_search] (Testofen OR "Fenugreek extract") AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1 hits)

### Thiamine (Vitamin B1) → Long COVID
- **claim_id:** `osmf:claim:agent-thiamine-vitamin-b1-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.
- **evidence_summary:** Extracted 1 registry trial(s) for Thiamine (Vitamin B1) → Long COVID: NCT05642923 (COMPLETED, phase=PHASE4, n=528, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 24661096: Protein design: toward functional metalloenzymes.; PMID 3070321: Linkage map of Salmonella typhimurium, edition VII.; PMID 35269860: The Role of l-Carnitine in Mitochondria, Prevention of Metabolic Inflexibility and Disease Initiation.. Europe PMC query `(Thiamine) AND ("long COVID" OR "post-COVID" OR PASC)` → 253 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05642923 — Post-COVID-19 Chronic Fatigue Syndrome, COMPLETED, PHASE4
  - [pmid] 24661096 — Protein design: toward functional metalloenzymes.
  - [pmid] 3070321 — Linkage map of Salmonella typhimurium, edition VII.
  - [pmid] 35269860 — The Role of l-Carnitine in Mitochondria, Prevention of Metabolic Inflexibility and Disease Initiatio
  - [pmid] 36701528 — Spin Hyperpolarization in Modern Magnetic Resonance.
  - [pmid] 37130947 — Metformin: update on mechanisms of action and repurposing potential.
  - [pubmed_search] (Thiamine) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (253 hits)

### Upadacitinib → Long COVID
- **claim_id:** `osmf:claim:agent-upadacitinib-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`
- **rationale:** Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.
- **evidence_summary:** Extracted 1 registry trial(s) for Upadacitinib → Long COVID: NCT06928272 (RECRUITING, phase=PHASE3, n=348, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 35617780: DMARD disruption, rheumatic disease flare, and prolonged COVID-19 symptom duration after acute COVID-19 among patients w; PMID 36379152: Role of SARS-CoV-2-induced cytokine storm in multi-organ failure: Molecular pathways and potential therapeutic options.; PMID 36516563: Rituximab is associated with worse COVID-19 outcomes in patients with rheumatoid arthritis: A retrospective, nationally . Europe PMC query `(Upadacitinib) AND ("long COVID" OR "post-COVID" OR PASC)` → 88 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Completed results
- **references:**
  - [nct] NCT06928272 — Long Covid (LC)-REVITALIZE - A Long Covid Repurposed Drug Study, RECRUITING, PHASE3
  - [pmid] 35617780 — DMARD disruption, rheumatic disease flare, and prolonged COVID-19 symptom duration after acute COVID
  - [pmid] 36379152 — Role of SARS-CoV-2-induced cytokine storm in multi-organ failure: Molecular pathways and potential t
  - [pmid] 36516563 — Rituximab is associated with worse COVID-19 outcomes in patients with rheumatoid arthritis: A retros
  - [pmid] 37731935 — Global, regional, and national incidence of six major immune-mediated inflammatory diseases: finding
  - [pmid] 40717900 — Macrophages: Subtypes, Distribution, Polarization, Immunomodulatory Functions, and Therapeutics.
  - [pubmed_search] (Upadacitinib) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (88 hits)

## Tier D

### Angiotensin Converting Enzyme Inhibitor → Long COVID
- **claim_id:** `osmf:claim:agent-angiotensin-converting-enzyme-inhibitor-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Class-level agent (ACEI/ARB) without drug-specific supportive LC treatment results in extracted refs.
- **evidence_summary:** Tracker lists a class-level RAS agent for Long COVID. Registry trial(s) reviewed: The COVID-RASi Trial (COVID-19). Without drug-specific completed positive trials and posted results for the named condition, evidence is insufficient for a clinical tier.
- **gaps:** Need drug-specific RCTs with posted results in the target condition
- **references:**
  - [nct] NCT04591210 — The COVID-RASi Trial (COVID-19), COMPLETED, PHASE3
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 32526206 — SARS-CoV-2 Reverse Genetics Reveals a Variable Infection Gradient in the Respiratory Tract.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (ACE inhibitor OR ACEI OR lisinopril OR enalapril) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (4405 hits)

### Angiotensin Ii Receptor Blockers → Long COVID
- **claim_id:** `osmf:claim:agent-angiotensin-ii-receptor-blockers-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Class-level agent (ACEI/ARB) without drug-specific supportive LC treatment results in extracted refs.
- **evidence_summary:** Tracker lists a class-level RAS agent for Long COVID. Registry trial(s) reviewed: The COVID-RASi Trial (COVID-19). Without drug-specific completed positive trials and posted results for the named condition, evidence is insufficient for a clinical tier.
- **gaps:** Need drug-specific RCTs with posted results in the target condition
- **references:**
  - [nct] NCT04591210 — The COVID-RASi Trial (COVID-19), COMPLETED, PHASE3
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 41092926 — Burden of 375 diseases and injuries, risk-attributable burden of 88 risk factors, and healthy life e
  - [pubmed_search] (ARB OR losartan OR valsartan OR "angiotensin receptor") AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1290 hits)

### Baricitinib 4 Mg → Long COVID
- **claim_id:** `osmf:claim:agent-baricitinib-4-mg-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Extracted 1 registry trial(s) for Baricitinib 4 Mg → Long COVID: NCT05858515 (WITHDRAWN, phase=PHASE3, n=0, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 33743212: COVID-19 and the human innate immune system.; PMID 35216673: A blood atlas of COVID-19 defines hallmarks of disease severity and specificity.; PMID 35271343: The immunology and immunopathology of COVID-19.. Europe PMC query `(Baricitinib) AND ("long COVID" OR "post-COVID" OR PASC)` → 882 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Not a systematic review; single-pass registry + Europe PMC sampling
- **references:**
  - [nct] NCT05858515 — REVERSE-Long COVID-19 With Baricitinib Study, WITHDRAWN, PHASE3
  - [pmid] 33743212 — COVID-19 and the human innate immune system.
  - [pmid] 35216673 — A blood atlas of COVID-19 defines hallmarks of disease severity and specificity.
  - [pmid] 35271343 — The immunology and immunopathology of COVID-19.
  - [pmid] 36253560 — Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential t
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pubmed_search] (Baricitinib) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (882 hits)

### Behavioral → Long COVID
- **claim_id:** `osmf:claim:agent-behavioral-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Behavioral' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 11424 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT06441955 — Covid-19 Long Haul Preventative and Health Promotion Care Clinical Trial Acceleration Program., RECRUITING, PHASE4
  - [pmid] 33753937 — Post-acute COVID-19 syndrome.
  - [pmid] 34373540 — More than 50 long-term effects of COVID-19: a systematic review and meta-analysis.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 38493795 — Global, regional, and national burden of disorders affecting the nervous system, 1990-2021: a system
  - [pubmed_search] (Behavioral) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (11424 hits)

### Biopsychological → Long COVID
- **claim_id:** `osmf:claim:agent-biopsychological-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Biopsychological' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 28 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT06441955 — Covid-19 Long Haul Preventative and Health Promotion Care Clinical Trial Acceleration Program., RECRUITING, PHASE4
  - [pmid] 34678213 — Addressing the post-acute sequelae of SARS-CoV-2 infection: a multidisciplinary model of care.
  - [pmid] 35796878 — Psychological outcomes of COVID-19 survivors at sixth months after diagnose: the role of kynurenine 
  - [pmid] 38188051 — Brooding and neuroticism are strongly interrelated manifestations of the phenome of depression.
  - [pmid] 39127088 — Immune activation and immune-associated neurotoxicity in Long-COVID: A systematic review and meta-an
  - [pmid] 40048451 — Increased galanin-galanin receptor 1 signaling, inflammation, and insulin resistance are associated 
  - [pubmed_search] (Biopsychological) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (28 hits)

### Cognitive Behavioural Therapy → ME/CFS
- **claim_id:** `osmf:claim:agent-cognitive-behavioural-therapy-treats-me-cfs`
- **proposed:** tier D, status `published`, confidence `medium`
- **rationale:** CBT for ME/CFS remains highly contested (PACE controversy; NICE NG206 does not recommend CBT as curative). Tier D.
- **evidence_summary:** CBT has been studied in ME/CFS, but the evidence base is contested and guideline positions diverge; it should not be framed as solid disease-modifying clinical evidence. Linked trial status: COMPLETED. Search hits=2590.
- **gaps:** Guideline conflict and outcome-measure disputes
- **references:**
  - [nct] NCT00860236 — Giardia Induced Fatigue and Functional Gastrointestinal Diseases, COMPLETED, PHASE4
  - [pmid] 20350028 — The effect of mindfulness-based therapy on anxiety and depression: A meta-analytic review.
  - [pmid] 23459093 — The Efficacy of Cognitive Behavioral Therapy: A Review of Meta-analyses.
  - [pmid] 34373540 — More than 50 long-term effects of COVID-19: a systematic review and meta-analysis.
  - [pmid] 36178003 — World guidelines for falls prevention and management for older adults: a global initiative.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pubmed_search] ("cognitive behavioural therapy" OR "cognitive behavioral therapy" OR CBT) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (2590 hits)

### Digital Cognitive Behavioral Intervention-Rxwell → Long COVID
- **claim_id:** `osmf:claim:agent-digital-cognitive-behavioral-intervention-rxwell-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Digital Cognitive Behavioral Intervention-Rxwell' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 1818 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT05597722 — Addressing Cognitive Fog in Long-COVID-19 Patients, TERMINATED, PHASE4
  - [pmid] 33166287 — Persistent fatigue following SARS-CoV-2 infection is common and independent of severity of initial i
  - [pmid] 34024217 — Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.
  - [pmid] 34373540 — More than 50 long-term effects of COVID-19: a systematic review and meta-analysis.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 41092926 — Burden of 375 diseases and injuries, risk-attributable burden of 88 risk factors, and healthy life e
  - [pubmed_search] ("cognitive behavioural therapy" OR "cognitive behavioral therapy" OR CBT) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1818 hits)

### Genetic → Long COVID
- **claim_id:** `osmf:claim:agent-genetic-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Genetic' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 11505 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT06441955 — Covid-19 Long Haul Preventative and Health Promotion Care Clinical Trial Acceleration Program., RECRUITING, PHASE4
  - [pmid] 26553804 — Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional an
  - [pmid] 32761142 — NCBI Taxonomy: a comprehensive update on curation, resources and tools.
  - [pmid] 33692530 — Attributes and predictors of long COVID.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Genetic) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (11505 hits)

### Igpro20 → Long COVID
- **claim_id:** `osmf:claim:agent-igpro20-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Extracted 1 registry trial(s) for Igpro20 → Long COVID: NCT06524739 (TERMINATED, phase=PHASE3, n=16, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 41089328: Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and Long COVID: current. Europe PMC query `(Igpro20) AND ("long COVID" OR "post-COVID" OR PASC)` → 1 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Not a systematic review; single-pass registry + Europe PMC sampling
- **references:**
  - [nct] NCT06524739 — Double-blind, Randomized, Placebo-controlled Study Evaluating Efficacy and Safety of IgPro20 in Post, TERMINATED, PHASE3
  - [pmid] 41089328 — Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and
  - [pubmed_search] (Igpro20) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1 hits)

### Intravenous Immunoglobulin (IVIG) → Other Post-Viral & Post-Infectious Syndromes
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-other-post-viral`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Extracted 2 registry trial(s) for Intravenous Immunoglobulin (IVIG) → Other Post-Viral & Post-Infectious Syndromes: NCT06305793 (COMPLETED, phase=PHASE2, n=200, relevant=False); NCT06305780 (COMPLETED, phase=PHASE2, n=381, relevant=False). No posted CT.gov results found in this pass. Literature notes: PMID 22185868: Myocarditis.; PMID 32298803: Are we facing a crashing wave of neuropsychiatric sequelae of COVID-19? Neuropsychiatric symptoms and potential immunolo; PMID 32493739: Kawasaki-like multisystem inflammatory syndrome in children during the covid-19 pandemic in Paris, France: prospective o. Europe PMC query `(IVIG OR "intravenous immunoglobulin") AND ("post-viral" OR "post viral fatigue")` → 536 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT06305793 — RECOVER-AUTONOMIC: Platform Protocol, Appendix A (IVIG), COMPLETED, PHASE2
  - [nct] NCT06305780 — RECOVER-AUTONOMIC Platform Protocol, COMPLETED, PHASE2
  - [pmid] 22185868 — Myocarditis.
  - [pmid] 32298803 — Are we facing a crashing wave of neuropsychiatric sequelae of COVID-19? Neuropsychiatric symptoms an
  - [pmid] 32493739 — Kawasaki-like multisystem inflammatory syndrome in children during the covid-19 pandemic in Paris, F
  - [pmid] 33176455 — Management of Acute Myocarditis and Chronic Inflammatory Cardiomyopathy: An Expert Consensus Documen
  - [pmid] 33753937 — Post-acute COVID-19 syndrome.
  - [pmid] 42137701 — Isolated Arterial Hypertension as a Rare Early Manifestation of Guillain-Barré Syndrome: A Case Repo

### Intravenous Immunoglobulin (IVIG) → Chronic Lyme / PTLDS
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-lyme`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Extracted 2 registry trial(s) for Intravenous Immunoglobulin (IVIG) → Chronic Lyme / PTLDS: NCT06305793 (COMPLETED, phase=PHASE2, n=200, relevant=False); NCT06305780 (COMPLETED, phase=PHASE2, n=381, relevant=False). No posted CT.gov results found in this pass. Literature notes: PMID 15870014: In vitro expanded human CD4+CD25+ regulatory T cells suppress effector T cell proliferation.; PMID 25077519: Evidence assessments and guideline recommendations in Lyme disease: the clinical management of known tick bites, erythem; PMID 27976670: Lyme borreliosis.. Europe PMC query `(IVIG OR "intravenous immunoglobulin") AND ("post-treatment Lyme" OR PTLDS OR "chronic Lyme")` → 100 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT06305793 — RECOVER-AUTONOMIC: Platform Protocol, Appendix A (IVIG), COMPLETED, PHASE2
  - [nct] NCT06305780 — RECOVER-AUTONOMIC Platform Protocol, COMPLETED, PHASE2
  - [pmid] 15870014 — In vitro expanded human CD4+CD25+ regulatory T cells suppress effector T cell proliferation.
  - [pmid] 25077519 — Evidence assessments and guideline recommendations in Lyme disease: the clinical management of known
  - [pmid] 27976670 — Lyme borreliosis.
  - [pmid] 32984564 — Post COVID-19 syndrome associated with orthostatic cerebral hypoperfusion syndrome, small fiber neur
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pmid] 42137701 — Isolated Arterial Hypertension as a Rare Early Manifestation of Guillain-Barré Syndrome: A Case Repo

### Intravenous Immunoglobulin (IVIG) → ME/CFS
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Extracted 2 registry trial(s) for Intravenous Immunoglobulin (IVIG) → ME/CFS: NCT06305793 (COMPLETED, phase=PHASE2, n=200, relevant=False); NCT06305780 (COMPLETED, phase=PHASE2, n=381, relevant=False). No posted CT.gov results found in this pass. Literature notes: PMID 19375665: Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.; PMID 19781793: Critical role of nociceptor plasticity in chronic pain.; PMID 21871249: Treating Clostridium difficile infection with fecal microbiota transplantation.. Europe PMC query `(IVIG OR "intravenous immunoglobulin") AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 497 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT06305793 — RECOVER-AUTONOMIC: Platform Protocol, Appendix A (IVIG), COMPLETED, PHASE2
  - [nct] NCT06305780 — RECOVER-AUTONOMIC Platform Protocol, COMPLETED, PHASE2
  - [pmid] 19375665 — Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.
  - [pmid] 19781793 — Critical role of nociceptor plasticity in chronic pain.
  - [pmid] 21871249 — Treating Clostridium difficile infection with fecal microbiota transplantation.
  - [pmid] 27885969 — 36th International Symposium on Intensive Care and Emergency Medicine : Brussels, Belgium. 15-18 Mar
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 42137701 — Isolated Arterial Hypertension as a Rare Early Manifestation of Guillain-Barré Syndrome: A Case Repo

### Ivermectin → Chronic Lyme / PTLDS
- **claim_id:** `osmf:claim:agent-ivermectin-treats-lyme`
- **proposed:** tier D, status `published`, confidence `high`
- **rationale:** Ivermectin lacks reliable supportive RCTs for established Long COVID / PTLDS treatment; contested.
- **evidence_summary:** For Chronic Lyme / PTLDS, extracted trials/literature do not provide solid supportive clinical efficacy for ivermectin. Broader COVID literature is contested; tracker PMID linkage may be off-target (safety/case report). CT.gov statuses: COMPLETED. Search hits=18.
- **gaps:** High-quality condition-specific RCTs with clear benefit not identified
- **references:**
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [pmid] 18323583 — Macaque models of human infectious disease.
  - [pmid] 29186062 — Viral Oncology: Molecular Biology and Pathogenesis.
  - [pmid] 32047861 — Lymelight: forecasting Lyme disease risk using web search data.
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 41421419 — Methemoglobinemia induced by dapsone, hydroxychloroquine, and rifampin combination for post-treatmen
  - [pubmed_search] (Ivermectin) AND ("post-treatment Lyme" OR PTLDS OR "chronic Lyme") — Europe PMC search (18 hits)

### Ivermectin → Long COVID
- **claim_id:** `osmf:claim:agent-ivermectin-treats-long-covid`
- **proposed:** tier D, status `published`, confidence `high`
- **rationale:** Ivermectin lacks reliable supportive RCTs for established Long COVID / PTLDS treatment; contested.
- **evidence_summary:** For Long COVID, extracted trials/literature do not provide solid supportive clinical efficacy for ivermectin. Broader COVID literature is contested; tracker PMID linkage may be off-target (safety/case report). CT.gov statuses: COMPLETED. Search hits=703.
- **gaps:** High-quality condition-specific RCTs with clear benefit not identified
- **references:**
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [pmid] 33856918 — COVID-19 and Cardiovascular Disease: From Bench to Bedside.
  - [pmid] 33941622 — COVID-19-related anosmia is associated with viral persistence and inflammation in human olfactory ep
  - [pmid] 36115368 — The Lancet Commission on lessons for the future from the COVID-19 pandemic.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 38378653 — Nanotechnology's frontier in combatting infectious and inflammatory diseases: prevention and treatme
  - [pmid] 41421419 — Methemoglobinemia induced by dapsone, hydroxychloroquine, and rifampin combination for post-treatmen
  - [pubmed_search] (Ivermectin) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (703 hits)

### Metformin → Gulf War Illness
- **claim_id:** `osmf:claim:agent-metformin-treats-gulf-war-illness`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Extracted 3 registry trial(s) for Metformin → Gulf War Illness: NCT04510194 (COMPLETED, phase=PHASE3, n=1323, relevant=False); NCT06128967 (COMPLETED, phase=PHASE3, n=399, relevant=False); NCT06147050 (UNKNOWN, phase=PHASE3, n=16, relevant=False). No posted CT.gov results found in this pass. Literature notes: PMID 36326761: Complexity and Challenges of the Clinical Diagnosis and Management of Long COVID.; PMID 37008131: Curcumin Formulations for Better Bioavailability: What We Learned from Clinical Trials Thus Far?; PMID 37082752: Role of Turmeric and Curcumin in Prevention and Treatment of Chronic Diseases: Lessons Learned from Clinical Trials.. Europe PMC query `(Metformin) AND ("Gulf War Illness" OR "Gulf War syndrome")` → 32 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT04510194 — COVID-OUT: Early Outpatient Treatment for SARS-CoV-2 Infection (COVID-19), COMPLETED, PHASE3
  - [nct] NCT06128967 — A Multicenter, Adaptive, Randomized, doublE-blinded, Placebo-controlled Study in Participants With L, COMPLETED, PHASE3
  - [nct] NCT06147050 — Effect of Metformin in Reducing Fatigue in Long COVID in Adolescents, UNKNOWN, PHASE3
  - [pmid] 36326761 — Complexity and Challenges of the Clinical Diagnosis and Management of Long COVID.
  - [pmid] 37008131 — Curcumin Formulations for Better Bioavailability: What We Learned from Clinical Trials Thus Far?
  - [pmid] 37082752 — Role of Turmeric and Curcumin in Prevention and Treatment of Chronic Diseases: Lessons Learned from 
  - [pmid] 37189617 — NLRP3 Inflammasome's Activation in Acute and Chronic Brain Diseases-An Update on Pathogenetic Mechan
  - [pmid] 40258841 — Targeting epigenetic and post-translational modifications of NRF2: key regulatory factors in disease

### Microcrystalline Cellulose → Long COVID
- **claim_id:** `osmf:claim:agent-microcrystalline-cellulose-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Microcrystalline Cellulose' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 240 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT05795816 — Effectiveness of Testofen Compared to Placebo on Long COVID Symptoms, COMPLETED, PHASE3
  - [nct] NCT06348212 — Effect of Probiotic Strain Lactobacillus Paracasei PS23 on Brain Fog in People With Long COVID, UNKNOWN, NA
  - [pmid] 21821740 — Oxidoreductive cellulose depolymerization by the enzymes cellobiose dehydrogenase and glycoside hydr
  - [pmid] 21876164 — Insights into the oxidative degradation of cellulose by a copper metalloenzyme that exploits biomass
  - [pmid] 23102010 — Production of four Neurospora crassa lytic polysaccharide monooxygenases in Pichia pastoris monitore
  - [pmid] 27287427 — Cellulases and beyond: the first 70 years of the enzyme producer Trichoderma reesei.
  - [pmid] 36701528 — Spin Hyperpolarization in Modern Magnetic Resonance.
  - [pubmed_search] (Microcrystalline Cellulose) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (240 hits)

### Moderna Covid-19 Vaccine → Long COVID
- **claim_id:** `osmf:claim:agent-moderna-covid-19-vaccine-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** COVID vaccines are prevention/acute tools; treating established Long COVID with additional vaccination is uncertain/insufficient.
- **evidence_summary:** Registry entries link Moderna Covid-19 Vaccine to Long COVID contexts, but vaccination is not established therapy for existing Long COVID. Statuses: RECRUITING. Search hits=3388.
- **gaps:** Condition-specific therapeutic RCTs for established LC
- **references:**
  - [nct] NCT06441955 — Covid-19 Long Haul Preventative and Health Promotion Care Clinical Trial Acceleration Program., RECRUITING, PHASE4
  - [pmid] 33497610 — Adaptive immunity to SARS-CoV-2 and COVID-19.
  - [pmid] 36580913 — Alarming antibody evasion properties of rising SARS-CoV-2 BQ and XBB subvariants.
  - [pmid] 37165196 — Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 38642570 — Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DA
  - [pubmed_search] (Moderna Covid-19 Vaccine) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (3388 hits)

### Moderna Mrna Covid-19 Vaccine → Long COVID
- **claim_id:** `osmf:claim:agent-moderna-mrna-covid-19-vaccine-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** COVID vaccines are prevention/acute tools; treating established Long COVID with additional vaccination is uncertain/insufficient.
- **evidence_summary:** Registry entries link Moderna Mrna Covid-19 Vaccine to Long COVID contexts, but vaccination is not established therapy for existing Long COVID. Statuses: COMPLETED. Search hits=2626.
- **gaps:** Condition-specific therapeutic RCTs for established LC
- **references:**
  - [nct] NCT05212610 — Assessing Safety of Coronavirus Infection (COVID-19) Messenger RNA (mRNA) Vaccine Administration in , COMPLETED, PHASE4
  - [pmid] 33497610 — Adaptive immunity to SARS-CoV-2 and COVID-19.
  - [pmid] 34715347 — Comparing COVID-19 vaccines for their characteristics, efficacy and effectiveness against SARS-CoV-2
  - [pmid] 36580913 — Alarming antibody evasion properties of rising SARS-CoV-2 BQ and XBB subvariants.
  - [pmid] 37165196 — Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Moderna Mrna Covid-19 Vaccine) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (2626 hits)

### Montelukast → MCAS
- **claim_id:** `osmf:claim:agent-montelukast-treats-mcas`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Extracted 1 registry trial(s) for Montelukast → MCAS: NCT04695704 (TERMINATED, phase=PHASE3, n=86, relevant=False). No posted CT.gov results found in this pass. Literature notes: PMID 15577865: Rhinosinusitis: establishing definitions for clinical research and patient care.; PMID 24388011: Prostaglandin D2 activates group 2 innate lymphoid cells through chemoattractant receptor-homologous molecule expressed ; PMID 25861976: Ion channels in innate and adaptive immunity.. Europe PMC query `(Montelukast) AND ("mast cell activation" OR MCAS)` → 663 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Not a systematic review; single-pass registry + Europe PMC sampling
- **references:**
  - [nct] NCT04695704 — Efficacy of Montelukast in Mild-moderate Respiratory Symptoms in Patients With Long-COVID-19:, TERMINATED, PHASE3
  - [pmid] 15577865 — Rhinosinusitis: establishing definitions for clinical research and patient care.
  - [pmid] 24388011 — Prostaglandin D2 activates group 2 innate lymphoid cells through chemoattractant receptor-homologous
  - [pmid] 25861976 — Ion channels in innate and adaptive immunity.
  - [pmid] 28689842 — Asthma Exacerbations: Pathogenesis, Prevention, and Treatment.
  - [pmid] 34789462 — Sex and gender in asthma.
  - [pubmed_search] (Montelukast) AND ("mast cell activation" OR MCAS) — Europe PMC search (663 hits)

### Montelukast → Long COVID
- **claim_id:** `osmf:claim:agent-montelukast-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Extracted 1 registry trial(s) for Montelukast → Long COVID: NCT04695704 (TERMINATED, phase=PHASE3, n=86, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 34067776: Post-COVID-19 Syndrome and the Potential Benefits of Exercise.; PMID 34563706: Mast cell activation symptoms are prevalent in Long-COVID.; PMID 34991982: An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.. Europe PMC query `(Montelukast) AND ("long COVID" OR "post-COVID" OR PASC)` → 226 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Not a systematic review; single-pass registry + Europe PMC sampling
- **references:**
  - [nct] NCT04695704 — Efficacy of Montelukast in Mild-moderate Respiratory Symptoms in Patients With Long-COVID-19:, TERMINATED, PHASE3
  - [pmid] 34067776 — Post-COVID-19 Syndrome and the Potential Benefits of Exercise.
  - [pmid] 34563706 — Mast cell activation symptoms are prevalent in Long-COVID.
  - [pmid] 34991982 — An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - [pmid] 36456834 — Data-driven identification of post-acute SARS-CoV-2 infection subphenotypes.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pubmed_search] (Montelukast) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (226 hits)

### Multidisciplinary Approach → Long COVID
- **claim_id:** `osmf:claim:agent-multidisciplinary-approach-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Multidisciplinary Approach' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 9114 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT06441955 — Covid-19 Long Haul Preventative and Health Promotion Care Clinical Trial Acceleration Program., RECRUITING, PHASE4
  - [pmid] 33753937 — Post-acute COVID-19 syndrome.
  - [pmid] 34308300 — Characterizing long COVID in an international cohort: 7 months of symptoms and their impact.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38493795 — Global, regional, and national burden of disorders affecting the nervous system, 1990-2021: a system
  - [pmid] 38642570 — Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DA
  - [pubmed_search] (Multidisciplinary Approach) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (9114 hits)

### Nutritional Blend (Immunerecov). → Long COVID
- **claim_id:** `osmf:claim:agent-nutritional-blend-immunerecov-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair.
- **evidence_summary:** Extracted 1 registry trial(s) for Nutritional Blend (Immunerecov). → Long COVID: NCT06166030 (UNKNOWN, phase=PHASE3, n=58, relevant=True). No posted CT.gov results found in this pass. Literature notes: PMID 36364899: A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.; PMID 38264914: 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Association.. Europe PMC query `(Nutritional Blend .) AND ("long COVID" OR "post-COVID" OR PASC)` → 133 hits (top cited sampled). This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D.
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT06166030 — IMMUNERECOV CONTRIBUTES TO IMPROVEMENT OF RESPIRATORY AND IMMUNOLOGICAL RESPONSE IN POST-COVID-19 PA, UNKNOWN, PHASE3
  - [pmid] 36364899 — A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pmid] 39900737 — Printable molecule-selective core-shell nanoparticles for wearable and implantable sensing.
  - [pubmed_search] (Nutritional Blend .) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (133 hits)

### Pfizer-Biontech Mrna Covid-19 Vaccine → Long COVID
- **claim_id:** `osmf:claim:agent-pfizer-biontech-mrna-covid-19-vaccine-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`
- **rationale:** COVID vaccines are prevention/acute tools; treating established Long COVID with additional vaccination is uncertain/insufficient.
- **evidence_summary:** Registry entries link Pfizer-Biontech Mrna Covid-19 Vaccine to Long COVID contexts, but vaccination is not established therapy for existing Long COVID. Statuses: COMPLETED. Search hits=2557.
- **gaps:** Condition-specific therapeutic RCTs for established LC
- **references:**
  - [nct] NCT05212610 — Assessing Safety of Coronavirus Infection (COVID-19) Messenger RNA (mRNA) Vaccine Administration in , COMPLETED, PHASE4
  - [pmid] 33497610 — Adaptive immunity to SARS-CoV-2 and COVID-19.
  - [pmid] 34281357 — Myocarditis With COVID-19 mRNA Vaccines.
  - [pmid] 34715347 — Comparing COVID-19 vaccines for their characteristics, efficacy and effectiveness against SARS-CoV-2
  - [pmid] 35614233 — Long COVID after breakthrough SARS-CoV-2 infection.
  - [pmid] 37165196 — Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer.
  - [pubmed_search] (Pfizer-Biontech Mrna Covid-19 Vaccine) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (2557 hits)

### Physiological Evaluation → Long COVID
- **claim_id:** `osmf:claim:agent-physiological-evaluation-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`
- **rationale:** Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.
- **evidence_summary:** 'Physiological Evaluation' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources. Associated registry entries appear procedural/class/placebo-related. Europe PMC query returned 5432 hits but do not establish a treatable-agent evidence base.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT06441955 — Covid-19 Long Haul Preventative and Health Promotion Care Clinical Trial Acceleration Program., RECRUITING, PHASE4
  - [pmid] 34373540 — More than 50 long-term effects of COVID-19: a systematic review and meta-analysis.
  - [pmid] 34634250 — Global prevalence and burden of depressive and anxiety disorders in 204 countries and territories in
  - [pmid] 36050306 — Lactate metabolism in human health and disease.
  - [pmid] 38484753 — Global age-sex-specific mortality, life expectancy, and population estimates in 204 countries and te
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Physiological Evaluation) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (5432 hits)

### Rituximab → ME/CFS
- **claim_id:** `osmf:claim:agent-rituximab-treats-me-cfs`
- **proposed:** tier D, status `published`, confidence `high`
- **rationale:** Phase 3 RituxME and related trials showed no clinical benefit in ME/CFS; evidence is insufficient/negative for treatment claim.
- **evidence_summary:** Rituximab was tested in ME/CFS including a Phase 3 program; published results did not support clinical efficacy, and the treatment claim is contested/insufficient. Registry statuses include: RECRUITING, TERMINATED, COMPLETED, COMPLETED, COMPLETED. Europe PMC hits=468.
- **gaps:** No need for further positive-efficacy framing without new contradictory trials
- **references:**
  - [nct] NCT06952413 — Study of the Efficacy and Safety for Rituximab in Myalgia Encephalomyelitis/Chronic Fatigue Syndrome, RECRUITING, PHASE2
  - [nct] NCT01156922 — B-cell Depletion Using the Monoclonal Anti-CD20 Antibody Rituximab in Very Severe Chronic Fatigue Sy, TERMINATED, PHASE2
  - [nct] NCT02229942 — B-lymphocyte Depletion Using Rituximab in Chronic Fatigue Syndrome/ Myalgic Encephalopathy (CFS/ME)., COMPLETED, PHASE3
  - [nct] NCT00848692 — Drug Intervention in Chronic Fatigue Syndrome, COMPLETED, PHASE2,PHASE3
  - [nct] NCT01156909 — B-cell Depletion Using the Monoclonal Anti-CD20 Antibody Rituximab in Chronic Fatigue Syndrome, COMPLETED, PHASE2
  - [pmid] 19375665 — Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.
  - [pmid] 30285773 — Chronic viral infections in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS).
  - [pmid] 31210940 — European Society for the Study of Coeliac Disease (ESsCD) guideline for coeliac disease and other gl

