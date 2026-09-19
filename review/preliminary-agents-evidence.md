# Preliminary agents — evidence evaluation report

**Date:** 2026-09-19 (America/Edmonton / MDT)
**Evaluator:** evidence-eval-bot
**Queue size:** 555 claims
**Waves:** A=83, B=472, C=0

## Tier distribution

- **Before:** all 555 were import-default **D** / `draft` (Tracker Preliminary)
- **After:** {'C': 47, 'D': 508}
- **Published after:** 39

- **A**: 0 (published=0, draft=0)
- **B**: 0 (published=0, draft=0)
- **C**: 47 (published=37, draft=10)
- **D**: 508 (published=2, draft=506)

## Method

Match graph `treats_candidate_for` claims whose subject agent label is in Tracker Evidence Level == Preliminary. Skip claims already covered by Moderate eval / published-13 deepdive / phase3 chase. **Wave A (deep):** COMPLETED Phase 2/3/4 or NCT `hasResults` → CT.gov API v2 + Europe PMC NCT publication search (+ agent+condition search). **Wave B (standard):** remaining NCT → study record; PubMed/Europe PMC only if title/status suggests published results. **Wave C (light):** no usable NCT → keep D draft. Honest bar: almost all stay D or C; A/B only for clear multi-source clinical packages (none expected for Preliminary). Publish only when confidence medium+ and refs support standing behind the claim.

## Notable upgrades / downgrades

- No A/B upgrades (honest: no verified solid multi-source clinical packages).
- Upgrades D→C: 0
- Remain D: 508
- Newly/confirmed published: 39
  - Amantadine → Long COVID (tier C, wave A)
  - Anakinra → ME/CFS (tier C, wave A)
  - Axa1125 → Long COVID (tier C, wave A)
  - Clonidine → ME/CFS (tier C, wave A)
  - Coenzyme Q10 (CoQ10) → ME/CFS (tier C, wave A)
  - Cognitive Behavioral Therapy → ME/CFS (tier D, wave A)
  - Cyclophosphamide → ME/CFS (tier C, wave A)
  - Ibudilast → Long COVID (tier C, wave A)
  - Ivabradine + Coordinated Care → Long COVID (tier C, wave A)
  - Ketamine Only → Long COVID (tier C, wave A)
  - Larazotide Acetate → Long COVID (tier C, wave A)
  - Lithium → Long COVID (tier C, wave A)
  - Melatonin → Long COVID (tier C, wave A)
  - Mind-Body Reprocessing Therapy → Long COVID (tier C, wave A)
  - Modafinil → Long COVID (tier C, wave A)
  - Nad+ → Long COVID (tier C, wave A)
  - Naltrexone → Long COVID (tier C, wave A)
  - Nicotinamide Riboside → Long COVID (tier C, wave A)
  - Nortriptyline → ME/CFS (tier C, wave A)
  - Pacing → ME/CFS (tier C, wave A)
  - Patient-Partner Videotelephone-Delivered Cognitive Behavioral Stress Management Intervention → ME/CFS (tier D, wave A)
  - Pentoxifylline → Long COVID (tier C, wave A)
  - Personalised Exercise Program → Long COVID (tier C, wave A)
  - Plasma Exchange Procedure → Long COVID (tier C, wave A)
  - Preprocessed Thawed Autologous Fmt → ME/CFS (tier C, wave A)
  - Preprocessed Thawed Donor Fmt → ME/CFS (tier C, wave A)
  - Probiotic Agent → Long COVID (tier C, wave A)
  - Pyridostigmine Bromide → ME/CFS (tier C, wave A)
  - Rintatolimod → Long COVID (tier C, wave A)
  - Ritonavir → Long COVID (tier C, wave A)
  - … +9 more

## Wave A deep-dive highlights

- **140 Ml Per Day Of Beet-It Nitrate Beverage → Long COVID**: tier C/draft — Early clinical signal thin (small n or sparse pubs) → C draft.
- **Active Tdcs → Long COVID**: tier D/draft — Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **Aer002 → Long COVID**: tier D/draft — Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **Amantadine → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Ampion → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Anakinra → ME/CFS**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Axa1125 → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Brainhq → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Brainhq/Active Comparator Activity → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Cardiopulmonary Exercise Test → ME/CFS**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Care As Usual → Long COVID**: tier D/draft — Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **Clonidine → ME/CFS**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Coenzyme Q10 (CoQ10) → Gulf War Illness**: tier D/draft — Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **Coenzyme Q10 (CoQ10) → Long COVID**: tier D/draft — Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **Coenzyme Q10 (CoQ10) → ME/CFS**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Coenzyme Q10 (CoQ10) → Other Post-Viral & Post-Infectious Syndromes**: tier D/draft — Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **Coenzyme Q10 (CoQ10) → POTS**: tier D/draft — Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **Cognitive Behavioral Therapy → ME/CFS**: tier D/published — CBT for ME/CFS remains highly contested (PACE controversy; NICE NG206 does not recommend CBT as curative). Tier D despite trial activity.
- **Coordinated Care → Long COVID**: tier D/draft — Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **Covid Rehab Formula Granules → Long COVID**: tier D/draft — Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **Ct38 → ME/CFS**: tier C/draft — Early clinical signal thin (small n or sparse pubs) → C draft.
- **Cyclophosphamide → ME/CFS**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Droxidopa → ME/CFS**: tier D/draft — Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **Duloxetine → ME/CFS**: tier C/draft — Completed Phase 3+ with results flag and literature hits, but this bot did not verify positive efficacy endpoints or a multi-source clinical
- **Efgartigimod → Long COVID**: tier D/draft — Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **Ensitrelvir → Long COVID**: tier D/draft — Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **Home-Based Telerehabilitation → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Ibudilast → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Institutional Standard Treatment For Xerostomia And Long Covid → Long COVID**: tier D/draft — Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **Ivabradine + Coordinated Care → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Ketamine → ME/CFS**: tier C/draft — Early clinical signal thin (small n or sparse pubs) → C draft.
- **Ketamine Only → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Lactose Capsula → ME/CFS**: tier D/draft — Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **Larazotide Acetate → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Lau-7B For 3 Cycles → Long COVID**: tier C/draft — Completed Phase 3+ with results flag and literature hits, but this bot did not verify positive efficacy endpoints or a multi-source clinical
- **Lithium → Long COVID**: tier C/published — Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory)
- **Long Covid Coping And Recovery (Lccr) Intervention → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Low Sugar Diet And 10-12 Hour Eating Window → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Low Sugar Diet, 8 Hour Eating Window And Fasting → Long COVID**: tier D/draft — Some completed condition-related work but phase/size/pubs too thin for C.
- **Medicabilis Cannabis Sativa 50 → Long COVID**: tier C/draft — Early clinical signal thin (small n or sparse pubs) → C draft.

## Tier C

