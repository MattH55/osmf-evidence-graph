#!/usr/bin/env python3
"""Chase posted CT.gov / PubMed results for draft Moderate-agent Phase3 claims."""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GRAPH = Path("/workspace/osmf-evidence-graph")
REVIEW = GRAPH / "review"
CACHE = REVIEW / "cache"
CLAIMS_DIR = GRAPH / "data" / "claims"
EVIDENCE = REVIEW / "moderate-agents-evidence.jsonl"
OUT_JSONL = REVIEW / "phase3-draft-results-chase.jsonl"
OUT_MD = REVIEW / "phase3-draft-results-chase.md"

USER_AGENT = "OSMF-EvidenceChase/1.0 (research; contact: opensourcemed.info)"
CHASE_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CHASE_DATE = "2026-09-19"
REVIEWED_BY = "evidence-chase-bot"

# Explicit "Phase 3 completed but results missing" from prior eval report +
# completed Phase2+/pivotal drafts called out similarly.
PRIORITY_CLAIM_IDS = {
    "osmf:claim:agent-compound-ciwujia-granules-guipi-granules-treats-me-cfs",
    "osmf:claim:agent-fluvoxamine-treats-me-cfs",
    "osmf:claim:agent-gcjbp-laennec-inj-treats-me-cfs",
    "osmf:claim:agent-hyperbaric-oxygen-therapy-hbot-treats-long-covid",
    "osmf:claim:agent-hyperbaric-oxygen-therapy-hbot-treats-me-cfs",
    "osmf:claim:agent-immulina-tm-treats-long-covid",
    "osmf:claim:agent-ivabradine-treats-long-covid",
    "osmf:claim:agent-metformin-treats-me-cfs",
    "osmf:claim:agent-pycnogenol-treats-long-covid",
    "osmf:claim:agent-regenecyte-treats-long-covid",
    "osmf:claim:agent-remdesivir-treats-long-covid",
    "osmf:claim:agent-solriamfetol-oral-tablet-sunosi-treats-me-cfs",
    "osmf:claim:agent-testofen-treats-long-covid",
    "osmf:claim:agent-thiamine-vitamin-b1-treats-long-covid",
    "osmf:claim:agent-sildenafil-treats-me-cfs",
    "osmf:claim:agent-sodium-oxybate-treats-me-cfs",
}


def http_get_json(url: str, timeout: int = 60) -> Any:
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_get_text(url: str, timeout: int = 60) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def is_phase3ish(phases: list | str | None) -> bool:
    if not phases:
        return False
    if isinstance(phases, str):
        phases = [phases]
    joined = ",".join(phases).upper().replace(" ", "")
    return any(x in joined for x in ("PHASE3", "PHASE4", "PHASE2,PHASE3", "PHASE2/PHASE3"))


def load_evidence() -> list[dict]:
    rows = []
    with EVIDENCE.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def claim_path(claim_id: str) -> Path:
    slug = claim_id.replace("osmf:claim:", "")
    return CLAIMS_DIR / f"{slug}.json"


def load_claim(claim_id: str) -> dict | None:
    p = claim_path(claim_id)
    if not p.exists():
        return None
    return json.loads(p.read_text())


def extract_ncts_from_claim_and_evidence(claim: dict, ev: dict) -> list[str]:
    ncts = []
    for s in claim.get("sources") or []:
        if s.get("type") == "nct" and s.get("value"):
            ncts.append(s["value"].upper())
    for r in ev.get("references") or []:
        if r.get("type") == "nct" and r.get("id"):
            ncts.append(r["id"].upper())
    # dedupe preserve order
    seen = set()
    out = []
    for n in ncts:
        if n not in seen and re.match(r"^NCT\d+$", n):
            seen.add(n)
            out.append(n)
    return out


