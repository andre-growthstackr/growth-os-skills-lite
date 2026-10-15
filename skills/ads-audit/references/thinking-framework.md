# Thinking framework — ten audit gates

Condensed from the Growth OS Ads thinking framework (claude-ads) for a single-conversation audit.
Each principle is an observable gate: before the report ships, you can point to where it was
applied.

| # | Principle | Gate in this audit |
|---|---|---|
| 1 | **Observe — external** | Look at the actual data before diagnosing: the export, the screenshot, the landing page exactly as the ad audience sees it (mobile, the real ad URL, not the homepage). No diagnosis from memory or a generic checklist. |
| 2 | **Observe — internal** | Name your assumptions and benchmark fit. Is the benchmark's cohort, window and attribution comparable? If not, it is directional only. |
| 3 | **Listen** | The operator's objective, economics and constraints override generic best practice. Ask before applying a threshold you cannot ground. |
| 4 | **Think** | First-principles math: break-even CPA/ROAS from AOV and margin, blended MER on booked revenue, conversion lag, sample size. Calculate, don't eyeball (`scripts/admath.py` or the formulas in `references/budget-allocation.md`). |
| 5 | **Connect — lateral** | Look across platforms: the same audience, offer and creative problem often shows up in several accounts. |
| 6 | **Connect — system** | Tracking, budget, creative, landing page and policy must be coherent. Never recommend "increase budget" and "pause this campaign" without naming the trade-off. |
| 7 | **Feel** | Read the ads and landing page as a first-time buyer. Does the headline make the right person feel something? Keep this qualitative review separate from the health score. |
| 8 | **Accept** | Uncertainty is a result. Missing evidence → `unknown`, lower confidence, a named data request. Never fill a gap with a plausible number. |
| 9 | **Create** | Every recommendation is decision-complete: owner, priority, effort, expected effect, success measure, measurement window, rollback condition. |
| 10 | **Grow** | End with what to measure next and when to re-audit, so the next run can compare like with like. |

## Anti-patterns to catch in your own draft

- Pausing because CPA crossed a fixed multiple, or applying a fixed budget-to-CPA ratio to every objective.
- Summing conversions across platforms with different windows or definitions.
- Recommending negative keywords without a search-terms report and an overblocking review.
- Treating a beta or unavailable feature as an account weakness.
- Calling an account profitable on summed platform-attributed ROAS.
