#!/usr/bin/env python3
"""Deterministic economics calculator for ads-audit (from the Growth OS ads backend).

Two domains:
  - economics: CPA, ROAS, break-even, LTV:CAC, MER, payback
  - experiment: sample size, significance (two-proportion z-test), duration

Every result is computed here (never by hand) so the audit numbers are
reproducible. No network, no state. Inputs come from the user's own data.

Usage:
  admath.py economics --spend 10000 --conversions 40 --revenue 60000 \
      --aov 1500 --margin 0.6 --ltv 4500 --customers 40
  admath.py breakeven --aov 1500 --margin 0.6 [--current-cpa 700] [--current-roas 3.2]
  admath.py ltvcac --spend 10000 --customers 40 --arpu 250 --lifespan 24 [--margin 0.6]
  admath.py samplesize --baseline 0.05 --mde 0.20 [--confidence 0.95] [--power 0.80] \
      [--absolute] [--variants 2]
  admath.py significance --a-users 5000 --a-conv 250 --b-users 5000 --b-conv 300 \
      [--confidence 0.95]
  admath.py duration --sample 7300 --daily-traffic 500 [--variants 2]

All monetary inputs are unit-agnostic (use one currency consistently).
Margin/rates are decimals (0.6 = 60%). Output is JSON on stdout.
"""
import argparse
import json
import math
import sys

# Standard normal inverse CDF (Acklam's algorithm) - avoids a scipy dependency.
def _norm_ppf(p):
    if not (0.0 < p < 1.0):
        raise ValueError("probability must be in (0,1)")
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
               ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / \
           (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)


def _norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def economics(a):
    out = {"warnings": []}
    if a.spend is not None and a.conversions:
        out["cpa"] = round(a.spend / a.conversions, 2)
    if a.revenue is not None and a.spend:
        out["roas"] = round(a.revenue / a.spend, 2)
        out["roas_pct"] = round((a.revenue - a.spend) / a.spend * 100, 1)
    if a.aov is not None and a.margin is not None:
        be_cpa = a.aov * a.margin
        out["break_even_cpa"] = round(be_cpa, 2)
        out["break_even_roas"] = round(1 / a.margin, 2) if a.margin else None
        if out.get("cpa") is not None:
            head = (be_cpa - out["cpa"]) / be_cpa * 100 if be_cpa else None
            out["cpa_headroom_pct"] = round(head, 1) if head is not None else None
            out["verdict"] = _scale_verdict(out["cpa"], be_cpa)
    if a.ltv is not None and a.spend is not None and a.customers:
        cac = a.spend / a.customers
        out["cac"] = round(cac, 2)
        out["ltv_cac_ratio"] = round(a.ltv / cac, 2) if cac else None
        out["ltv_cac_reading"] = _ltvcac_reading(out["ltv_cac_ratio"])
    if not out or set(out) == {"warnings"}:
        out["warnings"].append("no computable metric from the inputs given")
    return out


def _scale_verdict(cpa, be_cpa):
    """Position vs break-even only. Not a scale/cut decision: that needs sample size,
    conversion lag, objective and the operator's own thresholds (references/contract.md).
    Both inputs must be per the SAME conversion (cost per customer vs contribution per
    customer, or cost per lead vs contribution per lead)."""
    if be_cpa == 0:
        return "unknown"
    r = cpa / be_cpa
    side = "below" if r < 1 else ("at" if r == 1 else "above")
    return f"{side} break-even (CPA = {r:.2f} x break-even CPA); confirm both are per the same conversion"


def _ltvcac_reading(ratio):
    """Plain reading of the ratio. No universal benchmark is applied."""
    if ratio is None:
        return None
    if ratio < 1:
        return "<1:1 - customer lifetime value does not cover acquisition cost"
    return f"{ratio:.2f}:1 - compare with the operator's own target or a sourced, comparable benchmark"


def breakeven(a):
    out = {}
    out["break_even_cpa"] = round(a.aov * a.margin, 2)
    out["break_even_roas"] = round(1 / a.margin, 2)
    if a.current_cpa is not None:
        out["current_cpa"] = a.current_cpa
        out["cpa_verdict"] = _scale_verdict(a.current_cpa, out["break_even_cpa"])
    if a.current_roas is not None:
        out["current_roas"] = a.current_roas
        out["roas_verdict"] = ("above break-even (profitable)"
                               if a.current_roas > out["break_even_roas"]
                               else "below break-even (unprofitable)")
    return out


def ltvcac(a):
    cac = a.spend / a.customers
    ltv = a.arpu * a.lifespan
    out = {"cac": round(cac, 2), "ltv": round(ltv, 2)}
    if a.margin is not None:
        out["ltv_gross"] = round(ltv, 2)
        ltv = ltv * a.margin
        out["ltv_margin_adjusted"] = round(ltv, 2)
    out["ltv_cac_ratio"] = round(ltv / cac, 2) if cac else None
    out["ltv_cac_reading"] = _ltvcac_reading(out["ltv_cac_ratio"])
    out["payback_months"] = round(cac / a.arpu, 1) if a.arpu else None
    return out


