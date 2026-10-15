# Guarantee & Scarcity Afford-Logic Check

Any guarantee or scarcity/urgency claim creates a real liability. This check runs the
number **before the claim ships**, so a solvency-risky promise is caught at authoring time —
not by luck in a later review.

Run it in Phase 4 of this skill, when designing guarantees and scarcity. It needs
`business-profile.md` (or the user's own answers) for the cash/capacity facts; if those are
unknown, mark the guarantee **UNVERIFIED afford-logic** rather than passing it by default.

## The check

For each guarantee or scarcity claim:

1. **Name the worst-case liability** — the cost if the promise is called in at the worst
   plausible rate:
   - Results / "work-free-until-X" guarantee → (delivery cost per client) × (clients who hit the trigger). An open-ended "work free until it works" on a service with real delivery cost is an unbounded liability.
   - Money-back window → (refund rate) × (price) × (volume in the window).
   - Service-level promise ("we do X by Y, or Z") → cost of the make-good (Z) × expected miss rate.
   - Scarcity ("6 slots/month") → revenue given up if real demand exceeds the cap (opportunity cost, not solvency — but record it).
2. **Compare to the cash position** — pull cash on hand / runway / monthly revenue and
   capacity from `business-profile.md` or ask the user. Rule of thumb: if the worst-case
   liability exceeds **~1 month of cash** (or a materially risky fraction of runway), it is a
   **RISK**.
3. **Verdict** — **PASS** (afford-logic holds — state the number) · **RISK** (worst case vs
   cash, with the number) · **UNVERIFIED** (cash facts missing — do not pass by default).

## On a RISK verdict

Do not silently ship it. Surface the number to the user and offer a safer structure:
cap the guarantee (bounded window/amount), gate it behind qualification, convert to a
performance / pay-per-result term, or add a make-good that costs less than a refund. The
user decides — this check supplies the math, not the call. Record the chosen structure and
its afford-logic in the offer's Sources & freshness note (section 8 of `offer.md`).
