# Conversion Dimension — Checks & Scoring

Framed through the conversion formula: **increase perceived value, reduce perceived friction**. Friction comes in three kinds — this is the primary lens for every finding. Score this dimension 0-100.

## The friction model (tag every finding with one)

| Friction type | What it is | Examples |
|---|---|---|
| **Interactive** | The site physically gets in the way | Broken links, slow loading, clunky forms, popups blocking content, dead CTAs |
| **Cognitive** | The visitor has to think too hard | Unclear hierarchy, too much text, jargon, vague headlines, competing CTAs |
| **Emotional** | The visitor doesn't feel safe to act | Hidden prices, claims without proof, no cases/testimonials, unanswered objections, no guarantees |

## Sub-areas and weights

| Sub-area | Weight |
|---|---|
| Message & value clarity | 25% |
| Above-the-fold anatomy | 20% |
| Trust & proof (emotional friction) | 20% |
| CTA & form quality (interactive friction) | 20% |
| Awareness-level match | 15% |

## 1. Message & value clarity (25%) — cognitive friction

- Headline answers: what is this, who is it for, what value, why care? **Clear beats clever.**
- If a traffic source is known (ads, campaign): **message match** — does the page continue the promise of the ad/link verbatim? (Exact match 100 / partial 60 / weak 30 / mismatch 0)
- Jargon check: language the ICP actually uses (compare against `voice-of-customer.md` if loaded)
- One primary conversion goal per landing page; site pages may have more, but each page needs an obvious next step
- No wall-of-text sections before the value is established

## 2. Above-the-fold anatomy (20%)

Many visitors never scroll past the first screen, so it must carry the page. Check for (desktop AND mobile):
- Audience callout or clear targeting signal
- Value proposition headline + supporting subheadline
- Primary CTA visible without scrolling
- At least one trust element (logos, rating, customer count)
- Consent banner does not cover the CTA or push key content below the fold

## 3. Trust & proof (20%) — emotional friction

- Social proof: testimonials with names/photos/companies, case results with specific numbers, review scores
- Objection handling: FAQ or copy that answers the top objections (check `voice-of-customer.md` objections if loaded)
- Risk reversal: guarantees, free trial, cancel-anytime, clear pricing (hidden pricing on SME-targeted sites = High finding)
- Credibility: real about page, real people, physical address/contact for local businesses
- "For you / not for you" qualification present on offer pages

## 4. CTA & form quality (20%) — interactive friction

- CTA copy describes what you get ("Book a demo", "Get my free quote") — never "Submit" / "Send"
- CTA repeated at natural decision points down the page; full-width on mobile
- Form length matches funnel stage: 1-3 fields top-of-funnel, 4-5 mid, 6+ only bottom-funnel/high-value
- Multi-step with progress indicator for 5+ fields; inline validation; helpful error messages
- Phone numbers clickable (tel:); thank-you step has clear next steps
- Conversion tracking sanity check: does a form submit / thank-you page fire a detectable event? UTM/click-ID parameters preserved? (Report as "not verifiable" if you cannot test)

## 5. Awareness-level match (15%) — Schwartz

unaware → problem aware → solution aware → product aware → most aware.

- Does the page meet its likely visitor at their level? Cold-traffic pages that jump straight to "book a demo" with no problem/solution bridge = classic mistake, High finding
- Full page anatomy for offer/landing pages: above fold → problem → solution/system → how it works → social proof → value/offer → guarantees → for-you/not-for-you → price+CTA → FAQ → final CTA. Note which blocks are missing.

## Quick-win table (use in the action plan)

| Fix | Typical impact |
|---|---|
| Primary CTA above the fold on all devices | High |
| Cut form to essential fields | High |
| Add trust elements near CTA | Medium-High |
| Rewrite CTA copy to outcome language | Medium |
| Answer top 3 objections on the page | Medium |

Do not attach invented percentage lifts to these — impact estimates are directional unless the user has baseline data.

## Severity mapping

- **Critical**: broken conversion path (dead CTA/form, page won't load)
- **High**: no visible CTA above fold, message mismatch with paid traffic, zero proof elements, awareness-level mismatch on cold-traffic pages
- **Medium**: weak CTA copy, long forms, missing FAQ/objection handling, consent-banner interference
- **Low**: secondary CTA placement, minor copy polish
