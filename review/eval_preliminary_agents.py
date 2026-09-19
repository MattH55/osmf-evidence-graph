#!/usr/bin/env python3
"""Extract references and evaluate Preliminary Tracker agent treats_candidate_for claims.

Same methodology as Moderate eval (NOT one-by-one UI grading), with Wave A/B/C
API budget prioritization:

  Wave A (deep): COMPLETED Phase 2/3/4 OR NCT with results modules
                 → CT.gov API v2 + Europe PMC / PubMed NCT publications
  Wave B (standard): remaining with any NCT → study record; PubMed only if
                 title/status suggests published results
  Wave C (light): no usable NCT → keep D draft, document thinness
"""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GRAPH = Path("/workspace/osmf-evidence-graph")
TRACKER = Path("/workspace/osmf-research-tracker")
REVIEW = GRAPH / "review"
CACHE = REVIEW / "cache"
CLAIMS_DIR = GRAPH / "data" / "claims"
ENTITIES_DIR = GRAPH / "data" / "entities"
QUEUE_PATH = REVIEW / "preliminary-agents-queue.json"
JSONL_PATH = REVIEW / "preliminary-agents-evidence.jsonl"
MD_PATH = REVIEW / "preliminary-agents-evidence.md"
PROGRESS_PATH = REVIEW / "preliminary-agents-progress.json"

EVAL_DATE = "2026-09-19"
EVAL_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
REVIEWED_BY = "evidence-eval-bot"

USER_AGENT = "OSMF-EvidenceEval/1.0 (research; contact: opensourcemed.info)"

NON_TX_PATTERNS = re.compile(
    r"^(genetic|behavioral|biopsychological|physiological evaluation|multidisciplinary approach|"
    r"microcrystalline cellulose|digital cognitive|active comparator|placebo|"
    r"standard of care|usual care|best supportive|care as usual|lactose|"
    r"sham |control |coordinated care$|relaxation therapy$|routine daily|"
    r"institutional standard)",
    re.I,
)

TITLE_RESULTS_HINT = re.compile(
    r"\b(results?|efficacy|effectiveness|outcome|randomized|randomised|RCT|"
    r"phase\s*[234]|pivotal|primary endpoint|published)\b",
    re.I,
)


def http_get_json(url: str, timeout: int = 45) -> Any:
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
    )
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


def fetch_nct(nct_id: str, force: bool = False) -> dict:
    key = f"nct_{nct_id}.json"
    if not force:
        cached = cache_get(key)
        if cached is not None and cached.get("fetch_ok") is not None:
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
            "fetched_at": EVAL_ISO,
        }
    except Exception as e:
        out = {
            "nct_id": nct_id,
            "fetch_ok": False,
            "error": str(e),
            "url": f"https://clinicaltrials.gov/study/{nct_id}",
            "fetched_at": EVAL_ISO,
        }
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
        + urllib.parse.urlencode(
            {"query": f"EXT_ID:{pmid} AND SRC:MED", "format": "json", "pageSize": 1}
        )
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
            out = {
                "pmid": pmid,
                "fetch_ok": False,
                "error": "not found",
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            }
    except Exception as e:
        out = {
            "pmid": pmid,
            "fetch_ok": False,
            "error": str(e),
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        }
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
        + urllib.parse.urlencode(
            {"query": query, "format": "json", "pageSize": page_size, "sort": "CITED desc"}
        )
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
                    "url": (
                        f"https://pubmed.ncbi.nlm.nih.gov/{r.get('pmid')}/"
                        if r.get("pmid")
                        else None
                    ),
                }
            )
        out = {
            "query": query,
            "hit_count": data.get("hitCount", 0),
            "hits": hits,
            "fetch_ok": True,
        }
    except Exception as e:
        out = {
            "query": query,
            "hit_count": 0,
            "hits": [],
            "fetch_ok": False,
            "error": str(e),
        }
    cache_set(key, out)
    time.sleep(0.12)
    return out


def search_europepmc_nct(nct_id: str, limit: int = 8) -> dict:
    key = f"epmc_nct_{nct_id}.json"
    cached = cache_get(key)
    if cached is not None and cached.get("fetch_ok") is not None:
        return cached
    q = urllib.parse.quote(f'"{nct_id}"')
    url = (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        f"?query={q}&format=json&pageSize={limit}&resultType=core&sort=CITED%20desc"
    )
    try:
        data = http_get_json(url)
        hits = data.get("resultList", {}).get("result", []) or []
        papers = []
        for h in hits:
            papers.append(
                {
                    "pmid": h.get("pmid") or h.get("id"),
                    "doi": h.get("doi"),
                    "title": h.get("title"),
                    "year": h.get("pubYear"),
                    "journal": h.get("journalTitle"),
                    "cited_by": h.get("citedByCount"),
                }
            )
        out = {
            "nct_id": nct_id,
            "hit_count": data.get("hitCount"),
            "papers": papers,
            "url": f"https://europepmc.org/search?query=%22{nct_id}%22",
            "fetch_ok": True,
            "fetched_at": EVAL_ISO,
        }
    except Exception as e:
        out = {
            "nct_id": nct_id,
            "fetch_ok": False,
            "error": str(e),
            "papers": [],
            "hit_count": 0,
        }
    cache_set(key, out)
    time.sleep(0.15)
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
    a = agent
    a = re.sub(r"\(.*?\)", " ", a)
    a = re.sub(r"®", "", a)
    a = re.sub(r"\s+\d+\s*mg\b", "", a, flags=re.I)
    a = re.sub(r"\s+", " ", a).strip()
    if len(a) > 80:
        # truncate very long dose-protocol labels to first meaningful token span
        a = a[:80].rsplit(" ", 1)[0]
    return a


