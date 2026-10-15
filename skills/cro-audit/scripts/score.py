#!/usr/bin/env python3
"""Compute the weighted CRO Health Score from per-dimension scores.

Deterministic scoring so the report's headline number is math, not a vibe.
Friction lenses are scored so higher = less friction (100 = frictionless), so
every dimension points the same direction as value/clarity/trust/CTA.

Usage:
  score.py --value 52 --interactive 44 --cognitive 50 --emotional 40 \\
           --clarity 60 --trust 42 --cta 50

  # or feed a JSON object of dimension:score
  score.py --json '{"value":52,"interactive":44,"cognitive":50,
                    "emotional":40,"clarity":60,"trust":42,"cta":50}'

Any omitted dimension is dropped and the remaining weights are renormalized
(useful for single-lens scope). Prints the weighted score, letter grade, and a
bar per dimension.
"""

import argparse
import json
import sys

WEIGHTS = {
    "value": 0.22,
    "interactive": 0.16,
    "cognitive": 0.16,
    "emotional": 0.16,
    "clarity": 0.10,
    "trust": 0.10,
    "cta": 0.10,
}

LABELS = {
    "value": "Value",
    "interactive": "Interactive friction",
    "cognitive": "Cognitive friction",
    "emotional": "Emotional friction",
    "clarity": "Clarity",
    "trust": "Trust",
    "cta": "CTA",
}


def grade(score: float) -> str:
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 40:
        return "D"
    return "F"


def bar(score: float, width: int = 10) -> str:
    filled = int(score / 100 * width + 0.5)  # round half up
    filled = max(0, min(width, filled))
    return "█" * filled + "░" * (width - filled)


def compute(scores: dict) -> float:
    present = {k: v for k, v in scores.items() if v is not None}
    if not present:
        raise ValueError("No dimension scores provided.")
    for k, v in present.items():
        if k not in WEIGHTS:
            raise ValueError(f"Unknown dimension: {k}")
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise ValueError(f"{k}={v!r} must be a number 0-100")
        if not (0 <= v <= 100):
            raise ValueError(f"{k}={v} out of range 0-100")
    total_w = sum(WEIGHTS[k] for k in present)
    weighted = sum(present[k] * WEIGHTS[k] for k in present) / total_w
    return weighted


def main() -> int:
    p = argparse.ArgumentParser(description="CRO Health Score calculator")
    for dim in WEIGHTS:
        p.add_argument(f"--{dim}", type=float, default=None)
    p.add_argument("--json", dest="json_blob", default=None,
                   help="JSON object of dimension:score")
    args = p.parse_args()

    if args.json_blob:
        try:
            scores = json.loads(args.json_blob)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}", file=sys.stderr)
            return 2
    else:
        scores = {dim: getattr(args, dim) for dim in WEIGHTS}

    try:
        health = compute(scores)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    shown = int(health + 0.5)  # grade the number we print
    print(f"CRO Health Score: {shown}/100 — Grade {grade(shown)}\n")
    for dim in WEIGHTS:
        v = scores.get(dim)
        if v is None:
            continue
        print(f"{LABELS[dim]+':':<22}{bar(v)}  {v:.0f}/100")
    return 0


if __name__ == "__main__":
    sys.exit(main())
