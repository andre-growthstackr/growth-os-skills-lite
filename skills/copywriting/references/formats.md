# Format Playbooks

Read only the section the argument requires. Every format inherits the full method from
SKILL.md (context loading, banned list, verbatim quotes, quality gates) — this file only
adds format-specific structure. VoC section numbers refer to the standard Growth OS
`voice-of-customer.md` structure (as created by `/brand-voc`): §2 pains, §3 value drivers,
§4 objections & fears, §5 triggers, §6 language & diction (words they use, words they never
use, tone observations), §7 recommendations per surface (web, ads, sales, content, lead
magnets). If the user's file uses other headings, or the VoC was collected in chat, map by
meaning (pains, objections, triggers, diction) instead of by number.

## hero

Job: stop the skim and make the buyer feel recognized in under 3 seconds.
- Structure: Template 1 from SKILL.md (trigger → buyer's pain phrasing → context, not solution).
- VoC inputs: §2 top pain (verbatim), §5 triggers, §7 web recommendations.
- Add: audience callout (who this is for), value proposition sub-line, one trust element.
- Deliver: 3 headline variants + sub-line + CTA label for each.

## landing

Job: one conversion goal, message-matched to the traffic source.
- Ask (or take from the routing skill): traffic source and its promise, awareness level
  (unaware → most aware), the single conversion goal.
- Section order: above the fold (hero per above) → problem (VoC §2, verbatim) → solution
  as a system, not a campaign → how it works → social proof (only real proof from
  `offer.md` or user input) → offer and value stack → guarantees → for you / not for you
  (from `icp.md` tiers if present) → price + CTA → FAQ (VoC §4 objections, answered) →
  final CTA.
- Message match: the ad or email promise continues word for word in the headline.
- CTA labels describe what the visitor gets ("Get the teardown"), never "Submit".

## ad

Job: earn the click from a skimming, skeptical buyer inside platform constraints.
- Ask (or take from routing skill): platform, funnel stage (awareness / consideration /
  conversion), character limits.
- Hook: verbatim trigger language from VoC §5 — the buyer must recognize themselves in
  line one. Dog-whistle phrasing beats clever phrasing.
- Body: one pain, one concrete proof point, one next step. No feature lists.
- Awareness stage → Template 1 energy (recognition, no pitch). Consideration → case or
  proof. Conversion → Template 3 (this week + long term).
- Deliver: 3 hook variants per ad, primary text, headline, CTA label.

## email

Job: get opened by a stranger (cold) or move a known lead one step (nurture).
- Cold: subject = fragment of the buyer's own pain language (VoC §6), lowercase-normal,
  no clickbait. Opening line = the specific observed trigger, never "I hope this finds
  you well". One idea, one soft CTA (question or resource), under 120 words.
- Nurture: pick the objection (VoC §4) this email neutralizes; use Template 2. One email,
  one objection.
- Deliver: subject variants (3), body, plain-text formatting. Flag any claim that needs
  proof the context files do not contain.

## post

Job: peer-voice content that earns trust, not applause.
- Angle: one pain or trigger (VoC §2/§5) told from the buyer's chair; or one concrete
  observation with a real number from context files.
- Structure: hook line (would survive as a text message) → 2–4 short paragraphs or a
  tight list → comment-CTA if the routing skill's strategy calls for one.
- Kill every line that reads as broadcast marketing; keep lines that read as a colleague
  thinking out loud.

## script

Job: spoken lines for sales calls or video that sound like talking, not reading.
- Sales: discovery questions mirroring VoC §6 diction; objection responses per Template 2
  for each VoC §4 row the user selects.
- Video: hook (VoC trigger, first 3 seconds) → one pain → one payoff → one CTA. Write for
  the ear: shorter sentences than written copy, contractions up, zero jargon.
- Read the draft aloud before delivery; rewrite anything you stumbled on.

## cta

Job: microcopy that states the exchange plainly.
- CTA label = what the buyer gets, in their words ("Book the teardown", "Get the
  checklist"), never the mechanism ("Submit", "Send").
- Match commitment to awareness level: cold traffic gets low-commitment CTAs.
- Deliver: 3 variants each with a one-line rationale.

## objection

Job: neutralize one specific objection with honesty, not spin.
- Source: one row from VoC §4 (objection, verbatim quote, what is behind it, counter).
- Structure: Template 2 — name the specific past investment, absolve the buyer, then give
  the counter-proof from `offer.md` or user-supplied evidence.
- Never argue the objection is wrong; show what is different now and prove it. If no real
  proof exists in context, say so and stop — an unproven counter is spin.
