# Phase 3 draft results chase

**Date:** 2026-09-19 (America/Edmonton)
**Chase UTC:** 2026-09-19T18:00:00Z
**Bot:** evidence-chase-bot

## Summary

- Claims chased: **25**
- Unique NCTs fetched (CT.gov API v2): **31**
- NCTs with results modules present: **7** (`NCT00498485, NCT00598585, NCT02055898, NCT04510194, NCT05212610, NCT05874037, NCT06305780`)
- Claims where ≥1 linked NCT has a results module: **10**
- Tier changes: **3**
- Status changes: **1**
- **No A/B upgrades.** B reserved for solid published clinical evidence packages (none met bar).

### Newly actionable evidence (not necessarily tier-changing)

| Claim | Finding |
|---|---|
| Solriamfetol → ME/CFS | Peer-reviewed Phase 4 primary PMID 40958377 (NCT04622293); **C draft → C published** |
| Compound Ciwujia → ME/CFS | Chinese multicenter PMID 42543377; CT.gov still unposted; remain C draft |
| RegeneCyte → Long COVID | Phase IIa PMID 41625963; remain C draft (n=30) |
| Remdesivir → Long COVID | Feasibility PMID 42063202; remain C draft |
| HBOT → Long COVID | HOT-LoCO PMID 40228859 negative Phase 2 for NCT04842448; contested vs Israeli positives → **C → D** |
| Sildenafil / Sodium oxybate → ME/CFS | CT.gov results modules confirmed (tiny n); remain C draft |
| Fluvoxamine / Metformin → ME/CFS | Linked Phase 3s are LC/acute COVID (off-target) → **C → D** |
| IVIG → ME/CFS / Lyme / Other post-viral | RECOVER platform NCTs off-target; enrollment-only results → remain **D** |
| mRNA vaccines → Long COVID | NCT05212610 results = reactogenicity, not LC treatment → remain **D** |

### Tier changes

| Claim | Old → New | Status | 1-line |
|---|---|---|---|
| `agent-fluvoxamine-treats-me-cfs` | C → **D** | draft | [2026-09-19 chase] Off-target Phase 3 package for ME/CFS claim. NCT05874037 posted LC results 2026-06-25 (−47.3 vs −31.1 symptom score) but  |
| `agent-hyperbaric-oxygen-therapy-hbot-treats-long-covid` | C → **D** | draft | [2026-09-19 chase] Peer-reviewed negative Phase 2 for linked NCT04842448 plus conflicting positive Israeli RCTs → contested D (was C). |
| `agent-metformin-treats-me-cfs` | C → **D** | draft | [2026-09-19 chase] No ME/CFS-specific Phase 3 package; COVID trial results off-target. |

### Status changes

| Claim | Old → New | Tier | Note |
|---|---|---|---|
| `agent-solriamfetol-oral-tablet-sunosi-treats-me-cfs` | draft → **published** | C | [2026-09-19 chase] New peer-reviewed primary for NCT04622293 supports early clinical signal; published as C. Not multi-trial consensus → not |

## Method

1. Selected draft Moderate-agent `treats_candidate_for` claims with COMPLETED Phase 3/4 / pivotal linked NCTs (plus drafts whose NCTs already had or newly showed results modules).
2. Fresh-fetched ClinicalTrials.gov API v2 for each NCT (outcomes, arms, analyses/p-values when present).
3. Searched PubMed (Secondary Source ID / Title-Abstract) and Europe PMC for publications citing those NCTs.
4. Updated claim `sources`, `limitations`, `confidence_notes`; changed tier/status only when justified. No invented A/B.

## Per-claim findings

### Angiotensin Converting Enzyme Inhibitor → Long COVID
- **claim_id:** `osmf:claim:agent-angiotensin-converting-enzyme-inhibitor-treats-long-covid`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Class agent + unposted Phase 3 → D.
- **limitations:** Results chase 2026-09-19: class-level ACEI/ARB agent; NCT04591210 Phase 3 completed (n=372) still without CT.gov results; not drug-specific LC treatment evidence → D. Not medical advice.
- **NCTs chased:** NCT04591210
- **Results modules:** none
- **CT.gov findings:**
  - NCT04591210: COMPLETED phase=PHASE3 enroll=372 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 34991982 (2021): An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - PMID 35197452 (2022): The mechanism underlying extrapulmonary complications of the coronavirus disease 2019 and its therap
  - PMID 33793331 (2021): Hypertension, a Moving Target in COVID-19: Current Views and Perspectives.
  - PMID 35697684 (2022): Cell deaths: Involvement in the pathogenesis and intervention therapy of COVID-19.
  - PMID 34454035 (2021): Sex-tailored pharmacology and COVID-19: Next steps towards appropriateness and health equity.
  - PMID 34869917 (2021): COVID-19 and renin angiotensin aldosterone system: Pathogenesis and therapy.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/angiotensin-converting-enzyme-inhibitor/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT04591210 — ACEI/ARB COVID Phase 3 completed (no results module; class-level claim)
  - [pmid] 32201335 
  - [pmid] 32526206 
  - [pmid] 36695182 
  - [pmid] 38264914 
  - [pmid] 39866113 
  - [pmid] 37740450 — Effects of renin-angiotensin system blockers on outcomes from COVID-19: a systematic review and meta-analysis of randomi (2024)