def summarize_results_section(raw: dict) -> dict:
    """Extract primary/secondary outcome summaries + p-values when present."""
    out: dict[str, Any] = {
        "has_results_flag": bool(raw.get("hasResults")),
        "has_results_section": bool(raw.get("resultsSection")),
        "primary_outcomes": [],
        "secondary_outcomes_sample": [],
        "arm_groups": [],
        "ae_summary": None,
        "results_first_posted": None,
    }
    status = (raw.get("protocolSection") or {}).get("statusModule") or {}
    rfp = status.get("resultsFirstPostDateStruct") or {}
    out["results_first_posted"] = rfp.get("date")

    rs = raw.get("resultsSection") or {}
    if not rs:
        return out

    # arm labels from outcome groups or participant flow
    om = rs.get("outcomeMeasuresModule") or {}
    measures = om.get("outcomeMeasures") or []
    for m in measures:
        mtype = (m.get("type") or "").upper()
        entry = {
            "title": m.get("title") or "",
            "type": m.get("type"),
            "time_frame": m.get("timeFrame"),
            "unit": m.get("unitOfMeasure"),
            "param_type": m.get("paramType"),
            "dispersion_type": m.get("dispersionType"),
            "groups": [],
            "analyses": [],
        }
        # group labels
        groups = {g.get("id"): g.get("title") for g in (m.get("groups") or [])}
        # measurements
        for cls in m.get("classes") or []:
            for cat in cls.get("categories") or []:
                for meas in cat.get("measurements") or []:
                    gid = meas.get("groupId")
                    entry["groups"].append(
                        {
                            "group": groups.get(gid, gid),
                            "value": meas.get("value"),
                            "spread": meas.get("spread"),
                            "n_analyzed": None,
                        }
                    )
        # denoms for n
        denoms = {}
        for d in m.get("denoms") or []:
            for c in d.get("counts") or []:
                denoms[c.get("groupId")] = c.get("value")
        for g in entry["groups"]:
            # try match by rebuilding — leave n if we can find from denoms via group title reverse
            pass
        # attach n from denoms by iterating groups list with ids
        rebuilt = []
        for cls in m.get("classes") or []:
            for cat in cls.get("categories") or []:
                for meas in cat.get("measurements") or []:
                    gid = meas.get("groupId")
                    rebuilt.append(
                        {
                            "group": groups.get(gid, gid),
                            "group_id": gid,
                            "value": meas.get("value"),
                            "spread": meas.get("spread"),
                            "n_analyzed": denoms.get(gid),
                        }
                    )
        entry["groups"] = rebuilt

        for a in m.get("analyses") or []:
            entry["analyses"].append(
                {
                    "p_value": a.get("pValue"),
                    "p_value_comment": a.get("pValueComment"),
                    "statistical_method": a.get("statisticalMethod"),
                    "param_type": a.get("paramType"),
                    "param_value": a.get("paramValue"),
                    "ci_pct": a.get("ciPctValue"),
                    "ci_lower": a.get("ciLowerLimit"),
                    "ci_upper": a.get("ciUpperLimit"),
                    "groups": a.get("groupIds"),
                }
            )

        if mtype == "PRIMARY" or (m.get("type") or "").lower() == "primary":
            out["primary_outcomes"].append(entry)
        else:
            if len(out["secondary_outcomes_sample"]) < 3:
                out["secondary_outcomes_sample"].append(entry)

    # arm interventions from protocol for context
    arms = ((raw.get("protocolSection") or {}).get("armsInterventionsModule") or {}).get(
        "armGroups"
    ) or []
    out["arm_groups"] = [
        {"label": a.get("label"), "type": a.get("type"), "description": (a.get("description") or "")[:200]}
        for a in arms
    ]

    ae = rs.get("adverseEventsModule") or {}
    if ae:
        out["ae_summary"] = {
            "frequency_threshold": ae.get("frequencyThreshold"),
            "time_frame": ae.get("timeFrame"),
            "n_serious_events": len(ae.get("seriousEvents") or []),
            "n_other_events": len(ae.get("otherEvents") or []),
        }
    return out


def fetch_nct_fresh(nct_id: str) -> dict:
    """Always hit API (force refresh). Cache full raw + summary."""
    url = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}?format=json"
    try:
        raw = http_get_json(url)
    except Exception as e:
        return {
            "nct_id": nct_id,
            "fetch_ok": False,
            "error": str(e),
            "url": f"https://clinicaltrials.gov/study/{nct_id}",
        }

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

    results_summary = summarize_results_section(raw)
    has_results = bool(
        raw.get("hasResults")
        or status.get("resultsFirstPostDateStruct")
        or raw.get("resultsSection")
    )

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
        "brief_summary": (desc.get("briefSummary") or "")[:800],
        "url": f"https://clinicaltrials.gov/study/{nct_id}",
        "fetch_ok": True,
        "results": results_summary,
        "fetched_at": CHASE_ISO,
    }
    # cache summary (not full raw — keep size manageable)
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / f"nct_{nct_id}.json").write_text(json.dumps(out, indent=2))
    (CACHE / f"nct_{nct_id}_results.json").write_text(
        json.dumps(results_summary, indent=2)
    )
    return out


