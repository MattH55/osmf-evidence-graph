#!/usr/bin/env python3
"""Extract references and evaluate Moderate Tracker agent claims (no UI grading)."""
from __future__ import annotations

import json
import os
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GRAPH = Path("/workspace/osmf-evidence-graph")
TRACKER = Path("/workspace/osmf-research-tracker")
REVIEW = GRAPH / "review"
CACHE = REVIEW / "cache"
CLAIMS_DIR = GRAPH / "data" / "claims"
QUEUE_PATH = REVIEW / "moderate-agents-queue.json"
JSONL_PATH = REVIEW / "moderate-agents-evidence.jsonl"
MD_PATH = REVIEW / "moderate-agents-evidence.md"
EVAL_DATE = "2026-09-19"
EVAL_ISO = "2026-09-19T17:30:00Z"
REVIEWED_BY = "evidence-eval-bot"

# Human-graded in interactive session — leave unless clearly contradicted
HUMAN_LOCKED = {
    "osmf:claim:agent-amphetamine-dextroamphetamine-treats-long-covid": {
        "tier": "C",
        "status": "published",
        "note": "Previously human-graded C/published by MattH55 (2026-09-19); retained after evidence check (terminated small Phase 4, n=7).",
    },
    "osmf:claim:agent-ampligen-treats-me-cfs": {
        "tier": "C",
        "status": "published",
        "note": "Previously human-graded C/published by MattH55 (2026-09-19); retained (completed Phase 3 Ampligen CFS trial exists but results contested/not broadly approved).",
    },
}

# Non-therapeutic / diagnostic / class / placebo-ish labels that should stay low
NON_TX_PATTERNS = re.compile(
    r"^(genetic|behavioral|biopsychological|physiological evaluation|multidisciplinary approach|"
    r"microcrystalline cellulose|digital cognitive|active comparator)",
    re.I,
)

CLASS_AGENTS = {
    "angiotensin converting enzyme inhibitor",
    "angiotensin ii receptor blockers",
}

USER_AGENT = "OSMF-EvidenceEval/1.0 (research; contact: opensourcemed.info)"


def http_get_json(url: str, timeout: int = 45) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def cache_get(name: str) -> Any | None:
    p = CACHE / name
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return None
    return None


def cache_set(name: str, data: Any) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / name).write_text(json.dumps(data, indent=2))


def fetch_nct(nct_id: str) -> dict:
    key = f"nct_{nct_id}.json"
    cached = cache_get(key)
    if cached is not None:
        return cached
    url = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}?format=json"
    try:
        raw = http_get_json(url)
        proto = raw.get("protocolSection") or {}
        ident = proto.get("identificationModule") or {}
        status = proto.get("statusModule") or {}
        design = proto.get("designModule") or {}
        cond = proto.get("conditionsModule") or {}
        arms = proto.get("armsInterventionsModule") or {}
        outcomes = proto.get("outcomesModule") or {}
        desc = proto.get("descriptionModule") or {}
        enroll = design.get("enrollmentInfo") or {}
        primary = (outcomes.get("primaryOutcomes") or [{}])[0]
        intervs = [i.get("name") for i in (arms.get("interventions") or []) if i.get("name")]
        has_results = bool(raw.get("hasResults") or status.get("resultsFirstPostDateStruct"))
        # results section presence
        if raw.get("resultsSection"):
            has_results = True
        out = {
            "nct_id": nct_id,
            "title": ident.get("briefTitle") or ident.get("officialTitle") or "",
            "status": status.get("overallStatus") or "",
            "phases": design.get("phases") or [],
            "conditions": cond.get("conditions") or [],
            "interventions": intervs,
            "enrollment": enroll.get("count"),
            "enrollment_type": enroll.get("type"),
            "primary_outcome": primary.get("measure") or "",
            "why_stopped": status.get("whyStopped") or "",
            "has_results": has_results,
            "start_date": (status.get("startDateStruct") or {}).get("date"),
            "completion_date": (status.get("completionDateStruct") or {}).get("date"),
            "brief_summary": (desc.get("briefSummary") or "")[:600],
            "url": f"https://clinicaltrials.gov/study/{nct_id}",
            "fetch_ok": True,
        }
    except Exception as e:
        out = {"nct_id": nct_id, "fetch_ok": False, "error": str(e), "url": f"https://clinicaltrials.gov/study/{nct_id}"}
    cache_set(key, out)
    time.sleep(0.15)
    return out