### Angiotensin Ii Receptor Blockers → Long COVID
- **claim_id:** `osmf:claim:agent-angiotensin-ii-receptor-blockers-treats-long-covid`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Class agent + unposted Phase 3 → D.
- **limitations:** Results chase 2026-09-19: class-level ACEI/ARB agent; NCT04591210 Phase 3 completed (n=372) still without CT.gov results; not drug-specific LC treatment evidence → D. Not medical advice.
- **NCTs chased:** NCT04591210
- **Results modules:** none
- **CT.gov findings:**
  - NCT04591210: COMPLETED phase=PHASE3 enroll=372 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 34991982 (2021): An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - PMID 35197452 (2022): The mechanism underlying extrapulmonary complications of the coronavirus disease 2019 and its therap
  - PMID 33793331 (2021): Hypertension, a Moving Target in COVID-19: Current Views and Perspectives.
  - PMID 35697684 (2022): Cell deaths: Involvement in the pathogenesis and intervention therapy of COVID-19.
  - PMID 34454035 (2021): Sex-tailored pharmacology and COVID-19: Next steps towards appropriateness and health equity.
  - PMID 34869917 (2021): COVID-19 and renin angiotensin aldosterone system: Pathogenesis and therapy.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/angiotensin-ii-receptor-blockers/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT04591210 — ACEI/ARB COVID Phase 3 completed (no results module; class-level claim)
  - [pmid] 32201335 
  - [pmid] 36695182 
  - [pmid] 38264914 
  - [pmid] 39866113 
  - [pmid] 41092926 
  - [pmid] 37740450 — Effects of renin-angiotensin system blockers on outcomes from COVID-19: a systematic review and meta-analysis of randomi (2024)

### Compound Ciwujia Granules, Guipi Granules → ME/CFS
- **claim_id:** `osmf:claim:agent-compound-ciwujia-granules-guipi-granules-treats-me-cfs`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Peer-reviewed Chinese primary found; remain C draft pending broader replication / CT.gov posting.
- **limitations:** Results chase 2026-09-19: NCT06245642 completed Phase 4 (n=235) still without CT.gov results. PMID 42543377 reports multicenter RCT subgroup (heart-spleen deficiency TCM syndrome) with CFQ-11 benefit vs active control. Positive-drug-controlled TCM syndrome subgroup; English independent replication lacking → C draft not B. Not medical advice.
- **NCTs chased:** NCT06245642
- **Results modules:** none
- **CT.gov findings:**
  - NCT06245642: COMPLETED phase=PHASE4 enroll=235 has_results=False
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/compound-ciwujia-granules-guipi-granules/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT06245642 — Compound Ciwujia Granules CFS Phase 4 (completed; no CT.gov results module)
  - [pmid] 42543377 — Compound Ciwujia Granules CFS multicenter RCT subgroup (2026)
  - [doi] 10.19540/j.cnki.cjcmm.20260323.501 — Zhongguo Zhong Yao Za Zhi 2026

### Fluvoxamine → ME/CFS
- **claim_id:** `osmf:claim:agent-fluvoxamine-treats-me-cfs`
- **tier:** C → **D** (CHANGED)
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Off-target Phase 3 package for ME/CFS claim. NCT05874037 posted LC results 2026-06-25 (−47.3 vs −31.1 symptom score) but wrong condition.
- **limitations:** Results chase 2026-09-19: completed Phase 2/3 NCT05874037 and Phase 3 NCT06128967/NCT04510194 target Long COVID or acute COVID, not ME/CFS. Posted LC symptom-score results do not validate an ME/CFS treats_candidate_for claim → D. Not medical advice.
- **NCTs chased:** NCT05874037, NCT07359482, NCT04510194, NCT06128967
- **Results modules:** NCT05874037, NCT04510194
- **CT.gov findings:**
  - NCT05874037: COMPLETED phase=PHASE2,PHASE3 enroll=191 has_results=True results_posted=2026-06-25 | PRIMARY: Change in Total Symptom Scores — Fluvoxamine: -47.3±8.1 (n=66); Placebo: -31.1±7.0 (n=71)
  - NCT07359482: RECRUITING phase=PHASE3 enroll=160 has_results=False
  - NCT04510194: COMPLETED phase=PHASE3 enroll=1323 has_results=True results_posted=2023-07-13 | PRIMARY: Clinical Progression to Severe Covid — Active Metformin: 154 (n=652); Metformin Placebo: 179 (n=653); Active Ivermectin: 105 (n=407); Ivermectin Placebo: 96 (n=391)
  - NCT06128967: COMPLETED phase=PHASE3 enroll=399 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 37402856 (2023): Detrimental effects of COVID-19 in the brain and therapeutic options for long COVID: The role of Eps
  - PMID 39380062 (2024): SSRI use during acute COVID-19 and risk of long COVID among patients with depression.
  - PMID 39599909 (2024): Beyond Antivirals: Alternative Therapies for Long COVID.
  - PMID 42325367 (2025): Long COVID: current research and future directions.
  - PMID 37179335 (2023): Immunosenescence: molecular mechanisms and diseases.
  - PMID 37076602 (2023): Therapeutic strategies for COVID-19: progress and lessons learned.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/fluvoxamine/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05874037 — Fluvoxamine for Long COVID (results posted; off-target for ME/CFS)
  - [nct] NCT06128967 — REVIVE Long COVID fluvoxamine/metformin
  - [nct] NCT04510194 — COVID-OUT acute COVID (results posted)
  - [nct] NCT07359482 
  - [pmid] 41911553 — REVIVE Annals 2026 fluvoxamine fatigue in Long COVID
  - [pmid] 19428959 
  - [pmid] 23459093 

### Gcjbp Laennec Inj. → ME/CFS
- **claim_id:** `osmf:claim:agent-gcjbp-laennec-inj-treats-me-cfs`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Still no posted results or NCT-linked publication → C draft.
- **limitations:** Results chase 2026-09-19: NCT01742013 Phase 3 (n=78) completed; CT.gov results still unposted; no PubMed/Europe PMC primary citing NCT → C draft. Not medical advice.
- **NCTs chased:** NCT01742013
- **Results modules:** none
- **CT.gov findings:**
  - NCT01742013: COMPLETED phase=PHASE3 enroll=78 has_results=False
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/gcjbp-laennec-inj/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT01742013 — Laennec Inj CFS Phase 3 completed (no results module)