def search_europepmc_nct(nct_id: str, limit: int = 8) -> dict:
    key = f"epmc_nct_{nct_id}.json"
    cached_path = CACHE / key
    # allow short reuse within same chase if present with matching chase marker
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
                    "is_preprint": bool(h.get("isPreprint") or (h.get("source") == "PPR")),
                    "author_string": (h.get("authorString") or "")[:120],
                }
            )
        out = {
            "nct_id": nct_id,
            "hit_count": data.get("hitCount"),
            "papers": papers,
            "url": f"https://europepmc.org/search?query=%22{nct_id}%22",
            "fetch_ok": True,
            "fetched_at": CHASE_ISO,
        }
    except Exception as e:
        out = {"nct_id": nct_id, "fetch_ok": False, "error": str(e), "papers": []}
    CACHE.mkdir(parents=True, exist_ok=True)
    cached_path.write_text(json.dumps(out, indent=2))
    return out


def search_pubmed_nct(nct_id: str, limit: int = 8) -> dict:
    """NCBI esearch + esummary for NCT string."""
    try:
        term = urllib.parse.quote(f"{nct_id}[Secondary Source ID] OR {nct_id}[Title/Abstract]")
        esearch = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            f"?db=pubmed&retmode=json&retmax={limit}&term={term}"
        )
        es = http_get_json(esearch)
        ids = (es.get("esearchresult") or {}).get("idlist") or []
        count = int((es.get("esearchresult") or {}).get("count") or 0)
        papers = []
        if ids:
            idstr = ",".join(ids)
            esum = (
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
                f"?db=pubmed&retmode=json&id={idstr}"
            )
            time.sleep(0.35)  # be polite to NCBI
            sm = http_get_json(esum)
            result = sm.get("result") or {}
            for pid in ids:
                r = result.get(pid) or {}
                papers.append(
                    {
                        "pmid": pid,
                        "title": r.get("title"),
                        "year": (r.get("pubdate") or "")[:4],
                        "journal": r.get("fulljournalname") or r.get("source"),
                        "doi": next(
                            (
                                x.get("value")
                                for x in (r.get("articleids") or [])
                                if x.get("idtype") == "doi"
                            ),
                            None,
                        ),
                    }
                )
        out = {
            "nct_id": nct_id,
            "hit_count": count,
            "papers": papers,
            "fetch_ok": True,
            "fetched_at": CHASE_ISO,
        }
    except Exception as e:
        out = {"nct_id": nct_id, "fetch_ok": False, "error": str(e), "papers": []}
    (CACHE / f"pubmed_nct_{nct_id}.json").write_text(json.dumps(out, indent=2))
    return out


def prior_had_results(ev: dict, nct_id: str) -> bool | None:
    for r in ev.get("references") or []:
        if r.get("type") == "nct" and r.get("id", "").upper() == nct_id.upper():
            notes = (r.get("notes") or "").lower()
            if "hasresults=true" in notes:
                return True
            if "hasresults=false" in notes or "results not posted" in notes:
                return False
    return None


def format_outcome_brief(o: dict) -> str:
    parts = [o.get("title") or "?"]
    if o.get("groups"):
        gbits = []
        for g in o["groups"][:4]:
            bit = f"{g.get('group')}: {g.get('value')}"
            if g.get("spread"):
                bit += f"±{g['spread']}"
            if g.get("n_analyzed"):
                bit += f" (n={g['n_analyzed']})"
            gbits.append(bit)
        parts.append("; ".join(gbits))
    if o.get("analyses"):
        a = o["analyses"][0]
        if a.get("p_value") is not None:
            parts.append(f"p={a['p_value']}")
        if a.get("statistical_method"):
            parts.append(str(a["statistical_method"]))
    return " — ".join(parts)