def samplesize(a):
    z_a = _norm_ppf(1 - (1 - a.confidence) / 2)
    z_b = _norm_ppf(a.power)
    p = a.baseline
    if a.absolute:
        mde_abs = a.mde
    else:
        mde_abs = p * a.mde  # relative lift on the baseline
    if mde_abs <= 0:
        raise ValueError("mde must be > 0")
    n = ((z_a + z_b) ** 2) * 2 * p * (1 - p) / (mde_abs ** 2)
    n = math.ceil(n)
    return {
        "per_variant": n,
        "variants": a.variants,
        "total": n * a.variants,
        "baseline_cvr": p,
        "mde_relative_pct": None if a.absolute else round(a.mde * 100, 1),
        "mde_absolute_pp": round(mde_abs * 100, 3),
        "confidence": a.confidence,
        "power": a.power,
        "note": "per variant; assumes two-proportion test, equal split",
    }


def significance(a):
    p1 = a.a_conv / a.a_users
    p2 = a.b_conv / a.b_users
    pooled = (a.a_conv + a.b_conv) / (a.a_users + a.b_users)
    se = math.sqrt(pooled * (1 - pooled) * (1 / a.a_users + 1 / a.b_users))
    if se == 0:
        raise ValueError("zero standard error - check inputs")
    z = (p2 - p1) / se
    p_two = 2 * (1 - _norm_cdf(abs(z)))
    alpha = 1 - a.confidence
    significant = p_two < alpha
    rel_lift = (p2 - p1) / p1 * 100 if p1 else None
    return {
        "control_cvr": round(p1, 5),
        "variant_cvr": round(p2, 5),
        "absolute_diff_pp": round((p2 - p1) * 100, 3),
        "relative_lift_pct": round(rel_lift, 2) if rel_lift is not None else None,
        "z_score": round(z, 3),
        "p_value_two_sided": round(p_two, 5),
        "alpha": round(alpha, 3),
        "significant": significant,
        "winner": ("variant" if significant and p2 > p1
                   else "control" if significant and p1 > p2
                   else "no significant difference"),
        "note": "two-proportion z-test; verify test ran >=7 days before acting",
    }


def duration(a):
    per_variant = a.sample
    daily_per_variant = a.daily_traffic / a.variants
    if daily_per_variant <= 0:
        raise ValueError("daily traffic must be > 0")
    days = math.ceil(per_variant / daily_per_variant)
    return {
        "required_per_variant": per_variant,
        "daily_traffic_per_variant": round(daily_per_variant, 1),
        "raw_days": days,
        "recommended_days": max(days, 7),
        "min_days": 7,
        "max_recommended_days": 28,
        "note": "floor of 7 days to capture a weekly cycle; cap ~28 to avoid drift",
    }


def main():
    p = argparse.ArgumentParser(description="ads-audit deterministic economics calculator")
    sub = p.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("economics")
    e.add_argument("--spend", type=float)
    e.add_argument("--conversions", type=float)
    e.add_argument("--revenue", type=float)
    e.add_argument("--aov", type=float)
    e.add_argument("--margin", type=float, help="gross margin as decimal, e.g. 0.6")
    e.add_argument("--ltv", type=float)
    e.add_argument("--customers", type=float)
    e.set_defaults(fn=economics)

    b = sub.add_parser("breakeven")
    b.add_argument("--aov", type=float, required=True)
    b.add_argument("--margin", type=float, required=True)
    b.add_argument("--current-cpa", dest="current_cpa", type=float)
    b.add_argument("--current-roas", dest="current_roas", type=float)
    b.set_defaults(fn=breakeven)

    l = sub.add_parser("ltvcac")
    l.add_argument("--spend", type=float, required=True)
    l.add_argument("--customers", type=float, required=True)
    l.add_argument("--arpu", type=float, required=True, help="avg revenue per customer per period")
    l.add_argument("--lifespan", type=float, required=True, help="avg lifespan in periods")
    l.add_argument("--margin", type=float)
    l.set_defaults(fn=ltvcac)

    s = sub.add_parser("samplesize")
    s.add_argument("--baseline", type=float, required=True, help="baseline CVR decimal")
    s.add_argument("--mde", type=float, required=True, help="minimum detectable effect (relative decimal, or absolute pp with --absolute)")
    s.add_argument("--confidence", type=float, default=0.95)
    s.add_argument("--power", type=float, default=0.80)
    s.add_argument("--absolute", action="store_true", help="treat --mde as an absolute lift in rate")
    s.add_argument("--variants", type=int, default=2)
    s.set_defaults(fn=samplesize)

    g = sub.add_parser("significance")
    g.add_argument("--a-users", dest="a_users", type=float, required=True)
    g.add_argument("--a-conv", dest="a_conv", type=float, required=True)
    g.add_argument("--b-users", dest="b_users", type=float, required=True)
    g.add_argument("--b-conv", dest="b_conv", type=float, required=True)
    g.add_argument("--confidence", type=float, default=0.95)
    g.set_defaults(fn=significance)

    d = sub.add_parser("duration")
    d.add_argument("--sample", type=int, required=True, help="required sample per variant")
    d.add_argument("--daily-traffic", dest="daily_traffic", type=float, required=True, help="total daily traffic across variants")
    d.add_argument("--variants", type=int, default=2)
    d.set_defaults(fn=duration)

    args = p.parse_args()
    try:
        result = args.fn(args)
    except (ValueError, ZeroDivisionError) as exc:
        json.dump({"error": str(exc)}, sys.stdout, indent=2)
        sys.stdout.write("\n")
        sys.exit(1)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