### Hyperbaric Oxygen Therapy (HBOT) → Long COVID
- **claim_id:** `osmf:claim:agent-hyperbaric-oxygen-therapy-hbot-treats-long-covid`
- **tier:** C → **D** (CHANGED)
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Peer-reviewed negative Phase 2 for linked NCT04842448 plus conflicting positive Israeli RCTs → contested D (was C).
- **limitations:** Results chase 2026-09-19: NCT04842448 (HOT-LoCO Phase 2, n=80) completed without CT.gov results module, but PMID 40228859 reports no significant HBOT vs sham benefit on RAND-36 PF/RP. Separate Israeli sham-controlled RCTs (e.g. PMID 35821512; NCT04647656 lineage) reported benefit — contested package. Phase 3 NCT06267300 UNKNOWN without results → D 
- **NCTs chased:** NCT06452095, NCT04842448, NCT06267300, NCT04905888, NCT07621068
- **Results modules:** none
- **CT.gov findings:**
  - NCT06452095: RECRUITING phase=NA enroll=120 has_results=False
  - NCT04842448: COMPLETED phase=PHASE2 enroll=80 has_results=False
  - NCT06267300: UNKNOWN phase=PHASE3 enroll=120 has_results=False
  - NCT04905888: WITHDRAWN phase=PHASE2 enroll=0 has_results=False
  - NCT07621068: RECRUITING phase=NA enroll=74 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 36349400 (2023): Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - PMID 37396922 (2023): Fighting Post-COVID and ME/CFS - development of curative therapies.
  - PMID 36670365 (2023): Hyperbaric oxygen therapy for long COVID (HOT-LoCO), an interim safety report from a randomised cont
  - PMID 36323462 (2022): Hyperbaric oxygen for treatment of long COVID-19 syndrome (HOT-LoCO): protocol for a randomised, pla
  - PMID 36559025 (2022): The Hidden Pandemic of COVID-19-Induced Organizing Pneumonia.
  - PMID 34127622 (2021): At a crossroads: coronavirus disease 2019 recovery and the risk of pulmonary vascular disease.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/hyperbaric-oxygen-therapy-hbot/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT04842448 — HOT-LoCO HBOT Long COVID Phase 2 completed (no CT.gov results module)
  - [nct] NCT06267300 — HBOT Phase 3 UNKNOWN status; no results
  - [nct] NCT06452095 
  - [nct] NCT04905888 
  - [nct] NCT07621068 
  - [pmid] 40228859 — HOT-LoCO Phase 2: 10 HBOT sessions no better than sham (NCT04842448) (2025)
  - [pmid] 35821512 — Israeli HBOT RCT positive neurocognitive signal (2022; different program)

### Hyperbaric Oxygen Therapy (HBOT) → ME/CFS
- **claim_id:** `osmf:claim:agent-hyperbaric-oxygen-therapy-hbot-treats-me-cfs`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] No ME/CFS-specific completed pivotal results; LC HBOT evidence contested/off-target.
- **limitations:** Results chase 2026-09-19: ME/CFS-specific HBOT trials still recruiting (NCT07621068); linked completed NCT04842448 is Long COVID (HOT-LoCO negative). No completed confirmatory ME/CFS RCT results → C draft. Not medical advice.
- **NCTs chased:** NCT06452095, NCT04842448, NCT06267300, NCT04905888, NCT07621068
- **Results modules:** none
- **CT.gov findings:**
  - NCT06452095: RECRUITING phase=NA enroll=120 has_results=False
  - NCT04842448: COMPLETED phase=PHASE2 enroll=80 has_results=False
  - NCT06267300: UNKNOWN phase=PHASE3 enroll=120 has_results=False
  - NCT04905888: WITHDRAWN phase=PHASE2 enroll=0 has_results=False
  - NCT07621068: RECRUITING phase=NA enroll=74 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 36349400 (2023): Clinical trials on the pharmacological treatment of long COVID: A systematic review.
  - PMID 37396922 (2023): Fighting Post-COVID and ME/CFS - development of curative therapies.
  - PMID 36670365 (2023): Hyperbaric oxygen therapy for long COVID (HOT-LoCO), an interim safety report from a randomised cont
  - PMID 36323462 (2022): Hyperbaric oxygen for treatment of long COVID-19 syndrome (HOT-LoCO): protocol for a randomised, pla
  - PMID 36559025 (2022): The Hidden Pandemic of COVID-19-Induced Organizing Pneumonia.
  - PMID 34127622 (2021): At a crossroads: coronavirus disease 2019 recovery and the risk of pulmonary vascular disease.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/hyperbaric-oxygen-therapy-hbot/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT07621068 — ME/CFS HBOT recruiting
  - [nct] NCT04842448 — HOT-LoCO Long COVID (off-target for ME/CFS claim)
  - [nct] NCT06452095 
  - [nct] NCT06267300 
  - [nct] NCT04905888 
  - [pmid] 40228859 — HOT-LoCO negative Phase 2 (Long COVID)
  - [pmid] 42249466 

