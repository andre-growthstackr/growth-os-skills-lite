# Funnel Scope — Seam Analysis

When the scope is a funnel (`ad → LP → checkout`, `signup funnel`, or several
URLs), audit each step as its own page (all lenses), then audit the **seams** —
the transitions between steps, where funnels leak hardest.

## Score each step

Run the full three-lens audit on every step and produce a per-step scorecard.
Deliver each as its own file, `cro-audit-<step>-<yyyy-mm-dd>.md`.

## Then score each seam

A seam is the handoff from step N to step N+1. Two things to score per seam:

### Message-match (continuity)
Does step N+1 continue the exact promise the visitor just acted on?
- The ad's headline/offer → the LP's H1/offer (use the message-match scale in
  `references/scoring.md`).
- The LP's CTA label → the next page's heading and offer.
- The value the visitor was promised → the value the next step presents.
A break here forces re-orientation and is a top drop-off cause.

### Momentum (friction gradient)
Does friction rise or fall as intent rises?
- Friction should *drop* as the visitor moves deeper (they've already committed).
  A funnel that adds friction late (surprise fields, new price, an account wall
  before value) leaks at exactly the wrong moment.
- Check: new information demanded, new cost revealed, new decision imposed,
  progress indicator present on multi-step flows.

## Seam scorecard block

```
Funnel seams

Ad → Landing page:      Match ██████████ 100   Momentum ████████░░ 80
Landing page → Signup:  Match ████░░░░░░  40   Momentum █████░░░░░ 50  ← weakest seam
Signup → Confirmation:  Match ████████░░  80   Momentum ████████░░ 80
```

## Output additions for funnel scope

- One scorecard per step, plus the seam scorecard above.
- The **weakest seam** called out explicitly — it usually returns more than any
  single on-page fix.
- Fix list still impact-ordered across the whole funnel; a seam fix competes with
  page fixes on impact-per-effort.