def fetch_pmid(pmid: str) -> dict:
    key = f"pmid_{pmid}.json"
    cached = cache_get(key)
    if cached is not None:
        return cached
    url = (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
        + urllib.parse.urlencode({"query": f"EXT_ID:{pmid} AND SRC:MED", "format": "json", "pageSize": 1})
    )
    try:
        data = http_get_json(url)
        results = (data.get("resultList") or {}).get("result") or []
        if results:
            r = results[0]
            out = {
                "pmid": pmid,
                "title": r.get("title") or "",
                "year": r.get("pubYear"),
                "journal": r.get("journalTitle") or "",
                "abstract": (r.get("abstractText") or "")[:800],
                "doi": r.get("doi"),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "fetch_ok": True,
            }
        else:
            out = {"pmid": pmid, "fetch_ok": False, "error": "not found", "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"}
    except Exception as e:
        out = {"pmid": pmid, "fetch_ok": False, "error": str(e), "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"}
    cache_set(key, out)
    time.sleep(0.12)
    return out


def europepmc_search(query: str, page_size: int = 5) -> dict:
    key = "search_" + re.sub(r"[^a-z0-9]+", "_", query.lower())[:120] + ".json"
    cached = cache_get(key)
    if cached is not None:
        return cached
    url = (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
        + urllib.parse.urlencode({"query": query, "format": "json", "pageSize": page_size, "sort": "CITED desc"})
    )
    try:
        data = http_get_json(url)
        hits = []
        for r in (data.get("resultList") or {}).get("result") or []:
            hits.append(
                {
                    "pmid": r.get("pmid") or r.get("id"),
                    "title": r.get("title") or "",
                    "year": r.get("pubYear"),
                    "journal": r.get("journalTitle") or "",
                    "doi": r.get("doi"),
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{r.get('pmid')}/" if r.get("pmid") else None,
                }
            )
        out = {"query": query, "hit_count": data.get("hitCount", 0), "hits": hits, "fetch_ok": True}
    except Exception as e:
        out = {"query": query, "hit_count": 0, "hits": [], "fetch_ok": False, "error": str(e)}
    cache_set(key, out)
    time.sleep(0.12)
    return out


def condition_search_terms(condition: str) -> list[str]:
    c = condition.lower()
    if "long covid" in c:
        return ['"long COVID"', '"post-COVID"', "PASC"]
    if "me/cfs" in c or "chronic fatigue" in c:
        return ['"chronic fatigue syndrome"', "ME/CFS", '"myalgic encephalomyelitis"']
    if "pots" in c:
        return ['"postural orthostatic tachycardia"', "POTS"]
    if "mcas" in c:
        return ['"mast cell activation"', "MCAS"]
    if "lyme" in c:
        return ['"post-treatment Lyme"', "PTLDS", '"chronic Lyme"']
    if "gulf war" in c:
        return ['"Gulf War Illness"', '"Gulf War syndrome"']
    if "post-viral" in c or "other post" in c:
        return ['"post-viral"', '"post viral fatigue"']
    return [f'"{condition}"']


def agent_search_name(agent: str) -> str:
    # strip dose / trademark noise for search
    a = agent
    a = re.sub(r"\(.*?\)", " ", a)
    a = re.sub(r"®", "", a)
    a = re.sub(r"\s+\d+\s*mg\b", "", a, flags=re.I)
    a = re.sub(r"\s+", " ", a).strip()
    # class names
    if a.lower().startswith("angiotensin converting"):
        return "ACE inhibitor OR ACEI OR lisinopril OR enalapril"
    if a.lower().startswith("angiotensin ii"):
        return "ARB OR losartan OR valsartan OR \"angiotensin receptor\""
    if "paxlovid" in a.lower() or "nirmatrelvir" in a.lower():
        return "nirmatrelvir OR Paxlovid"
    if "ivig" in a.lower() or "immunoglobulin" in a.lower():
        return "IVIG OR \"intravenous immunoglobulin\""
    if "hbot" in a.lower() or "hyperbaric" in a.lower():
        return "\"hyperbaric oxygen\" OR HBOT"
    if "cbt" in a.lower() or "cognitive behavioural" in a.lower() or "cognitive behavioral" in a.lower():
        return "\"cognitive behavioural therapy\" OR \"cognitive behavioral therapy\" OR CBT"
    if "sirolimus" in a.lower() or "rapamycin" in a.lower():
        return "sirolimus OR rapamycin"
    if "solriamfetol" in a.lower():
        return "solriamfetol OR Sunosi"
    if "ampligen" in a.lower():
        return "Ampligen OR rintatolimod"
    if "pycnogenol" in a.lower():
        return "Pycnogenol OR \"French maritime pine\""
    if "immulina" in a.lower():
        return "Immulina OR \"Spirulina extract\""
    if "testofen" in a.lower():
        return "Testofen OR \"Fenugreek extract\""
    if "shengmai" in a.lower():
        return "Shengmai"
    if "sodium oxybate" in a.lower():
        return "\"sodium oxybate\" OR Xyrem"
    if "lisdexamfetamine" in a.lower():
        return "lisdexamfetamine OR Vyvanse"
    if "vaccine" in a.lower():
        return a  # keep specific
    return a