### Immulina Tm → Long COVID
- **claim_id:** `osmf:claim:agent-immulina-tm-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] No new posted results or primary publication → C draft.
- **limitations:** Results chase 2026-09-19: NCT05524532 Phase 3 (n=101) completed; CT.gov results still unposted; no clear peer-reviewed primary outcome paper in NCT citation search → C draft. Not medical advice.
- **NCTs chased:** NCT05524532
- **Results modules:** none
- **CT.gov findings:**
  - NCT05524532: COMPLETED phase=PHASE3 enroll=101 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 37623720 (2023): Review of Marine Cyanobacteria and the Aspects Related to Their Roles: Chemical, Biological Properti
  - PMID 37317282 (2023): Strategies for the Management of Spike Protein-Related Pathology.
  - PMID 42325367 (2025): Long COVID: current research and future directions.
  - PMID 40979082 (2025): Building a collaborative ecosystem across the IDeA-CTR networks in response to a public health emerg
  - PMID PPR644266 (2023): Strategies for the Management of Spike Protein-Related Pathology
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/immulina-tm/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05524532 — Immulina PASC Phase 3 completed (no results module)
  - [pmid] 35204236 
  - [pmid] 37388814 
  - [pmid] 39179099 
  - [pmid] 40722944 
  - [pmid] 42325367 

### Intravenous Immunoglobulin (IVIG) → Chronic Lyme / PTLDS
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-lyme`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Reverted automated D→C upgrade. Off-target NCTs for Lyme; platform results are enrollment, not condition-specific efficacy.
- **limitations:** Results chase 2026-09-19: linked RECOVER platform NCT06305780/NCT06305793 target Long COVID autonomic/POTS appendices, not Lyme. NCT06305780 results module posts enrollment counts only (not efficacy for this claim condition). Off-target registry linkage → tier D. Not medical advice.
- **NCTs chased:** NCT06305793, NCT06305780
- **Results modules:** NCT06305780
- **CT.gov findings:**
  - NCT06305793: COMPLETED phase=PHASE2 enroll=200 has_results=False
  - NCT06305780: COMPLETED phase=PHASE2 enroll=381 has_results=True results_posted=2026-08-03 | PRIMARY: Total Number of Participants Enrolled in Each Appendix — IVIG: 200 (n=200); Ivabradine: 181 (n=181)
- **Publications citing NCTs (sampled):**
  - PMID 41089328 (2025): Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and
  - PMID 42053865 (2026): Pathogenic IgG from long COVID patients with neurological sequelae triggers sensitive but not cognit
  - PMID 41836927 (2026): Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - PMID 42325367 (2025): Long COVID: current research and future directions.
  - PMID 42325370 (2025): Viral persistence in long COVID: Research advances and treatment strategies.
  - PMID 41720282 (2026): Design and rationale of RECOVER-AUTONOMIC: A randomized platform trial evaluating interventions for 
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/intravenous-immunoglobulin-ivig/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT06305780 — RECOVER-AUTONOMIC platform (enrollment results only; Long COVID)
  - [nct] NCT06305793 — RECOVER-AUTONOMIC IVIG appendix (Long COVID/POTS)
  - [pmid] 42391726 
  - [pmid] 42243711 
  - [pmid] 42137701 
  - [pmid] 15870014 
  - [pmid] 25077519 

### Intravenous Immunoglobulin (IVIG) → ME/CFS
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-me-cfs`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Reverted automated D→C upgrade. Off-target NCTs for ME/CFS; platform results are enrollment, not condition-specific efficacy.
- **limitations:** Results chase 2026-09-19: linked RECOVER platform NCT06305780/NCT06305793 target Long COVID autonomic/POTS appendices, not ME/CFS. NCT06305780 results module posts enrollment counts only (not efficacy for this claim condition). Off-target registry linkage → tier D. Not medical advice.
- **NCTs chased:** NCT06305793, NCT06305780
- **Results modules:** NCT06305780
- **CT.gov findings:**
  - NCT06305793: COMPLETED phase=PHASE2 enroll=200 has_results=False
  - NCT06305780: COMPLETED phase=PHASE2 enroll=381 has_results=True results_posted=2026-08-03 | PRIMARY: Total Number of Participants Enrolled in Each Appendix — IVIG: 200 (n=200); Ivabradine: 181 (n=181)
- **Publications citing NCTs (sampled):**
  - PMID 41089328 (2025): Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and
  - PMID 42053865 (2026): Pathogenic IgG from long COVID patients with neurological sequelae triggers sensitive but not cognit
  - PMID 41836927 (2026): Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - PMID 42325367 (2025): Long COVID: current research and future directions.
  - PMID 42325370 (2025): Viral persistence in long COVID: Research advances and treatment strategies.
  - PMID 41720282 (2026): Design and rationale of RECOVER-AUTONOMIC: A randomized platform trial evaluating interventions for 
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/intravenous-immunoglobulin-ivig/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT06305780 — RECOVER-AUTONOMIC platform (enrollment results only; Long COVID)
  - [nct] NCT06305793 — RECOVER-AUTONOMIC IVIG appendix (Long COVID/POTS)
  - [pmid] 42391726 
  - [pmid] 42243711 
  - [pmid] 42137701 
  - [pmid] 19375665 
  - [pmid] 19781793 

### Intravenous Immunoglobulin (IVIG) → Other Post-Viral & Post-Infectious Syndromes
- **claim_id:** `osmf:claim:agent-intravenous-immunoglobulin-ivig-treats-other-post-viral`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Reverted automated D→C upgrade. Off-target NCTs for Other post-viral; platform results are enrollment, not condition-specific efficacy.
- **limitations:** Results chase 2026-09-19: linked RECOVER platform NCT06305780/NCT06305793 target Long COVID autonomic/POTS appendices, not Other post-viral. NCT06305780 results module posts enrollment counts only (not efficacy for this claim condition). Off-target registry linkage → tier D. Not medical advice.
- **NCTs chased:** NCT06305793, NCT06305780
- **Results modules:** NCT06305780
- **CT.gov findings:**
  - NCT06305793: COMPLETED phase=PHASE2 enroll=200 has_results=False
  - NCT06305780: COMPLETED phase=PHASE2 enroll=381 has_results=True results_posted=2026-08-03 | PRIMARY: Total Number of Participants Enrolled in Each Appendix — IVIG: 200 (n=200); Ivabradine: 181 (n=181)
- **Publications citing NCTs (sampled):**
  - PMID 41089328 (2025): Immunotherapies for postural orthostatic tachycardia syndrome, other common autonomic disorders, and
  - PMID 42053865 (2026): Pathogenic IgG from long COVID patients with neurological sequelae triggers sensitive but not cognit
  - PMID 41836927 (2026): Candidate treatments for long COVID: a narrative review of expert and patient-driven priorities.
  - PMID 42325367 (2025): Long COVID: current research and future directions.
  - PMID 42325370 (2025): Viral persistence in long COVID: Research advances and treatment strategies.
  - PMID 41720282 (2026): Design and rationale of RECOVER-AUTONOMIC: A randomized platform trial evaluating interventions for 
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/intravenous-immunoglobulin-ivig/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT06305780 — RECOVER-AUTONOMIC platform (enrollment results only; Long COVID)
  - [nct] NCT06305793 — RECOVER-AUTONOMIC IVIG appendix (Long COVID/POTS)
  - [pmid] 42391726 
  - [pmid] 42243711 
  - [pmid] 42137701 
  - [pmid] 22185868 
  - [pmid] 32298803 

### Ivabradine → Long COVID
- **claim_id:** `osmf:claim:agent-ivabradine-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Still awaiting RECOVER ivabradine efficacy posting → C draft.
- **limitations:** Results chase 2026-09-19: RECOVER-AUTONOMIC ivabradine appendix NCT06305806 completed Phase 2 (n=181) without efficacy results posted; NCT05481177 UNKNOWN. Platform NCT06305780 results module is enrollment counts only. Design paper PMID 41720282. No posted primary efficacy → C draft. Not medical advice.
- **NCTs chased:** NCT06305806, NCT05481177
- **Results modules:** none
- **CT.gov findings:**
  - NCT06305806: COMPLETED phase=PHASE2 enroll=181 has_results=False
  - NCT05481177: UNKNOWN phase=PHASE4 enroll=250 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 42325367 (2025): Long COVID: current research and future directions.
  - PMID 41720282 (2026): Design and rationale of RECOVER-AUTONOMIC: A randomized platform trial evaluating interventions for 
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/ivabradine/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT06305806 — RECOVER-AUTONOMIC ivabradine appendix (completed Phase 2; no efficacy results)
  - [nct] NCT06305780 — RECOVER-AUTONOMIC platform (enrollment results only)
  - [nct] NCT05481177 — Ivabradine LC Phase 4 UNKNOWN status
  - [pmid] 41720282 — RECOVER-AUTONOMIC design and rationale (2026)
  - [pmid] 32201335 
  - [pmid] 34024217 
  - [pmid] 35176758 