def decide_update(
    claim: dict,
    ev: dict,
    nct_data: list[dict],
    pubs: dict[str, dict],
) -> dict:
    """Propose claim field updates. Never invent A/B; B only if solid published package."""
    claim_id = claim["id"]
    agent = ev.get("agent") or ""
    condition = ev.get("condition") or ""
    old_tier = claim.get("evidence_tier")
    old_status = claim.get("status")

    new_results = [n for n in nct_data if n.get("has_results")]
    completed_p3 = [
        n
        for n in nct_data
        if (n.get("status") or "").upper() == "COMPLETED" and is_phase3ish(n.get("phases"))
    ]
    completed_any = [n for n in nct_data if (n.get("status") or "").upper() == "COMPLETED"]

    # Collect relevant publications citing NCTs
    relevant_pmids = []
    pub_notes = []
    for nct, pdata in pubs.items():
        for src in ("europepmc", "pubmed"):
            block = pdata.get(src) or {}
            for p in block.get("papers") or []:
                title = (p.get("title") or "").lower()
                # filter obvious off-target reviews that merely mention NCT in passing later manually
                pmid = str(p.get("pmid") or "")
                if pmid and pmid not in relevant_pmids:
                    relevant_pmids.append(pmid)
                    pub_notes.append(
                        f"PMID {pmid} ({p.get('year')}): {(p.get('title') or '')[:100]}"
                    )

    findings_bits = []
    for n in nct_data:
        if not n.get("fetch_ok"):
            findings_bits.append(f"{n['nct_id']}: fetch failed ({n.get('error')})")
            continue
        bit = f"{n['nct_id']}: {n.get('status')} phase={','.join(n.get('phases') or [])} enroll={n.get('enrollment')} has_results={n.get('has_results')}"
        if n.get("has_results"):
            rs = n.get("results") or {}
            bit += f" results_posted={rs.get('results_first_posted')}"
            for po in (rs.get("primary_outcomes") or [])[:2]:
                bit += f" | PRIMARY: {format_outcome_brief(po)[:220]}"
        findings_bits.append(bit)

    # Tier policy: stay conservative
    new_tier = old_tier
    new_status = old_status
    tier_change = False
    status_change = False
    rationale_parts = []

    # Special cases from prior eval
    agent_l = agent.lower()
    if agent_l in ("angiotensin converting enzyme inhibitor", "angiotensin ii receptor blockers"):
        new_tier = "D"
        rationale_parts.append("Class-level ACEI/ARB claim — not drug-specific.")
    elif "vaccine" in agent_l:
        new_tier = "D"
        rationale_parts.append("Vaccine prevention ≠ treatment of established Long COVID.")
    elif "microcrystalline cellulose" in agent_l:
        new_tier = "D"
        rationale_parts.append("Placebo/excipient label, not a therapeutic.")

    # Analyze results content for supportive vs negative vs empty
    supportive_signal = False
    negative_signal = False
    posted_but_thin = False

    for n in new_results:
        rs = n.get("results") or {}
        primaries = rs.get("primary_outcomes") or []
        if not primaries:
            posted_but_thin = True
            continue
        for po in primaries:
            analyses = po.get("analyses") or []
            groups = po.get("groups") or []
            # Heuristic: look at p-values
            for a in analyses:
                try:
                    pv = float(str(a.get("p_value")).replace("<", "").strip())
                    if pv < 0.05:
                        supportive_signal = True
                    elif pv >= 0.05:
                        negative_signal = True
                except Exception:
                    pass
            # If values posted without analyses — thin
            if groups and not analyses:
                posted_but_thin = True

    # Known small completed with results already (sildenafil, sodium oxybate)
    small_n = all((n.get("enrollment") or 999) < 50 for n in completed_any) if completed_any else False

    if new_results:
        rationale_parts.append(
            f"{len(new_results)} NCT(s) now have CT.gov results modules: "
            + ", ".join(n["nct_id"] for n in new_results)
        )
        if supportive_signal and not small_n:
            # Still not B without peer-reviewed multi-trial package
            new_tier = "C"
            # Could publish if condition-relevant completed results exist
            if any(
                condition_relevant(n, condition) for n in new_results
            ):
                # Keep draft unless peer-reviewed package is clear — prefer draft→published only for clear curated signal
                new_status = "draft"
                rationale_parts.append(
                    "Posted registry outcomes include nominal significance, but no solid multi-trial published clinical package → remain C (not B); status stays draft pending peer-reviewed primary curation."
                )
        elif negative_signal:
            new_tier = "D" if old_tier in ("C", "D") else old_tier
            rationale_parts.append("Posted results suggest null/negative primary → D or retain contested.")
        elif posted_but_thin or small_n:
            new_tier = "C"
            rationale_parts.append(
                "Results module present but thin (no inferential stats and/or very small n) → remain C draft."
            )
        else:
            new_tier = "C"
            rationale_parts.append("Results posted; early clinical signal only → C draft, not B.")
    else:
        # Still no results
        if completed_p3:
            rationale_parts.append(
                "Completed Phase 3/4 trial(s) still lack posted CT.gov results modules."
            )
            new_tier = old_tier or "C"
            new_status = "draft"
        else:
            rationale_parts.append("No new posted CT.gov results for linked NCTs in this chase.")

    # Publications: if we find a clear peer-reviewed primary for the NCT, enrich sources;
    # upgrade to published only when we have a clear peer-reviewed efficacy package (still not B lightly)
    # Manual overrides applied after automated pass in main().

    if new_tier != old_tier:
        tier_change = True
    if new_status != old_status:
        status_change = True

    # Build richer sources: keep osmf_page, add NCTs, add best PMIDs (limit)
    sources = []
    seen = set()
    for s in claim.get("sources") or []:
        key = (s.get("type"), s.get("value"))
        if key not in seen:
            seen.add(key)
            sources.append(s)
    for n in nct_data:
        key = ("nct", n["nct_id"])
        if key not in seen and n.get("fetch_ok"):
            seen.add(key)
            label = n.get("title") or n["nct_id"]
            if n.get("has_results"):
                label += " (results posted)"
            sources.append({"type": "nct", "value": n["nct_id"], "label": label[:180]})
    # add up to 5 new pmids from searches that look on-target
    added_pmids = 0
    for nct, pdata in pubs.items():
        for block in ((pdata.get("pubmed") or {}), (pdata.get("europepmc") or {})):
            for p in block.get("papers") or []:
                pmid = str(p.get("pmid") or "")
                if not pmid or not pmid.isdigit():
                    continue
                key = ("pmid", pmid)
                if key in seen:
                    continue
                title = p.get("title") or ""
                if not title_looks_relevant(title, agent, condition):
                    continue
                seen.add(key)
                sources.append(
                    {
                        "type": "pmid",
                        "value": pmid,
                        "label": f"{title[:120]} ({p.get('year') or ''})".strip(),
                    }
                )
                added_pmids += 1
                if added_pmids >= 5:
                    break
            if added_pmids >= 5:
                break
        if added_pmids >= 5:
            break

    limitations = build_limitations(
        claim, ev, nct_data, new_results, completed_p3, rationale_parts
    )
    confidence_notes = (
        f"[{CHASE_DATE} chase] "
        + " ".join(rationale_parts)
        + " | "
        + " || ".join(findings_bits)[:1500]
    )

    return {
        "claim_id": claim_id,
        "agent": agent,
        "condition": condition,
        "old_tier": old_tier,
        "new_tier": new_tier,
        "old_status": old_status,
        "new_status": new_status,
        "tier_changed": tier_change,
        "status_changed": status_change,
        "ncts_chased": [n["nct_id"] for n in nct_data],
        "ncts_with_new_or_any_results": [n["nct_id"] for n in new_results],
        "ncts_completed_phase3ish": [n["nct_id"] for n in completed_p3],
        "findings": findings_bits,
        "pub_notes": pub_notes[:12],
        "rationale": " ".join(rationale_parts),
        "proposed_sources": sources,
        "proposed_limitations": limitations,
        "proposed_confidence_notes": confidence_notes[:4000],
        "updated_claim_fields": {
            "evidence_tier": new_tier,
            "status": new_status,
            "sources": sources,
            "limitations": limitations,
            "confidence_notes": confidence_notes[:4000],
            "reviewed_by": REVIEWED_BY,
            "reviewed_at": CHASE_ISO,
        },
    }


