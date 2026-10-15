# Scoring, Thresholds & Prioritization

Each dimension is scored 0–100 from concrete on-page evidence, then weighted into
the CRO Health Score. No score without a cited observation.

**How to compute it.** If code execution is available, run `scripts/score.py`
(offline, standard library only) with the per-dimension scores. If not, do the
same arithmetic by hand and show it in the report:

```
CRO Health Score = Σ (dimension score × weight) ÷ Σ (weights of scored dimensions)
```

Example: Value 52, Interactive 44, Cognitive 50, Emotional 40, Clarity 60,
Trust 42, CTA 50 → (52×0.22 + 44×0.16 + 50×0.16 + 40×0.16 + 60×0.10 + 42×0.10
+ 50×0.10) ÷ 1.00 = 11.44 + 7.04 + 8.00 + 6.40 + 6.00 + 4.20 + 5.00 = 48.08
→ **48, Grade D**. A dimension that is out of scope (single-lens run) is left
out and the remaining weights are renormalized, exactly as the script does.
Bars: one █ per 10 points, rounded, padded with ░ to ten characters.

## Dimensions and weights

| Dimension | Weight | What it measures |
|---|---|---|
| Value | 0.22 | Perceived value: clarity, specificity, awareness match, offer presence |
| Interactive friction | 0.16 | Speed, mobile mechanics, forms, broken/blocking elements (higher = less friction) |
| Cognitive friction | 0.16 | Hierarchy, reading load, jargon, one-goal focus, message match (higher = less friction) |
| Emotional friction | 0.16 | Proof, social proof, objection handling, risk reversal (higher = less friction) |
| Clarity | 0.10 | Core message understood in one pass |
| Trust | 0.10 | Credible enough to act on |
| CTA | 0.10 | One obvious, action-describing, well-placed CTA |

Friction lenses are scored so **higher = less friction** (100 = frictionless), so
every dimension points the same direction and the weighted sum is a clean 0–100.

## Grade bands

| Grade | Score | Read |
|---|---|---|
| A | 90–100 | Converting well; test to optimize |
| B | 75–89 | Solid; a few clear lifts available |
| C | 60–74 | Leaking; several fixable frictions |
| D | 40–59 | Underconverting; structural work needed |
| F | <40 | Broken conversion; rebuild the fundamentals |

## Scorecard block (render in the report)

```
CRO Health Score: 48/100 — Grade D

Value:                █████░░░░░  52/100
Interactive friction: ████░░░░░░  44/100   (LCP 4.3s, banner over CTA)
Cognitive friction:   █████░░░░░  50/100   (feature-first H1, dense copy)
Emotional friction:   ████░░░░░░  40/100   (no proof, top objection unanswered)
Clarity:              ██████░░░░  60/100
Trust:                ████░░░░░░  42/100
CTA:                  █████░░░░░  50/100   ("Submit", below fold on mobile)
```

## Speed thresholds (measure — never estimate)

| Metric | Pass (→100) | Warning (→60) | Fail (→20) |
|---|---|---|---|
| LCP | <2.5s | 2.5–4.0s | >4.0s |
| INP | <200ms | 200–500ms | >500ms |
| CLS | <0.1 | 0.1–0.25 | >0.25 |
| TTI | <3.0s | 3.0–5.0s | >5.0s |
| Page weight | <2MB | 2–5MB | >5MB |

Speed feeds the interactive-friction score. Source every figure with retrieval date.
If speed was not measured, score interactive friction on the other observed signals
and say "speed not measured" next to the bar. Never fill the gap with an estimate.

## Message-match scale (feeds cognitive friction when traffic is paid/search)

| Level | Description | Points |
|---|---|---|
| Exact | H1, offer, CTA all continue the ad's promise | 100 |
| Partial | Headline matches but offer/CTA drifts | 60 |
| Weak | Generic page loosely related to the ad | 30 |
| Mismatch | Page doesn't reflect the ad promise | 0 |

## Form-length guide (feeds interactive friction)

| Fields | CVR posture | Fits |
|---|---|---|
| 1–3 | Highest | TOF / free offer |
| 4–5 | Moderate | MOF / qualified lead |
| 6–8 | Lower | BOF / sales-ready |
| 9+ | Lowest | High-value offers only |

Judge field count against the funnel stage, not in the abstract. A 7-field form on
a cold-traffic TOF page is high friction; the same form for an enterprise quote is fine.

## Prioritization (how to rank the fix list)

Score each finding on **impact** and **effort**, then sort by impact-per-effort.

- **Impact** (1–5): how much conversion the fix likely returns. Above-the-fold,
  CTA, message-match, and top-objection fixes usually score highest — 50% never
  scroll past the fold, so fold-level problems gate everything below.
- **Effort** (1–5): 1 = copy/CSS tweak, 5 = rebuild or new asset (case study,
  proof, redesign).
- **Priority score = impact ÷ effort.** Rank descending.
- **Quick wins** = impact ≥4 and effort ≤2. Surface these first — they ship today.
- **Structural** = high impact but effort ≥4 (new proof, redesign, re-architecture).
  List separately with the outcome they unlock.

Every fix states: the dimension it lifts, the on-page observation behind it, and
the concrete change (the new headline direction, the fields to cut, the proof to
add) — never "improve the headline".

Cite any conversion-lift figure with its source. Do not attach invented
percentage lifts to individual fixes; describe expected direction and rationale
unless you have a sourced benchmark.