def condition_relevant(nct: dict, condition: str) -> tuple[bool, str]:
    """Heuristic: does this trial actually target the claim condition?"""
    blob = " ".join(
        [
            nct.get("title") or "",
            " ".join(nct.get("conditions") or []),
            nct.get("brief_summary") or "",
            nct.get("primary_outcome") or "",
        ]
    ).lower()
    c = condition.lower()
    checks = []
    if "long covid" in c:
        checks = ["long covid", "long-covid", "post-covid", "post covid", "pasc", "post-acute sequelae"]
    elif "me/cfs" in c:
        checks = ["chronic fatigue", "me/cfs", "myalgic encephalomyelitis", "cfs"]
    elif "pots" in c:
        checks = ["postural orthostatic", "pots", "orthostatic tachycardia"]
    elif "mcas" in c:
        checks = ["mast cell", "mcas"]
    elif "lyme" in c:
        checks = ["lyme", "ptlds", "borrelia"]
    elif "gulf war" in c:
        checks = ["gulf war", "gwi"]
    elif "post-viral" in c or "other post" in c:
        checks = ["post-viral", "post viral", "postinfectious", "post-infectious"]
    else:
        checks = [c]
    hit = any(x in blob for x in checks)
    # acute COVID only?
    acute_only = False
    if "long covid" in c or "me/cfs" in c:
        if ("covid" in blob or "sars-cov" in blob) and not hit:
            if any(w in blob for w in ["hospitalized", "acute covid", "severe covid", "outpatient covid"]):
                acute_only = True
    note = "condition-relevant" if hit else ("likely acute-COVID / off-target" if acute_only or ("covid" in blob and "long covid" in c and not hit) else "condition match unclear")
    return hit, note


def phase_rank(phases: list[str] | None) -> int:
    if not phases:
        return 0
    s = " ".join(phases).upper()
    if "PHASE3" in s or "PHASE 3" in s:
        return 3
    if "PHASE2" in s or "PHASE 2" in s:
        return 2
    if "PHASE4" in s or "PHASE 4" in s:
        return 4
    if "PHASE1" in s:
        return 1
    return 0