def condition_relevant(nct: dict, condition: str) -> bool:
    blob = " ".join(
        [
            nct.get("title") or "",
            " ".join(nct.get("conditions") or []),
            nct.get("brief_summary") or "",
        ]
    ).lower()
    c = condition.lower()
    if "long covid" in c or "pasc" in c:
        return any(x in blob for x in ("long covid", "post-covid", "post covid", "pasc", "post-acute"))
    if "me/cfs" in c or "chronic fatigue" in c:
        return any(
            x in blob
            for x in ("chronic fatigue", "me/cfs", "myalgic", "cfs")
        )
    if "gulf war" in c:
        return "gulf" in blob
    return True


def title_looks_relevant(title: str, agent: str, condition: str) -> bool:
    t = title.lower()
    # reject obvious off-target mega-reviews unless agent+condition both present
    agent_tokens = [w for w in re.split(r"[^a-z0-9]+", agent.lower()) if len(w) > 3][:3]
    cond_l = condition.lower()
    agent_hit = any(tok in t for tok in agent_tokens) if agent_tokens else True
    if "long covid" in cond_l:
        cond_hit = any(x in t for x in ("long covid", "post-covid", "pasc", "post covid"))
    elif "me/cfs" in cond_l or "chronic fatigue" in cond_l:
        cond_hit = any(x in t for x in ("chronic fatigue", "me/cfs", "myalgic", "cfs"))
    else:
        cond_hit = True
    # accept if NCT-primary-looking clinical trial title with agent
    if agent_hit and cond_hit:
        return True
    if agent_hit and any(x in t for x in ("randomized", "randomised", "phase 3", "phase3", "trial")):
        return True
    return False