def condition_relevant(nct: dict, condition: str) -> tuple[bool, str]:
    blob = " ".join(
        [
            nct.get("title") or "",
            " ".join(nct.get("conditions") or []),
            nct.get("brief_summary") or "",
            nct.get("primary_outcome") or "",
        ]
    ).lower()
    c = condition.lower()
    checks: list[str] = []
    if "long covid" in c:
        checks = [
            "long covid",
            "long-covid",
            "post-covid",
            "post covid",
            "pasc",
            "post-acute sequelae",
        ]
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
    acute_only = False
    if "long covid" in c or "me/cfs" in c:
        if ("covid" in blob or "sars-cov" in blob) and not hit:
            if any(
                w in blob
                for w in ["hospitalized", "acute covid", "severe covid", "outpatient covid"]
            ):
                acute_only = True
    note = (
        "condition-relevant"
        if hit
        else (
            "likely acute-COVID / off-target"
            if acute_only or ("covid" in blob and "long covid" in c and not hit)
            else "condition match unclear"
        )
    )
    return hit, note


def phase_rank(phases: list[str] | None) -> int:
    if not phases:
        return 0
    s = " ".join(phases).upper()
    if "PHASE4" in s or "PHASE 4" in s:
        return 4
    if "PHASE3" in s or "PHASE 3" in s:
        return 3
    if "PHASE2" in s or "PHASE 2" in s:
        return 2
    if "PHASE1" in s:
        return 1
    return 0


def tracker_phase_rank(phase: str | None) -> int:
    if not phase:
        return 0
    s = str(phase).upper().replace(" ", "")
    if "PHASE4" in s or s == "4":
        return 4
    if "PHASE3" in s or s == "3":
        return 3
    if "PHASE2" in s or s == "2":
        return 2
    if "PHASE1" in s or s == "1":
        return 1
    return 0


def is_wave_a_trial(t: dict, nct_enrich: dict | None = None) -> bool:
    status = (t.get("status") or "").upper()
    if nct_enrich and nct_enrich.get("status"):
        status = (nct_enrich.get("status") or status).upper()
    ph_rank = tracker_phase_rank(t.get("phase"))
    if nct_enrich and nct_enrich.get("phases"):
        ph_rank = max(ph_rank, phase_rank(nct_enrich.get("phases")))
    if status == "COMPLETED" and ph_rank >= 2:
        return True
    if nct_enrich and nct_enrich.get("has_results"):
        return True
    return False


def title_suggests_published_results(title: str, nct: dict | None = None) -> bool:
    if TITLE_RESULTS_HINT.search(title or ""):
        return True
    if nct and nct.get("has_results"):
        return True
    status = ((nct or {}).get("status") or "").upper()
    if status == "COMPLETED" and phase_rank((nct or {}).get("phases")) >= 2:
        return True
    return False


def load_skip_claim_ids() -> set[str]:
    skip: set[str] = set()
    for name in (
        "moderate-agents-evidence.jsonl",
        "published-13-deepdive.jsonl",
        "phase3-draft-results-chase.jsonl",
    ):
        p = REVIEW / name
        if not p.exists():
            continue
        for line in p.open():
            if not line.strip():
                continue
            row = json.loads(line)
            cid = row.get("claim_id") or row.get("id")
            if cid:
                skip.add(cid)
    return skip