### Metformin → Gulf War Illness
- **claim_id:** `osmf:claim:agent-metformin-treats-gulf-war-illness`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Reverted automated D→C upgrade. COVID-OUT results do not evidence metformin for GWI.
- **limitations:** Results chase 2026-09-19: linked NCT04510194 (COVID-OUT) and NCT06128967 (REVIVE) address acute COVID / Long COVID, not Gulf War Illness. Posted COVID-OUT results are off-target for this claim → D. Not medical advice.
- **NCTs chased:** NCT04510194, NCT06128967, NCT06147050
- **Results modules:** NCT04510194
- **CT.gov findings:**
  - NCT04510194: COMPLETED phase=PHASE3 enroll=1323 has_results=True results_posted=2023-07-13 | PRIMARY: Clinical Progression to Severe Covid — Active Metformin: 154 (n=652); Metformin Placebo: 179 (n=653); Active Ivermectin: 105 (n=407); Ivermectin Placebo: 96 (n=391)
  - NCT06128967: COMPLETED phase=PHASE3 enroll=399 has_results=False
  - NCT06147050: UNKNOWN phase=PHASE3 enroll=16 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 37179335 (2023): Immunosenescence: molecular mechanisms and diseases.
  - PMID 37076602 (2023): Therapeutic strategies for COVID-19: progress and lessons learned.
  - PMID 36070710 (2022): Randomized Trial of Metformin, Ivermectin, and Fluvoxamine for Covid-19.
  - PMID 37302406 (2023): Outpatient treatment of COVID-19 and incidence of post-COVID-19 condition over 10 months (COVID-OUT)
  - PMID 34991982 (2021): An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - PMID 33798464 (2021): Prescription of glucose-lowering therapies and risk of COVID-19 mortality in people with type 2 diab
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/metformin/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT04510194 — COVID-OUT (acute COVID; results posted; off-target for GWI)
  - [nct] NCT06128967 — REVIVE Long COVID (off-target for GWI)
  - [nct] NCT06147050 
  - [pmid] 37302406 — COVID-OUT long-COVID incidence secondary outcomes (2023)
  - [pmid] 40544605 
  - [pmid] 36326761 
  - [pmid] 37008131 

### Metformin → ME/CFS
- **claim_id:** `osmf:claim:agent-metformin-treats-me-cfs`
- **tier:** C → **D** (CHANGED)
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] No ME/CFS-specific Phase 3 package; COVID trial results off-target.
- **limitations:** Results chase 2026-09-19: linked Phase 3 NCTs are COVID-OUT / REVIVE (acute COVID / Long COVID), not ME/CFS-specific. Off-target → D. Not medical advice.
- **NCTs chased:** NCT04510194, NCT06128967, NCT06147050
- **Results modules:** NCT04510194
- **CT.gov findings:**
  - NCT04510194: COMPLETED phase=PHASE3 enroll=1323 has_results=True results_posted=2023-07-13 | PRIMARY: Clinical Progression to Severe Covid — Active Metformin: 154 (n=652); Metformin Placebo: 179 (n=653); Active Ivermectin: 105 (n=407); Ivermectin Placebo: 96 (n=391)
  - NCT06128967: COMPLETED phase=PHASE3 enroll=399 has_results=False
  - NCT06147050: UNKNOWN phase=PHASE3 enroll=16 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 37179335 (2023): Immunosenescence: molecular mechanisms and diseases.
  - PMID 37076602 (2023): Therapeutic strategies for COVID-19: progress and lessons learned.
  - PMID 36070710 (2022): Randomized Trial of Metformin, Ivermectin, and Fluvoxamine for Covid-19.
  - PMID 37302406 (2023): Outpatient treatment of COVID-19 and incidence of post-COVID-19 condition over 10 months (COVID-OUT)
  - PMID 34991982 (2021): An update on drugs with therapeutic potential for SARS-CoV-2 (COVID-19) treatment.
  - PMID 33798464 (2021): Prescription of glucose-lowering therapies and risk of COVID-19 mortality in people with type 2 diab
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/metformin/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT04510194 — COVID-OUT (results posted; off-target for ME/CFS)
  - [nct] NCT06128967 — REVIVE Long COVID
  - [nct] NCT06147050 
  - [pmid] 37302406 — COVID-OUT metformin reduces incident long COVID (prevention context)
  - [pmid] 41911553 — REVIVE: metformin arm no significant fatigue benefit in Long COVID
  - [pmid] 40544605 
  - [pmid] 18923511 

