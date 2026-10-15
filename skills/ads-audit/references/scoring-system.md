# Scoring — Growth OS Lite rubric

Adapted from the Growth OS Ads scoring contract (claude-ads). Lite has no control registry
or scoring engine, so severities are assigned in the run with the rubric below and the math is
done with `scripts/score.py` (or by hand with the same formulas). Label every score
**"Lite rubric score"**: it is consistent within one audit and across re-audits run the same
way, but not comparable to the full version's registry-based score.

## Four separate outputs

1. `health_score` — observed performance and implementation health, 0–100.
2. `evidence_coverage` — share of applicable control weight with a known result.
3. `regulatory_exposure` — P0/P1 policy, privacy and legal risks, listed separately (never
   folded into health).
4. `opportunities` — optional, beta, premium or ineligible features. Unscored.

No letter grades. Every score is paired with its coverage status and data window.

## Control states

| State | Meaning | Health | Coverage |
|---|---|---|---|
| `pass` | Evidence satisfies the control | counts (earns weight) | counts as known |
| `fail` | Evidence does not satisfy the control | counts (earns 0) | counts as known |
| `unknown` | Applicable, but evidence is missing or inconclusive | excluded | stays in denominator |
| `not_applicable` | Control does not apply to this account | excluded | excluded |

## Severity rubric (assign per control, before you know pass/fail)

Severity is the impact **if the control fails**. Decide it from the account's economics and
objective, not from how new or interesting a feature is.

| Severity | Weight | Use when a failure would… |
|---|---:|---|
| critical | 5 | break measurement of the primary conversion, create a policy/privacy/legal risk, or let spend run without control |
| high | 3 | materially waste spend or suppress performance (structure, targeting, bidding, creative fatigue) |
| medium | 1 | leave a meaningful improvement on the table with lower urgency |
| info | 0 | context only, or an unscored opportunity |

Rules: one root cause = one scored control (do not also penalize every symptom). Beta,
premium or unavailable features are never health controls.

## Formulas

Per category (known, applicable controls only):

```text
category_health   = 100 × Σ(weight of passed controls) / Σ(weight of known controls)
category_coverage = 100 × Σ(weight of known controls)  / Σ(weight of applicable controls)
```

Per platform (category weights below; drop categories with no **known** controls, since their
health is undefined, and renormalize the remaining weights to 100; their unknown weight still
counts against coverage):

```text
platform_health   = Σ(category_health × category_weight) / Σ(category_weight)
platform_coverage = 100 × Σ(known weight) / Σ(applicable weight)   (over all categories)
```

Portfolio (only platforms with coverage ≥ 60%):

```text
portfolio_health = Σ(platform_health × same-window spend share)
```

If spend per platform is unknown, use equal weights and label the portfolio **provisional**.
A platform with no data or a failed read is **excluded** (not scored as zero) and the bundle is
labeled `partial`. If no defensible weights remain, withhold the portfolio score.

## Coverage status

| Coverage | Status | Reporting rule |
|---:|---|---|
| 80–100% | graded | Publish health with coverage |
| 60–79.99% | provisional | Publish health labeled provisional |
| below 60% | insufficient_evidence | Do not present health as an account grade |

Unknown **critical** controls always appear in the priority list, whatever the coverage.

## Category weights per platform (reference profiles)

| Platform | Category weights (total 100) |
|---|---|
| Google | measurement 25 · waste 20 · structure 15 · keywords 15 · creative 15 · settings 10 |
| Meta | measurement 25 · creative 25 · structure 20 · audiences 15 · delivery 10 · policy 5 |
| YouTube | measurement 25 · creative 25 · structure 20 · audiences 15 · delivery 10 · policy 5 |
| LinkedIn | measurement 25 · audiences 20 · creative 20 · structure 15 · delivery 15 · policy 5 |
| TikTok | measurement 25 · creative 25 · delivery 15 · structure 15 · audiences 15 · policy 5 |
| Microsoft | measurement 25 · structure 20 · delivery 15 · creative 15 · audiences 15 · policy 10 |
| Apple | measurement 25 · structure 20 · keywords 20 · creative 15 · delivery 15 · policy 5 |

Map each assessed control to the closest category of its platform (e.g. budget and pacing →
delivery; bidding → structure or settings; tracking and attribution → measurement; ad copy,
formats and landing-page match → creative). Record the mapping in the findings table so a
re-audit uses the same mapping.

## Recommendations

Scores prioritize investigation; they do not authorize changes. Each recommendation cites its
finding, states confidence, and considers sample size and conversion lag. This skill never
changes an account.