def build_queue() -> list[dict]:
    ta = json.load(open(TRACKER / "data" / "therapeutic_agents.json"))["agents"]
    prelim = {
        a["Therapeutic Agent"].strip().lower(): a
        for a in ta
        if (a.get("Evidence Level") or "") == "Preliminary"
    }
    ents = {}
    for ep in ENTITIES_DIR.glob("*.json"):
        d = json.loads(ep.read_text())
        if d.get("id"):
            ents[d["id"]] = d

    skip = load_skip_claim_ids()
    queue: list[dict] = []

    for p in sorted(CLAIMS_DIR.glob("*.json")):
        claim = json.loads(p.read_text())
        if claim.get("predicate") != "treats_candidate_for":
            continue
        if claim["id"] in skip:
            continue
        subj = ents.get(claim.get("subject_id") or "")
        if not subj:
            continue
        label = (subj.get("label") or "").strip()
        agent_rec = prelim.get(label.lower())
        if not agent_rec:
            continue

        # object condition label
        obj_id = claim.get("object_id") or ""
        cond_ent = ents.get(obj_id) or {}
        cond_label = cond_ent.get("label") or obj_id.replace("osmf:condition:", "").replace("-", " ")

        trials = []
        for t in agent_rec.get("trials") or []:
            if not t.get("nct_id"):
                continue
            # keep trials that look related to this condition when multiple exist
            trials.append(
                {
                    "nct_id": t["nct_id"].upper(),
                    "title": t.get("title") or "",
                    "status": t.get("status") or "",
                    "phase": t.get("phase") or "",
                    "size_category": t.get("size_category"),
                    "start_date": t.get("start_date"),
                    "completion_date": t.get("completion_date"),
                }
            )

        # Prefer condition-matching trials for multi-condition agents
        cond_l = cond_label.lower()
        matched_trials = []
        for t in trials:
            blob = (t.get("title") or "").lower()
            ok = False
            if "long covid" in cond_l and any(
                x in blob for x in ("long covid", "long-covid", "post-covid", "pasc")
            ):
                ok = True
            elif "me/cfs" in cond_l and any(
                x in blob for x in ("fatigue", "me/cfs", "myalgic", "cfs")
            ):
                ok = True
            elif "pots" in cond_l and ("orthostatic" in blob or "pots" in blob):
                ok = True
            elif "mcas" in cond_l and "mast cell" in blob:
                ok = True
            elif "lyme" in cond_l and "lyme" in blob:
                ok = True
            elif "gulf war" in cond_l and "gulf war" in blob:
                ok = True
            if ok:
                matched_trials.append(t)
        use_trials = matched_trials if matched_trials else trials

        wave = "C"
        if any(is_wave_a_trial(t) for t in use_trials):
            wave = "A"
        elif use_trials:
            wave = "B"

        slug_agent = (claim.get("subject_id") or "").replace("osmf:agent:", "")
        queue.append(
            {
                "claim_id": claim["id"],
                "agent_id": claim.get("subject_id"),
                "agent": label,
                "condition_id": obj_id,
                "condition": cond_label,
                "current_tier": claim.get("evidence_tier") or "D",
                "status": claim.get("status") or "draft",
                "tracker_evidence_level": "Preliminary",
                "mechanism": (agent_rec.get("Proposed Mechanism") or "")[:240],
                "key_studies": agent_rec.get("Key Studies / References"),
                "studies": agent_rec.get("studies") or [],
                "trials": use_trials,
                "wave": wave,
                "desk_url": f"https://desk.opensourcemed.info/entity/osmf/agent/{slug_agent}",
                "claim_url": f"https://desk.opensourcemed.info/claim/{claim['id'].replace(':', '/')}",
                "tracker_url": f"https://research.opensourcemed.info/agents/{slug_agent}/",
            }
        )

    # stable order: Wave A first, then B, then C; alpha within
    wave_ord = {"A": 0, "B": 1, "C": 2}
    queue.sort(key=lambda c: (wave_ord.get(c["wave"], 9), c["agent"].lower(), c["condition"].lower()))
    return queue