### Microcrystalline Cellulose → Long COVID
- **claim_id:** `osmf:claim:agent-microcrystalline-cellulose-treats-long-covid`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Non-therapeutic placebo-class label retained as D.
- **limitations:** Results chase 2026-09-19: label is placebo/excipient (Testofen trial comparator context NCT05795816), not a therapeutic → D. Not medical advice.
- **NCTs chased:** NCT05795816, NCT06348212
- **Results modules:** none
- **CT.gov findings:**
  - NCT05795816: COMPLETED phase=PHASE3 enroll=150 has_results=False
  - NCT06348212: UNKNOWN phase=NA enroll=60 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 39599909 (2024): Beyond Antivirals: Alternative Therapies for Long COVID.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/microcrystalline-cellulose/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05795816 — Testofen vs placebo (MCC is placebo arm context)
  - [nct] NCT06348212 
  - [pmid] 21821740 
  - [pmid] 21876164 
  - [pmid] 23102010 
  - [pmid] 27287427 
  - [pmid] 36701528 

### Moderna Mrna Covid-19 Vaccine → Long COVID
- **claim_id:** `osmf:claim:agent-moderna-mrna-covid-19-vaccine-treats-long-covid`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Results module present but wrong question (vaccine reactogenicity), not LC treatment efficacy.
- **limitations:** Results chase 2026-09-19: NCT05212610 Phase 4 completed with results (allergy/reaction endpoints for additional doses), not a treatment trial of established Long COVID → D. Not medical advice.
- **NCTs chased:** NCT05212610
- **Results modules:** NCT05212610
- **CT.gov findings:**
  - NCT05212610: COMPLETED phase=PHASE4 enroll=137 has_results=True results_posted=2026-03-27 | PRIMARY: Participants Who Had a Reaction to an Initial or Additional Dose of the Pfizer-BioNTech or Moderna COVID-19 mRNA Vaccine, or Who Had Long COVID — Pfizer-BioNTech mRNA COVID-19 Vaccine: 71 (n=95); Moderna mRNA COVID-19 Va | PRIMARY: Number of Participants With Treatment-related Allergic Reaction Adverse Events — Pfizer-BioNTech mRNA COVID-19 Vaccine: 3 (n=95); Moderna mRNA COVID-19 Vaccine: 1 (n=6); Pfizer-BioNTech mRNA COVID-19 Vaccine: 1 (n=95); M
- **Publications citing NCTs (sampled):**
  - PMID 36063274 (2022): Current clinical status of new COVID-19 vaccines and immunotherapy.
  - PMID 42369559 (2026): mRNA vaccines against viral pathogens: molecular design, delivery systems, and clinical applications
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/moderna-mrna-covid-19-vaccine/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05212610 — mRNA COVID vaccine additional dose reactions (results posted; not LC treatment)
  - [pmid] 33497610 
  - [pmid] 34715347 
  - [pmid] 36580913 
  - [pmid] 37165196 
  - [pmid] 38264914 

### Pfizer-Biontech Mrna Covid-19 Vaccine → Long COVID
- **claim_id:** `osmf:claim:agent-pfizer-biontech-mrna-covid-19-vaccine-treats-long-covid`
- **tier:** D → **D**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Results module present but wrong question (vaccine reactogenicity), not LC treatment efficacy.
- **limitations:** Results chase 2026-09-19: NCT05212610 Phase 4 completed with results (allergy/reaction endpoints for additional doses), not a treatment trial of established Long COVID → D. Not medical advice.
- **NCTs chased:** NCT05212610
- **Results modules:** NCT05212610
- **CT.gov findings:**
  - NCT05212610: COMPLETED phase=PHASE4 enroll=137 has_results=True results_posted=2026-03-27 | PRIMARY: Participants Who Had a Reaction to an Initial or Additional Dose of the Pfizer-BioNTech or Moderna COVID-19 mRNA Vaccine, or Who Had Long COVID — Pfizer-BioNTech mRNA COVID-19 Vaccine: 71 (n=95); Moderna mRNA COVID-19 Va | PRIMARY: Number of Participants With Treatment-related Allergic Reaction Adverse Events — Pfizer-BioNTech mRNA COVID-19 Vaccine: 3 (n=95); Moderna mRNA COVID-19 Vaccine: 1 (n=6); Pfizer-BioNTech mRNA COVID-19 Vaccine: 1 (n=95); M
- **Publications citing NCTs (sampled):**
  - PMID 36063274 (2022): Current clinical status of new COVID-19 vaccines and immunotherapy.
  - PMID 42369559 (2026): mRNA vaccines against viral pathogens: molecular design, delivery systems, and clinical applications
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/pfizer-biontech-mrna-covid-19-vaccine/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05212610 — mRNA COVID vaccine additional dose reactions (results posted; not LC treatment)
  - [pmid] 33497610 
  - [pmid] 34281357 
  - [pmid] 34715347 
  - [pmid] 35614233 
  - [pmid] 37165196 