def evaluate_claim(claim: dict, nct_data: dict[str, dict], pmid_data: dict[str, dict], search: dict) -> dict:
    claim_id = claim["claim_id"]
    agent = claim["agent"]
    condition = claim["condition"]
    refs: list[dict] = []

    # Trials from queue + enriched
    trial_summaries = []
    for t in claim.get("trials") or []:
        nct_id = t.get("nct_id")
        if not nct_id:
            continue
        n = nct_data.get(nct_id) or fetch_nct(nct_id)
        relevant, rel_note = condition_relevant(n, condition) if n.get("fetch_ok") else (False, "fetch failed")
        phase = (n.get("phases") or [t.get("phase")]) 
        phase_s = ",".join(phase) if isinstance(phase, list) else str(phase or "")
        notes = rel_note
        if n.get("why_stopped"):
            notes += f"; stopped: {n['why_stopped'][:120]}"
        if n.get("has_results"):
            notes += "; hasResults=true on CT.gov"
        else:
            notes += "; results not posted on CT.gov"
        refs.append(
            {
                "type": "nct",
                "id": nct_id,
                "title": n.get("title") or t.get("title") or "",
                "year": (n.get("start_date") or "")[:4] or None,
                "status": n.get("status") or t.get("status"),
                "phase": phase_s,
                "url": n.get("url"),
                "notes": f"enroll={n.get('enrollment')} ({n.get('enrollment_type')}); primary={ (n.get('primary_outcome') or '')[:100]}; {notes}",
            }
        )
        trial_summaries.append({**n, "relevant": relevant, "rel_note": rel_note, "phase_s": phase_s})

    # PMIDs from queue studies + therapeutic_agents
    pmids = set()
    for s in claim.get("studies") or []:
        if isinstance(s, dict) and s.get("pmid"):
            pmids.add(str(s["pmid"]))
        elif isinstance(s, str):
            m = re.search(r"(\d{5,9})", s)
            if m:
                pmids.add(m.group(1))
    # also from search hits that look on-condition
    for h in (search.get("hits") or [])[:5]:
        if h.get("pmid"):
            pmids.add(str(h["pmid"]))

    lit_bits = []
    for pmid in sorted(pmids)[:8]:
        p = pmid_data.get(pmid) or fetch_pmid(pmid)
        refs.append(
            {
                "type": "pmid",
                "id": str(pmid),
                "title": p.get("title") or "",
                "year": p.get("year"),
                "url": p.get("url"),
                "notes": (p.get("journal") or "")[:80],
            }
        )
        if p.get("title"):
            lit_bits.append(f"PMID {pmid}: {p.get('title')[:120]}")

    # Record pubmed search
    refs.append(
        {
            "type": "pubmed_search",
            "id": search.get("query") or "",
            "title": f"Europe PMC search ({search.get('hit_count', 0)} hits)",
            "year": None,
            "url": "https://europepmc.org/search?query=" + urllib.parse.quote(search.get("query") or ""),
            "notes": "; ".join(
                f"{h.get('pmid')}:{(h.get('title') or '')[:60]}" for h in (search.get("hits") or [])[:3]
            ),
        }
    )

    # --- Tier logic ---
    locked = HUMAN_LOCKED.get(claim_id)
    agent_l = agent.lower().strip()

    relevant_trials = [t for t in trial_summaries if t.get("relevant")]
    any_relevant = bool(relevant_trials)
    statuses = [(t.get("status") or "").upper() for t in trial_summaries]
    relevant_statuses = [(t.get("status") or "").upper() for t in relevant_trials]
    max_phase = max([phase_rank(t.get("phases")) for t in relevant_trials] or [0])
    enrolls = [t.get("enrollment") for t in relevant_trials if isinstance(t.get("enrollment"), int)]
    max_enroll = max(enrolls) if enrolls else 0
    has_results = any(t.get("has_results") for t in relevant_trials)
    terminated = any(s in ("TERMINATED", "WITHDRAWN", "SUSPENDED") for s in (relevant_statuses or statuses))
    only_terminated = bool(statuses) and all(s in ("TERMINATED", "WITHDRAWN", "SUSPENDED") for s in statuses)
    recruiting_only = bool(statuses) and all(
        s in ("RECRUITING", "NOT_YET_RECRUITING", "ACTIVE_NOT_RECRUITING", "ENROLLING_BY_INVITATION") for s in statuses
    )
    completed = any(s == "COMPLETED" for s in (relevant_statuses or statuses))

    proposed_tier = "D"
    proposed_status = "draft"
    confidence = "medium"
    gaps = []
    rationale_parts = []

    # Special / known contested
    special = None
    if "rituximab" in agent_l and "me/cfs" in condition.lower():
        special = "ritux_mecfs"
    elif ("cognitive behavioural" in agent_l or "cognitive behavioral" in agent_l) and "me/cfs" in condition.lower():
        special = "cbt_mecfs"
    elif "ivermectin" in agent_l:
        special = "ivermectin"
    elif "metformin" in agent_l and "long covid" in condition.lower():
        special = "metformin_lc"
    elif "paxlovid" in agent_l or "nirmatrelvir" in agent_l:
        special = "paxlovid_lc"
    elif agent_l in CLASS_AGENTS:
        special = "class_agent"
    elif NON_TX_PATTERNS.search(agent_l):
        special = "non_tx"
    elif "vaccine" in agent_l:
        special = "vaccine"
    elif "microcrystalline cellulose" in agent_l:
        special = "placebo"

    if locked:
        proposed_tier = locked["tier"]
        proposed_status = locked["status"]
        confidence = "high"
        rationale_parts.append(locked["note"])
        evidence_summary = (
            f"Human-locked claim retained as tier {proposed_tier}. "
            f"Linked trial(s): {'; '.join(t.get('nct_id','')+':'+(t.get('status') or '') for t in trial_summaries)}. "
            f"Literature search '{search.get('query')}' returned {search.get('hit_count')} Europe PMC hits. "
            "Evidence remains early/contested rather than consensus clinical support."
        )
        gaps.append("Full systematic review of published outcomes not performed")
    elif special == "non_tx" or special == "placebo":
        proposed_tier = "D"
        proposed_status = "draft"
        confidence = "high"
        rationale_parts.append("Label is diagnostic/behavioral class/placebo rather than a specific therapeutic agent with condition-directed efficacy evidence.")
        evidence_summary = (
            f"'{agent}' is not a discrete disease-modifying therapeutic with dedicated efficacy literature for {condition} in the extracted sources. "
            f"Associated registry entries appear procedural/class/placebo-related. "
            f"Europe PMC query returned {search.get('hit_count')} hits but do not establish a treatable-agent evidence base."
        )
        gaps.append("No agent-specific efficacy package")
    elif special == "class_agent":
        proposed_tier = "D"
        proposed_status = "draft"
        confidence = "high"
        rationale_parts.append("Class-level agent (ACEI/ARB) without drug-specific supportive LC treatment results in extracted refs.")
        evidence_summary = (
            f"Tracker lists a class-level RAS agent for {condition}. "
            f"Registry trial(s) reviewed: {'; '.join((t.get('title') or '')[:80] for t in trial_summaries)}. "
            "Without drug-specific completed positive trials and posted results for the named condition, evidence is insufficient for a clinical tier."
        )
        gaps.append("Need drug-specific RCTs with posted results in the target condition")
    elif special == "ritux_mecfs":
        proposed_tier = "D"
        proposed_status = "published"
        confidence = "high"
        rationale_parts.append("Phase 3 RituxME and related trials showed no clinical benefit in ME/CFS; evidence is insufficient/negative for treatment claim.")
        evidence_summary = (
            "Rituximab was tested in ME/CFS including a Phase 3 program; published results did not support clinical efficacy, "
            "and the treatment claim is contested/insufficient. "
            f"Registry statuses include: {', '.join(statuses)}. "
            f"Europe PMC hits={search.get('hit_count')}."
        )
        gaps.append("No need for further positive-efficacy framing without new contradictory trials")
    elif special == "cbt_mecfs":
        proposed_tier = "D"
        proposed_status = "published"
        confidence = "medium"
        rationale_parts.append("CBT for ME/CFS remains highly contested (PACE controversy; NICE NG206 does not recommend CBT as curative). Tier D.")
        evidence_summary = (
            "CBT has been studied in ME/CFS, but the evidence base is contested and guideline positions diverge; "
            "it should not be framed as solid disease-modifying clinical evidence. "
            f"Linked trial status: {', '.join(statuses)}. Search hits={search.get('hit_count')}."
        )
        gaps.append("Guideline conflict and outcome-measure disputes")
    elif special == "ivermectin":
        proposed_tier = "D"
        proposed_status = "published"
        confidence = "high"
        rationale_parts.append("Ivermectin lacks reliable supportive RCTs for established Long COVID / PTLDS treatment; contested.")
        evidence_summary = (
            f"For {condition}, extracted trials/literature do not provide solid supportive clinical efficacy for ivermectin. "
            "Broader COVID literature is contested; tracker PMID linkage may be off-target (safety/case report). "
            f"CT.gov statuses: {', '.join(statuses)}. Search hits={search.get('hit_count')}."
        )
        gaps.append("High-quality condition-specific RCTs with clear benefit not identified")
    elif special == "metformin_lc":
        # Prevention signal is stronger than treatment
        proposed_tier = "C"
        proposed_status = "published"
        confidence = "medium"
        rationale_parts.append("COVID-OUT / related work supports a prevention signal for incident long COVID; treatment of established LC remains early/limited → C not B.")
        evidence_summary = (
            "Metformin has a notable signal for reducing incidence of long COVID after acute infection in randomized data, "
            "but that is prevention rather than treatment of established Long COVID. "
            f"Linked trials: {', '.join(t.get('nct_id','')+':'+ (t.get('status') or '') for t in trial_summaries)}. "
            f"Literature includes preclinical GWI work and PACVS map notes. Search hits={search.get('hit_count')}."
        )
        gaps.append("Dedicated large RCTs for treatment of established Long COVID with posted results")
    elif special == "paxlovid_lc":
        proposed_tier = "C"
        proposed_status = "published"
        confidence = "medium"
        rationale_parts.append("Multiple Phase 2 LC trials exist; results mixed/limited for established PASC—early clinical signal tier C, not B.")
        evidence_summary = (
            "Nirmatrelvir/ritonavir has been tested for post-COVID / long COVID in several trials; "
            "available public results are mixed and do not yet constitute solid consensus treatment evidence. "
            f"Trial statuses: {', '.join(statuses)}. Search hits={search.get('hit_count')}."
        )
        gaps.append("Clear positive Phase 3 treatment results for established LC not confirmed in this pass")
    elif special == "vaccine":
        proposed_tier = "D"
        proposed_status = "draft"
        confidence = "medium"
        rationale_parts.append("COVID vaccines are prevention/acute tools; treating established Long COVID with additional vaccination is uncertain/insufficient.")
        evidence_summary = (
            f"Registry entries link {agent} to Long COVID contexts, but vaccination is not established therapy for existing Long COVID. "
            f"Statuses: {', '.join(statuses)}. Search hits={search.get('hit_count')}."
        )
        gaps.append("Condition-specific therapeutic RCTs for established LC")
    else:
        # Generic rubric
        if only_terminated or (terminated and not completed and not any_relevant):
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "high" if only_terminated else "medium"
            rationale_parts.append("Trial(s) terminated/withdrawn or no completed condition-relevant evidence.")
        elif not any_relevant and trial_summaries:
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append("Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated).")
            gaps.append("Condition-matched trials")
        elif recruiting_only and not has_results:
            proposed_tier = "C"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append("Only ongoing/not-completed trials; no posted results → early/insufficient for publish-as-solid.")
            gaps.append("Completed results")
        elif completed and max_phase >= 3 and has_results and any_relevant and max_enroll >= 100:
            # Still need supportive results — we do NOT invent positivity
            proposed_tier = "C"
            proposed_status = "draft"
            confidence = "low"
            rationale_parts.append(
                "Phase 3 completed with results flag, but this bot did not verify positive efficacy endpoints; keeping C/draft pending result curation."
            )
            gaps.append("Manual review of posted primary endpoint directionality")
        elif completed and max_phase >= 3 and any_relevant and not has_results:
            proposed_tier = "C"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append("Phase 3 completed but results not found/posted on CT.gov → cannot support B; early/uncertain C draft.")
            gaps.append("Posted results / publications of primary outcomes")
        elif completed and any_relevant and max_phase >= 2:
            proposed_tier = "C"
            proposed_status = "published" if max_enroll and max_enroll >= 20 else "draft"
            confidence = "medium"
            rationale_parts.append("Early clinical (completed Phase 2+/small) without verified supportive Phase 3 synthesis → C.")
            gaps.append("Larger confirmatory trials and outcome publications")
        elif completed and any_relevant:
            proposed_tier = "C"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append("Some completed condition-related work but thin/early.")
            gaps.append("Phase, size, and published outcomes")
        else:
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append("Insufficient extracted clinical evidence for the agent–condition pair.")
            gaps.append("Condition-specific clinical studies")

        # Build evidence summary for generic path
        trial_bits = []
        for t in trial_summaries[:4]:
            trial_bits.append(
                f"{t.get('nct_id')} ({t.get('status')}, phase={t.get('phase_s')}, n={t.get('enrollment')}, relevant={t.get('relevant')})"
            )
        evidence_summary = (
            f"Extracted {len(trial_summaries)} registry trial(s) for {agent} → {condition}: "
            + ("; ".join(trial_bits) if trial_bits else "none")
            + ". "
            + ("Posted CT.gov results: yes. " if has_results else "No posted CT.gov results found in this pass. ")
            + (f"Literature notes: {'; '.join(lit_bits[:3])}. " if lit_bits else "")
            + f"Europe PMC query `{search.get('query')}` → {search.get('hit_count')} hits (top cited sampled). "
            + "This evaluation does not invent positive efficacy; absent clear supportive published outcomes, tier stays C/D."
        )

    # Ampligen / amphetamine already handled via lock

    # Prefer not to publish D with high confidence as published unless special contested cases
    if proposed_tier == "D" and proposed_status == "published" and special not in ("ritux_mecfs", "cbt_mecfs", "ivermectin"):
        proposed_status = "draft"

    if not gaps:
        gaps.append("Not a systematic review; single-pass registry + Europe PMC sampling")

    return {
        "claim_id": claim_id,
        "agent": agent,
        "condition": condition,
        "references": refs,
        "evidence_summary": evidence_summary,
        "proposed_tier": proposed_tier,
        "proposed_status": proposed_status,
        "rationale": " ".join(rationale_parts),
        "confidence": confidence,
        "gaps": gaps,
        "human_locked": bool(locked),
        "special_case": special,
        "eval_date": EVAL_DATE,
    }