def evaluate_claim(
    claim: dict,
    nct_data: dict[str, dict],
    pmid_data: dict[str, dict],
    search: dict | None,
    nct_pubs: dict[str, dict],
) -> dict:
    claim_id = claim["claim_id"]
    agent = claim["agent"]
    condition = claim["condition"]
    wave = claim.get("wave") or "C"
    refs: list[dict] = []

    trial_summaries = []
    for t in claim.get("trials") or []:
        nct_id = t.get("nct_id")
        if not nct_id:
            continue
        n = nct_data.get(nct_id) or {"nct_id": nct_id, "fetch_ok": False}
        relevant, rel_note = (
            condition_relevant(n, condition) if n.get("fetch_ok") else (False, "fetch failed")
        )
        phase = n.get("phases") or [t.get("phase")]
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
                "url": n.get("url") or f"https://clinicaltrials.gov/study/{nct_id}",
                "notes": (
                    f"enroll={n.get('enrollment')} ({n.get('enrollment_type')}); "
                    f"primary={(n.get('primary_outcome') or '')[:100]}; {notes}"
                ),
            }
        )
        trial_summaries.append(
            {**n, "relevant": relevant, "rel_note": rel_note, "phase_s": phase_s}
        )

        # Wave A / selective B: publications for this NCT
        pubs = nct_pubs.get(nct_id)
        if pubs and pubs.get("papers"):
            for paper in (pubs.get("papers") or [])[:4]:
                pmid = paper.get("pmid")
                if not pmid:
                    continue
                refs.append(
                    {
                        "type": "pmid",
                        "id": str(pmid),
                        "title": paper.get("title") or "",
                        "year": paper.get("year"),
                        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                        "notes": f"via NCT {nct_id}; {(paper.get('journal') or '')[:60]}",
                    }
                )

    # PMIDs from tracker studies
    pmids = set()
    for s in claim.get("studies") or []:
        if isinstance(s, dict) and s.get("pmid"):
            pmids.add(str(s["pmid"]))
        elif isinstance(s, str):
            m = re.search(r"(\d{5,9})", s)
            if m:
                pmids.add(m.group(1))

    if search:
        for h in (search.get("hits") or [])[:5]:
            if h.get("pmid"):
                pmids.add(str(h["pmid"]))

    lit_bits = []
    for pmid in sorted(pmids)[:8]:
        # skip if already added via nct pubs
        if any(r.get("type") == "pmid" and r.get("id") == str(pmid) for r in refs):
            continue
        p = pmid_data.get(pmid) or {"pmid": pmid, "fetch_ok": False}
        refs.append(
            {
                "type": "pmid",
                "id": str(pmid),
                "title": p.get("title") or "",
                "year": p.get("year"),
                "url": p.get("url") or f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "notes": (p.get("journal") or "")[:80],
            }
        )
        if p.get("title"):
            lit_bits.append(f"PMID {pmid}: {p.get('title')[:120]}")

    if search:
        refs.append(
            {
                "type": "pubmed_search",
                "id": search.get("query") or "",
                "title": f"Europe PMC search ({search.get('hit_count', 0)} hits)",
                "year": None,
                "url": "https://europepmc.org/search?query="
                + urllib.parse.quote(search.get("query") or ""),
                "notes": "; ".join(
                    f"{h.get('pmid')}:{(h.get('title') or '')[:60]}"
                    for h in (search.get("hits") or [])[:3]
                ),
            }
        )

    agent_l = agent.lower().strip()
    relevant_trials = [t for t in trial_summaries if t.get("relevant")]
    any_relevant = bool(relevant_trials)
    statuses = [(t.get("status") or "").upper() for t in trial_summaries]
    relevant_statuses = [(t.get("status") or "").upper() for t in relevant_trials]
    max_phase = max([phase_rank(t.get("phases")) for t in relevant_trials] or [0])
    enrolls = [
        t.get("enrollment") for t in relevant_trials if isinstance(t.get("enrollment"), int)
    ]
    max_enroll = max(enrolls) if enrolls else 0
    has_results = any(t.get("has_results") for t in relevant_trials)
    terminated = any(
        s in ("TERMINATED", "WITHDRAWN", "SUSPENDED")
        for s in (relevant_statuses or statuses)
    )
    only_terminated = bool(statuses) and all(
        s in ("TERMINATED", "WITHDRAWN", "SUSPENDED") for s in statuses
    )
    recruiting_only = bool(statuses) and all(
        s
        in (
            "RECRUITING",
            "NOT_YET_RECRUITING",
            "ACTIVE_NOT_RECRUITING",
            "ENROLLING_BY_INVITATION",
        )
        for s in statuses
    )
    completed = any(s == "COMPLETED" for s in (relevant_statuses or statuses))
    n_pub_pmids = sum(1 for r in refs if r.get("type") == "pmid")

    proposed_tier = "D"
    proposed_status = "draft"
    confidence = "medium"
    gaps: list[str] = []
    rationale_parts: list[str] = []

    special = None
    if NON_TX_PATTERNS.search(agent_l) or "lactose" in agent_l or agent_l in {
        "care as usual",
        "coordinated care",
        "relaxation therapy",
        "routine daily activity",
    }:
        special = "non_tx"
    elif "placebo" in agent_l or "microcrystalline cellulose" in agent_l or "sham" in agent_l:
        special = "placebo"
    elif "vaccine" in agent_l:
        special = "vaccine"
    elif (
        ("cognitive behavioral" in agent_l or "cognitive behavioural" in agent_l)
        and "me/cfs" in condition.lower()
    ):
        special = "cbt_mecfs"

    if special in ("non_tx", "placebo"):
        proposed_tier = "D"
        proposed_status = "draft"
        confidence = "high"
        rationale_parts.append(
            "Label is diagnostic/behavioral/class/placebo rather than a discrete therapeutic "
            "with condition-directed efficacy evidence."
        )
        evidence_summary = (
            f"'{agent}' is not a discrete disease-modifying therapeutic with dedicated efficacy "
            f"literature for {condition} in the extracted sources (wave {wave}). "
            f"Associated registry entries appear procedural/class/placebo-related."
        )
        gaps.append("No agent-specific efficacy package")
    elif special == "vaccine":
        proposed_tier = "D"
        proposed_status = "draft"
        confidence = "medium"
        rationale_parts.append(
            "Vaccines are prevention/acute tools; treating established post-viral disease with "
            "additional vaccination remains uncertain/insufficient."
        )
        evidence_summary = (
            f"Registry entries link {agent} to {condition} contexts, but vaccination is not "
            f"established therapy for the named post-acute condition. "
            f"Statuses: {', '.join(statuses) or 'none'}."
        )
        gaps.append("Condition-specific therapeutic RCTs for established disease")
    elif special == "cbt_mecfs":
        proposed_tier = "D"
        proposed_status = "published"
        confidence = "medium"
        rationale_parts.append(
            "CBT for ME/CFS remains highly contested (PACE controversy; NICE NG206 does not "
            "recommend CBT as curative). Tier D despite trial activity."
        )
        evidence_summary = (
            "CBT has been studied in ME/CFS, but the evidence base is contested and guideline "
            f"positions diverge. Linked statuses: {', '.join(statuses)}. "
            "Not framed as solid disease-modifying clinical evidence."
        )
        gaps.append("Guideline conflict and outcome-measure disputes")
    elif wave == "C" or not trial_summaries:
        proposed_tier = "D"
        proposed_status = "draft"
        confidence = "high"
        rationale_parts.append(
            "No usable interventional NCT / thin registration linkage; Preliminary tracker "
            "level — keep D draft."
        )
        evidence_summary = (
            f"Wave C / thin evidence for {agent} → {condition}: no fetched condition-relevant "
            "interventional package. Tracker Evidence Level=Preliminary. Not upgraded."
        )
        gaps.append("Usable NCT with condition-matched interventional design")
    else:
        # Generic rubric — honest bar: almost all stay D or C
        if only_terminated or (terminated and not completed and not any_relevant):
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "high" if only_terminated else "medium"
            rationale_parts.append(
                "Trial(s) terminated/withdrawn or no completed condition-relevant evidence."
            )
        elif not any_relevant and trial_summaries:
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append(
                "Linked NCT(s) do not clearly target the claim condition (off-target / acute / unrelated)."
            )
            gaps.append("Condition-matched trials")
        elif recruiting_only and not has_results:
            # Preliminary + only recruiting → stay D (stricter than Moderate C)
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append(
                "Only ongoing/not-completed trials and no posted results; Preliminary → D draft."
            )
            gaps.append("Completed results")
        elif completed and any_relevant and max_phase >= 3 and has_results and n_pub_pmids >= 1 and max_enroll >= 50:
            # Still not B without verified positive multi-source package
            proposed_tier = "C"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append(
                "Completed Phase 3+ with results flag and literature hits, but this bot did not "
                "verify positive efficacy endpoints or a multi-source clinical package → C draft "
                "(not B)."
            )
            gaps.append("Manual review of primary endpoint directionality / multi-source synthesis")
        elif completed and any_relevant and max_phase >= 2 and (has_results or n_pub_pmids >= 1):
            proposed_tier = "C"
            # Publish only when we can stand behind early clinical signal documentation
            if max_enroll >= 20 and confidence_ok_for_publish(has_results, n_pub_pmids, max_phase):
                proposed_status = "published"
                confidence = "medium"
                rationale_parts.append(
                    "Early clinical (completed Phase 2+/condition-relevant) with results or "
                    "NCT-linked publications → C published (Preliminary; not confirmatory)."
                )
            else:
                proposed_status = "draft"
                confidence = "medium"
                rationale_parts.append(
                    "Early clinical signal thin (small n or sparse pubs) → C draft."
                )
            gaps.append("Larger confirmatory trials and outcome publications")
        elif completed and any_relevant and max_phase >= 2:
            proposed_tier = "C"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append(
                "Completed Phase 2+ condition-relevant trial without posted results/pubs in this "
                "pass → C draft."
            )
            gaps.append("Posted results / publications of primary outcomes")
        elif completed and any_relevant:
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append(
                "Some completed condition-related work but phase/size/pubs too thin for C."
            )
            gaps.append("Phase, size, and published outcomes")
        else:
            proposed_tier = "D"
            proposed_status = "draft"
            confidence = "medium"
            rationale_parts.append(
                "Insufficient extracted clinical evidence for the agent–condition pair "
                "(Preliminary tracker level)."
            )
            gaps.append("Condition-specific clinical studies")

        trial_bits = []
        for t in trial_summaries[:4]:
            trial_bits.append(
                f"{t.get('nct_id')} ({t.get('status')}, phase={t.get('phase_s')}, "
                f"n={t.get('enrollment')}, relevant={t.get('relevant')})"
            )
        evidence_summary = (
            f"Wave {wave}. Extracted {len(trial_summaries)} registry trial(s) for "
            f"{agent} → {condition}: "
            + ("; ".join(trial_bits) if trial_bits else "none")
            + ". "
            + ("Posted CT.gov results: yes. " if has_results else "No posted CT.gov results in this pass. ")
            + (f"Literature notes: {'; '.join(lit_bits[:3])}. " if lit_bits else "")
            + (
                f"Europe PMC query `{search.get('query')}` → {search.get('hit_count')} hits. "
                if search
                else "No agent+condition Europe PMC search (wave B/C budget). "
            )
            + "Honest bar: Preliminary claims stay D/C unless a clear multi-source clinical "
            "package is present (not claimed here without verified supportive endpoints)."
        )

    if not gaps:
        gaps.append("Not a systematic review; single-pass registry + selective literature sampling")

    return {
        "claim_id": claim_id,
        "agent": agent,
        "condition": condition,
        "wave": wave,
        "references": refs,
        "evidence_summary": evidence_summary,
        "proposed_tier": proposed_tier,
        "proposed_status": proposed_status,
        "rationale": " ".join(rationale_parts),
        "confidence": confidence,
        "gaps": gaps,
        "eval_date": EVAL_DATE,
        "prior_tier": claim.get("current_tier"),
        "prior_status": claim.get("status"),
    }