### 140 Ml Per Day Of Beet-It Nitrate Beverage → Long COVID
- **claim_id:** `osmf:claim:agent-140-ml-per-day-of-beet-it-nitrate-beverage-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Early clinical signal thin (small n or sparse pubs) → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for 140 Ml Per Day Of Beet-It Nitrate Beverage → Long COVID: NCT05618574 (COMPLETED, phase=PHASE2, n=17, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 15896867: Optimising two-dye microarray designs for estimating associations with a quantitative trait.; PMID 26452528: The 29(th) Annual Symposium of the Protein Society, Barcelona, Spain, July 22-25, 2015.. Europe PMC query `(140 Ml Per Day Of Beet-It Nitrate Beverage) AND ("long COVID" OR "post-COVID" OR PASC)` → 3 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05618574 — Nitrite Supplementation in Long COVID Patients, COMPLETED, PHASE2
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [pmid] 15896867 — Optimising two-dye microarray designs for estimating associations with a quantitative trait.
  - [pmid] 26452528 — The 29(th) Annual Symposium of the Protein Society, Barcelona, Spain, July 22-25, 2015.
  - [pmid] PMC11208286 — 
  - [pubmed_search] (140 Ml Per Day Of Beet-It Nitrate Beverage) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (3 hits)

### Amantadine → Long COVID
- **claim_id:** `osmf:claim:agent-amantadine-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Amantadine → Long COVID: NCT06055244 (COMPLETED, phase=PHASE2, n=64, relevant=True); NCT06234462 (WITHDRAWN, phase=PHASE2, n=0, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 32885037: COVID-19 and possible links with Parkinson's disease and parkinsonism: from bench to bedside.; PMID 33755344: Persistent neurologic symptoms and cognitive dysfunction in non-hospitalized Covid-19 "long haulers".; PMID 34346558: Multidisciplinary collaborative consensus guidance statement on the assessment and treatment of fatigue in postacute seq. Europe PMC query `(Amantadine) AND ("long COVID" OR "post-COVID" OR PASC)` → 172 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06055244 — Amantadine Therapy for Cognitive Impairment in Long COVID, COMPLETED, PHASE2
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [nct] NCT06234462 — A Study of Amantadine for Cognitive Dysfunction in Patients With Long-Covid, WITHDRAWN, PHASE2
  - [pmid] 39516425 — Neurological, psychological, psychosocial complications of long-COVID and their management.
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 32885037 — COVID-19 and possible links with Parkinson's disease and parkinsonism: from bench to bedside.
  - [pmid] 33755344 — Persistent neurologic symptoms and cognitive dysfunction in non-hospitalized Covid-19 "long haulers"
  - [pmid] 34346558 — Multidisciplinary collaborative consensus guidance statement on the assessment and treatment of fati

### Anakinra → ME/CFS
- **claim_id:** `osmf:claim:agent-anakinra-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Anakinra → ME/CFS: NCT02108210 (COMPLETED, phase=PHASE2,PHASE3, n=50, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 29462012: Neuroinflammation and Central Sensitization in Chronic and Widespread Pain.; PMID 30920354: The Sleep-Immune Crosstalk in Health and Disease.; PMID 33743212: COVID-19 and the human innate immune system.. Europe PMC query `(Anakinra) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 142 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT02108210 — Cytokine Inhibition in Chronic Fatigue Syndrome Patients, COMPLETED, PHASE2,PHASE3
  - [pmid] 28265678 — Cytokine Inhibition in Patients With Chronic Fatigue Syndrome: A Randomized Trial.
  - [pmid] 29284500 — Cytokine signatures in chronic fatigue syndrome patients: a Case Control Study and the effect of ana
  - [pmid] 26438161 — Cytokine inhibition in chronic fatigue syndrome patients: study protocol for a randomized controlled
  - [pmid] 29462012 — Neuroinflammation and Central Sensitization in Chronic and Widespread Pain.
  - [pmid] 30920354 — The Sleep-Immune Crosstalk in Health and Disease.
  - [pmid] 33743212 — COVID-19 and the human innate immune system.
  - [pmid] 35176758 — Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.

### Axa1125 → Long COVID
- **claim_id:** `osmf:claim:agent-axa1125-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Axa1125 → Long COVID: NCT05152849 (COMPLETED, phase=PHASE2, n=41, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 37316880: Long COVID: Costs for the German economy and health care and pension system.; PMID 37445634: Laboratory Findings and Biomarkers in Long COVID: What Do We Know So Far? Insights into Epidemiology, Pathogenesis, Ther; PMID 39326415: Mechanisms of long COVID and the path toward therapeutics.. Europe PMC query `(Axa1125) AND ("long COVID" OR "post-COVID" OR PASC)` → 31 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05152849 — Efficacy, Safety, Tolerability of AXA1125 in Fatigue After COVID-19 Infection, COMPLETED, PHASE2
  - [pmid] 37699892 — Amino acid metabolism in health and disease.
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 36349400 — Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - [pmid] 37223439 — Efficacy and tolerability of an endogenous metabolic modulator (AXA1125) in fatigue-predominant long
  - [pmid] 37316880 — Long COVID: Costs for the German economy and health care and pension system.
  - [pmid] 37445634 — Laboratory Findings and Biomarkers in Long COVID: What Do We Know So Far? Insights into Epidemiology
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.

### Clonidine → ME/CFS
- **claim_id:** `osmf:claim:agent-clonidine-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Clonidine → ME/CFS: NCT01040429 (COMPLETED, phase=PHASE2, n=120, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 19207771: Postural tachycardia syndrome (POTS).; PMID 19713422: Guidelines for the diagnosis and management of syncope (version 2009).; PMID 25980576: 2015 heart rhythm society expert consensus statement on the diagnosis and treatment of postural tachycardia syndrome, in. Europe PMC query `(Clonidine) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 254 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT01040429 — The Norwegian Study of Chronic Fatigue Syndrome in Adolescents: Pathophysiology and Intervention Tri, COMPLETED, PHASE2
  - [pmid] 24493300 — Disease mechanisms and clonidine treatment in adolescent chronic fatigue syndrome: a combined cross-
  - [pmid] 28494812 — Whole blood gene expression in adolescent chronic fatigue syndrome: an exploratory cross-sectional s
  - [pmid] 27414048 — Aberrant Resting-State Functional Connectivity in the Salience Network of Adolescent Chronic Fatigue
  - [pmid] 27149955 — Altered neuroendocrine control and association to clinical symptoms in adolescent chronic fatigue sy
  - [pmid] 19207771 — Postural tachycardia syndrome (POTS).
  - [pmid] 19713422 — Guidelines for the diagnosis and management of syncope (version 2009).
  - [pmid] 25980576 — 2015 heart rhythm society expert consensus statement on the diagnosis and treatment of postural tach

### Coenzyme Q10 (CoQ10) → ME/CFS
- **claim_id:** `osmf:claim:agent-coenzyme-q10-coq10-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 3 registry trial(s) for Coenzyme Q10 (CoQ10) → ME/CFS: NCT03186027 (COMPLETED, phase=NA, n=282, relevant=True); NCT05128292 (COMPLETED, phase=NA, n=42, relevant=True); NCT02063126 (COMPLETED, phase=PHASE2,PHASE3, n=80, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 22747645: Depression and sickness behavior are Janus-faced responses to shared inflammatory pathways.; PMID 33808247: Magnesium: Biochemistry, Nutrition, Detection, and Social Impact of Diseases Linked to Its Deficiency.; PMID 33918736: Fibromyalgia: Pathogenesis, Mechanisms, Diagnosis and Treatment Options Update.. Europe PMC query `(Coenzyme Q10) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 423 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03186027 — Coenzyme Q10 Plus NADH Supplementation in Chronic Fatigue Syndrome/Myalgic Encephalomyelitis, COMPLETED, NA
  - [pmid] 34444817 — Effect of Dietary Coenzyme Q10 Plus NADH Supplementation on Fatigue Perception and Health-Related Qu
  - [nct] NCT05128292 — Effect of CoQ10 Plus Selenium Supplementation on Clinical Outcomes and Biochemical Markers in ME/CFS, COMPLETED, NA
  - [pmid] 35229657 — Does Coenzyme Q10 Plus Selenium Supplementation Ameliorate Clinical Outcomes by Modulating Oxidative
  - [nct] NCT02063126 — Clinical Trial to Measure the Maximun HR After ReConnect ® Supplementation vs. Placebo in CFS., COMPLETED, PHASE2,PHASE3
  - [pmid] 25386668 — Does oral coenzyme Q10 plus NADH supplementation improve fatigue and biochemical parameters in chron
  - [pmid] 34067632 — Coenzyme Q<sub>10</sub>: Clinical Applications beyond Cardiovascular Diseases.
  - [pmid] 26212172 — Effect of coenzyme Q10 plus nicotinamide adenine dinucleotide supplementation on maximum heart rate 

### Ct38 → ME/CFS
- **claim_id:** `osmf:claim:agent-ct38-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Early clinical signal thin (small n or sparse pubs) → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ct38 → ME/CFS: NCT03613129 (COMPLETED, phase=PHASE1,PHASE2, n=17, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 38256459: Advancing Research and Treatment: An Overview of Clinical Trials in Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (; PMID 42063971: A unifying theory of brain signaling and its possible role in acquired chronic disease.. Europe PMC query `(Ct38) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 4 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03613129 — Clinical Trial to Investigate CT38 in the Treatment of Myalgic Encephalomyelitis / Chronic Fatigue S, COMPLETED, PHASE1,PHASE2
  - [pmid] 34539356 — Acute Corticotropin-Releasing Factor Receptor Type 2 Agonism Results in Sustained Symptom Improvemen
  - [pmid] 39942672 — Antimicrobial Neuropeptides and Their Receptors: Immunoregulator and Therapeutic Targets for Immune 
  - [pmid] 38256459 — Advancing Research and Treatment: An Overview of Clinical Trials in Myalgic Encephalomyelitis/Chroni
  - [pmid] 42063971 — A unifying theory of brain signaling and its possible role in acquired chronic disease.
  - [pmid] PMC7111423 — 
  - [pubmed_search] (Ct38) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (4 hits)

### Cyclophosphamide → ME/CFS
- **claim_id:** `osmf:claim:agent-cyclophosphamide-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Cyclophosphamide → ME/CFS: NCT02444091 (COMPLETED, phase=PHASE2, n=40, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 10515901: Q fever.; PMID 17655751: Sweet's syndrome--a comprehensive review of an acute febrile neutrophilic dermatosis.; PMID 19375665: Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.. Europe PMC query `(Cyclophosphamide) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 490 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT02444091 — Cyclophosphamide in Myalgic Encephalopathy/ Chronic Fatigue Syndrome (ME/CFS), COMPLETED, PHASE2
  - [pmid] 28018972 — Metabolic profiling indicates impaired pyruvate dehydrogenase function in myalgic encephalopathy/chr
  - [pmid] 34423789 — A map of metabolic phenotypes in patients with myalgic encephalomyelitis/chronic fatigue syndrome.
  - [pmid] 32210306 — Human Leukocyte Antigen alleles associated with Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (
  - [pmid] 32411717 — Intravenous Cyclophosphamide in Myalgic Encephalomyelitis/Chronic Fatigue Syndrome. An Open-Label Ph
  - [pmid] 10515901 — Q fever.
  - [pmid] 17655751 — Sweet's syndrome--a comprehensive review of an acute febrile neutrophilic dermatosis.
  - [pmid] 19375665 — Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.

### Duloxetine → ME/CFS
- **claim_id:** `osmf:claim:agent-duloxetine-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Completed Phase 3+ with results flag and literature hits, but this bot did not verify positive efficacy endpoints or a multi-source clinical package → C draft (not B).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Duloxetine → ME/CFS: NCT00375973 (COMPLETED, phase=PHASE2,PHASE3, n=60, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 22094191: Central pain mechanisms in chronic pain states--maybe it is all in their head.; PMID 26267006: Physical exercise as non-pharmacological treatment of chronic pain: Why and when.; PMID 29876878: Role of the Prefrontal Cortex in Pain Processing.. Europe PMC query `(Duloxetine) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 413 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Manual review of primary endpoint directionality / multi-source synthesis
- **references:**
  - [nct] NCT00375973 — Double Blind Trial of Duloxetine in Chronic Fatigue Syndrome, COMPLETED, PHASE2,PHASE3
  - [pmid] 22094191 — Central pain mechanisms in chronic pain states--maybe it is all in their head.
  - [pmid] 26267006 — Physical exercise as non-pharmacological treatment of chronic pain: Why and when.
  - [pmid] 29876878 — Role of the Prefrontal Cortex in Pain Processing.
  - [pmid] 30223011 — Brain glial activation in fibromyalgia - A multi-site positron emission tomography investigation.
  - [pmid] 30975301 — Screening and Management of Depression in Patients With Cardiovascular Disease: JACC State-of-the-Ar
  - [pubmed_search] (Duloxetine) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (413 hits)

### Ibudilast → Long COVID
- **claim_id:** `osmf:claim:agent-ibudilast-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ibudilast → Long COVID: NCT05513560 (COMPLETED, phase=PHASE2,PHASE3, n=460, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33240091: Challenges for Drug Repurposing in the COVID-19 Pandemic Era.; PMID 33421734: The neuropsychiatric manifestations of COVID-19: Interactions with psychiatric illness and pharmacological treatment.. Europe PMC query `(Ibudilast) AND ("long COVID" OR "post-COVID" OR PASC)` → 24 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05513560 — RECLAIM: Recovering From COVID-19 Lingering Symptoms Adaptive Integrative Medicine, COMPLETED, PHASE2,PHASE3
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [pmid] 33240091 — Challenges for Drug Repurposing in the COVID-19 Pandemic Era.
  - [pmid] 33421734 — The neuropsychiatric manifestations of COVID-19: Interactions with psychiatric illness and pharmacol
  - [pubmed_search] (Ibudilast) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (24 hits)

### Ivabradine + Coordinated Care → Long COVID
- **claim_id:** `osmf:claim:agent-ivabradine-coordinated-care-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ivabradine + Coordinated Care → Long COVID: NCT06305780 (COMPLETED, phase=PHASE2, n=381, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 34069603: European Network on Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (EUROMENE): Expert Consensus on the Diagnosis, Se; PMID 34607799: Recommendations for the recognition, diagnosis, and management of long COVID: a Delphi study.; PMID 35720084: Dysautonomia in COVID-19 Patients: A Narrative Review on Clinical Course, Diagnostic and Therapeutic Strategies.. Europe PMC query `(Ivabradine + Coordinated Care) AND ("long COVID" OR "post-COVID" OR PASC)` → 28 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06305780 — RECOVER-AUTONOMIC Platform Protocol, COMPLETED, PHASE2
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [pmid] 41720282 — Design and rationale of RECOVER-AUTONOMIC: A randomized platform trial evaluating interventions for 
  - [pmid] 34069603 — European Network on Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (EUROMENE): Expert Consensus 
  - [pmid] 34607799 — Recommendations for the recognition, diagnosis, and management of long COVID: a Delphi study.
  - [pmid] 35720084 — Dysautonomia in COVID-19 Patients: A Narrative Review on Clinical Course, Diagnostic and Therapeutic
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV

### Ketamine → ME/CFS
- **claim_id:** `osmf:claim:agent-ketamine-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Early clinical signal thin (small n or sparse pubs) → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ketamine → ME/CFS: NCT04141696 (COMPLETED, phase=PHASE1,PHASE2, n=10, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 18923511: The molecular neurobiology of depression.; PMID 23644052: Inflammatory cytokines in depression: neurobiological mechanisms and therapeutic implications.; PMID 29876878: Role of the Prefrontal Cortex in Pain Processing.. Europe PMC query `(Ketamine) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 449 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT04141696 — A Proof-of-Concept Trial on the Effect of Ketamine on Fatigue, COMPLETED, PHASE1,PHASE2
  - [pmid] 18923511 — The molecular neurobiology of depression.
  - [pmid] 23644052 — Inflammatory cytokines in depression: neurobiological mechanisms and therapeutic implications.
  - [pmid] 29876878 — Role of the Prefrontal Cortex in Pain Processing.
  - [pmid] 31379879 — The Role of Inflammation in Depression and Fatigue.
  - [pmid] 34973396 — Fatigue and cognitive impairment in Post-COVID-19 Syndrome: A systematic review and meta-analysis.
  - [pubmed_search] (Ketamine) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (449 hits)

### Ketamine Only → Long COVID
- **claim_id:** `osmf:claim:agent-ketamine-only-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ketamine Only → Long COVID: NCT06821087 (COMPLETED, phase=PHASE2, n=20, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33769431: How COVID-19 Affects the Brain.; PMID 33941622: COVID-19-related anosmia is associated with viral persistence and inflammation in human olfactory epithelium and brain i; PMID 34749198: Alcohol and other substance use during the COVID-19 pandemic: A systematic review.. Europe PMC query `(Ketamine Only) AND ("long COVID" OR "post-COVID" OR PASC)` → 600 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06821087 — Evaluating the Neuromodulatory Effect of Ketamine in Long COVID-19, COMPLETED, PHASE2
  - [pmid] 33769431 — How COVID-19 Affects the Brain.
  - [pmid] 33941622 — COVID-19-related anosmia is associated with viral persistence and inflammation in human olfactory ep
  - [pmid] 34749198 — Alcohol and other substance use during the COVID-19 pandemic: A systematic review.
  - [pmid] 34973396 — Fatigue and cognitive impairment in Post-COVID-19 Syndrome: A systematic review and meta-analysis.
  - [pmid] 35768006 — Mild respiratory COVID can cause multi-lineage neural cell and myelin dysregulation.
  - [pubmed_search] (Ketamine Only) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (600 hits)

### Larazotide Acetate → Long COVID
- **claim_id:** `osmf:claim:agent-larazotide-acetate-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Larazotide Acetate → Long COVID: NCT05747534 (COMPLETED, phase=PHASE2, n=107, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 35727635: Markers of fungal translocation are elevated during post-acute sequelae of SARS-CoV-2 and induce NF-κB signaling.; PMID 35868344: Gut-brain communication in COVID-19: molecular mechanisms, mediators, biomarkers, and therapeutics.; PMID 36476388: Neutrophil profiles of pediatric COVID-19 and multisystem inflammatory syndrome in children.. Europe PMC query `(Larazotide Acetate) AND ("long COVID" OR "post-COVID" OR PASC)` → 15 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05747534 — AT1001 for the Treatment of Long COVID, COMPLETED, PHASE2
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 40529374 — Core features and inherent diversity of post-acute infection syndromes.
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [pmid] 35727635 — Markers of fungal translocation are elevated during post-acute sequelae of SARS-CoV-2 and induce NF-
  - [pmid] 35868344 — Gut-brain communication in COVID-19: molecular mechanisms, mediators, biomarkers, and therapeutics.
  - [pmid] 36476388 — Neutrophil profiles of pediatric COVID-19 and multisystem inflammatory syndrome in children.
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.

### Lau-7B For 3 Cycles → Long COVID
- **claim_id:** `osmf:claim:agent-lau-7b-for-3-cycles-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Completed Phase 3+ with results flag and literature hits, but this bot did not verify positive efficacy endpoints or a multi-source clinical package → C draft (not B).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Lau-7B For 3 Cycles → Long COVID: NCT05999435 (COMPLETED, phase=PHASE2,PHASE3, n=272, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33313986: ESICM LIVES 2020.; PMID 35084716: Multiomics Analysis-Based Biomarkers in Diagnosis of Polycystic Ovary Syndrome.; PMID 35920845: 58<sup>th</sup> EASD Annual Meeting of the European Association for the Study of Diabetes : Stockholm, Sweden, 19 - 23 S. Europe PMC query `(Lau-7B For 3 Cycles) AND ("long COVID" OR "post-COVID" OR PASC)` → 22 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Manual review of primary endpoint directionality / multi-source synthesis
- **references:**
  - [nct] NCT05999435 — Study of LAU-7b for the Treatment of Long COVID in Adults, COMPLETED, PHASE2,PHASE3
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 40559563 — Digestive Manifestations of Post-COVID-19: A Focus on Therapeutic Strategies.
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [pmid] 33313986 — ESICM LIVES 2020.
  - [pmid] 35084716 — Multiomics Analysis-Based Biomarkers in Diagnosis of Polycystic Ovary Syndrome.
  - [pmid] 35920845 — 58<sup>th</sup> EASD Annual Meeting of the European Association for the Study of Diabetes : Stockhol
  - [pmid] 36599369 — Influenza vaccination reveals sex dimorphic imprints of prior mild COVID-19.

### Lithium → Long COVID
- **claim_id:** `osmf:claim:agent-lithium-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Lithium → Long COVID: NCT05618587 (COMPLETED, phase=PHASE2, n=52, relevant=True); NCT06108297 (COMPLETED, phase=PHASE1, n=5, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 32682460: How mental health care should change as a consequence of the COVID-19 pandemic.; PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 35987197: Neurological and psychiatric risk trajectories after SARS-CoV-2 infection: an analysis of 2-year retrospective cohort st. Europe PMC query `(Lithium) AND ("long COVID" OR "post-COVID" OR PASC)` → 554 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05618587 — Effect of Lithium Therapy on Long COVID Symptoms, COMPLETED, PHASE2
  - [pmid] 36899952 — Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutic
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [nct] NCT06108297 — Lithium Long COVID Dose-finding Study, COMPLETED, PHASE1
  - [pmid] 39356507 — Lithium Aspartate for Long COVID Fatigue and Cognitive Dysfunction: A Randomized Clinical Trial.
  - [pmid] 40526103 — Glycogen synthase kinase 3β: a key player in progressive chronic kidney disease.

### Medicabilis Cannabis Sativa 50 → Long COVID
- **claim_id:** `osmf:claim:agent-medicabilis-cannabis-sativa-50-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Early clinical signal thin (small n or sparse pubs) → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Medicabilis Cannabis Sativa 50 → Long COVID: NCT04997395 (COMPLETED, phase=PHASE2, n=12, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 38612615: Possible Role of Cannabis in the Management of Neuroinflammation in Patients with Post-COVID Condition.. Europe PMC query `(Medicabilis Cannabis Sativa 50) AND ("long COVID" OR "post-COVID" OR PASC)` → 4 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT04997395 — Feasibility of Cannabidiol for the Treatment of Long COVID, COMPLETED, PHASE2
  - [pmid] 36899952 — Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutic
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 37265584 — Biological mechanisms underpinning the development of long COVID.
  - [pmid] 37344737 — Long COVID and possible preventive options.
  - [pmid] 38612615 — Possible Role of Cannabis in the Management of Neuroinflammation in Patients with Post-COVID Conditi
  - [pmid] PPR686531 — 
  - [pubmed_search] (Medicabilis Cannabis Sativa 50) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (4 hits)

### Melatonin → Long COVID
- **claim_id:** `osmf:claim:agent-melatonin-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Melatonin → Long COVID: NCT06404112 (COMPLETED, phase=PHASE2, n=469, relevant=True); NCT06404086 (COMPLETED, phase=PHASE2, n=830, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 32637987: The emerging spectrum of COVID-19 neurology: clinical, radiological and laboratory findings.; PMID 33856918: COVID-19 and Cardiovascular Disease: From Bench to Bedside.; PMID 36253560: Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential therapies.. Europe PMC query `(Melatonin) AND ("long COVID" OR "post-COVID" OR PASC)` → 759 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06404112 — RECOVER-SLEEP: Platform Protocol, Appendix_B (CPSD), COMPLETED, PHASE2
  - [pmid] 40537100 — Multidimensional Characterization of Long COVID Fatigue.
  - [nct] NCT06404086 — RECOVER-SLEEP: Platform Protocol, COMPLETED, PHASE2
  - [pmid] 32637987 — The emerging spectrum of COVID-19 neurology: clinical, radiological and laboratory findings.
  - [pmid] 33856918 — COVID-19 and Cardiovascular Disease: From Bench to Bedside.
  - [pmid] 36253560 — Endothelial dysfunction in COVID-19: an overview of evidence, biomarkers, mechanisms and potential t
  - [pmid] 37117704 — Wearable chemical sensors for biomarker discovery in the omics era.
  - [pmid] 37848036 — Serotonin reduction in post-acute sequelae of viral infection.

### Midazolam → ME/CFS
- **claim_id:** `osmf:claim:agent-midazolam-treats-me-cfs`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Early clinical signal thin (small n or sparse pubs) → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Midazolam → ME/CFS: NCT04141696 (COMPLETED, phase=PHASE1,PHASE2, n=10, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 23452057: Characterization of different courses of atopic dermatitis in adolescent and adult patients.; PMID 24929099: GABAA receptor-acting neurosteroids: a role in the development and regulation of the stress response.; PMID 27885969: 36th International Symposium on Intensive Care and Emergency Medicine : Brussels, Belgium. 15-18 March 2016.. Europe PMC query `(Midazolam) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 190 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT04141696 — A Proof-of-Concept Trial on the Effect of Ketamine on Fatigue, COMPLETED, PHASE1,PHASE2
  - [pmid] 23452057 — Characterization of different courses of atopic dermatitis in adolescent and adult patients.
  - [pmid] 24929099 — GABAA receptor-acting neurosteroids: a role in the development and regulation of the stress response
  - [pmid] 27885969 — 36th International Symposium on Intensive Care and Emergency Medicine : Brussels, Belgium. 15-18 Mar
  - [pmid] 28674681 — Myalgic Encephalomyelitis/Chronic Fatigue Syndrome Diagnosis and Management in Young People: A Prime
  - [pmid] 30844399 — Composite Pain Biomarker Signatures for Objective Assessment and Effective Treatment.
  - [pubmed_search] (Midazolam) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (190 hits)

### Mind-Body Reprocessing Therapy → Long COVID
- **claim_id:** `osmf:claim:agent-mind-body-reprocessing-therapy-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Mind-Body Reprocessing Therapy → Long COVID: NCT05703074 (COMPLETED, phase=PHASE2, n=310, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33441072: PTSD in the COVID-19 Era.; PMID 33706815: An observational study of the impact of COVID-19 and the rapid implementation of telehealth on community mental health c; PMID 33975774: Overview of sleep management during COVID-19.. Europe PMC query `(Mind-Body Reprocessing Therapy) AND ("long COVID" OR "post-COVID" OR PASC)` → 46 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05703074 — Mental Intervention and Nicotinamide Riboside Supplementation in Long Covid, COMPLETED, PHASE2
  - [pmid] 38668888 — Mitochondrial dysfunction in long COVID: mechanisms, consequences, and potential therapeutic approac
  - [pmid] 40536597 — Role of mitochondria in physiological activities, diseases, and therapy.
  - [pmid] 39495479 — Novel biomarkers of mitochondrial dysfunction in Long COVID patients.
  - [pmid] 41008646 — Mitochondrial Reactive Oxygen Species: A Unifying Mechanism in Long COVID and Spike Protein-Associat
  - [pmid] 33441072 — PTSD in the COVID-19 Era.
  - [pmid] 33706815 — An observational study of the impact of COVID-19 and the rapid implementation of telehealth on commu
  - [pmid] 33975774 — Overview of sleep management during COVID-19.

### Modafinil → Long COVID
- **claim_id:** `osmf:claim:agent-modafinil-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Modafinil → Long COVID: NCT06404099 (COMPLETED, phase=PHASE2, n=361, relevant=True); NCT06404086 (COMPLETED, phase=PHASE2, n=830, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33723532: Long-Haul Post-COVID-19 Symptoms Presenting as a Variant of Postural Orthostatic Tachycardia Syndrome: The Swedish Exper; PMID 33755344: Persistent neurologic symptoms and cognitive dysfunction in non-hospitalized Covid-19 "long haulers".; PMID 34346558: Multidisciplinary collaborative consensus guidance statement on the assessment and treatment of fatigue in postacute seq. Europe PMC query `(Modafinil) AND ("long COVID" OR "post-COVID" OR PASC)` → 114 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06404099 — RECOVER-SLEEP: Platform Protocol, Appendix_A (Hypersomnia), COMPLETED, PHASE2
  - [pmid] 40537100 — Multidimensional Characterization of Long COVID Fatigue.
  - [nct] NCT06404086 — RECOVER-SLEEP: Platform Protocol, COMPLETED, PHASE2
  - [pmid] 33723532 — Long-Haul Post-COVID-19 Symptoms Presenting as a Variant of Postural Orthostatic Tachycardia Syndrom
  - [pmid] 33755344 — Persistent neurologic symptoms and cognitive dysfunction in non-hospitalized Covid-19 "long haulers"
  - [pmid] 34346558 — Multidisciplinary collaborative consensus guidance statement on the assessment and treatment of fati
  - [pmid] 34390682 — Post-COVID-19 Tachycardia Syndrome: A Distinct Phenotype of Post-Acute COVID-19 Syndrome.
  - [pmid] 34991982 — An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.

### Nad+ → Long COVID
- **claim_id:** `osmf:claim:agent-nad-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Nad+ → Long COVID: NCT04604704 (COMPLETED, phase=PHASE2, n=36, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 34366606: Pancreatic cancer: A review of epidemiology, trend, and risk factors.; PMID 36050306: Lactate metabolism in human health and disease.; PMID 37130947: Metformin: update on mechanisms of action and repurposing potential.. Europe PMC query `(Nad+) AND ("long COVID" OR "post-COVID" OR PASC)` → 724 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT04604704 — Pilot Study Into LDN and NAD+ for Treatment of Patients With Post-COVID-19 Syndrome, COMPLETED, PHASE2
  - [pmid] 34067776 — Post-COVID-19 Syndrome and the Potential Benefits of Exercise.
  - [pmid] 35874958 — Long COVID and its Management.
  - [pmid] 36100326 — Analysis of post COVID-19 condition and its overlap with myalgic encephalomyelitis/chronic fatigue s
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 34366606 — Pancreatic cancer: A review of epidemiology, trend, and risk factors.
  - [pmid] 36050306 — Lactate metabolism in human health and disease.
  - [pmid] 37130947 — Metformin: update on mechanisms of action and repurposing potential.

### Naltrexone → Long COVID
- **claim_id:** `osmf:claim:agent-naltrexone-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Naltrexone → Long COVID: NCT04604704 (COMPLETED, phase=PHASE2, n=36, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 35172971: Risks of mental health outcomes in people with covid-19: cohort study.; PMID 36639608: Long COVID: major findings, mechanisms and recommendations.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.. Europe PMC query `(Naltrexone) AND ("long COVID" OR "post-COVID" OR PASC)` → 366 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT04604704 — Pilot Study Into LDN and NAD+ for Treatment of Patients With Post-COVID-19 Syndrome, COMPLETED, PHASE2
  - [pmid] 34067776 — Post-COVID-19 Syndrome and the Potential Benefits of Exercise.
  - [pmid] 35874958 — Long COVID and its Management.
  - [pmid] 36100326 — Analysis of post COVID-19 condition and its overlap with myalgic encephalomyelitis/chronic fatigue s
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 35172971 — Risks of mental health outcomes in people with covid-19: cohort study.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.

### Nicotinamide Riboside → Long COVID
- **claim_id:** `osmf:claim:agent-nicotinamide-riboside-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Nicotinamide Riboside → Long COVID: NCT05703074 (COMPLETED, phase=PHASE2, n=310, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 34400495: Redox imbalance links COVID-19 and myalgic encephalomyelitis/chronic fatigue syndrome.; PMID 35282780: Registered clinical trials investigating treatment of long COVID: a scoping review and recommendations for research.; PMID 36551869: Understanding Long COVID; Mitochondrial Health and Adaptation-Old Pathways, New Problems.. Europe PMC query `(Nicotinamide Riboside) AND ("long COVID" OR "post-COVID" OR PASC)` → 85 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05703074 — Mental Intervention and Nicotinamide Riboside Supplementation in Long Covid, COMPLETED, PHASE2
  - [pmid] 38668888 — Mitochondrial dysfunction in long COVID: mechanisms, consequences, and potential therapeutic approac
  - [pmid] 40536597 — Role of mitochondria in physiological activities, diseases, and therapy.
  - [pmid] 39495479 — Novel biomarkers of mitochondrial dysfunction in Long COVID patients.
  - [pmid] 41008646 — Mitochondrial Reactive Oxygen Species: A Unifying Mechanism in Long COVID and Spike Protein-Associat
  - [pmid] 34400495 — Redox imbalance links COVID-19 and myalgic encephalomyelitis/chronic fatigue syndrome.
  - [pmid] 35282780 — Registered clinical trials investigating treatment of long COVID: a scoping review and recommendatio
  - [pmid] 36551869 — Understanding Long COVID; Mitochondrial Health and Adaptation-Old Pathways, New Problems.

### Nortriptyline → ME/CFS
- **claim_id:** `osmf:claim:agent-nortriptyline-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Nortriptyline → ME/CFS: NCT03844412 (COMPLETED, phase=PHASE2, n=209, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 17488783: Guidelines on the irritable bowel syndrome: mechanisms and practical management.; PMID 23644052: Inflammatory cytokines in depression: neurobiological mechanisms and therapeutic implications.; PMID 26357876: Inflammation: depression fans the flames and feasts on the heat.. Europe PMC query `(Nortriptyline) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 144 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03844412 — Vestibulodynia: Understanding Pathophysiology and Determining Appropriate Treatments, COMPLETED, PHASE2
  - [pmid] 32478052 — Let-7i-5p Regulation of Cell Morphology and Migration Through Distinct Signaling Pathways in Normal 
  - [pmid] 38984334 — This pain drives me crazy: Psychiatric symptoms in women with interstitial cystitis/bladder pain syn
  - [pmid] 36269028 — Rationale and design of a multicenter randomized clinical trial of vestibulodynia: understanding pat
  - [pmid] 17488783 — Guidelines on the irritable bowel syndrome: mechanisms and practical management.
  - [pmid] 23644052 — Inflammatory cytokines in depression: neurobiological mechanisms and therapeutic implications.
  - [pmid] 26357876 — Inflammation: depression fans the flames and feasts on the heat.
  - [pmid] 27480574 — Inflammation Effects on Motivation and Motor Activity: Role of Dopamine.

### Pacing → ME/CFS
- **claim_id:** `osmf:claim:agent-pacing-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Pacing → ME/CFS: NCT01512342 (COMPLETED, phase=PHASE2, n=33, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 19713422: Guidelines for the diagnosis and management of syncope (version 2009).; PMID 25980576: 2015 heart rhythm society expert consensus statement on the diagnosis and treatment of postural tachycardia syndrome, in; PMID 28506916: 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement on catheter and surgical ablation of atrial fibrillation.. Europe PMC query `(Pacing) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 1084 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT01512342 — Pacing Activity Self-management for Patients With Chronic Fatigue Syndrome, COMPLETED, PHASE2
  - [pmid] 28444695 — Exercise therapy for chronic fatigue syndrome.
  - [pmid] 37838675 — A scoping review of 'Pacing' for management of Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (M
  - [pmid] 26356665 — Activity Pacing Self-Management in Chronic Fatigue Syndrome: A Randomized Controlled Trial.
  - [pmid] 27995604 — Exercise therapy for chronic fatigue syndrome.
  - [pmid] 19713422 — Guidelines for the diagnosis and management of syncope (version 2009).
  - [pmid] 25980576 — 2015 heart rhythm society expert consensus statement on the diagnosis and treatment of postural tach
  - [pmid] 28506916 — 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement on catheter and surgical ablation of atr

### Pentoxifylline → Long COVID
- **claim_id:** `osmf:claim:agent-pentoxifylline-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Pentoxifylline → Long COVID: NCT05513560 (COMPLETED, phase=PHASE2,PHASE3, n=460, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33240091: Challenges for Drug Repurposing in the COVID-19 Pandemic Era.; PMID 35373533: International consensus statement on allergy and rhinology: Olfaction.; PMID 36899952: Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutics.. Europe PMC query `(Pentoxifylline) AND ("long COVID" OR "post-COVID" OR PASC)` → 108 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05513560 — RECLAIM: Recovering From COVID-19 Lingering Symptoms Adaptive Integrative Medicine, COMPLETED, PHASE2,PHASE3
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [pmid] 33240091 — Challenges for Drug Repurposing in the COVID-19 Pandemic Era.
  - [pmid] 35373533 — International consensus statement on allergy and rhinology: Olfaction.
  - [pmid] 36899952 — Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutic

### Personalised Exercise Program → Long COVID
- **claim_id:** `osmf:claim:agent-personalised-exercise-program-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Personalised Exercise Program → Long COVID: NCT06822179 (COMPLETED, phase=PHASE2, n=57, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 35390342: The Lancet Global Health Commission on financing primary health care: putting people at the centre.; PMID 38484753: Global age-sex-specific mortality, life expectancy, and population estimates in 204 countries and territories and 811 su; PMID 38642570: Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DALYs), and healthy li. Europe PMC query `(Personalised Exercise Program) AND ("long COVID" OR "post-COVID" OR PASC)` → 293 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06822179 — Effectiveness of a Personalized In-home Telerehabilitation Program on Self-Care in Patients With Lon, COMPLETED, PHASE2
  - [pmid] 35390342 — The Lancet Global Health Commission on financing primary health care: putting people at the centre.
  - [pmid] 38484753 — Global age-sex-specific mortality, life expectancy, and population estimates in 204 countries and te
  - [pmid] 38642570 — Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DA
  - [pmid] 41092926 — Burden of 375 diseases and injuries, risk-attributable burden of 88 risk factors, and healthy life e
  - [pmid] 41092928 — Global burden of 292 causes of death in 204 countries and territories and 660 subnational locations,
  - [pubmed_search] (Personalised Exercise Program) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (293 hits)

### Photobiomodulation Therapy → Long COVID
- **claim_id:** `osmf:claim:agent-photobiomodulation-therapy-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Early clinical signal thin (small n or sparse pubs) → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Photobiomodulation Therapy → Long COVID: NCT05760092 (COMPLETED, phase=PHASE2, n=10, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 34066560: Probiotics, Photobiomodulation, and Disease Management: Controversies and Challenges.; PMID 36551869: Understanding Long COVID; Mitochondrial Health and Adaptation-Old Pathways, New Problems.; PMID 37298527: Neurodegenerative and Neurodevelopmental Diseases and the Gut-Brain Axis: The Potential of Therapeutic Targeting of the . Europe PMC query `(Photobiomodulation Therapy) AND ("long COVID" OR "post-COVID" OR PASC)` → 100 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05760092 — The Use of Photobiomodulation in the Treatment of Oral Complaints of Long COVID-19.A Randomized Cont, COMPLETED, PHASE2
  - [pmid] 34066560 — Probiotics, Photobiomodulation, and Disease Management: Controversies and Challenges.
  - [pmid] 36551869 — Understanding Long COVID; Mitochondrial Health and Adaptation-Old Pathways, New Problems.
  - [pmid] 37298527 — Neurodegenerative and Neurodevelopmental Diseases and the Gut-Brain Axis: The Potential of Therapeut
  - [pmid] 38067515 — Molecular Hydrogen Therapy-A Review on Clinical Studies and Outcomes.
  - [pmid] 39603702 — Interventions for the management of long covid (post-covid condition): living systematic review.
  - [pubmed_search] (Photobiomodulation Therapy) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (100 hits)

### Plasma Exchange Procedure → Long COVID
- **claim_id:** `osmf:claim:agent-plasma-exchange-procedure-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Plasma Exchange Procedure → Long COVID: NCT05445674 (COMPLETED, phase=PHASE2, n=50, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.; PMID 38264914: 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Association.. Europe PMC query `(Plasma Exchange Procedure) AND ("long COVID" OR "post-COVID" OR PASC)` → 637 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05445674 — Plasma Exchange Therapy for Post- COVID-19 Condition: A Pilot, Randomized Double-Blind Study, COMPLETED, PHASE2
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 37265584 — Biological mechanisms underpinning the development of long COVID.
  - [pmid] 37491597 — Plasmapheresis to remove amyloid fibrin(ogen) particles for treating the post-COVID-19 condition.
  - [pmid] 39994269 — Plasma exchange therapy for the post COVID-19 condition: a phase II, double-blind, placebo-controlle
  - [pmid] 33909761 — Brazilian Guidelines of Hypertension - 2020.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass

### Preprocessed Thawed Autologous Fmt → ME/CFS
- **claim_id:** `osmf:claim:agent-preprocessed-thawed-autologous-fmt-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Preprocessed Thawed Autologous Fmt → ME/CFS: NCT03691987 (COMPLETED, phase=PHASE2, n=80, relevant=True). No posted CT.gov results in this pass. Europe PMC query `(Preprocessed Thawed Autologous Fmt) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 3 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03691987 — The Comeback Study, COMPLETED, PHASE2
  - [pmid] 31201141 — Fecal microbiota transplantation beyond Clostridioides difficile infections.
  - [pmid] 35046929 — The Gut Microbiome in Myalgic Encephalomyelitis (ME)/Chronic Fatigue Syndrome (CFS).
  - [pmid] 33510784 — Fecal Microbiota Transplantation: A New Therapeutic Attempt from the Gut to the Brain.
  - [pmid] 39301964 — Fecal microbial transplants as investigative tools in cancer.
  - [pmid] PMC13254489 — 
  - [pmid] PMC13421919 — 
  - [pmid] PMC6493311 — 

### Preprocessed Thawed Donor Fmt → ME/CFS
- **claim_id:** `osmf:claim:agent-preprocessed-thawed-donor-fmt-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Preprocessed Thawed Donor Fmt → ME/CFS: NCT03691987 (COMPLETED, phase=PHASE2, n=80, relevant=True). No posted CT.gov results in this pass. Europe PMC query `(Preprocessed Thawed Donor Fmt) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 3 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03691987 — The Comeback Study, COMPLETED, PHASE2
  - [pmid] 31201141 — Fecal microbiota transplantation beyond Clostridioides difficile infections.
  - [pmid] 35046929 — The Gut Microbiome in Myalgic Encephalomyelitis (ME)/Chronic Fatigue Syndrome (CFS).
  - [pmid] 33510784 — Fecal Microbiota Transplantation: A New Therapeutic Attempt from the Gut to the Brain.
  - [pmid] 39301964 — Fecal microbial transplants as investigative tools in cancer.
  - [pmid] PMC13254489 — 
  - [pmid] PMC13421919 — 
  - [pmid] PMC6493311 — 

### Probiotic Agent → Long COVID
- **claim_id:** `osmf:claim:agent-probiotic-agent-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Probiotic Agent → Long COVID: NCT06643299 (COMPLETED, phase=PHASE2, n=194, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 36050306: Lactate metabolism in human health and disease.; PMID 36364899: A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.; PMID 37130947: Metformin: update on mechanisms of action and repurposing potential.. Europe PMC query `(Probiotic Agent) AND ("long COVID" OR "post-COVID" OR PASC)` → 253 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06643299 — Probiotic Use for Recovery Enhancement From Long COVID-19, COMPLETED, PHASE2
  - [pmid] 40492581 — Post-COVID-19 condition: clinical phenotypes, pathophysiological mechanisms, pathology, and manageme
  - [pmid] 36050306 — Lactate metabolism in human health and disease.
  - [pmid] 36364899 — A Comprehensive Review on Nutraceuticals: Therapy Support and Formulation Challenges.
  - [pmid] 37130947 — Metformin: update on mechanisms of action and repurposing potential.
  - [pmid] 37358082 — L-arginine metabolism as pivotal interface of mutual host-microbe interactions in the gut.
  - [pmid] 39774607 — Mucosal immune response in biology, disease prevention and treatment.
  - [pubmed_search] (Probiotic Agent) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (253 hits)

### Pyridostigmine Bromide → ME/CFS
- **claim_id:** `osmf:claim:agent-pyridostigmine-bromide-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Pyridostigmine Bromide → ME/CFS: NCT03674541 (COMPLETED, phase=PHASE2, n=45, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 16518518: Anticholinesterase toxicity and oxidative stress.; PMID 18332428: Acetylcholinesterase inhibitors and Gulf War illnesses.; PMID 19375665: Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.. Europe PMC query `(Pyridostigmine Bromide) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 148 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT03674541 — The Exercise Response to Pharmacologic Cholinergic Stimulation in Myalgic Encephalomyelitis / Chroni, COMPLETED, PHASE2
  - [pmid] 35526605 — Neurovascular Dysregulation and Acute Exercise Intolerance in Myalgic Encephalomyelitis/Chronic Fati
  - [pmid] 16518518 — Anticholinesterase toxicity and oxidative stress.
  - [pmid] 18332428 — Acetylcholinesterase inhibitors and Gulf War illnesses.
  - [pmid] 19375665 — Autoimmune myasthenia gravis: emerging clinical and biological heterogeneity.
  - [pmid] 26493934 — Recent research on Gulf War illness and other health problems in veterans of the 1991 Gulf War: Effe
  - [pmid] 34991982 — An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - [pubmed_search] (Pyridostigmine Bromide) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (148 hits)

### Rintatolimod → Long COVID
- **claim_id:** `osmf:claim:agent-rintatolimod-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Rintatolimod → Long COVID: NCT05592418 (COMPLETED, phase=PHASE2, n=80, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33391502: COVID-19 and Cancer Comorbidity: Therapeutic Opportunities and Challenges.; PMID 34024217: Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.; PMID 34181102: The Neurological Manifestations of Post-Acute Sequelae of SARS-CoV-2 infection.. Europe PMC query `(Rintatolimod) AND ("long COVID" OR "post-COVID" OR PASC)` → 43 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05592418 — Study to Evaluate the Efficacy and Safety of Ampligen in Patients With Post-COVID Conditions, COMPLETED, PHASE2
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 39988665 — Toll-like receptor 3: a double-edged sword.
  - [pmid] 37344737 — Long COVID and possible preventive options.
  - [pmid] 33391502 — COVID-19 and Cancer Comorbidity: Therapeutic Opportunities and Challenges.
  - [pmid] 34024217 — Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.
  - [pmid] 34181102 — The Neurological Manifestations of Post-Acute Sequelae of SARS-CoV-2 infection.

### Ritonavir → Long COVID
- **claim_id:** `osmf:claim:agent-ritonavir-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 3 registry trial(s) for Ritonavir → Long COVID: NCT05965726 (COMPLETED, phase=PHASE2, n=964, relevant=True); NCT05576662 (COMPLETED, phase=PHASE2, n=168, relevant=True); NCT05668091 (COMPLETED, phase=PHASE2, n=100, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 32201335: Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID-19 Pandemic.; PMID 33428867: 6-month consequences of COVID-19 in patients discharged from hospital: a cohort study.; PMID 33431578: Gut microbiota composition reflects disease severity and dysfunctional immune responses in patients with COVID-19.. Europe PMC query `(Ritonavir) AND ("long COVID" OR "post-COVID" OR PASC)` → 2077 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05965726 — RECOVER-VITAL: Platform Protocol, Appendix to Measure the Effects of Paxlovid on Long COVID Symptoms, COMPLETED, PHASE2
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 40559563 — Digestive Manifestations of Post-COVID-19: A Focus on Therapeutic Strategies.
  - [nct] NCT05576662 — Paxlovid for Treatment of Long Covid, COMPLETED, PHASE2
  - [pmid] 36899952 — Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutic
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon

### Rslv-132 → Long COVID
- **claim_id:** `osmf:claim:agent-rslv-132-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Rslv-132 → Long COVID: NCT04944121 (COMPLETED, phase=PHASE2, n=112, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 39326415: Mechanisms of long COVID and the path toward therapeutics.. Europe PMC query `(Rslv-132) AND ("long COVID" OR "post-COVID" OR PASC)` → 24 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT04944121 — Phase 2 Study of RSLV-132 in Subjects With Long COVID, COMPLETED, PHASE2
  - [pmid] 36899952 — Pathogenesis Underlying Neurological Manifestations of Long COVID Syndrome and Potential Therapeutic
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 36349400 — Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pubmed_search] (Rslv-132) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (24 hits)

### Self-Administered Acupressure → ME/CFS
- **claim_id:** `osmf:claim:agent-self-administered-acupressure-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Self-Administered Acupressure → ME/CFS: NCT00959998 (COMPLETED, phase=PHASE2, n=43, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 21982157: The evidence for Shiatsu: a systematic review of Shiatsu and acupressure.; PMID 22340435: Societal and individual burden of illness among fibromyalgia patients in France: association between disease severity an; PMID 23067573: The effectiveness of acupuncture research across components of the trauma spectrum response (tsr): a systematic review o. Europe PMC query `(Self-Administered Acupressure) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 38 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT00959998 — Acupressure for Post-Treatment Cancer Fatigue, COMPLETED, PHASE2
  - [pmid] 21982157 — The evidence for Shiatsu: a systematic review of Shiatsu and acupressure.
  - [pmid] 22340435 — Societal and individual burden of illness among fibromyalgia patients in France: association between
  - [pmid] 23067573 — The effectiveness of acupuncture research across components of the trauma spectrum response (tsr): a
  - [pmid] 34490854 — Pragmatic trials of pain therapies: a systematic review of methods.
  - [pmid] 38214047 — Rehabilitation and COVID-19: systematic review by Cochrane Rehabilitation.
  - [pubmed_search] (Self-Administered Acupressure) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (38 hits)

### Solriamfetol → Long COVID
- **claim_id:** `osmf:claim:agent-solriamfetol-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Solriamfetol → Long COVID: NCT06404099 (COMPLETED, phase=PHASE2, n=361, relevant=True); NCT06404086 (COMPLETED, phase=PHASE2, n=830, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 35887329: Proteomic Biomarkers of the Apnea Hypopnea Index and Obstructive Sleep Apnea: Insights into the Pathophysiology of Prese; PMID 36313516: Sleep medicine: Practice, challenges and new frontiers.; PMID 39125722: Comprehensive Review of COVID-19: Epidemiology, Pathogenesis, Advancement in Diagnostic and Detection Techniques, and Po. Europe PMC query `(Solriamfetol) AND ("long COVID" OR "post-COVID" OR PASC)` → 14 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06404099 — RECOVER-SLEEP: Platform Protocol, Appendix_A (Hypersomnia), COMPLETED, PHASE2
  - [pmid] 40537100 — Multidimensional Characterization of Long COVID Fatigue.
  - [nct] NCT06404086 — RECOVER-SLEEP: Platform Protocol, COMPLETED, PHASE2
  - [pmid] 35887329 — Proteomic Biomarkers of the Apnea Hypopnea Index and Obstructive Sleep Apnea: Insights into the Path
  - [pmid] 36313516 — Sleep medicine: Practice, challenges and new frontiers.
  - [pmid] 39125722 — Comprehensive Review of COVID-19: Epidemiology, Pathogenesis, Advancement in Diagnostic and Detectio
  - [pmid] 40046430 — Neurological sequelae of long COVID: a comprehensive review of diagnostic imaging, underlying mechan
  - [pmid] 40261198 — Multidisciplinary collaborative guidance on the assessment and treatment of patients with Long COVID

### Tailored Lighting (Tl) Active → Long COVID
- **claim_id:** `osmf:claim:agent-tailored-lighting-tl-active-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Tailored Lighting (Tl) Active → Long COVID: NCT06404112 (COMPLETED, phase=PHASE2, n=469, relevant=True); NCT06404086 (COMPLETED, phase=PHASE2, n=830, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 34687662: The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.; PMID 36202135: Clinical guidelines for the use of lifestyle-based mental health care in major depressive disorder: World Federation of ; PMID 37712135: Lifestyle management of hypertension: International Society of Hypertension position paper endorsed by the World Hyperte. Europe PMC query `(Tailored Lighting Active) AND ("long COVID" OR "post-COVID" OR PASC)` → 162 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06404112 — RECOVER-SLEEP: Platform Protocol, Appendix_B (CPSD), COMPLETED, PHASE2
  - [pmid] 40537100 — Multidimensional Characterization of Long COVID Fatigue.
  - [nct] NCT06404086 — RECOVER-SLEEP: Platform Protocol, COMPLETED, PHASE2
  - [pmid] 34687662 — The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.
  - [pmid] 36202135 — Clinical guidelines for the use of lifestyle-based mental health care in major depressive disorder: 
  - [pmid] 37712135 — Lifestyle management of hypertension: International Society of Hypertension position paper endorsed 
  - [pmid] 37977174 — The 2023 report of the Lancet Countdown on health and climate change: the imperative for a health-ce
  - [pmid] 39471819 — Bifidobacteria with indole-3-lactic acid-producing capacity exhibit psychobiotic potential via reduc

### Temelimab 54Mg/Kg → Long COVID
- **claim_id:** `osmf:claim:agent-temelimab-54mgkg-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Temelimab 54Mg/Kg → Long COVID: NCT05497089 (COMPLETED, phase=PHASE2, n=203, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 37388279: Long COVID: Complications, Underlying Mechanisms, and Treatment Strategies.; PMID 37493802: Longitudinal analysis and treatment of neuropsychiatric symptoms in post-acute sequelae of COVID-19.; PMID 39240417: Towards an understanding of physical activity-induced post-exertional malaise: Insights into microvascular alterations a. Europe PMC query `(Temelimab/Kg) AND ("long COVID" OR "post-COVID" OR PASC)` → 5 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05497089 — Temelimab as a Disease Modifying Therapy in Patients With Neuropsychiatric Symptoms in Post-COVID 19, COMPLETED, PHASE2
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 37457901 — Post-COVID cognitive dysfunction: current status and research recommendations for high risk populati
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 37388279 — Long COVID: Complications, Underlying Mechanisms, and Treatment Strategies.
  - [pmid] 37493802 — Longitudinal analysis and treatment of neuropsychiatric symptoms in post-acute sequelae of COVID-19.
  - [pmid] 39240417 — Towards an understanding of physical activity-induced post-exertional malaise: Insights into microva

### Tnx-102 Sl → Long COVID
- **claim_id:** `osmf:claim:agent-tnx-102-sl-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Tnx-102 Sl → Long COVID: NCT05472090 (COMPLETED, phase=PHASE2, n=63, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 37316880: Long COVID: Costs for the German economy and health care and pension system.. Europe PMC query `(Tnx-102 Sl) AND ("long COVID" OR "post-COVID" OR PASC)` → 4 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT05472090 — A Phase 2 Study to Evaluate the Efficacy and Safety of TNX-102 SL in Patients With Multi-Site Pain A, COMPLETED, PHASE2
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 40384184 — Transforming Niclosamide through Nanotechnology: A Promising Approach for Long COVID Management.
  - [pmid] 37680987 — The current landscape of long COVID clinical trials: NIH's RECOVER to Stanford Medicine's STOP-PASC 
  - [pmid] 37316880 — Long COVID: Costs for the German economy and health care and pension system.
  - [pubmed_search] (Tnx-102 Sl) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (4 hits)

### Tonabersat → Long COVID
- **claim_id:** `osmf:claim:agent-tonabersat-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `A`
- **rationale:** Completed Phase 2+ condition-relevant trial without posted results/pubs in this pass → C draft.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Tonabersat → Long COVID: NCT06437223 (COMPLETED, phase=PHASE2, n=16, relevant=True). No posted CT.gov results in this pass. Europe PMC query `(Tonabersat) AND ("long COVID" OR "post-COVID" OR PASC)` → 0 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT06437223 — Study of Xiflam™ Treatment in Patients Post COVID-19 Infection Suffering From What is Known as Long , COMPLETED, PHASE2
  - [pubmed_search] (Tonabersat) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (0 hits)

### Valacyclovir Celecoxib Dose 1 → Long COVID
- **claim_id:** `osmf:claim:agent-valacyclovir-celecoxib-dose-1-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Valacyclovir Celecoxib Dose 1 → Long COVID: NCT06316843 (COMPLETED, phase=PHASE2, n=59, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33052705: Angioedema in African American Patients Hospitalized for COVID-19.; PMID 36969241: Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOVER initiative.; PMID 39762640: Impact of extended-course oral nirmatrelvir/ritonavir in established Long COVID: a case series.. Europe PMC query `(Valacyclovir Celecoxib Dose 1) AND ("long COVID" OR "post-COVID" OR PASC)` → 10 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06316843 — Valacyclovir Plus Celecoxib for Post-Acute Sequelae of SARS-CoV-2, COMPLETED, PHASE2
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 40559563 — Digestive Manifestations of Post-COVID-19: A Focus on Therapeutic Strategies.
  - [pmid] 33052705 — Angioedema in African American Patients Hospitalized for COVID-19.
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 39762640 — Impact of extended-course oral nirmatrelvir/ritonavir in established Long COVID: a case series.
  - [pmid] 39984803 — Interventions for Long COVID: A Narrative Review.
  - [pmid] 41257741 — Imaging brain inflammation and blood brain barrier permeability in neurological and psychiatric dise

### Valacyclovir Celecoxib Dose 2 → Long COVID
- **claim_id:** `osmf:claim:agent-valacyclovir-celecoxib-dose-2-treats-long-covid`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Valacyclovir Celecoxib Dose 2 → Long COVID: NCT06316843 (COMPLETED, phase=PHASE2, n=59, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 33052705: Angioedema in African American Patients Hospitalized for COVID-19.; PMID 36969241: Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOVER initiative.; PMID 39762640: Impact of extended-course oral nirmatrelvir/ritonavir in established Long COVID: a case series.. Europe PMC query `(Valacyclovir Celecoxib Dose 2) AND ("long COVID" OR "post-COVID" OR PASC)` → 10 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT06316843 — Valacyclovir Plus Celecoxib for Post-Acute Sequelae of SARS-CoV-2, COMPLETED, PHASE2
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 40559563 — Digestive Manifestations of Post-COVID-19: A Focus on Therapeutic Strategies.
  - [pmid] 33052705 — Angioedema in African American Patients Hospitalized for COVID-19.
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 39762640 — Impact of extended-course oral nirmatrelvir/ritonavir in established Long COVID: a case series.
  - [pmid] 39984803 — Interventions for Long COVID: A Narrative Review.
  - [pmid] 41257741 — Imaging brain inflammation and blood brain barrier permeability in neurological and psychiatric dise

### Valganciclovir → ME/CFS
- **claim_id:** `osmf:claim:agent-valganciclovir-treats-me-cfs`
- **proposed:** tier C, status `published`, confidence `medium`, wave `A`
- **rationale:** Early clinical (completed Phase 2+/condition-relevant) with results or NCT-linked publications → C published (Preliminary; not confirmatory).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Valganciclovir → ME/CFS: NCT00478465 (COMPLETED, phase=PHASE1,PHASE2, n=30, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 19515747: Epstein-Barr virus-associated lymphoproliferative disease in non-immunocompromised hosts: a status report and summary of; PMID 30285773: Chronic viral infections in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS).; PMID 31394725: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: A Comprehensive Review.. Europe PMC query `(Valganciclovir) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 107 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Larger confirmatory trials and outcome publications
- **references:**
  - [nct] NCT00478465 — Valganciclovir (Valcyte) for Chronic Fatigue Syndrome Patients Who Have Elevated Antibody Titers Aga, COMPLETED, PHASE1,PHASE2
  - [pmid] 41451409 — Stereoselective design of amino acid bioconjugates: targeting strategies and physicochemical optimiz
  - [pmid] 19515747 — Epstein-Barr virus-associated lymphoproliferative disease in non-immunocompromised hosts: a status r
  - [pmid] 30285773 — Chronic viral infections in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS).
  - [pmid] 31394725 — Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: A Comprehensive Review.
  - [pmid] 33726557 — A review: Mechanism of action of antiviral drugs.
  - [pmid] 36639608 — Long COVID: major findings, mechanisms and recommendations.
  - [pubmed_search] (Valganciclovir) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (107 hits)

### Immunoadsorption → Long COVID
- **claim_id:** `osmf:claim:agent-immunoadsorption-treats-long-covid`
- **proposed:** tier C, status `draft`, confidence `medium`, wave `B`
- **rationale:** Completed Phase 2+ condition-relevant trial without posted results/pubs in this pass → C draft.
- **evidence_summary:** Wave B. Extracted 2 registry trial(s) for Immunoadsorption → Long COVID: NCT05710770 (COMPLETED, phase=NA, n=66, relevant=True); NCT07316127 (RECRUITING, phase=PHASE2, n=70, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Posted results / publications of primary outcomes
- **references:**
  - [nct] NCT05710770 — Immunoadsorption in Patients With Chronic Fatigue Syndrome Including Patients With Post-COVID-19 CFS, COMPLETED, NA
  - [nct] NCT07316127 — Immunoadsorption in Autoimmune Long COVID, RECRUITING, PHASE2

## Tier D

### Active Tdcs → Long COVID
- **claim_id:** `osmf:claim:agent-active-tdcs-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Active Tdcs → Long COVID: NCT05092516 (ACTIVE_NOT_RECRUITING, phase=NA, n=31, relevant=True); NCT05589272 (WITHDRAWN, phase=NA, n=0, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 35734582: Non-invasive brain stimulation and neuroenhancement.; PMID 38378653: Nanotechnology's frontier in combatting infectious and inflammatory diseases: prevention and treatment.; PMID 39232147: Immune system adaptation during gender-affirming testosterone treatment.. Europe PMC query `(Active Tdcs) AND ("long COVID" OR "post-COVID" OR PASC)` → 143 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT05092516 — Home-based Brain Stimulation Treatment for Post-acute Sequelae of COVID-19 (PASC), ACTIVE_NOT_RECRUITING, NA
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [nct] NCT05589272 — TDCS-potentiated Generalization of Cognitive Training in the Rehabilitation of Long COVID Symptoms, WITHDRAWN, NA
  - [pmid] 35734582 — Non-invasive brain stimulation and neuroenhancement.
  - [pmid] 38378653 — Nanotechnology's frontier in combatting infectious and inflammatory diseases: prevention and treatme
  - [pmid] 39232147 — Immune system adaptation during gender-affirming testosterone treatment.
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pmid] 39482575 — Hallmarks of primary headache: part 1 - migraine.

### Aer002 → Long COVID
- **claim_id:** `osmf:claim:agent-aer002-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Aer002 → Long COVID: NCT05877508 (ACTIVE_NOT_RECRUITING, phase=PHASE2, n=36, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 38221576: A First-in-Human Randomized Study to Assess the Safety, Tolerability, Pharmacokinetics, and Neutralization Profile of Tw; PMID 38432691: Emerging anti-spike monoclonal antibodies against SARS-CoV-2.; PMID 41836927: Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.. Europe PMC query `(Aer002) AND ("long COVID" OR "post-COVID" OR PASC)` → 8 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT05877508 — Anti-SARS-CoV-2 Monoclonal Antibodies for Long COVID (COVID-19), ACTIVE_NOT_RECRUITING, PHASE2
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 41089328 — Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and
  - [pmid] 40346201 — Impact of COVID-19 vaccination on symptoms and immune phenotypes in vaccine-naïve individuals with L
  - [pmid] 39536121 — Infection-associated chronic conditions: Why Long Covid is our best chance to untangle Osler's web.
  - [pmid] 38221576 — A First-in-Human Randomized Study to Assess the Safety, Tolerability, Pharmacokinetics, and Neutrali
  - [pmid] 38432691 — Emerging anti-spike monoclonal antibodies against SARS-CoV-2.
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.

### Ampion → Long COVID
- **claim_id:** `osmf:claim:agent-ampion-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ampion → Long COVID: NCT04880161 (COMPLETED, phase=PHASE1, n=32, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 34371768: Inhalation Delivery for the Treatment and Prevention of COVID-19 Infection.; PMID 35282780: Registered clinical trials investigating treatment of long COVID: a scoping review and recommendations for research.; PMID 35745708: Post-COVID Syndrome: The Research Progress in the Treatment of Pulmonary <i>sequelae</i> after COVID-19 Infection.. Europe PMC query `(Ampion) AND ("long COVID" OR "post-COVID" OR PASC)` → 6 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT04880161 — A Study to Evaluate Ampion in Patients With Prolonged Respiratory Symptoms Due to COVID-19 (Long COV, COMPLETED, PHASE1
  - [pmid] 36349400 — Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - [pmid] 37344737 — Long COVID and possible preventive options.
  - [pmid] 34371768 — Inhalation Delivery for the Treatment and Prevention of COVID-19 Infection.
  - [pmid] 35282780 — Registered clinical trials investigating treatment of long COVID: a scoping review and recommendatio
  - [pmid] 35745708 — Post-COVID Syndrome: The Research Progress in the Treatment of Pulmonary <i>sequelae</i> after COVID
  - [pmid] 36758333 — Are we ready to combat the ecotoxicity of COVID-19 pharmaceuticals? An in silico aquatic risk assess
  - [pubmed_search] (Ampion) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (6 hits)

### Brainhq → Long COVID
- **claim_id:** `osmf:claim:agent-brainhq-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Brainhq → Long COVID: NCT05965752 (COMPLETED, phase=NA, n=328, relevant=True); NCT05965739 (COMPLETED, phase=NA, n=328, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 34655835: Telehealth transcranial direct current stimulation for recovery from Post-Acute Sequelae of SARS-CoV-2 (PASC).; PMID 36202328: Combination of transcranial direct current stimulation with online cognitive training improves symptoms of Post-acute Se; PMID 39429966: COVID-19 and multiple sclerosis: challenges and lessons for patient care.. Europe PMC query `(Brainhq) AND ("long COVID" OR "post-COVID" OR PASC)` → 17 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05965752 — RECOVER-NEURO: Platform Protocol to Measure the Effects of Cognitive Dysfunction Interventions on Lo, COMPLETED, NA
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [nct] NCT05965739 — RECOVER-NEURO: Platform Protocol, Appendix_A to Measure the Effects of BrainHQ, PASC CoRE and tDCS I, COMPLETED, NA
  - [pmid] 38495306 — Neurovascular coupling impairment as a mechanism for cognitive deficits in COVID-19.
  - [pmid] 38755688 — RECOVER-NEURO: study protocol for a multi-center, multi-arm, phase 2, randomized, active comparator 
  - [pmid] 41212544 — Evaluation of Interventions for Cognitive Symptoms in Long COVID: A Randomized Clinical Trial.
  - [pmid] 34655835 — Telehealth transcranial direct current stimulation for recovery from Post-Acute Sequelae of SARS-CoV
  - [pmid] 36202328 — Combination of transcranial direct current stimulation with online cognitive training improves sympt

### Brainhq/Active Comparator Activity → Long COVID
- **claim_id:** `osmf:claim:agent-brainhqactive-comparator-activity-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Brainhq/Active Comparator Activity → Long COVID: NCT05965752 (COMPLETED, phase=NA, n=328, relevant=True); NCT05965739 (COMPLETED, phase=NA, n=328, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33346896: Abstracts of the 16th International E-Congress of the European Geriatric Medicine Society : 7-9 October 2020.. Europe PMC query `(Brainhq/Active Comparator Activity) AND ("long COVID" OR "post-COVID" OR PASC)` → 4 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05965752 — RECOVER-NEURO: Platform Protocol to Measure the Effects of Cognitive Dysfunction Interventions on Lo, COMPLETED, NA
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [nct] NCT05965739 — RECOVER-NEURO: Platform Protocol, Appendix_A to Measure the Effects of BrainHQ, PASC CoRE and tDCS I, COMPLETED, NA
  - [pmid] 38495306 — Neurovascular coupling impairment as a mechanism for cognitive deficits in COVID-19.
  - [pmid] 38755688 — RECOVER-NEURO: study protocol for a multi-center, multi-arm, phase 2, randomized, active comparator 
  - [pmid] 41212544 — Evaluation of Interventions for Cognitive Symptoms in Long COVID: A Randomized Clinical Trial.
  - [pmid] 33346896 — Abstracts of the 16th International E-Congress of the European Geriatric Medicine Society : 7-9 Octo
  - [pmid] PMC10729595 — 

### Cardiopulmonary Exercise Test → ME/CFS
- **claim_id:** `osmf:claim:agent-cardiopulmonary-exercise-test-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Cardiopulmonary Exercise Test → ME/CFS: NCT02669212 (COMPLETED, phase=NA, n=52, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 19713422: Guidelines for the diagnosis and management of syncope (version 2009).; PMID 25266247: Guidelines for the treatment of hypothyroidism: prepared by the american thyroid association task force on thyroid hormo; PMID 25980576: 2015 heart rhythm society expert consensus statement on the diagnosis and treatment of postural tachycardia syndrome, in. Europe PMC query `(Cardiopulmonary Exercise Test) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 868 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT02669212 — Myalgic Encephalomyelitis Chronic Fatigue at the National Institutes of Health, COMPLETED, NA
  - [pmid] 37147136 — Deep Phenotyping of Neurologic Postacute Sequelae of SARS-CoV-2 Infection.
  - [pmid] 37579159 — WASF3 disrupts mitochondrial respiration and may mediate exercise intolerance in myalgic encephalomy
  - [pmid] 40337174 — Post-exertional malaise in Long COVID: subjective reporting versus objective assessment.
  - [pmid] 38352048 — Mixed methods system for the assessment of post-exertional malaise in myalgic encephalomyelitis/chro
  - [pmid] 19713422 — Guidelines for the diagnosis and management of syncope (version 2009).
  - [pmid] 25266247 — Guidelines for the treatment of hypothyroidism: prepared by the american thyroid association task fo
  - [pmid] 25980576 — 2015 heart rhythm society expert consensus statement on the diagnosis and treatment of postural tach

### Care As Usual → Long COVID
- **claim_id:** `osmf:claim:agent-care-as-usual-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **evidence_summary:** 'Care As Usual' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources (wave A). Associated registry entries appear procedural/class/placebo-related.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT05703074 — Mental Intervention and Nicotinamide Riboside Supplementation in Long Covid, COMPLETED, PHASE2
  - [pmid] 38668888 — Mitochondrial dysfunction in long COVID: mechanisms, consequences, and potential therapeutic approac
  - [pmid] 40536597 — Role of mitochondria in physiological activities, diseases, and therapy.
  - [pmid] 39495479 — Novel biomarkers of mitochondrial dysfunction in Long COVID patients.
  - [pmid] 41008646 — Mitochondrial Reactive Oxygen Species: A Unifying Mechanism in Long COVID and Spike Protein-Associat
  - [pmid] 32526206 — SARS-CoV-2 Reverse Genetics Reveals a Variable Infection Gradient in the Respiratory Tract.
  - [pmid] 33428867 — 6-month consequences of COVID-19 in patients discharged from hospital: a cohort study.
  - [pmid] 34973396 — Fatigue and cognitive impairment in Post-COVID-19 Syndrome: A systematic review and meta-analysis.

### Coenzyme Q10 (CoQ10) → Gulf War Illness
- **claim_id:** `osmf:claim:agent-coenzyme-q10-coq10-treats-gulf-war-illness`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Wave A. Extracted 4 registry trial(s) for Coenzyme Q10 (CoQ10) → Gulf War Illness: NCT06597682 (NOT_YET_RECRUITING, phase=NA, n=632, relevant=False); NCT03186027 (COMPLETED, phase=NA, n=282, relevant=False); NCT05128292 (COMPLETED, phase=NA, n=42, relevant=False); NCT02063126 (COMPLETED, phase=PHASE2,PHASE3, n=80, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 26770107: Mitochondrial Dysfunction and Chronic Disease: Treatment With Natural Supplements.; PMID 30144465: Neurotoxicity in acute and repeated organophosphate exposure.; PMID 37008131: Curcumin Formulations for Better Bioavailability: What We Learned from Clinical Trials Thus Far?. Europe PMC query `(Coenzyme Q10) AND ("Gulf War Illness" OR "Gulf War syndrome")` → 56 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT06597682 — Evaluating Immunomodulatory Interventions in Post-Acute Sequelae of SARS-CoV-2 InfEction, NOT_YET_RECRUITING, NA
  - [nct] NCT03186027 — Coenzyme Q10 Plus NADH Supplementation in Chronic Fatigue Syndrome/Myalgic Encephalomyelitis, COMPLETED, NA
  - [pmid] 34444817 — Effect of Dietary Coenzyme Q10 Plus NADH Supplementation on Fatigue Perception and Health-Related Qu
  - [nct] NCT05128292 — Effect of CoQ10 Plus Selenium Supplementation on Clinical Outcomes and Biochemical Markers in ME/CFS, COMPLETED, NA
  - [pmid] 35229657 — Does Coenzyme Q10 Plus Selenium Supplementation Ameliorate Clinical Outcomes by Modulating Oxidative
  - [nct] NCT02063126 — Clinical Trial to Measure the Maximun HR After ReConnect ® Supplementation vs. Placebo in CFS., COMPLETED, PHASE2,PHASE3
  - [pmid] 25386668 — Does oral coenzyme Q10 plus NADH supplementation improve fatigue and biochemical parameters in chron
  - [pmid] 34067632 — Coenzyme Q<sub>10</sub>: Clinical Applications beyond Cardiovascular Diseases.

### Coenzyme Q10 (CoQ10) → Long COVID
- **claim_id:** `osmf:claim:agent-coenzyme-q10-coq10-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave A. Extracted 4 registry trial(s) for Coenzyme Q10 (CoQ10) → Long COVID: NCT06597682 (NOT_YET_RECRUITING, phase=NA, n=632, relevant=True); NCT03186027 (COMPLETED, phase=NA, n=282, relevant=False); NCT05128292 (COMPLETED, phase=NA, n=42, relevant=False); NCT02063126 (COMPLETED, phase=PHASE2,PHASE3, n=80, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 34024217: Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.; PMID 34400495: Redox imbalance links COVID-19 and myalgic encephalomyelitis/chronic fatigue syndrome.. Europe PMC query `(Coenzyme Q10) AND ("long COVID" OR "post-COVID" OR PASC)` → 254 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT06597682 — Evaluating Immunomodulatory Interventions in Post-Acute Sequelae of SARS-CoV-2 InfEction, NOT_YET_RECRUITING, NA
  - [nct] NCT03186027 — Coenzyme Q10 Plus NADH Supplementation in Chronic Fatigue Syndrome/Myalgic Encephalomyelitis, COMPLETED, NA
  - [pmid] 34444817 — Effect of Dietary Coenzyme Q10 Plus NADH Supplementation on Fatigue Perception and Health-Related Qu
  - [nct] NCT05128292 — Effect of CoQ10 Plus Selenium Supplementation on Clinical Outcomes and Biochemical Markers in ME/CFS, COMPLETED, NA
  - [pmid] 35229657 — Does Coenzyme Q10 Plus Selenium Supplementation Ameliorate Clinical Outcomes by Modulating Oxidative
  - [nct] NCT02063126 — Clinical Trial to Measure the Maximun HR After ReConnect ® Supplementation vs. Placebo in CFS., COMPLETED, PHASE2,PHASE3
  - [pmid] 25386668 — Does oral coenzyme Q10 plus NADH supplementation improve fatigue and biochemical parameters in chron
  - [pmid] 34067632 — Coenzyme Q<sub>10</sub>: Clinical Applications beyond Cardiovascular Diseases.

### Coenzyme Q10 (CoQ10) → Other Post-Viral & Post-Infectious Syndromes
- **claim_id:** `osmf:claim:agent-coenzyme-q10-coq10-treats-other-post-viral`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Wave A. Extracted 4 registry trial(s) for Coenzyme Q10 (CoQ10) → Other Post-Viral & Post-Infectious Syndromes: NCT06597682 (NOT_YET_RECRUITING, phase=NA, n=632, relevant=False); NCT03186027 (COMPLETED, phase=NA, n=282, relevant=False); NCT05128292 (COMPLETED, phase=NA, n=42, relevant=False); NCT02063126 (COMPLETED, phase=PHASE2,PHASE3, n=80, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 25147756: Association of Mitochondrial Dysfunction and Fatigue: A Review of the Literature.; PMID 31394725: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: A Comprehensive Review.; PMID 34024217: Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.. Europe PMC query `(Coenzyme Q10) AND ("post-viral" OR "post viral fatigue")` → 81 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT06597682 — Evaluating Immunomodulatory Interventions in Post-Acute Sequelae of SARS-CoV-2 InfEction, NOT_YET_RECRUITING, NA
  - [nct] NCT03186027 — Coenzyme Q10 Plus NADH Supplementation in Chronic Fatigue Syndrome/Myalgic Encephalomyelitis, COMPLETED, NA
  - [pmid] 34444817 — Effect of Dietary Coenzyme Q10 Plus NADH Supplementation on Fatigue Perception and Health-Related Qu
  - [nct] NCT05128292 — Effect of CoQ10 Plus Selenium Supplementation on Clinical Outcomes and Biochemical Markers in ME/CFS, COMPLETED, NA
  - [pmid] 35229657 — Does Coenzyme Q10 Plus Selenium Supplementation Ameliorate Clinical Outcomes by Modulating Oxidative
  - [nct] NCT02063126 — Clinical Trial to Measure the Maximun HR After ReConnect ® Supplementation vs. Placebo in CFS., COMPLETED, PHASE2,PHASE3
  - [pmid] 25386668 — Does oral coenzyme Q10 plus NADH supplementation improve fatigue and biochemical parameters in chron
  - [pmid] 34067632 — Coenzyme Q<sub>10</sub>: Clinical Applications beyond Cardiovascular Diseases.

### Coenzyme Q10 (CoQ10) → POTS
- **claim_id:** `osmf:claim:agent-coenzyme-q10-coq10-treats-pots`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Wave A. Extracted 4 registry trial(s) for Coenzyme Q10 (CoQ10) → POTS: NCT06597682 (NOT_YET_RECRUITING, phase=NA, n=632, relevant=False); NCT03186027 (COMPLETED, phase=NA, n=282, relevant=False); NCT05128292 (COMPLETED, phase=NA, n=42, relevant=False); NCT02063126 (COMPLETED, phase=PHASE2,PHASE3, n=80, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 31394725: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome: A Comprehensive Review.; PMID 34024217: Long COVID or post-COVID-19 syndrome: putative pathophysiology, risk factors, and treatments.; PMID 35198136: Neurological manifestations of long-COVID syndrome: a narrative review.. Europe PMC query `(Coenzyme Q10) AND ("postural orthostatic tachycardia" OR POTS)` → 128 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT06597682 — Evaluating Immunomodulatory Interventions in Post-Acute Sequelae of SARS-CoV-2 InfEction, NOT_YET_RECRUITING, NA
  - [nct] NCT03186027 — Coenzyme Q10 Plus NADH Supplementation in Chronic Fatigue Syndrome/Myalgic Encephalomyelitis, COMPLETED, NA
  - [pmid] 34444817 — Effect of Dietary Coenzyme Q10 Plus NADH Supplementation on Fatigue Perception and Health-Related Qu
  - [nct] NCT05128292 — Effect of CoQ10 Plus Selenium Supplementation on Clinical Outcomes and Biochemical Markers in ME/CFS, COMPLETED, NA
  - [pmid] 35229657 — Does Coenzyme Q10 Plus Selenium Supplementation Ameliorate Clinical Outcomes by Modulating Oxidative
  - [nct] NCT02063126 — Clinical Trial to Measure the Maximun HR After ReConnect ® Supplementation vs. Placebo in CFS., COMPLETED, PHASE2,PHASE3
  - [pmid] 25386668 — Does oral coenzyme Q10 plus NADH supplementation improve fatigue and biochemical parameters in chron
  - [pmid] 34067632 — Coenzyme Q<sub>10</sub>: Clinical Applications beyond Cardiovascular Diseases.

### Cognitive Behavioral Therapy → ME/CFS
- **claim_id:** `osmf:claim:agent-cognitive-behavioral-therapy-treats-me-cfs`
- **proposed:** tier D, status `published`, confidence `medium`, wave `A`
- **rationale:** CBT for ME/CFS remains highly contested (PACE controversy; NICE NG206 does not recommend CBT as curative). Tier D despite trial activity.
- **evidence_summary:** CBT has been studied in ME/CFS, but the evidence base is contested and guideline positions diverge. Linked statuses: COMPLETED. Not framed as solid disease-modifying clinical evidence.
- **gaps:** Guideline conflict and outcome-measure disputes
- **references:**
  - [nct] NCT00540254 — Behavioral Insomnia Therapy With Chronic Fatigue Syndrome, COMPLETED, PHASE1,PHASE2
  - [pmid] 20350028 — The effect of mindfulness-based therapy on anxiety and depression: A meta-analytic review.
  - [pmid] 23459093 — The Efficacy of Cognitive Behavioral Therapy: A Review of Meta-analyses.
  - [pmid] 30496104 — Global, regional, and national incidence, prevalence, and years lived with disability for 354 diseas
  - [pmid] 32437679 — Psychiatric and neuropsychiatric presentations associated with severe coronavirus infections: a syst
  - [pmid] 34373540 — More than 50 long-term effects of COVID-19: a systematic review and meta-analysis.
  - [pubmed_search] (Cognitive Behavioral Therapy) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (3234 hits)

### Coordinated Care → Long COVID
- **claim_id:** `osmf:claim:agent-coordinated-care-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **evidence_summary:** 'Coordinated Care' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources (wave A). Associated registry entries appear procedural/class/placebo-related.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT06305793 — RECOVER-AUTONOMIC: Platform Protocol, Appendix A (IVIG), COMPLETED, PHASE2
  - [pmid] 41089328 — Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and
  - [pmid] 42053865 — Pathogenic IgG from long COVID patients with neurological sequelae triggers sensitive but not cognit
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [nct] NCT06305806 — RECOVER-AUTONOMIC: Platform Protocol, Appendix B (Ivabradine), COMPLETED, PHASE2
  - [pmid] 42325367 — Long COVID: current research and future directions.
  - [pmid] 41720282 — Design and rationale of RECOVER-AUTONOMIC: A randomized platform trial evaluating interventions for 

### Covid Rehab Formula Granules → Long COVID
- **claim_id:** `osmf:claim:agent-covid-rehab-formula-granules-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Covid Rehab Formula Granules → Long COVID: NCT04924881 (COMPLETED, phase=PHASE2, n=68, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 36008648: World Congress on Osteoporosis, Osteoarthritis and Musculoskeletal Diseases (WCO-IOF-ESCEO 2022).; PMID 38746044: Traditional, complementary and integrative medicine for fatigue post COVID-19 infection: A systematic review of randomiz; PMID 39361093: ESICM LIVES 2024. Barcelona, Spain. 5–9 October 2024.. Europe PMC query `(Covid Rehab Formula Granules) AND ("long COVID" OR "post-COVID" OR PASC)` → 22 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT04924881 — Chinese Medicine for Patients With LCOVID-19 Symptoms, COMPLETED, PHASE2
  - [pmid] 36687403 — Chinese medicine for residual symptoms of COVID-19 recovered patients (long COVID)-A double-blind, r
  - [pmid] 36008648 — World Congress on Osteoporosis, Osteoarthritis and Musculoskeletal Diseases (WCO-IOF-ESCEO 2022).
  - [pmid] 38746044 — Traditional, complementary and integrative medicine for fatigue post COVID-19 infection: A systemati
  - [pmid] 39361093 — ESICM LIVES 2024. Barcelona, Spain. 5–9 October 2024.
  - [pmid] 40986224 — World Congress on Osteoporosis, Osteoarthritis and Musculoskeletal Diseases (WCO-IOF-ESCEO 2025).
  - [pubmed_search] (Covid Rehab Formula Granules) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (22 hits)

### Droxidopa → ME/CFS
- **claim_id:** `osmf:claim:agent-droxidopa-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Droxidopa → ME/CFS: NCT00977171 (TERMINATED, phase=PHASE2, n=3, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 23569093: Common syndromes of orthostatic intolerance.; PMID 24819031: Adolescent fatigue, POTS, and recovery: a guide for clinicians.; PMID 29222399: Pediatric Disorders of Orthostatic Intolerance.. Europe PMC query `(Droxidopa) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 44 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Not a systematic review; single-pass registry + selective literature sampling
- **references:**
  - [nct] NCT00977171 — Study To Assess The Clinical Benefit Of Droxidopa In Subjects With Chronic Fatigue Syndrome, TERMINATED, PHASE2
  - [pmid] 23569093 — Common syndromes of orthostatic intolerance.
  - [pmid] 24819031 — Adolescent fatigue, POTS, and recovery: a guide for clinicians.
  - [pmid] 29222399 — Pediatric Disorders of Orthostatic Intolerance.
  - [pmid] 33723532 — Long-Haul Post-COVID-19 Symptoms Presenting as a Variant of Postural Orthostatic Tachycardia Syndrom
  - [pmid] 34821709 — Post-Acute Sequelae of COVID-19 and Cardiovascular Autonomic Dysfunction: What Do We Know?
  - [pubmed_search] (Droxidopa) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (44 hits)

### Efgartigimod → Long COVID
- **claim_id:** `osmf:claim:agent-efgartigimod-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Efgartigimod → Long COVID: NCT05918978 (TERMINATED, phase=PHASE2, n=33, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33802650: In Translation: FcRn across the Therapeutic Spectrum.; PMID 37396922: Fighting Post-COVID and ME/CFS - development of curative therapies.; PMID 38617189: Structure and function of therapeutic antibodies approved by the US FDA in 2023.. Europe PMC query `(Efgartigimod) AND ("long COVID" OR "post-COVID" OR PASC)` → 40 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Not a systematic review; single-pass registry + selective literature sampling
- **references:**
  - [nct] NCT05918978 — Open Label Extension of Efgartigimod in Adults With Post-COVID-19 POTS, TERMINATED, PHASE2
  - [pmid] 40156757 — Targeting the Neonatal Fc Receptor in Autoimmune Diseases: Pipeline and Progress.
  - [pmid] 39189008 — Cardiovascular disease and covid-19: A systematic review.
  - [pmid] 33802650 — In Translation: FcRn across the Therapeutic Spectrum.
  - [pmid] 37396922 — Fighting Post-COVID and ME/CFS - development of curative therapies.
  - [pmid] 38617189 — Structure and function of therapeutic antibodies approved by the US FDA in 2023.
  - [pmid] 39736771 — Platelet signaling in immune landscape: comprehensive mechanism and clinical therapy.
  - [pubmed_search] (Efgartigimod) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (40 hits)

### Ensitrelvir → Long COVID
- **claim_id:** `osmf:claim:agent-ensitrelvir-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Ensitrelvir → Long COVID: NCT06161688 (ACTIVE_NOT_RECRUITING, phase=PHASE2, n=40, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 37076602: Therapeutic strategies for COVID-19: progress and lessons learned.; PMID 37112923: Evolution of SARS-CoV-2 Variants: Implications on Immune Escape, Vaccination, Therapeutic and Diagnostic Strategies.; PMID 37173515: Accelerating antiviral drug discovery: lessons from COVID-19.. Europe PMC query `(Ensitrelvir) AND ("long COVID" OR "post-COVID" OR PASC)` → 112 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT06161688 — Ensitrelvir for Viral Persistence and Inflammation in People Experiencing Long COVID, ACTIVE_NOT_RECRUITING, PHASE2
  - [pmid] 39947217 — Targeting the SARS-CoV-2 reservoir in long COVID.
  - [pmid] 39062511 — Inhibitors of SARS-CoV-2 Main Protease (Mpro) as Anti-Coronavirus Agents.
  - [pmid] 41836927 — Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - [pmid] 40559563 — Digestive Manifestations of Post-COVID-19: A Focus on Therapeutic Strategies.
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 37112923 — Evolution of SARS-CoV-2 Variants: Implications on Immune Escape, Vaccination, Therapeutic and Diagno
  - [pmid] 37173515 — Accelerating antiviral drug discovery: lessons from COVID-19.

### Home-Based Telerehabilitation → Long COVID
- **claim_id:** `osmf:claim:agent-home-based-telerehabilitation-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Home-Based Telerehabilitation → Long COVID: NCT05205460 (COMPLETED, phase=NA, n=182, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 32369030: Considerations for Postacute Rehabilitation for Survivors of COVID-19.; PMID 33642858: Pulmonary Rehabilitation in a Post-COVID-19 World: Telerehabilitation as a New Standard in Patients with COPD.; PMID 34051516: Physical and mental health complications post-COVID-19: Scoping review.. Europe PMC query `(Home-Based Telerehabilitation) AND ("long COVID" OR "post-COVID" OR PASC)` → 528 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05205460 — Telerehabilitation in People With Long COVID, COMPLETED, NA
  - [pmid] 38824899 — Effectiveness of a 12-week telerehabilitation training in people with long COVID: A randomized contr
  - [pmid] 32369030 — Considerations for Postacute Rehabilitation for Survivors of COVID-19.
  - [pmid] 33642858 — Pulmonary Rehabilitation in a Post-COVID-19 World: Telerehabilitation as a New Standard in Patients 
  - [pmid] 34051516 — Physical and mental health complications post-COVID-19: Scoping review.
  - [pmid] 36191860 — Home-based respiratory muscle training on quality of life and exercise tolerance in long-term post-C
  - [pmid] 37581410 — Pulmonary Rehabilitation for Adults with Chronic Respiratory Disease: An Official American Thoracic 
  - [pubmed_search] (Home-Based Telerehabilitation) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (528 hits)

### Institutional Standard Treatment For Xerostomia And Long Covid → Long COVID
- **claim_id:** `osmf:claim:agent-institutional-standard-treatment-for-xerostomia-and-long-covid-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **evidence_summary:** 'Institutional Standard Treatment For Xerostomia And Long Covid' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources (wave A). Associated registry entries appear procedural/class/placebo-related.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT05760092 — The Use of Photobiomodulation in the Treatment of Oral Complaints of Long COVID-19.A Randomized Cont, COMPLETED, PHASE2
  - [pmid] 34066174 — A Review of Prolonged Post-COVID-19 Symptoms and Their Implications on Dental Management.
  - [pmid] 35373533 — International consensus statement on allergy and rhinology: Olfaction.
  - [pmid] 37468867 — Gastrointestinal symptoms of long COVID-19 related to the ectopic colonization of specific bacteria 
  - [pmid] 37676726 — Evidence of a Sjögren's disease-like phenotype following COVID-19 in mice and humans.
  - [pmid] 38342941 — Post-COVID-19 patients suffer from chemosensory, trigeminal, and salivary dysfunctions.
  - [pubmed_search] (Institutional Standard Treatment For Xerostomia And Long Covid) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (79 hits)

### Lactose Capsula → ME/CFS
- **claim_id:** `osmf:claim:agent-lactose-capsula-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **evidence_summary:** 'Lactose Capsula' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for ME/CFS in the extracted sources (wave A). Associated registry entries appear procedural/class/placebo-related.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT01040429 — The Norwegian Study of Chronic Fatigue Syndrome in Adolescents: Pathophysiology and Intervention Tri, COMPLETED, PHASE2
  - [pmid] 24493300 — Disease mechanisms and clonidine treatment in adolescent chronic fatigue syndrome: a combined cross-
  - [pmid] 28494812 — Whole blood gene expression in adolescent chronic fatigue syndrome: an exploratory cross-sectional s
  - [pmid] 27414048 — Aberrant Resting-State Functional Connectivity in the Salience Network of Adolescent Chronic Fatigue
  - [pmid] 27149955 — Altered neuroendocrine control and association to clinical symptoms in adolescent chronic fatigue sy
  - [pmid] 26138694 — Health related quality of life in adolescents with chronic fatigue syndrome: a cross-sectional study
  - [pubmed_search] (Lactose Capsula) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (1 hits)

### Long Covid Coping And Recovery (Lccr) Intervention → Long COVID
- **claim_id:** `osmf:claim:agent-long-covid-coping-and-recovery-lccr-intervention-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Long Covid Coping And Recovery (Lccr) Intervention → Long COVID: NCT05453201 (COMPLETED, phase=NA, n=22, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 32536736: Effects of COVID-19 on business and research.; PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 34505369: The growing field of digital psychiatry: current evidence and the future of apps, social media, chatbots, and virtual re. Europe PMC query `(Long Covid Coping And Recovery Intervention) AND ("long COVID" OR "post-COVID" OR PASC)` → 1402 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05453201 — Developing an Integrative, Recovery-Based, Post-Acute COVID-19 Syndrome (PACS) Psychotherapeutic Int, COMPLETED, NA
  - [pmid] PPR671900 — Long Covid Coping and Recovery (Lccr): Developing a Novel Recovery-Oriented Treatment for Veterans w
  - [pmid] 32536736 — Effects of COVID-19 on business and research.
  - [pmid] 33909761 — Brazilian Guidelines of Hypertension - 2020.
  - [pmid] 34505369 — The growing field of digital psychiatry: current evidence and the future of apps, social media, chat
  - [pmid] 34818601 — The impact of the prolonged COVID-19 pandemic on stress resilience and mental health: A critical rev
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Long Covid Coping And Recovery Intervention) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (1402 hits)

### Low Sugar Diet And 10-12 Hour Eating Window → Long COVID
- **claim_id:** `osmf:claim:agent-low-sugar-diet-and-10-12-hour-eating-window-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Low Sugar Diet And 10-12 Hour Eating Window → Long COVID: NCT06214455 (COMPLETED, phase=NA, n=77, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33313986: ESICM LIVES 2020.; PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 34281723: Using crowdsourced medicine to manage uncertainty on Reddit: The case of COVID-19 long-haulers.. Europe PMC query `(Low Sugar Diet And 10-12 Hour Eating Window) AND ("long COVID" OR "post-COVID" OR PASC)` → 119 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT06214455 — Intermittent Fasting and a No-Sugar Diet for Long COVID Symptoms, COMPLETED, NA
  - [pmid] 40730806 — Intermittent fasting and a no-sugar diet for Long COVID symptoms: a randomized crossover trial.
  - [pmid] 33313986 — ESICM LIVES 2020.
  - [pmid] 33909761 — Brazilian Guidelines of Hypertension - 2020.
  - [pmid] 34281723 — Using crowdsourced medicine to manage uncertainty on Reddit: The case of COVID-19 long-haulers.
  - [pmid] 35373533 — International consensus statement on allergy and rhinology: Olfaction.
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Low Sugar Diet And 10-12 Hour Eating Window) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (119 hits)

### Low Sugar Diet, 8 Hour Eating Window And Fasting → Long COVID
- **claim_id:** `osmf:claim:agent-low-sugar-diet-8-hour-eating-window-and-fasting-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Low Sugar Diet, 8 Hour Eating Window And Fasting → Long COVID: NCT06214455 (COMPLETED, phase=NA, n=77, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 33313986: ESICM LIVES 2020.; PMID 33909761: Brazilian Guidelines of Hypertension - 2020.; PMID 35373533: International consensus statement on allergy and rhinology: Olfaction.. Europe PMC query `(Low Sugar Diet, 8 Hour Eating Window And Fasting) AND ("long COVID" OR "post-COVID" OR PASC)` → 94 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT06214455 — Intermittent Fasting and a No-Sugar Diet for Long COVID Symptoms, COMPLETED, NA
  - [pmid] 40730806 — Intermittent fasting and a no-sugar diet for Long COVID symptoms: a randomized crossover trial.
  - [pmid] 33313986 — ESICM LIVES 2020.
  - [pmid] 33909761 — Brazilian Guidelines of Hypertension - 2020.
  - [pmid] 35373533 — International consensus statement on allergy and rhinology: Olfaction.
  - [pmid] 36456712 — Network meta-analysis as a tool in clinical practice guidelines.
  - [pmid] 39866113 — 2025 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass
  - [pubmed_search] (Low Sugar Diet, 8 Hour Eating Window And Fasting) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (94 hits)

### Metoprolol Succinate → Long COVID
- **claim_id:** `osmf:claim:agent-metoprolol-succinate-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Metoprolol Succinate → Long COVID: NCT05096884 (TERMINATED, phase=EARLY_PHASE1, n=14, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 35291413: Development of myocarditis and pericarditis after COVID-19 vaccination in adult population: A systematic review.; PMID 35660931: Global reports of myocarditis following COVID-19 vaccination: A systematic review and meta-analysis.; PMID 36074973: Sinus Tachycardia: a Multidisciplinary Expert Focused Review.. Europe PMC query `(Metoprolol Succinate) AND ("long COVID" OR "post-COVID" OR PASC)` → 40 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Not a systematic review; single-pass registry + selective literature sampling
- **references:**
  - [nct] NCT05096884 — Post-Acute Sequelae of Coronavirus-19 (COVID-19) With Dyspnea on Exertion And Associated TaChycardia, TERMINATED, EARLY_PHASE1
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 36969241 — Therapeutic trials for long COVID-19: A call to action from the interventions taskforce of the RECOV
  - [pmid] 36349400 — Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - [pmid] 37344737 — Long COVID and possible preventive options.
  - [pmid] 35291413 — Development of myocarditis and pericarditis after COVID-19 vaccination in adult population: A system
  - [pmid] 35660931 — Global reports of myocarditis following COVID-19 vaccination: A systematic review and meta-analysis.
  - [pmid] 36074973 — Sinus Tachycardia: a Multidisciplinary Expert Focused Review.

### Naltrexone → Other Post-Viral & Post-Infectious Syndromes
- **claim_id:** `osmf:claim:agent-naltrexone-treats-other-post-viral`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Naltrexone → Other Post-Viral & Post-Infectious Syndromes: NCT04604704 (COMPLETED, phase=PHASE2, n=36, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 28267064: Nerve injury-induced epigenetic silencing of opioid receptors controlled by DNMT3a in primary afferent neurons.; PMID 34069603: European Network on Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (EUROMENE): Expert Consensus on the Diagnosis, Se; PMID 34419372: Consensus document for the selection of lung transplant candidates: An update from the International Society for Heart a. Europe PMC query `(Naltrexone) AND ("post-viral" OR "post viral fatigue")` → 79 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT04604704 — Pilot Study Into LDN and NAD+ for Treatment of Patients With Post-COVID-19 Syndrome, COMPLETED, PHASE2
  - [pmid] 34067776 — Post-COVID-19 Syndrome and the Potential Benefits of Exercise.
  - [pmid] 35874958 — Long COVID and its Management.
  - [pmid] 36100326 — Analysis of post COVID-19 condition and its overlap with myalgic encephalomyelitis/chronic fatigue s
  - [pmid] 37907497 — The long-term health outcomes, pathophysiological mechanisms and multidisciplinary management of lon
  - [pmid] 28267064 — Nerve injury-induced epigenetic silencing of opioid receptors controlled by DNMT3a in primary affere
  - [pmid] 34069603 — European Network on Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (EUROMENE): Expert Consensus 
  - [pmid] 34419372 — Consensus document for the selection of lung transplant candidates: An update from the International

### Nasal Cpap Treatment During Sleep → ME/CFS
- **claim_id:** `osmf:claim:agent-nasal-cpap-treatment-during-sleep-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Nasal Cpap Treatment During Sleep → ME/CFS: NCT00252629 (COMPLETED, phase=NA, n=29, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 17625094: Adult obstructive sleep apnea: pathophysiology and diagnosis.; PMID 23205286: Excessive daytime sleepiness in sleep disorders.; PMID 23452057: Characterization of different courses of atopic dermatitis in adolescent and adult patients.. Europe PMC query `(Nasal Cpap Treatment During Sleep) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 128 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT00252629 — Sleep Disordered Breathing in Gulf War Illness and the Effect of Nasal CPAP Treatment, COMPLETED, NA
  - [pmid] 17625094 — Adult obstructive sleep apnea: pathophysiology and diagnosis.
  - [pmid] 23205286 — Excessive daytime sleepiness in sleep disorders.
  - [pmid] 23452057 — Characterization of different courses of atopic dermatitis in adolescent and adult patients.
  - [pmid] 27885969 — 36th International Symposium on Intensive Care and Emergency Medicine : Brussels, Belgium. 15-18 Mar
  - [pmid] 33569660 — Post-COVID-19 Symptom Burden: What is Long-COVID and How Should We Manage It?
  - [pubmed_search] (Nasal Cpap Treatment During Sleep) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (128 hits)

### Omega-3 → Long COVID
- **claim_id:** `osmf:claim:agent-omega-3-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Omega-3 → Long COVID: NCT05121766 (TERMINATED, phase=PHASE1, n=32, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 34687662: The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.; PMID 38264914: 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Association.. Europe PMC query `(Omega-3) AND ("long COVID" OR "post-COVID" OR PASC)` → 1334 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Not a systematic review; single-pass registry + selective literature sampling
- **references:**
  - [nct] NCT05121766 — Feasibility Pilot Clinical Trial of Omega-3 Supplement vs. Placebo for Post Covid-19 Recovery Among , TERMINATED, PHASE1
  - [pmid] 35874958 — Long COVID and its Management.
  - [pmid] 36349400 — Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - [pmid] 37286535 — Metabolic alterations upon SARS-CoV-2 infection and potential therapeutic targets against coronaviru
  - [pmid] 37317282 — Strategies for the Management of Spike Protein-Related Pathology.
  - [pmid] 34687662 — The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.
  - [pmid] 38264914 — 2024 Heart Disease and Stroke Statistics: A Report of US and Global Data From the American Heart Ass

### Pasc Core → Long COVID
- **claim_id:** `osmf:claim:agent-pasc-core-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Pasc Core → Long COVID: NCT05965752 (COMPLETED, phase=NA, n=328, relevant=True); NCT05965739 (COMPLETED, phase=NA, n=328, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 25259891: SDT: a virus classification tool based on pairwise sequence alignment and identity calculation.; PMID 29064822: Advanced capabilities for materials modelling with Quantum ESPRESSO.; PMID 32761142: NCBI Taxonomy: a comprehensive update on curation, resources and tools.. Europe PMC query `(Pasc Core) AND ("long COVID" OR "post-COVID" OR PASC)` → 1431 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05965752 — RECOVER-NEURO: Platform Protocol to Measure the Effects of Cognitive Dysfunction Interventions on Lo, COMPLETED, NA
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [nct] NCT05965739 — RECOVER-NEURO: Platform Protocol, Appendix_A to Measure the Effects of BrainHQ, PASC CoRE and tDCS I, COMPLETED, NA
  - [pmid] 38495306 — Neurovascular coupling impairment as a mechanism for cognitive deficits in COVID-19.
  - [pmid] 38755688 — RECOVER-NEURO: study protocol for a multi-center, multi-arm, phase 2, randomized, active comparator 
  - [pmid] 41212544 — Evaluation of Interventions for Cognitive Symptoms in Long COVID: A Randomized Clinical Trial.
  - [pmid] 25259891 — SDT: a virus classification tool based on pairwise sequence alignment and identity calculation.
  - [pmid] 29064822 — Advanced capabilities for materials modelling with Quantum ESPRESSO.

### Patient-Partner Videotelephone-Delivered Cognitive Behavioral Stress Management Intervention → ME/CFS
- **claim_id:** `osmf:claim:agent-patient-partner-videotelephone-delivered-cognitive-behavioral-stress-management-intervention-treats-me-cfs`
- **proposed:** tier D, status `published`, confidence `medium`, wave `A`
- **rationale:** CBT for ME/CFS remains highly contested (PACE controversy; NICE NG206 does not recommend CBT as curative). Tier D despite trial activity.
- **evidence_summary:** CBT has been studied in ME/CFS, but the evidence base is contested and guideline positions diverge. Linked statuses: COMPLETED. Not framed as solid disease-modifying clinical evidence.
- **gaps:** Guideline conflict and outcome-measure disputes
- **references:**
  - [nct] NCT01650636 — Patient-Partner Stress Management Effects on Chronic Fatigue Syndrome Symptoms and Neuroimmune Proce, COMPLETED, NA
  - [pmid] 31377502 — Relationship satisfaction, communication self-efficacy, and chronic fatigue syndrome-related fatigue
  - [pmid] 38736736 — Videoconference-delivered group Cognitive Behavioral Stress Management for ME/CFS patients who prese
  - [pmid] 39991131 — BRIEF REPORT: Assessing Adherence and Competence in Delivering Telehealth Group Cognitive Behavioral
  - [pubmed_search] (Patient-Partner Videotelephone-Delivered Cognitive Behavioral Stress Management) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (0 hits)

### Patient-Partner Videotelephone-Delivered Health Information → ME/CFS
- **claim_id:** `osmf:claim:agent-patient-partner-videotelephone-delivered-health-information-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Patient-Partner Videotelephone-Delivered Health Information → ME/CFS: NCT01650636 (COMPLETED, phase=NA, n=300, relevant=True). Posted CT.gov results: yes. Europe PMC query `(Patient-Partner Videotelephone-Delivered Health Information) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 0 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT01650636 — Patient-Partner Stress Management Effects on Chronic Fatigue Syndrome Symptoms and Neuroimmune Proce, COMPLETED, NA
  - [pmid] 31377502 — Relationship satisfaction, communication self-efficacy, and chronic fatigue syndrome-related fatigue
  - [pmid] 38736736 — Videoconference-delivered group Cognitive Behavioral Stress Management for ME/CFS patients who prese
  - [pmid] 39991131 — BRIEF REPORT: Assessing Adherence and Competence in Delivering Telehealth Group Cognitive Behavioral
  - [pubmed_search] (Patient-Partner Videotelephone-Delivered Health Information) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (0 hits)

### Relaxation Therapy → ME/CFS
- **claim_id:** `osmf:claim:agent-relaxation-therapy-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `high`, wave `A`
- **rationale:** Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **evidence_summary:** 'Relaxation Therapy' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for ME/CFS in the extracted sources (wave A). Associated registry entries appear procedural/class/placebo-related.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT01512342 — Pacing Activity Self-management for Patients With Chronic Fatigue Syndrome, COMPLETED, PHASE2
  - [pmid] 28444695 — Exercise therapy for chronic fatigue syndrome.
  - [pmid] 37838675 — A scoping review of 'Pacing' for management of Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (M
  - [pmid] 26356665 — Activity Pacing Self-Management in Chronic Fatigue Syndrome: A Randomized Controlled Trial.
  - [pmid] 27995604 — Exercise therapy for chronic fatigue syndrome.
  - [pmid] 17716101 — Stress and health: psychological, behavioral, and biological determinants.
  - [pmid] 20350028 — The effect of mindfulness-based therapy on anxiety and depression: A meta-analytic review.
  - [pmid] 23459093 — The Efficacy of Cognitive Behavioral Therapy: A Review of Meta-analyses.

### Tdcs-Active → Long COVID
- **claim_id:** `osmf:claim:agent-tdcs-active-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 2 registry trial(s) for Tdcs-Active → Long COVID: NCT05965752 (COMPLETED, phase=NA, n=328, relevant=True); NCT05965739 (COMPLETED, phase=NA, n=328, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 35734582: Non-invasive brain stimulation and neuroenhancement.; PMID 38378653: Nanotechnology's frontier in combatting infectious and inflammatory diseases: prevention and treatment.; PMID 39232147: Immune system adaptation during gender-affirming testosterone treatment.. Europe PMC query `(Tdcs-Active) AND ("long COVID" OR "post-COVID" OR PASC)` → 143 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05965752 — RECOVER-NEURO: Platform Protocol to Measure the Effects of Cognitive Dysfunction Interventions on Lo, COMPLETED, NA
  - [pmid] 38611624 — Long COVID: Long-Term Impact of SARS-CoV2.
  - [nct] NCT05965739 — RECOVER-NEURO: Platform Protocol, Appendix_A to Measure the Effects of BrainHQ, PASC CoRE and tDCS I, COMPLETED, NA
  - [pmid] 38495306 — Neurovascular coupling impairment as a mechanism for cognitive deficits in COVID-19.
  - [pmid] 38755688 — RECOVER-NEURO: study protocol for a multi-center, multi-arm, phase 2, randomized, active comparator 
  - [pmid] 41212544 — Evaluation of Interventions for Cognitive Symptoms in Long COVID: A Randomized Clinical Trial.
  - [pmid] 35734582 — Non-invasive brain stimulation and neuroenhancement.
  - [pmid] 38378653 — Nanotechnology's frontier in combatting infectious and inflammatory diseases: prevention and treatme

### Tens - High-Dose → Long COVID
- **claim_id:** `osmf:claim:agent-tens-high-dose-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Tens - High-Dose → Long COVID: NCT05200858 (COMPLETED, phase=NA, n=30, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 34687662: The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.; PMID 36115368: The Lancet Commission on lessons for the future from the COVID-19 pandemic.; PMID 36701528: Spin Hyperpolarization in Modern Magnetic Resonance.. Europe PMC query `(Tens - High-Dose) AND ("long COVID" OR "post-COVID" OR PASC)` → 298 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05200858 — Transcutaneous Electrical Nerve Stimulation (TENS) in Patients With Postacute Sequelae of Sars-CoV-2, COMPLETED, NA
  - [pmid] 39516528 — Transcutaneous electrical nerve stimulation for fibromyalgia-like syndrome in patients with Long-COV
  - [pmid] 34687662 — The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.
  - [pmid] 36115368 — The Lancet Commission on lessons for the future from the COVID-19 pandemic.
  - [pmid] 36701528 — Spin Hyperpolarization in Modern Magnetic Resonance.
  - [pmid] 37402746 — TRP (transient receptor potential) ion channel family: structures, biological functions and therapeu
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pubmed_search] (Tens - High-Dose) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (298 hits)

### Tens - Low-Dose → Long COVID
- **claim_id:** `osmf:claim:agent-tens-low-dose-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Tens - Low-Dose → Long COVID: NCT05200858 (COMPLETED, phase=NA, n=30, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 34687662: The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.; PMID 36115368: The Lancet Commission on lessons for the future from the COVID-19 pandemic.; PMID 36701528: Spin Hyperpolarization in Modern Magnetic Resonance.. Europe PMC query `(Tens - Low-Dose) AND ("long COVID" OR "post-COVID" OR PASC)` → 277 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05200858 — Transcutaneous Electrical Nerve Stimulation (TENS) in Patients With Postacute Sequelae of Sars-CoV-2, COMPLETED, NA
  - [pmid] 39516528 — Transcutaneous electrical nerve stimulation for fibromyalgia-like syndrome in patients with Long-COV
  - [pmid] 34687662 — The 2021 report of the Lancet Countdown on health and climate change: code red for a healthy future.
  - [pmid] 36115368 — The Lancet Commission on lessons for the future from the COVID-19 pandemic.
  - [pmid] 36701528 — Spin Hyperpolarization in Modern Magnetic Resonance.
  - [pmid] 37402746 — TRP (transient receptor potential) ion channel family: structures, biological functions and therapeu
  - [pmid] 39326415 — Mechanisms of long COVID and the path toward therapeutics.
  - [pubmed_search] (Tens - Low-Dose) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (277 hits)

### Transcutaneous Non-Invasive Vagus Nerve Stimulation → Long COVID
- **claim_id:** `osmf:claim:agent-transcutaneous-non-invasive-vagus-nerve-stimulation-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Transcutaneous Non-Invasive Vagus Nerve Stimulation → Long COVID: NCT05608629 (COMPLETED, phase=NA, n=17, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 36169154: Multi-disciplinary collaborative consensus guidance statement on the assessment and treatment of autonomic dysfunction i; PMID 36174571: Bioelectronic medicine: Preclinical insights and clinical advances.; PMID 37028776: Neuroimmune nexus in the pathophysiology and therapy of inflammatory disorders: Role of α7 nicotinic acetylcholine recep. Europe PMC query `(Transcutaneous Non-Invasive Vagus Nerve Stimulation) AND ("long COVID" OR "post-COVID" OR PASC)` → 132 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05608629 — Vagus Nerve Stimulation as Treatment for Long Covid, COMPLETED, NA
  - [pmid] 37402856 — Detrimental effects of COVID-19 in the brain and therapeutic options for long COVID: The role of Eps
  - [pmid] 41783176 — Vagus nerve stimulation: An update of currently registered clinical trials on ClinicalTrials.gov.
  - [pmid] 36169154 — Multi-disciplinary collaborative consensus guidance statement on the assessment and treatment of aut
  - [pmid] 36174571 — Bioelectronic medicine: Preclinical insights and clinical advances.
  - [pmid] 37028776 — Neuroimmune nexus in the pathophysiology and therapy of inflammatory disorders: Role of α7 nicotinic
  - [pmid] 39363044 — Vagus nerve stimulation (VNS): recent advances and future directions.
  - [pmid] 39482575 — Hallmarks of primary headache: part 1 - migraine.

### Transcutaneous Non-Invasive Vagus Nerve Stimulation → ME/CFS
- **claim_id:** `osmf:claim:agent-transcutaneous-non-invasive-vagus-nerve-stimulation-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Transcutaneous Non-Invasive Vagus Nerve Stimulation → ME/CFS: NCT05608629 (COMPLETED, phase=NA, n=17, relevant=True). Posted CT.gov results: yes. Literature notes: PMID 29884281: Interoception and Mental Health: A Roadmap.; PMID 30201788: Vagus Nerve Stimulation at the Interface of Brain-Gut Interactions.; PMID 33723717: Pain in Women: A Perspective Review on a Relevant Clinical Issue that Deserves Prioritization.. Europe PMC query `(Transcutaneous Non-Invasive Vagus Nerve Stimulation) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 87 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05608629 — Vagus Nerve Stimulation as Treatment for Long Covid, COMPLETED, NA
  - [pmid] 37402856 — Detrimental effects of COVID-19 in the brain and therapeutic options for long COVID: The role of Eps
  - [pmid] 41783176 — Vagus nerve stimulation: An update of currently registered clinical trials on ClinicalTrials.gov.
  - [pmid] 29884281 — Interoception and Mental Health: A Roadmap.
  - [pmid] 30201788 — Vagus Nerve Stimulation at the Interface of Brain-Gut Interactions.
  - [pmid] 33723717 — Pain in Women: A Perspective Review on a Relevant Clinical Issue that Deserves Prioritization.
  - [pmid] 36543841 — Safety of transcutaneous auricular vagus nerve stimulation (taVNS): a systematic review and meta-ana
  - [pmid] 37775758 — Multimodal non-invasive non-pharmacological therapies for chronic pain: mechanisms and progress.

### Unfractionated Heparin → Long COVID
- **claim_id:** `osmf:claim:agent-unfractionated-heparin-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `A`
- **rationale:** Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).
- **evidence_summary:** Wave A. Extracted 1 registry trial(s) for Unfractionated Heparin → Long COVID: NCT05204550 (COMPLETED, phase=PHASE2,PHASE3, n=506, relevant=False). No posted CT.gov results in this pass. Literature notes: PMID 32201335: Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID-19 Pandemic.; PMID 33146552: Global Initiative for the Diagnosis, Management, and Prevention of Chronic Obstructive Lung Disease. The 2020 GOLD Scien; PMID 36695182: Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.. Europe PMC query `(Unfractionated Heparin) AND ("long COVID" OR "post-COVID" OR PASC)` → 368 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-matched trials
- **references:**
  - [nct] NCT05204550 — Intranasal Heparin Treatment to Reduce Transmission Among Household Contacts of COVID 19 Positive Ad, COMPLETED, PHASE2,PHASE3
  - [pmid] 37076602 — Therapeutic strategies for COVID-19: progress and lessons learned.
  - [pmid] 36560624 — Heparin Inhibits SARS-CoV-2 Replication in Human Nasal Epithelial Cells.
  - [pmid] 38649069 — Heparin-mediated PCR interference in SARS-CoV-2 assays and subsequent reversal with heparinase I.
  - [pmid] 41474164 — Diagnostic accuracy of self-collected anterior nasal swabs for SARS-CoV-2 RT-PCR testing.
  - [pmid] 32201335 — Cardiovascular Considerations for Patients, Health Care Workers, and Health Systems During the COVID
  - [pmid] 33146552 — Global Initiative for the Diagnosis, Management, and Prevention of Chronic Obstructive Lung Disease.
  - [pmid] 36695182 — Heart Disease and Stroke Statistics-2023 Update: A Report From the American Heart Association.

### 7-Day Ambulatory Caloric Restriction Intervention Using The Buchinger-Wilhelmi Method → Long COVID
- **claim_id:** `osmf:claim:agent-7-day-ambulatory-caloric-restriction-intervention-using-the-buchinger-wilhelmi-method-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for 7-Day Ambulatory Caloric Restriction Intervention Using The Buchinger-Wilhelmi Method → Long COVID: NCT06522750 (RECRUITING, phase=NA, n=20, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT06522750 — Periodic Fasting for Treatment of Long Covid in Adults: a Pilot Study, RECRUITING, NA

### [11C]Cppc Injection → Long COVID
- **claim_id:** `osmf:claim:agent-11ccppc-injection-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for [11C]Cppc Injection → Long COVID: NCT06223971 (COMPLETED, phase=EARLY_PHASE1, n=6, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT06223971 — Long COVID-19 [11C]CPPC Study, COMPLETED, EARLY_PHASE1

### [Zr-89]Oxine-Labeled Leukocytes Pet/Mri → ME/CFS
- **claim_id:** `osmf:claim:agent-zr-89oxine-labeled-leukocytes-petmri-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `high`, wave `B`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for [Zr-89]Oxine-Labeled Leukocytes Pet/Mri → ME/CFS: NCT03807973 (SUSPENDED, phase=PHASE1, n=120, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Not a systematic review; single-pass registry + selective literature sampling
- **references:**
  - [nct] NCT03807973 — Tracking Peripheral Immune Cell Infiltration of the Brain in Central Inflammatory Disorders Using [Z, SUSPENDED, PHASE1

### A 3-Day Course → ME/CFS
- **claim_id:** `osmf:claim:agent-a-3-day-course-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for A 3-Day Course → ME/CFS: NCT05236465 (RECRUITING, phase=NA, n=100, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT05236465 — A 3-day Course for CFS/ME, RECRUITING, NA

### A.1 - [¹⁸F]F-Arag Pet/Ct → Long COVID
- **claim_id:** `osmf:claim:agent-a1-ff-arag-petct-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for A.1 - [¹⁸F]F-Arag Pet/Ct → Long COVID: NCT07076862 (RECRUITING, phase=EARLY_PHASE1, n=51, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT07076862 — Multiparametric [18F]F-AraG Imaging in Post-Acute Sequelae of COVID-19 (PASC), RECRUITING, EARLY_PHASE1

### A.2 - [¹⁸F]F-Arag Pet/Ct → Long COVID
- **claim_id:** `osmf:claim:agent-a2-ff-arag-petct-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for A.2 - [¹⁸F]F-Arag Pet/Ct → Long COVID: NCT07076862 (RECRUITING, phase=EARLY_PHASE1, n=51, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT07076862 — Multiparametric [18F]F-AraG Imaging in Post-Acute Sequelae of COVID-19 (PASC), RECRUITING, EARLY_PHASE1

### Abrocitinib → Long COVID
- **claim_id:** `osmf:claim:agent-abrocitinib-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Abrocitinib → Long COVID: NCT06597396 (ACTIVE_NOT_RECRUITING, phase=PHASE2, n=46, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 37479495: COVID-19 outcomes in patients with rheumatoid arthritis with biologic or targeted synthetic DMARDs.; PMID 38979496: Autism spectrum disorder and a possible role of anti-inflammatory treatments: experience in the pediatric allergy/immuno; PMID 40717900: Macrophages: Subtypes, Distribution, Polarization, Immunomodulatory Functions, and Therapeutics.. Europe PMC query `(Abrocitinib) AND ("long COVID" OR "post-COVID" OR PASC)` → 21 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT06597396 — Study to Investigate the Efficacy of Abrocitinib in Adult Participants With Severe Fatigue From Post, ACTIVE_NOT_RECRUITING, PHASE2
  - [pmid] 41388153 — Long COVID involves activation of proinflammatory and immune exhaustion pathways.
  - [pmid] 42449996 — Increased Mannosylation of Extracellular Vesicles in Long COVID Plasma as a Binding Target for &lt;i
  - [pmid] 37479495 — COVID-19 outcomes in patients with rheumatoid arthritis with biologic or targeted synthetic DMARDs.
  - [pmid] 38979496 — Autism spectrum disorder and a possible role of anti-inflammatory treatments: experience in the pedi
  - [pmid] 40717900 — Macrophages: Subtypes, Distribution, Polarization, Immunomodulatory Functions, and Therapeutics.
  - [pmid] 40843597 — European S2k Guideline on Chronic Pruritus
  - [pubmed_search] (Abrocitinib) AND ("long COVID" OR "post-COVID" OR PASC) — Europe PMC search (21 hits)

### Accelerated Intermittent Theta Burst Stimulation → Long COVID
- **claim_id:** `osmf:claim:agent-accelerated-intermittent-theta-burst-stimulation-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Accelerated Intermittent Theta Burst Stimulation → Long COVID: NCT06940609 (RECRUITING, phase=PHASE2, n=60, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT06940609 — Magnetic Resonance Analysis of Neural Inflammatory Factors and External Stimulation, RECRUITING, PHASE2

### Acceptance And Commitment Therapy → ME/CFS
- **claim_id:** `osmf:claim:agent-acceptance-and-commitment-therapy-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acceptance And Commitment Therapy → ME/CFS: NCT03562325 (COMPLETED, phase=NA, n=40, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT03562325 — ACT for ME/CFS - an Open Case Trial, COMPLETED, NA

### Acceptance Commitment Therapy For Chronic Fatigue → ME/CFS
- **claim_id:** `osmf:claim:agent-acceptance-commitment-therapy-for-chronic-fatigue-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acceptance Commitment Therapy For Chronic Fatigue → ME/CFS: NCT05168124 (RECRUITING, phase=NA, n=90, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 17488783: Guidelines on the irritable bowel syndrome: mechanisms and practical management.; PMID 20350028: The effect of mindfulness-based therapy on anxiety and depression: A meta-analytic review.; PMID 27885969: 36th International Symposium on Intensive Care and Emergency Medicine : Brussels, Belgium. 15-18 March 2016.. Europe PMC query `(Acceptance Commitment Therapy For Chronic Fatigue) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 456 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT05168124 — Effectiveness of Acceptance Commitment Therapy or Micro Breaks in Patients with Chronic Fatigue Synd, RECRUITING, NA
  - [pmid] 39964319 — Application of acceptance and commitment therapy in cancer-related fatigue management: insights from
  - [pmid] 17488783 — Guidelines on the irritable bowel syndrome: mechanisms and practical management.
  - [pmid] 20350028 — The effect of mindfulness-based therapy on anxiety and depression: A meta-analytic review.
  - [pmid] 27885969 — 36th International Symposium on Intensive Care and Emergency Medicine : Brussels, Belgium. 15-18 Mar
  - [pmid] 28506916 — 2017 HRS/EHRA/ECAS/APHRS/SOLAECE expert consensus statement on catheter and surgical ablation of atr
  - [pmid] 29876878 — Role of the Prefrontal Cortex in Pain Processing.
  - [pubmed_search] (Acceptance Commitment Therapy For Chronic Fatigue) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (456 hits)

### Actigraphy → ME/CFS
- **claim_id:** `osmf:claim:agent-actigraphy-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `high`, wave `B`
- **rationale:** Trial(s) terminated/withdrawn or no completed condition-relevant evidence.
- **evidence_summary:** Wave B. Extracted 2 registry trial(s) for Actigraphy → ME/CFS: NCT04363606 (TERMINATED, phase=NA, n=69, relevant=True); NCT03849326 (WITHDRAWN, phase=NA, n=0, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Not a systematic review; single-pass registry + selective literature sampling
- **references:**
  - [nct] NCT04363606 — Chronic Fatigue Etiology and Recovery in Covid-19 Patients: the Role of Fatigability, TERMINATED, NA
  - [nct] NCT03849326 — Chronic Fatigue Etiology in Intensive Care Unit Survivors: the Role of Neuromuscular Function, WITHDRAWN, NA

### Active → ME/CFS
- **claim_id:** `osmf:claim:agent-active-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Active → ME/CFS: NCT04301609 (COMPLETED, phase=NA, n=67, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT04301609 — Clinical Trial to Assess the Improvement of Fatigue, Sleep Problems, Anxiety / Depression, Neurovege, COMPLETED, NA

### Active Comparator: Usual Treatment → Long COVID
- **claim_id:** `osmf:claim:agent-active-comparator-usual-treatment-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `high`, wave `B`
- **rationale:** Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic with condition-directed efficacy evidence.
- **evidence_summary:** 'Active Comparator: Usual Treatment' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for Long COVID in the extracted sources (wave B). Associated registry entries appear procedural/class/placebo-related.
- **gaps:** No agent-specific efficacy package
- **references:**
  - [nct] NCT05894629 — Effects of an Active Coping Program in Patients With Persistent Post-Covid Pain., COMPLETED, NA

### Active Kinetic Oscillation Stimulation → ME/CFS
- **claim_id:** `osmf:claim:agent-active-kinetic-oscillation-stimulation-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Active Kinetic Oscillation Stimulation → ME/CFS: NCT03502044 (UNKNOWN, phase=NA, n=200, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT03502044 — New MRT Imaging Biomarkers and Treatment With Kinetic Oscillatory Stimulation (KOS) in Nasal Cavity , UNKNOWN, NA

### Active Smell Training → Long COVID
- **claim_id:** `osmf:claim:agent-active-smell-training-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Active Smell Training → Long COVID: NCT05855369 (RECRUITING, phase=PHASE2,PHASE3, n=145, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT05855369 — Study of Chemosensory Enhancement Through Neuromodulation Training (SCENT for Long COVID), RECRUITING, PHASE2,PHASE3

### Active Tdcs And Cognitive Training → Long COVID
- **claim_id:** `osmf:claim:agent-active-tdcs-and-cognitive-training-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Active Tdcs And Cognitive Training → Long COVID: NCT05389592 (COMPLETED, phase=NA, n=60, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT05389592 — Treatment of COVID-19 Post-acute Cognitive Impairment Sequelae With tDCS, COMPLETED, NA

### Active Transcutaneous Vns → ME/CFS
- **claim_id:** `osmf:claim:agent-active-transcutaneous-vns-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Active Transcutaneous Vns → ME/CFS: NCT06170645 (RECRUITING, phase=NA, n=60, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT06170645 — Transcutaneous Vagus Nerve Stimulation as a Complementary Therapy to Exercise in Chronic Fatigue, RECRUITING, NA

### Acupressure → ME/CFS
- **claim_id:** `osmf:claim:agent-acupressure-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acupressure → ME/CFS: NCT04435002 (COMPLETED, phase=NA, n=39, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT04435002 — The Effect of Acupressure on Fatigue in Individuals With Chronic Fatigue Syndrome, COMPLETED, NA

### Acupressure Treatment. → ME/CFS
- **claim_id:** `osmf:claim:agent-acupressure-treatment-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Some completed condition-related work but phase/size/pubs too thin for C.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acupressure Treatment. → ME/CFS: NCT02075489 (COMPLETED, phase=NA, n=7, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Phase, size, and published outcomes
- **references:**
  - [nct] NCT02075489 — Acupressure for Pain Management and Fatigue Relief in Gulf War Veterans, COMPLETED, NA

### Acupuncture And Tcm-Based Lifestyle Management → Long COVID
- **claim_id:** `osmf:claim:agent-acupuncture-and-tcm-based-lifestyle-management-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acupuncture And Tcm-Based Lifestyle Management → Long COVID: NCT06042777 (UNKNOWN, phase=NA, n=100, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT06042777 — Non-pharmacological and TCM-based Treatment for Long COVID Symptoms, UNKNOWN, NA

### Acupuncture. → ME/CFS
- **claim_id:** `osmf:claim:agent-acupuncture-treats-me-cfs`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Insufficient extracted clinical evidence for the agent–condition pair (Preliminary tracker level).
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acupuncture. → ME/CFS: NCT01907711 (UNKNOWN, phase=PHASE2,PHASE3, n=60, relevant=True). No posted CT.gov results in this pass. Literature notes: PMID 24733803: Screening, assessment, and management of fatigue in adult survivors of cancer: an American Society of Clinical oncology ; PMID 29462012: Neuroinflammation and Central Sensitization in Chronic and Widespread Pain.; PMID 29876878: Role of the Prefrontal Cortex in Pain Processing.. Europe PMC query `(Acupuncture.) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis")` → 1023 hits. Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Condition-specific clinical studies
- **references:**
  - [nct] NCT01907711 — Clinical Trial to Evaluate the Effectiveness of Acupuncture as a Treatment in Patients Diagnosed Wit, UNKNOWN, PHASE2,PHASE3
  - [pmid] 24733803 — Screening, assessment, and management of fatigue in adult survivors of cancer: an American Society o
  - [pmid] 29462012 — Neuroinflammation and Central Sensitization in Chronic and Widespread Pain.
  - [pmid] 29876878 — Role of the Prefrontal Cortex in Pain Processing.
  - [pmid] 35176758 — Long COVID: post-acute sequelae of COVID-19 with a cardiovascular focus.
  - [pmid] 41092926 — Burden of 375 diseases and injuries, risk-attributable burden of 88 risk factors, and healthy life e
  - [pubmed_search] (Acupuncture.) AND ("chronic fatigue syndrome" OR ME/CFS OR "myalgic encephalomyelitis") — Europe PMC search (1023 hits)

### Acute Intermittent Hypoxia → Long COVID
- **claim_id:** `osmf:claim:agent-acute-intermittent-hypoxia-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acute Intermittent Hypoxia → Long COVID: NCT06614309 (RECRUITING, phase=NA, n=45, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT06614309 — Non-invasive Treatment for Long COVID (Post COVID-19 Condition) Brain Fog, RECRUITING, NA

### Acute Progressive Carbon Dioxide → Long COVID
- **claim_id:** `osmf:claim:agent-acute-progressive-carbon-dioxide-treats-long-covid`
- **proposed:** tier D, status `draft`, confidence `medium`, wave `B`
- **rationale:** Only ongoing/not-completed trials and no posted results; Preliminary → D draft.
- **evidence_summary:** Wave B. Extracted 1 registry trial(s) for Acute Progressive Carbon Dioxide → Long COVID: NCT06614309 (RECRUITING, phase=NA, n=45, relevant=True). No posted CT.gov results in this pass. No agent+condition Europe PMC search (wave B/C budget). Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical package is present (not claimed here without verified supportive endpoints).
- **gaps:** Completed results
- **references:**
  - [nct] NCT06614309 — Non-invasive Treatment for Long COVID (Post COVID-19 Condition) Brain Fog, RECRUITING, NA

_… 448 additional tier-D claims in JSONL only._