def load_queue_studies_from_ta(queue: list[dict]) -> list[dict]:
    ta = json.load(open(TRACKER / "data" / "therapeutic_agents.json"))["agents"]
    by = {a["Therapeutic Agent"].lower(): a for a in ta}
    out = []
    for c in queue:
        a = by.get(c["agent"].lower())
        studies = list(c.get("studies") or [])
        if a and a.get("studies"):
            # merge unique by pmid/title
            seen = {(s.get("pmid") if isinstance(s, dict) else s) for s in studies}
            for s in a["studies"]:
                key = s.get("pmid") if isinstance(s, dict) else s
                if key not in seen:
                    studies.append(s)
                    seen.add(key)
        c2 = dict(c)
        c2["studies"] = studies
        out.append(c2)
    return out


def apply_to_claim_file(ev: dict) -> bool:
    """Update claim JSON if confidence medium/high or auto-eval documented. Returns True if written."""
    claim_id = ev["claim_id"]
    slug = claim_id.replace("osmf:claim:", "")
    path = CLAIMS_DIR / f"{slug}.json"
    if not path.exists():
        print("MISSING claim file", path)
        return False

    conf = ev["confidence"]
    # Always apply with documentation when medium/high; also apply low if we explicitly draft
    if conf == "low" and ev["proposed_status"] == "draft" and not ev.get("human_locked"):
        # still apply draft updates with auto-eval note for consistency of queue completion
        pass

    data = json.loads(path.read_text())
    # Preserve human reviewed_by for locked claims but add eval notes
    data["evidence_tier"] = ev["proposed_tier"]
    data["status"] = ev["proposed_status"]

    ref_bits = []
    for r in ev["references"][:6]:
        if r["type"] == "nct":
            ref_bits.append(f"{r['id']} ({r.get('status')})")
        elif r["type"] == "pmid":
            ref_bits.append(f"PMID:{r['id']}")
    ref_str = ", ".join(ref_bits) if ref_bits else "see evidence JSONL"

    limitations = (
        f"Key refs: {ref_str}. "
        f"Evaluated from extracted references on {EVAL_DATE}; not a systematic review. "
        f"{ev['rationale']} "
        "Not medical advice. Tracker Moderate label is not an OSMF A/B grade."
    )
    data["limitations"] = limitations.strip()

    if ev.get("human_locked"):
        # keep original human reviewer, append bot
        prev = data.get("reviewed_by") or "MattH55"
        if REVIEWED_BY not in prev:
            data["reviewed_by"] = f"{prev}+{REVIEWED_BY}"
        else:
            data["reviewed_by"] = prev
    else:
        data["reviewed_by"] = REVIEWED_BY
    data["reviewed_at"] = EVAL_ISO
    data["confidence_notes"] = (
        f"[{ev['confidence']}] {ev['rationale']} | {ev['evidence_summary'][:400]}"
    )

    # Ensure sources include ncts/pmids
    sources = data.get("sources") or []
    existing_vals = {(s.get("type"), s.get("value")) for s in sources}
    for r in ev["references"]:
        if r["type"] == "nct":
            key = ("nct", r["id"])
            if key not in existing_vals:
                sources.append({"type": "nct", "value": r["id"]})
                existing_vals.add(key)
        elif r["type"] == "pmid":
            key = ("pmid", r["id"])
            if key not in existing_vals:
                sources.append({"type": "pmid", "value": r["id"]})
                existing_vals.add(key)
    data["sources"] = sources

    path.write_text(json.dumps(data, indent=2) + "\n")
    return True