def confidence_ok_for_publish(has_results: bool, n_pub_pmids: int, max_phase: int) -> bool:
    """Publish only when medium+ confidence refs can stand behind the claim."""
    if has_results and n_pub_pmids >= 1:
        return True
    if n_pub_pmids >= 2 and max_phase >= 2:
        return True
    if has_results and max_phase >= 3:
        return True
    return False


def apply_to_claim_file(ev: dict) -> bool:
    claim_id = ev["claim_id"]
    slug = claim_id.replace("osmf:claim:", "")
    path = CLAIMS_DIR / f"{slug}.json"
    if not path.exists():
        print("MISSING claim file", path)
        return False

    # Publish gate: only when confidence medium+ AND status proposed published
    conf = ev["confidence"]
    apply_status = ev["proposed_status"]
    apply_tier = ev["proposed_tier"]
    if apply_status == "published" and conf not in ("medium", "high"):
        apply_status = "draft"

    data = json.loads(path.read_text())
    data["evidence_tier"] = apply_tier
    data["status"] = apply_status

    ref_bits = []
    for r in ev["references"][:6]:
        if r["type"] == "nct":
            ref_bits.append(f"{r['id']} ({r.get('status')})")
        elif r["type"] == "pmid":
            ref_bits.append(f"PMID:{r['id']}")
    ref_str = ", ".join(ref_bits) if ref_bits else "see evidence JSONL"

    limitations = (
        f"Key refs: {ref_str}. "
        f"Evaluated from extracted references on {EVAL_DATE} (Preliminary wave {ev.get('wave')}); "
        f"not a systematic review. {ev['rationale']} "
        "Not medical advice. Tracker Preliminary label is not an OSMF A/B grade."
    )
    data["limitations"] = limitations.strip()
    data["reviewed_by"] = REVIEWED_BY
    data["reviewed_at"] = EVAL_ISO
    data["confidence_notes"] = (
        f"[{conf}] wave={ev.get('wave')} {ev['rationale']} | {ev['evidence_summary'][:400]}"
    )

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


