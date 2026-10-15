# The Three-Friction Lens

The audit backbone. Conversion = perceived value up, perceived friction down.
Friction is not one thing — it shows up in three places, and a fix aimed at the
wrong one wastes effort. Score each lens separately; a page can be fast and
trustworthy yet still fail on cognitive load.

## Value side (score first — friction is relative to it)

Friction only matters relative to what the visitor is being asked to trade for.
Read value before friction.

- **Value clarity**: does the headline answer what / who / why-care in one read?
- **Awareness match** (Schwartz): unaware → problem-aware → solution-aware →
  product-aware → most-aware. Cold traffic sent straight to "book a demo" is the
  classic mistake. Does the page meet the visitor where they are?
- **Specificity**: concrete outcome vs vague benefit ("cut onboarding to 2 days"
  beats "streamline your workflow").
- **Offer presence**: is the actual offer, price posture, and its proof on the
  page, above the fold where it counts (many visitors never scroll past it)?
- **Value-per-glance**: could a skimmer get the core value in 5 seconds?

## Lens 1 — Interactive friction (the cost of acting)

The mechanical, physical cost of taking the next step. Mostly measurable.

- **Speed**: LCP, INP, CLS, TTI, page weight (measure — see scoring thresholds).
  Deloitte's "Milliseconds Make Millions" study (2020, for Google) found a 0.1s
  mobile speed gain lifted retail conversions 8.4%. If you cite it, find and
  include the source URL with web search; otherwise leave the number out.
- **Mobile mechanics**: tap targets ≥48×48px with ≥8px spacing, ≥16px body text,
  no horizontal scroll, CTA reachable without hunting, tel: links tappable.
- **Forms**: field count vs funnel stage, keyboard type matches input, inline
  validation, no dead-end errors, specific submit label, multi-step for 5+ fields.
- **Broken / dead elements**: 404 links, dead buttons, mislinked CTAs, images not
  loading, form that fails to submit.
- **Blockers on load**: interstitials, popups, chat widgets, and consent banners
  that cover the CTA or push the offer below the fold or delay interaction.
- **Path integrity**: does the primary CTA actually go where it promises?

## Lens 2 — Cognitive friction (the cost of thinking)

The mental effort to understand and decide. Cheap to fix, often the biggest lever.

- **Visual hierarchy**: does the eye land on headline → value → CTA, or is
  everything shouting equally? One clear focal point per section.
- **Reading load**: wall-of-text vs scannable; short paragraphs, subheads, bullets.
- **Jargon and abstraction**: internal language, acronyms, feature names the
  visitor doesn't know. Clear beats clever.
- **One goal**: a page with two co-equal CTAs (demo *and* newsletter *and*
  pricing) splits attention. Navigation on a landing page is a leak.
- **Choice overload**: too many plans, options, or links; decision paralysis.
- **Directional cues**: does layout guide toward the CTA, or scatter attention?
- **Message match**: if traffic came from an ad/search, does the H1 continue the
  ad's exact promise (headline, offer, keyword)? A break here is pure cognitive
  friction — the visitor has to re-orient.

## Lens 3 — Emotional friction (the cost of trusting)

The felt risk of saying yes. This is where most "good-looking" pages quietly fail.

- **Proof for every claim**: numbers, outcomes, and superlatives backed by
  evidence, or bare assertions the visitor must take on faith.
- **Social proof**: testimonials with names/photos/companies, client logos, star
  ratings, customer counts, case studies with specific metrics.
- **Objection handling**: are the top VoC objections answered on the page? (Pull
  them from `voice-of-customer.md`.) The unanswered objection is the silent killer.
- **Price transparency**: hidden pricing, "contact us" walls, or surprise cost
  breeds distrust for many buyers. Judge relative to the offer and awareness level.
- **Risk reversal**: guarantee, free trial, no-card-required, cancel-anytime — is
  the risk of yes reduced?
- **Authority / credibility**: security badges, certifications, real company
  details, named authors, recognizable customers.
- **Congruence**: does the tone and polish match the promise, or does something
  feel off (stock-photo overload, dead testimonials, broken English)?

## Cross-cutting dimensions (scored on their own)

These read across all three lenses so the fix list can point at the true lever.

- **Clarity**: is the core message understood in one pass? (spans value +
  cognitive)
- **Trust**: is the page credible enough to act on? (spans emotional)
- **CTA quality**: is there one obvious, action-describing CTA, above the fold,
  repeated at natural decision points? Label describes what you get ("Book demo"),
  not the mechanism ("Submit"). Contrast and placement make it unmissable.