def build_limitations(claim, ev, nct_data, new_results, completed_p3, rationale_parts) -> str:
    bits = []
    bits.append(
        "Results chase "
        + CHASE_DATE
        + " (CT.gov API v2 + PubMed/Europe PMC NCT citation search); not a systematic review."
    )
    if completed_p3 and not new_results:
        bits.append(
            "Completed Phase 3/4 NCT(s) "
            + ", ".join(n["nct_id"] for n in completed_p3)
            + " still without posted results modules → cannot support tier B."
        )
    if new_results:
        bits.append(
            "Posted results on "
            + ", ".join(n["nct_id"] for n in new_results)
            + " may be registry-only without peer-reviewed primary; interpret cautiously."
        )
    bits.append("Not medical advice. Tracker Moderate label is not an OSMF A/B grade.")
    bits.append(" ".join(rationale_parts)[:500])
    return " ".join(bits)[:2000]


def select_chase_targets(rows: list[dict]) -> list[dict]:
    """Draft claims with completed P3/pivotal OR priority list OR any draft NCT to scan for new results."""
    targets = []
    for ev in rows:
        if ev.get("proposed_status") != "draft" and ev.get("claim_id") not in PRIORITY_CLAIM_IDS:
            # Only draft
            claim = load_claim(ev["claim_id"])
            if not claim or claim.get("status") != "draft":
                continue
        claim = load_claim(ev["claim_id"])
        if not claim:
            continue
        if claim.get("status") != "draft":
            continue
        nct_refs = [r for r in (ev.get("references") or []) if r.get("type") == "nct"]
        completed_p3 = False
        for r in nct_refs:
            st = (r.get("status") or "").upper()
            ph = (r.get("phase") or "").upper()
            if st == "COMPLETED" and is_phase3ish(ph):
                completed_p3 = True
        rationale = (ev.get("rationale") or "").lower()
        missing_flag = "results not found" in rationale or "cannot support b" in rationale
        priority = ev["claim_id"] in PRIORITY_CLAIM_IDS
        # Include: priority OR (draft + completed p3) OR (draft + missing results language)
        # Also include other drafts so we can detect newly posted results modules
        include = priority or completed_p3 or missing_flag
        # Broaden: all draft moderate claims with at least one COMPLETED trial
        any_completed = any((r.get("status") or "").upper() == "COMPLETED" for r in nct_refs)
        if any_completed:
            include = True
        if include:
            targets.append({"evidence": ev, "claim": claim})
    # dedupe by claim_id
    seen = set()
    out = []
    for t in targets:
        cid = t["claim"]["id"]
        if cid not in seen:
            seen.add(cid)
            out.append(t)
    return out