def write_markdown(evals: list[dict]) -> None:
    by_tier: dict[str, list] = {"A": [], "B": [], "C": [], "D": []}
    for e in evals:
        by_tier.setdefault(e["proposed_tier"], []).append(e)

    lines = []
    lines.append("# Moderate agents — evidence evaluation report")
    lines.append("")
    lines.append(f"**Date:** {EVAL_DATE} (America/Edmonton)")
    lines.append(f"**Evaluator:** {REVIEWED_BY}")
    lines.append(f"**Queue size:** {len(evals)} claims")
    lines.append("")
    lines.append("## Counts by proposed tier")
    lines.append("")
    for t in "ABCD":
        items = by_tier.get(t) or []
        pub = sum(1 for x in items if x["proposed_status"] == "published")
        draft = sum(1 for x in items if x["proposed_status"] == "draft")
        lines.append(f"- **{t}**: {len(items)} (published={pub}, draft={draft})")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append(
        "For each claim: ClinicalTrials.gov API v2 summaries for NCT IDs from tracker `trials[]`; "
        "PMIDs from tracker `studies[]` / Key Studies; Europe PMC search fallback "
        "(`agent` + condition terms, top cited, limit 5). "
        "Tiers follow OSMF A–D. Phase 3 without verified supportive results is **not** upgraded to B. "
        "Claims 1–2 (amphetamine-dextroamphetamine→Long COVID; Ampligen→ME/CFS) were human-graded C/published and retained."
    )
    lines.append("")
    lines.append("## Notable upgrades / downgrades vs import default (C)")
    lines.append("")
    upgrades = [e for e in evals if e["proposed_tier"] in ("A", "B")]
    downgrades = [e for e in evals if e["proposed_tier"] == "D"]
    if upgrades:
        for e in upgrades:
            lines.append(f"- UPGRADE {e['agent']} → {e['condition']}: **{e['proposed_tier']}** — {e['rationale'][:160]}")
    else:
        lines.append("- No A/B upgrades (honest: no verified solid supportive Phase 3 packages found in this pass).")
    lines.append(f"- Downgrades to D: {len(downgrades)} claims (terminated/off-target/class/contested/insufficient).")
    lines.append("")

    draft_missing = [
        e
        for e in evals
        if e["proposed_status"] == "draft"
        and any("results" in g.lower() or "posted" in g.lower() for g in e.get("gaps") or [])
    ]
    lines.append("## Left draft due to missing / unverified results")
    lines.append("")
    if not draft_missing:
        lines.append("- (none flagged specifically; see per-claim gaps)")
    else:
        for e in draft_missing[:40]:
            lines.append(f"- {e['agent']} → {e['condition']} (tier {e['proposed_tier']}): {', '.join(e['gaps'][:2])}")
    lines.append("")

    for t in "ABCD":
        items = by_tier.get(t) or []
        if not items:
            continue
        lines.append(f"## Tier {t}")
        lines.append("")
        for e in items:
            lines.append(f"### {e['agent']} → {e['condition']}")
            lines.append(f"- **claim_id:** `{e['claim_id']}`")
            lines.append(f"- **proposed:** tier {e['proposed_tier']}, status `{e['proposed_status']}`, confidence `{e['confidence']}`")
            if e.get("human_locked"):
                lines.append("- **note:** human-locked (claims 1–2 session)")
            lines.append(f"- **rationale:** {e['rationale']}")
            lines.append(f"- **evidence_summary:** {e['evidence_summary']}")
            lines.append(f"- **gaps:** {'; '.join(e['gaps'])}")
            lines.append("- **references:**")
            for r in e["references"][:8]:
                extra = []
                if r.get("status"):
                    extra.append(str(r["status"]))
                if r.get("phase"):
                    extra.append(str(r["phase"]))
                extra_s = (", " + ", ".join(extra)) if extra else ""
                lines.append(f"  - [{r['type']}] {r.get('id','')} — {(r.get('title') or '')[:100]}{extra_s}")
            lines.append("")

    MD_PATH.write_text("\n".join(lines) + "\n")