### Pycnogenol® → Long COVID
- **claim_id:** `osmf:claim:agent-pycnogenol-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Still no posted CT.gov results / peer-reviewed primary outcomes paper → C draft.
- **limitations:** Results chase 2026-09-19: NCT05890534 PYCNOVID Phase 3 (n=153) completed; CT.gov results still unposted. PMID 38879571 is protocol only; preprint PPR1039664 not treated as peer-reviewed primary → C draft not B. Not medical advice.
- **NCTs chased:** NCT05890534
- **Results modules:** none
- **CT.gov findings:**
  - NCT05890534: COMPLETED phase=PHASE3 enroll=153 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 38543815 (2024): Small Molecules for the Treatment of Long-COVID-Related Vascular Damage and Abnormal Blood Clotting:
  - PMID 38879571 (2024): Effects of Pycnogenol® in people with post-COVID-19 condition (PYCNOVID): study protocol for a singl
  - PMID 41878337 (2026): Therapeutic potential of pycnogenol: antioxidant, anti-inflammatory, immunomodulatory, antiviral, an
  - PMID 42118816 (2026): Measurement properties of the 30-second sit-to-stand test in post COVID-19 condition: Results from t
  - PMID PPR1039664 (2025): Effects of Pycnogenol<sup>®</sup>in post-COVID-19 condition (PYCNOVID): A single-center, placebo con
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/pycnogenol/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05890534 — PYCNOVID Pycnogenol post-COVID Phase 3 (completed; no results module)
  - [pmid] 38879571 — PYCNOVID study protocol (2024)
  - [pmid] 35566252 
  - [pmid] 36043493 
  - [pmid] 36364899 
  - [pmid] 36639608 
  - [pmid] 37080828 

### Regenecyte → Long COVID
- **claim_id:** `osmf:claim:agent-regenecyte-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Peer-reviewed Phase IIa primary found; remain C draft (n=30).
- **limitations:** Results chase 2026-09-19: NCT05682560 Phase 2 (n=30) completed without CT.gov results; PMID 41625963 reports Phase IIa RCT with fatigue improvement vs placebo. Small early trial; pivotal NCT07184385 not yet recruiting → C draft not B. Not medical advice.
- **NCTs chased:** NCT07184385, NCT05682560
- **Results modules:** none
- **CT.gov findings:**
  - NCT07184385: NOT_YET_RECRUITING phase=PHASE3 enroll=60 has_results=False
  - NCT05682560: COMPLETED phase=PHASE2 enroll=30 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 41625963 (2026): REGENECYTE cord blood cell therapy in post-COVID syndrome: a phase IIa randomized, placebo-controlle
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/regenecyte/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05682560 — RegeneCyte Phase 2 completed (no CT.gov results module)
  - [nct] NCT07184385 — RegeneCyte Phase 3 not yet recruiting
  - [pmid] 41625963 — REGENECYTE Phase IIa RCT post-COVID fatigue (2026; NCT05682560)
  - [doi] 10.1016/j.eclinm.2025.103737 — eClinicalMedicine 2026

