#!/usr/bin/env python3
"""Lite rubric scorer for ads-audit. Offline, stdlib only.

Implements references/scoring-system.md exactly, so the numbers are reproducible.
If code execution is unavailable, do the same math by hand with the formulas there.

Input (JSON file path or stdin):
{
  "platforms": [
    {
      "platform": "meta",
      "spend": 12000,                       # same-window spend, optional
      "controls": [
        {"id": "M01", "category": "measurement", "severity": "critical", "result": "pass"},
        {"id": "M28", "category": "creative", "severity": "high", "result": "unknown"}
      ]
    }
  ]
}

Usage: python3 score.py findings.json   (or: cat findings.json | python3 score.py)
Output: JSON with per-platform health, coverage, status and the portfolio score.
"""
import json
import sys

SEVERITY_WEIGHT = {"critical": 5, "high": 3, "medium": 1, "info": 0}
RESULTS = {"pass", "fail", "unknown", "not_applicable"}
CATEGORY_WEIGHTS = {
    "google": {"measurement": 25, "waste": 20, "structure": 15, "keywords": 15, "creative": 15, "settings": 10},
    "meta": {"measurement": 25, "creative": 25, "structure": 20, "audiences": 15, "delivery": 10, "policy": 5},
    "youtube": {"measurement": 25, "creative": 25, "structure": 20, "audiences": 15, "delivery": 10, "policy": 5},
    "linkedin": {"measurement": 25, "audiences": 20, "creative": 20, "structure": 15, "delivery": 15, "policy": 5},
    "tiktok": {"measurement": 25, "creative": 25, "delivery": 15, "structure": 15, "audiences": 15, "policy": 5},
    "microsoft": {"measurement": 25, "structure": 20, "delivery": 15, "creative": 15, "audiences": 15, "policy": 10},
    "apple": {"measurement": 25, "structure": 20, "keywords": 20, "creative": 15, "delivery": 15, "policy": 5},
}


def coverage_status(cov):
    if cov is None:
        return "insufficient_evidence"
    if cov >= 80:
        return "graded"
    if cov >= 60:
        return "provisional"
    return "insufficient_evidence"


def score_platform(p):
    name = p["platform"].lower()
    weights = CATEGORY_WEIGHTS.get(name)
    if weights is None:
        raise ValueError(f"unknown platform '{name}' (Lite scores: {', '.join(CATEGORY_WEIGHTS)})")
    cats = {}
    unknown_critical = []
    for c in p.get("controls", []):
        res, sev, cat = c["result"], c["severity"], c["category"].lower()
        if res not in RESULTS:
            raise ValueError(f"{c['id']}: result must be one of {sorted(RESULTS)}")
        if sev not in SEVERITY_WEIGHT:
            raise ValueError(f"{c['id']}: severity must be one of {sorted(SEVERITY_WEIGHT)}")
        if cat not in weights:
            raise ValueError(f"{c['id']}: category '{cat}' not in {name} profile {sorted(weights)}")
        if res == "not_applicable":
            continue
        w = SEVERITY_WEIGHT[sev]
        b = cats.setdefault(cat, {"applicable": 0, "known": 0, "passed": 0})
        b["applicable"] += w
        if res != "unknown":
            b["known"] += w
            if res == "pass":
                b["passed"] += w
        elif sev == "critical":
            unknown_critical.append(c["id"])

    applicable = sum(b["applicable"] for b in cats.values())
    known = sum(b["known"] for b in cats.values())
    coverage = round(100 * known / applicable, 1) if applicable else None
    scored = {k: v for k, v in cats.items() if v["known"] > 0}
    total_w = sum(weights[k] for k in scored)
    health = None
    if total_w:
        health = round(sum(100 * v["passed"] / v["known"] * weights[k] for k, v in scored.items()) / total_w, 1)
    status = coverage_status(coverage)
    return {
        "platform": name,
        "health_score": health if status != "insufficient_evidence" else None,
        "raw_health_score": health,
        "evidence_coverage": coverage,
        "coverage_status": status,
        "categories": {
            k: {
                "health": round(100 * v["passed"] / v["known"], 1) if v["known"] else None,
                "coverage": round(100 * v["known"] / v["applicable"], 1) if v["applicable"] else None,
            }
            for k, v in cats.items()
        },
        "unknown_critical_controls": unknown_critical,
        "spend": p.get("spend"),
    }


def portfolio(results):
    eligible = [r for r in results if r["health_score"] is not None]
    if not eligible:
        return {"portfolio_health": None, "basis": "withheld: no platform with coverage >= 60%"}
    if all(isinstance(r["spend"], (int, float)) and r["spend"] > 0 for r in eligible):
        total = sum(r["spend"] for r in eligible)
        value = sum(r["health_score"] * r["spend"] / total for r in eligible)
        basis = "same-window spend share"
    else:
        value = sum(r["health_score"] for r in eligible) / len(eligible)
        basis = "equal weights (spend missing) - provisional"
    excluded = [r["platform"] for r in results if r["health_score"] is None]
    return {"portfolio_health": round(value, 1), "basis": basis, "excluded_platforms": excluded}


def main():
    raw = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    data = json.loads(raw)
    results = [score_platform(p) for p in data.get("platforms", [])]
    out = {"label": "Lite rubric score", "platforms": results, "portfolio": portfolio(results)}
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