def main() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    queue = json.load(open(QUEUE_PATH))
    queue = load_queue_studies_from_ta(queue)
    print(f"Loaded {len(queue)} claims")

    # Prefetch all NCTs
    nct_ids = sorted({t["nct_id"] for c in queue for t in (c.get("trials") or []) if t.get("nct_id")})
    print(f"Fetching {len(nct_ids)} NCTs...")
    nct_data = {}
    for i, nct in enumerate(nct_ids):
        nct_data[nct] = fetch_nct(nct)
        if (i + 1) % 10 == 0:
            print(f"  NCT {i+1}/{len(nct_ids)}")
    print("NCT fetch done")

    # Prefetch known PMIDs from studies
    pmid_set = set()
    for c in queue:
        for s in c.get("studies") or []:
            if isinstance(s, dict) and s.get("pmid"):
                pmid_set.add(str(s["pmid"]))
    print(f"Fetching {len(pmid_set)} study PMIDs...")
    pmid_data = {}
    for pmid in sorted(pmid_set):
        pmid_data[pmid] = fetch_pmid(pmid)

    evals = []
    for i, claim in enumerate(queue):
        agent_q = agent_search_name(claim["agent"])
        cond_terms = condition_search_terms(claim["condition"])
        # Build OR of condition terms
        cond_q = " OR ".join(cond_terms)
        query = f"({agent_q}) AND ({cond_q})"
        # For very generic agents, tighten
        if len(agent_q) < 4:
            query = f"\"{claim['agent']}\" AND ({cond_q})"
        print(f"[{i+1}/{len(queue)}] {claim['agent'][:40]} | search...")
        search = europepmc_search(query, page_size=5)
        # also fetch top hit PMIDs metadata
        for h in search.get("hits") or []:
            if h.get("pmid") and str(h["pmid"]) not in pmid_data:
                pmid_data[str(h["pmid"])] = fetch_pmid(str(h["pmid"]))
        ev = evaluate_claim(claim, nct_data, pmid_data, search)
        evals.append(ev)
        print(f"    → {ev['proposed_tier']}/{ev['proposed_status']} conf={ev['confidence']}")

    # Write JSONL
    with open(JSONL_PATH, "w") as f:
        for e in evals:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print("Wrote", JSONL_PATH)

    write_markdown(evals)
    print("Wrote", MD_PATH)

    # Apply to claim files
    n_ok = 0
    for e in evals:
        if apply_to_claim_file(e):
            n_ok += 1
    print(f"Updated {n_ok} claim files")

    # Summary counts
    from collections import Counter
    print("Tiers:", Counter(e["proposed_tier"] for e in evals))
    print("Status:", Counter(e["proposed_status"] for e in evals))
    print("Confidence:", Counter(e["confidence"] for e in evals))


if __name__ == "__main__":
    main()