### Remdesivir → Long COVID
- **claim_id:** `osmf:claim:agent-remdesivir-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Feasibility publication found; no confirmatory efficacy package → C draft.
- **limitations:** Results chase 2026-09-19: NCT05911906 completed Phase 4 open-label feasibility (n=73) without CT.gov results module. PMID 42063202 is a feasibility/methods report (ISRCTN72940450 / NCT05911906), not confirmatory efficacy → C draft. Not medical advice.
- **NCTs chased:** NCT05911906
- **Results modules:** none
- **CT.gov findings:**
  - NCT05911906: COMPLETED phase=PHASE4 enroll=73 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 39947217 (2025): Targeting the SARS-CoV-2 reservoir in long COVID.
  - PMID 42063202 (2026): An open-label, clinical feasibility study of the efficacy of Remdesivir for Long-COVID.
  - PMID 40559563 (2025): Digestive Manifestations of Post-COVID-19: A Focus on Therapeutic Strategies.
  - PMID 42325370 (2025): Viral persistence in long COVID: Research advances and treatment strategies.
  - PMID 42271537 (2026): Patient and public involvement and engagement in Long COVID research: embedding inclusion in researc
  - PMID PPR1161844 (2026): An open-label, clinical feasibility study of the efficacy of Remdesivir for Long-COVID
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/remdesivir/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05911906 — Remdesivir Long COVID Phase 4 feasibility (completed; no results module)
  - [pmid] 42063202 — Open-label feasibility study of Remdesivir for Long-COVID (2026)
  - [pmid] 32201335 
  - [pmid] 33146552 
  - [pmid] 33892403 
  - [pmid] 35271343 
  - [pmid] 37076602 

### Sildenafil → ME/CFS
- **claim_id:** `osmf:claim:agent-sildenafil-treats-me-cfs`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Confirmed posted results module (2017-06-27) with nominal FIS benefit; n too small for B.
- **limitations:** Results chase 2026-09-19: NCT00598585 Phase 4 (n=12) has CT.gov results: FIS change −32.6±31.5 (sildenafil n=5) vs −1.5±12.2 (placebo n=6), p<0.05. Extremely small single-center → C draft not B. Not medical advice.
- **NCTs chased:** NCT00598585
- **Results modules:** NCT00598585
- **CT.gov findings:**
  - NCT00598585: COMPLETED phase=PHASE4 enroll=12 has_results=True results_posted=2017-06-27 | PRIMARY: Change in Fatigue Impact Scale at 6 Weeks — Sildenafil: -32.6±31.5 (n=5); Placebo: -1.5±12.2 (n=6) — p=< 0.05 — t-test, 2 sided
- **Publications citing NCTs (sampled):**
  - PMID 37396922 (2023): Fighting Post-COVID and ME/CFS - development of curative therapies.
  - PMID 39240417 (2025): Towards an understanding of physical activity-induced post-exertional malaise: Insights into microva
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/sildenafil/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT00598585 — Sildenafil CFS Phase 4 n=12 (results posted; FIS p<0.05)
  - [nct] NCT01584934 — Related sildenafil listing
  - [pmid] 28506916 
  - [pmid] 34686843 
  - [pmid] 34991982 
  - [pmid] 36364899 
  - [pmid] 39083764 

### Sodium Oxybate → ME/CFS
- **claim_id:** `osmf:claim:agent-sodium-oxybate-treats-me-cfs`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Confirmed results modules on both NCTs; remain early C.
- **limitations:** Results chase 2026-09-19: NCT00498485 Phase 4 (n≈11 analyzable) posted Global Assessment benefit (p<0.04); NCT02055898 (n=13) posted EEG slow-wave endpoints without clear clinical efficacy package. Tiny n → C draft not B. Not medical advice.
- **NCTs chased:** NCT01584934, NCT02055898, NCT00498485
- **Results modules:** NCT02055898, NCT00498485
- **CT.gov findings:**
  - NCT01584934: WITHDRAWN phase=PHASE4 enroll=0 has_results=False
  - NCT02055898: COMPLETED phase=PHASE4 enroll=13 has_results=True results_posted=2020-11-18 | PRIMARY: EEG Slow Wave Activity During Sleep — Sodium Oxybate: 0.00002653±0.00000406 (n=9); Placebo: 0.00002257±0.00000339 (n=9) | PRIMARY: EEG Slow Wave Activity During Sleep — Sodium Oxybate: 0.00003051±0.00000492 (n=9); Placebo: 0.00001759±0.00000225 (n=9)
  - NCT00498485: TERMINATED phase=PHASE4 enroll=17 has_results=True results_posted=2016-04-21 | PRIMARY: Global Assessment of Change — Placebo: 6 (n=6); Drug Treated: 5 (n=5) — p=<0.04 — Wilcoxon (Mann-Whitney) | PRIMARY: Self Reported Assessment of Sleep
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/sodium-oxybate/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT00498485 — Sodium oxybate CFS (results posted; Global Assessment p<0.04)
  - [nct] NCT02055898 — SAFES sodium oxybate CFS sleep EEG (results posted)
  - [nct] NCT01584934 
  - [pmid] 19225604 
  - [pmid] 22802155 
  - [pmid] 22811766 
  - [pmid] 24289848 

### Solriamfetol Oral Tablet [Sunosi] → ME/CFS
- **claim_id:** `osmf:claim:agent-solriamfetol-oral-tablet-sunosi-treats-me-cfs`
- **tier:** C → **C**
- **status:** draft → **published** (CHANGED)
- **confidence_notes:** [2026-09-19 chase] New peer-reviewed primary for NCT04622293 supports early clinical signal; published as C. Not multi-trial consensus → not B.
- **limitations:** Results chase 2026-09-19: NCT04622293 (Phase 4, n=44) still lacks CT.gov results module, but peer-reviewed primary (PMID 40958377) reports Week-8 FSI severity benefit (p=0.039) and BRIEF-A executive improvement. Single small short-term RCT → tier C not B. Not medical advice.
- **NCTs chased:** NCT04622293
- **Results modules:** none
- **CT.gov findings:**
  - NCT04622293: COMPLETED phase=PHASE4 enroll=44 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 40958377 (2025): Solriamfetol improves daily fatigue symptoms in adults with myalgic encephalomyelitis/chronic fatigu
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/solriamfetol-oral-tablet-sunosi/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT04622293 — Solriamfetol ME/CFS Phase 4 RCT (completed; results not posted on CT.gov)
  - [pmid] 40958377 — Solriamfetol improves daily fatigue in ME/CFS (Phase 4 RCT; NCT04622293) (2025)
  - [pmid] 39125722 
  - [pmid] 39150700 
  - [pmid] 40046430 
  - [pmid] 40261198 
  - [pmid] 41076550 

### Testofen → Long COVID
- **claim_id:** `osmf:claim:agent-testofen-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Still no posted results → C draft.
- **limitations:** Results chase 2026-09-19: NCT05795816 Phase 3 (n=150) completed; CT.gov results still unposted; no peer-reviewed primary in NCT search → C draft. Not medical advice.
- **NCTs chased:** NCT05795816
- **Results modules:** none
- **CT.gov findings:**
  - NCT05795816: COMPLETED phase=PHASE3 enroll=150 has_results=False
- **Publications citing NCTs (sampled):**
  - PMID 39599909 (2024): Beyond Antivirals: Alternative Therapies for Long COVID.
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/testofen/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05795816 — Testofen Long COVID Phase 3 completed (no results module)
  - [pmid] 39599909 

### Thiamine (Vitamin B1) → Long COVID
- **claim_id:** `osmf:claim:agent-thiamine-vitamin-b1-treats-long-covid`
- **tier:** C → **C**
- **status:** draft → **draft**
- **confidence_notes:** [2026-09-19 chase] Large completed Phase 4 still without posted results or NCT-linked pubs → C draft.
- **limitations:** Results chase 2026-09-19: NCT05642923 Phase 4 (n=528) completed; CT.gov results still unposted; no PubMed/Europe PMC hits for NCT → C draft. Not medical advice.
- **NCTs chased:** NCT05642923
- **Results modules:** none
- **CT.gov findings:**
  - NCT05642923: COMPLETED phase=PHASE4 enroll=528 has_results=False
- **Updated sources:**
  - [osmf_page] https://research.opensourcemed.info/agents/thiamine-vitamin-b1/ — OSMF Research Tracker (therapeutic agent)
  - [nct] NCT05642923 — Post-COVID CFS thiamine Phase 4 n=528 completed (no results module)
  - [pmid] 24661096 
  - [pmid] 3070321 
  - [pmid] 35269860 
  - [pmid] 36701528 
  - [pmid] 37130947 

---
_Not medical advice. Registry postings and single small trials are not equivalent to guideline-level efficacy._