def apply_manual_overrides(decision: dict, nct_data: list[dict], pubs: dict) -> dict:
    """Hand-tuned judgments after automated heuristics (still no invented A/B)."""
    cid = decision["claim_id"]

    # Sildenafil ME/CFS: tiny Phase 4 n=12 with results — early C, keep draft
    if cid.endswith("sildenafil-treats-me-cfs"):
        decision["new_tier"] = "C"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "NCT00598585 completed Phase 4 (n=12) with posted FIS primary results; "
            "very small single-center signal only → C draft, not B."
        )

    # Sodium oxybate: n=13 Phase 4 with results — C draft
    if cid.endswith("sodium-oxybate-treats-me-cfs"):
        decision["new_tier"] = "C"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "NCT02055898 completed Phase 4 (n=13) with posted results; tiny n → C draft, not B."
        )

    # Fluvoxamine→ME/CFS: linked trials are Long COVID / acute COVID — off-target for ME/CFS claim
    if cid.endswith("fluvoxamine-treats-me-cfs"):
        decision["new_tier"] = "D"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "Linked completed Phase 3 trials (NCT05874037, NCT06128967, NCT04510194) target Long COVID or acute COVID, "
            "not ME/CFS treatment; no ME/CFS-specific Phase 3 package → D draft."
        )

    # Metformin→ME/CFS: same off-target issue
    if cid.endswith("metformin-treats-me-cfs"):
        decision["new_tier"] = "D"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "Linked Phase 3 NCTs are COVID-OUT / REVIVE (Long COVID / acute COVID contexts), not ME/CFS-specific → D draft."
        )

    # HBOT Long COVID: Phase 2 completed NCT04842448 often cited in literature — check pubs
    if cid.endswith("hbot-treats-long-covid") or "hyperbaric-oxygen-therapy-hbot-treats-long-covid" in cid:
        # Keep C draft unless we find solid multi-trial — literature exists but not upgrading to B
        decision["new_tier"] = "C"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "NCT04842448 (Phase 2, n=80) completed; Phase 3 NCT06267300 status UNKNOWN without results. "
            "Peer-reviewed HBOT-LC literature exists but not a confirmatory Phase 3 package → C draft, not B."
        )

    # Remdesivir LC: Phase 4 open-label feasibility — early C
    if cid.endswith("remdesivir-treats-long-covid"):
        decision["new_tier"] = "C"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "NCT05911906 completed Phase 4 open-label feasibility (n=73) still without posted results module → C draft."
        )

    # Vaccines / class agents
    if "mrna-covid-19-vaccine" in cid or "moderna-covid-19-vaccine" in cid:
        decision["new_tier"] = "D"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "COVID vaccine trials address prevention/acute infection, not treatment of established Long COVID → D."
        )

    if "angiotensin-converting-enzyme-inhibitor" in cid or "angiotensin-ii-receptor-blockers" in cid:
        decision["new_tier"] = "D"
        decision["new_status"] = "draft"

    if "microcrystalline-cellulose" in cid:
        decision["new_tier"] = "D"
        decision["new_status"] = "draft"

    # Compound Ciwujia: has a Chinese PMID in prior eval — still C draft without English Phase 3 package confirmation
    if "compound-ciwujia" in cid:
        decision["new_tier"] = "C"
        decision["new_status"] = "draft"
        decision["rationale"] = (
            "NCT06245642 completed Phase 4 (n=235); CT.gov results still unposted. "
            "Prior PMID 42543377 appears to be a related Chinese multicenter report — needs full-text confirmation; remain C draft, not B."
        )

    decision["tier_changed"] = decision["new_tier"] != decision["old_tier"]
    decision["status_changed"] = decision["new_status"] != decision["old_status"]
    # refresh updated fields
    u = decision["updated_claim_fields"]
    u["evidence_tier"] = decision["new_tier"]
    u["status"] = decision["new_status"]
    # refresh limitations/confidence with final rationale
    u["limitations"] = (
        f"Results chase {CHASE_DATE} (CT.gov API v2 + PubMed/Europe PMC). "
        + decision["rationale"]
        + " Not a systematic review. Not medical advice. Tracker Moderate label is not an OSMF A/B grade."
    )[:2000]
    u["confidence_notes"] = (
        f"[{CHASE_DATE} chase] {decision['rationale']} | "
        + " || ".join(decision.get("findings") or [])[:1500]
    )[:4000]
    decision["proposed_limitations"] = u["limitations"]
    decision["proposed_confidence_notes"] = u["confidence_notes"]
    return decision