def write_markdown(evals: list[dict], queue: list[dict]) -> None:
    by_tier: dict[str, list] = {"A": [], "B": [], "C": [], "D": []}
    for e in evals:
        by_tier.setdefault(e["proposed_tier"], []).append(e)

    wave_counts = Counter(e.get("wave") for e in evals)
    prior_tiers = Counter(e.get("prior_tier") for e in evals)
    after_tiers = Counter(e["proposed_tier"] for e in evals)
    pub = sum(1 for e in evals if e["proposed_status"] == "published")

    lines = []
    lines.append("# Preliminary agents — evidence evaluation report")
    lines.append("")
    lines.append(f"**Date:** {EVAL_DATE} (America/Edmonton / MDT)")
    lines.append(f"**Evaluator:** {REVIEWED_BY}")
    lines.append(f"**Queue size:** {len(evals)} claims")
    lines.append(f"**Waves:** A={wave_counts.get('A',0)}, B={wave_counts.get('B',0)}, C={wave_counts.get('C',0)}")
    lines.append("")
    lines.append("## Tier distribution")
    lines.append("")
    lines.append(f"- **Before:** {dict(prior_tiers)}")
    lines.append(f"- **After:** {dict(after_tiers)}")
    lines.append(f"- **Published after:** {pub}")
    lines.append("")
    for t in "ABCD":
        items = by_tier.get(t) or []
        pub_t = sum(1 for x in items if x["proposed_status"] == "published")
        draft = sum(1 for x in items if x["proposed_status"] == "draft")
        lines.append(f"- **{t}**: {len(items)} (published={pub_t}, draft={draft})")
    lines.append("")
    lines.append("## Method")
    lines.append("")
    lines.append(
        "Match graph `treats_candidate_for` claims whose subject agent label is in Tracker "
        "Evidence Level == Preliminary. Skip claims already covered by Moderate eval / "
        "published-13 deepdive / phase3 chase. "
        "**Wave A (deep):** COMPLETED Phase 2/3/4 or NCT `hasResults` → CT.gov API v2 + "
        "Europe PMC NCT publication search (+ agent+condition search). "
        "**Wave B (standard):** remaining NCT → study record; PubMed/Europe PMC only if "
        "title/status suggests published results. "
        "**Wave C (light):** no usable NCT → keep D draft. "
        "Honest bar: almost all stay D or C; A/B only for clear multi-source clinical packages "
        "(none expected for Preliminary). Publish only when confidence medium+ and refs support "
        "standing behind the claim."
    )
    lines.append("")

    upgrades = [e for e in evals if e["proposed_tier"] in ("A", "B")]
    to_c = [
        e
        for e in evals
        if e["proposed_tier"] == "C" and (e.get("prior_tier") or "D") == "D"
    ]
    stay_d = [e for e in evals if e["proposed_tier"] == "D"]
    lines.append("## Notable upgrades / downgrades")
    lines.append("")
    if upgrades:
        for e in upgrades:
            lines.append(
                f"- UPGRADE {e['agent']} → {e['condition']}: **{e['proposed_tier']}** — "
                f"{e['rationale'][:160]}"
            )
    else:
        lines.append("- No A/B upgrades (honest: no verified solid multi-source clinical packages).")
    lines.append(f"- Upgrades D→C: {len(to_c)}")
    lines.append(f"- Remain D: {len(stay_d)}")
    pub_list = [e for e in evals if e["proposed_status"] == "published"]
    lines.append(f"- Newly/confirmed published: {len(pub_list)}")
    for e in pub_list[:30]:
        lines.append(
            f"  - {e['agent']} → {e['condition']} (tier {e['proposed_tier']}, wave {e.get('wave')})"
        )
    if len(pub_list) > 30:
        lines.append(f"  - … +{len(pub_list)-30} more")
    lines.append("")

    lines.append("## Wave A deep-dive highlights")
    lines.append("")
    for e in [x for x in evals if x.get("wave") == "A"][:40]:
        lines.append(
            f"- **{e['agent']} → {e['condition']}**: tier {e['proposed_tier']}/"
            f"{e['proposed_status']} — {e['rationale'][:140]}"
        )
    lines.append("")

    for t in "ABCD":
        items = by_tier.get(t) or []
        if not items:
            continue
        lines.append(f"## Tier {t}")
        lines.append("")
        # Cap per-tier detail to keep MD readable; full detail in JSONL
        show = items if t in ("A", "B") or len(items) <= 80 else items[:60]
        for e in show:
            lines.append(f"### {e['agent']} → {e['condition']}")
            lines.append(f"- **claim_id:** `{e['claim_id']}`")
            lines.append(
                f"- **proposed:** tier {e['proposed_tier']}, status `{e['proposed_status']}`, "
                f"confidence `{e['confidence']}`, wave `{e.get('wave')}`"
            )
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
                lines.append(
                    f"  - [{r['type']}] {r.get('id','')} — {(r.get('title') or '')[:100]}{extra_s}"
                )
            lines.append("")
        if len(items) > len(show):
            lines.append(f"_… {len(items)-len(show)} additional tier-{t} claims in JSONL only._")
            lines.append("")

    MD_PATH.write_text("\n".join(lines) + "\n")