def write_md(decisions: list[dict], nct_fetch_count: int, results_count: int) -> str:
    lines = []
    lines.append("# Phase 3 draft results chase")
    lines.append("")
    lines.append(f"**Date:** {CHASE_DATE} (America/Edmonton)")
    lines.append(f"**Chase UTC:** {CHASE_ISO}")
    lines.append(f"**Bot:** {REVIEWED_BY}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Claims chased: **{len(decisions)}**")
    lines.append(f"- Unique NCTs fetched: **{nct_fetch_count}**")
    lines.append(f"- NCTs with results modules (any): **{results_count}**")
    tier_changes = [d for d in decisions if d.get("tier_changed")]
    status_changes = [d for d in decisions if d.get("status_changed")]
    lines.append(f"- Tier changes: **{len(tier_changes)}**")
    lines.append(f"- Status changes: **{len(status_changes)}**")
    lines.append("- Policy: no invented A/B; B only if solid published clinical evidence package (none applied this pass).")
    lines.append("")
    if tier_changes:
        lines.append("### Tier changes")
        lines.append("")
        lines.append("| Claim | Old → New | Status | Note |")
        lines.append("|---|---|---|---|")
        for d in tier_changes:
            lines.append(
                f"| `{d['claim_id'].replace('osmf:claim:','')}` | {d['old_tier']} → **{d['new_tier']}** | {d['new_status']} | {d['rationale'][:120]} |"
            )
        lines.append("")
    lines.append("## Per-claim findings")
    lines.append("")
    for d in decisions:
        lines.append(f"### {d['agent']} → {d['condition']}")
        lines.append(f"- **claim_id:** `{d['claim_id']}`")
        lines.append(
            f"- **tier/status:** {d['old_tier']}/{d['old_status']} → **{d['new_tier']}/{d['new_status']}**"
            + (" (tier changed)" if d["tier_changed"] else " (tier unchanged)")
        )
        lines.append(f"- **rationale:** {d['rationale']}")
        lines.append(f"- **NCTs chased:** {', '.join(d['ncts_chased']) or '(none)'}")
        if d.get("ncts_with_new_or_any_results"):
            lines.append(
                f"- **Results modules present:** {', '.join(d['ncts_with_new_or_any_results'])}"
            )
        else:
            lines.append("- **Results modules present:** none")
        lines.append("- **CT.gov findings:**")
        for f in d.get("findings") or []:
            lines.append(f"  - {f}")
        if d.get("pub_notes"):
            lines.append("- **Publications citing NCTs (sampled):**")
            for p in d["pub_notes"][:8]:
                lines.append(f"  - {p}")
        lines.append("")
    lines.append("---")
    lines.append("_Not medical advice. Registry postings are not equivalent to peer-reviewed efficacy._")
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = load_evidence()
    targets = select_chase_targets(rows)
    print(f"Targets: {len(targets)}")

    # Collect all NCTs
    all_ncts = []
    for t in targets:
        ncts = extract_ncts_from_claim_and_evidence(t["claim"], t["evidence"])
        all_ncts.extend(ncts)
    unique_ncts = []
    seen = set()
    for n in all_ncts:
        if n not in seen:
            seen.add(n)
            unique_ncts.append(n)
    print(f"Unique NCTs to fetch: {len(unique_ncts)}")

    nct_map: dict[str, dict] = {}
    for i, nct in enumerate(unique_ncts, 1):
        print(f"[{i}/{len(unique_ncts)}] CT.gov {nct}...")
        nct_map[nct] = fetch_nct_fresh(nct)
        time.sleep(0.25)

    # Publications for NCTs that are completed or have results
    pub_map: dict[str, dict] = {}
    for i, nct in enumerate(unique_ncts, 1):
        nd = nct_map[nct]
        if not nd.get("fetch_ok"):
            continue
        st = (nd.get("status") or "").upper()
        if st != "COMPLETED" and not nd.get("has_results"):
            # still search priority completed ones only to save time? Search all completed + has_results
            continue
        print(f"[{i}/{len(unique_ncts)}] Pubs {nct}...")
        epmc = search_europepmc_nct(nct)
        time.sleep(0.2)
        pubmed = search_pubmed_nct(nct)
        time.sleep(0.35)
        pub_map[nct] = {"europepmc": epmc, "pubmed": pubmed}

    decisions = []
    for t in targets:
        claim = t["claim"]
        ev = t["evidence"]
        ncts = extract_ncts_from_claim_and_evidence(claim, ev)
        nct_data = [nct_map[n] for n in ncts if n in nct_map]
        pubs = {n: pub_map[n] for n in ncts if n in pub_map}
        d = decide_update(claim, ev, nct_data, pubs)
        d = apply_manual_overrides(d, nct_data, pubs)
        # ensure updated_claim_fields sources from decide
        decisions.append(d)

    # Apply claim JSON updates
    for d in decisions:
        claim = load_claim(d["claim_id"])
        if not claim:
            continue
        fields = d["updated_claim_fields"]
        claim["evidence_tier"] = fields["evidence_tier"]
        claim["status"] = fields["status"]
        claim["sources"] = fields["sources"]
        claim["limitations"] = fields["limitations"]
        claim["confidence_notes"] = fields["confidence_notes"]
        claim["reviewed_by"] = fields["reviewed_by"]
        claim["reviewed_at"] = fields["reviewed_at"]
        claim_path(d["claim_id"]).write_text(json.dumps(claim, indent=2) + "\n")

    # Write jsonl
    with OUT_JSONL.open("w") as f:
        for d in decisions:
            # slim for jsonl
            row = {k: v for k, v in d.items() if k != "proposed_sources"}
            row["sources_count"] = len(d.get("proposed_sources") or [])
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    results_ncts = sorted({n for d in decisions for n in d.get("ncts_with_new_or_any_results") or []})
    md = write_md(decisions, len(unique_ncts), len(results_ncts))
    OUT_MD.write_text(md)

    print("Wrote", OUT_JSONL)
    print("Wrote", OUT_MD)
    print("NCTs", len(unique_ncts), "with results", len(results_ncts), results_ncts)
    print("Tier changes", sum(1 for d in decisions if d["tier_changed"]))
    for d in decisions:
        if d["tier_changed"] or d["status_changed"] or d.get("ncts_with_new_or_any_results"):
            print(
                f"  {d['claim_id']}: {d['old_tier']}/{d['old_status']}->{d['new_tier']}/{d['new_status']} results={d.get('ncts_with_new_or_any_results')}"
            )


if __name__ == "__main__":
    main()