def save_progress(**kwargs) -> None:
    data = {"updated_at": EVAL_ISO, **kwargs}
    PROGRESS_PATH.write_text(json.dumps(data, indent=2) + "\n")


def main() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)

    print("Building Preliminary queue...")
    queue = build_queue()
    QUEUE_PATH.write_text(json.dumps(queue, indent=2) + "\n")
    wave_counts = Counter(c["wave"] for c in queue)
    print(f"Queue: {len(queue)} claims | waves {dict(wave_counts)}")
    save_progress(phase="queue", total=len(queue), waves=dict(wave_counts))

    # Collect NCTs
    nct_ids = sorted(
        {t["nct_id"] for c in queue for t in (c.get("trials") or []) if t.get("nct_id")}
    )
    print(f"Fetching {len(nct_ids)} unique NCTs (cached when present)...")
    nct_data: dict[str, dict] = {}
    for i, nct in enumerate(nct_ids):
        nct_data[nct] = fetch_nct(nct)
        if (i + 1) % 25 == 0:
            print(f"  NCT {i+1}/{len(nct_ids)}")
            save_progress(phase="nct_fetch", done=i + 1, total=len(nct_ids))
    print("NCT fetch done")

    # Promote Wave B → A when API shows has_results or completed P2+
    promoted = 0
    for c in queue:
        if c["wave"] != "B":
            continue
        for t in c.get("trials") or []:
            n = nct_data.get(t["nct_id"])
            if n and is_wave_a_trial(t, n):
                c["wave"] = "A"
                promoted += 1
                break
    # re-sort
    wave_ord = {"A": 0, "B": 1, "C": 2}
    queue.sort(
        key=lambda c: (wave_ord.get(c["wave"], 9), c["agent"].lower(), c["condition"].lower())
    )
    QUEUE_PATH.write_text(json.dumps(queue, indent=2) + "\n")
    wave_counts = Counter(c["wave"] for c in queue)
    print(f"After promotion: waves {dict(wave_counts)} (promoted {promoted})")

    # Wave A: Europe PMC NCT pubs + agent/condition search
    # Wave B: selective pubs when title suggests results
    nct_pubs: dict[str, dict] = {}
    pmid_data: dict[str, dict] = {}
    searches: dict[str, dict] = {}

    wave_a_ncts = set()
    wave_b_selective_ncts = set()
    for c in queue:
        for t in c.get("trials") or []:
            nct_id = t.get("nct_id")
            if not nct_id:
                continue
            n = nct_data.get(nct_id) or {}
            if c["wave"] == "A":
                wave_a_ncts.add(nct_id)
            elif c["wave"] == "B" and title_suggests_published_results(
                n.get("title") or t.get("title") or "", n
            ):
                wave_b_selective_ncts.add(nct_id)

    print(f"Europe PMC NCT pubs: Wave A={len(wave_a_ncts)}, Wave B selective={len(wave_b_selective_ncts)}")
    for i, nct_id in enumerate(sorted(wave_a_ncts | wave_b_selective_ncts)):
        nct_pubs[nct_id] = search_europepmc_nct(nct_id)
        for paper in (nct_pubs[nct_id].get("papers") or [])[:5]:
            pmid = paper.get("pmid")
            if pmid and str(pmid).isdigit() and str(pmid) not in pmid_data:
                pmid_data[str(pmid)] = fetch_pmid(str(pmid))
        if (i + 1) % 20 == 0:
            print(f"  NCT pubs {i+1}/{len(wave_a_ncts | wave_b_selective_ncts)}")

    # Prefetch tracker study PMIDs
    pmid_set = set()
    for c in queue:
        for s in c.get("studies") or []:
            if isinstance(s, dict) and s.get("pmid"):
                pmid_set.add(str(s["pmid"]))
    print(f"Fetching {len(pmid_set)} tracker study PMIDs...")
    for pmid in sorted(pmid_set):
        pmid_data[pmid] = fetch_pmid(pmid)

    # Wave A agent+condition Europe PMC searches
    wave_a_claims = [c for c in queue if c["wave"] == "A"]
    print(f"Wave A agent+condition searches: {len(wave_a_claims)}")
    for i, claim in enumerate(wave_a_claims):
        agent_q = agent_search_name(claim["agent"])
        cond_q = " OR ".join(condition_search_terms(claim["condition"]))
        query = f"({agent_q}) AND ({cond_q})"
        if len(agent_q) < 4:
            query = f"\"{claim['agent']}\" AND ({cond_q})"
        search = europepmc_search(query, page_size=5)
        searches[claim["claim_id"]] = search
        for h in search.get("hits") or []:
            if h.get("pmid") and str(h["pmid"]) not in pmid_data:
                pmid_data[str(h["pmid"])] = fetch_pmid(str(h["pmid"]))
        if (i + 1) % 10 == 0:
            print(f"  search {i+1}/{len(wave_a_claims)}")

    # Wave B selective agent searches only when we already selected NCT pubs
    wave_b_selective_claims = [
        c
        for c in queue
        if c["wave"] == "B"
        and any(t.get("nct_id") in wave_b_selective_ncts for t in (c.get("trials") or []))
    ]
    print(f"Wave B selective agent searches: {len(wave_b_selective_claims)}")
    for i, claim in enumerate(wave_b_selective_claims):
        agent_q = agent_search_name(claim["agent"])
        cond_q = " OR ".join(condition_search_terms(claim["condition"]))
        query = f"({agent_q}) AND ({cond_q})"
        search = europepmc_search(query, page_size=5)
        searches[claim["claim_id"]] = search
        for h in search.get("hits") or []:
            if h.get("pmid") and str(h["pmid"]) not in pmid_data:
                pmid_data[str(h["pmid"])] = fetch_pmid(str(h["pmid"]))

    # Evaluate all
    evals = []
    for i, claim in enumerate(queue):
        search = searches.get(claim["claim_id"])
        ev = evaluate_claim(claim, nct_data, pmid_data, search, nct_pubs)
        # keep wave from (possibly promoted) queue
        ev["wave"] = claim["wave"]
        evals.append(ev)
        if (i + 1) % 50 == 0:
            print(
                f"[{i+1}/{len(queue)}] last={ev['agent'][:30]} → "
                f"{ev['proposed_tier']}/{ev['proposed_status']}"
            )
            save_progress(phase="eval", done=i + 1, total=len(queue))

    with open(JSONL_PATH, "w") as f:
        for e in evals:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print("Wrote", JSONL_PATH)

    write_markdown(evals, queue)
    print("Wrote", MD_PATH)

    n_ok = 0
    for e in evals:
        if apply_to_claim_file(e):
            n_ok += 1
    print(f"Updated {n_ok} claim files")

    print("Tiers:", Counter(e["proposed_tier"] for e in evals))
    print("Status:", Counter(e["proposed_status"] for e in evals))
    print("Confidence:", Counter(e["confidence"] for e in evals))
    print("Waves:", Counter(e.get("wave") for e in evals))
    save_progress(
        phase="done",
        total=len(evals),
        tiers=dict(Counter(e["proposed_tier"] for e in evals)),
        status=dict(Counter(e["proposed_status"] for e in evals)),
        waves=dict(Counter(e.get("wave") for e in evals)),
        published=sum(1 for e in evals if e["proposed_status"] == "published"),
    )


if __name__ == "__main__":
    main()
