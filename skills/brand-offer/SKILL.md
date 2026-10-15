---
name: brand-offer
description: "Designs offer.md with the $100M Offers method: value stack, guarantees, pricing logic, name. Use for: designa vårt erbjudande, paketera erbjudandet, design our offer."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: brand-os
---

# Brand Offer

Design one offer end to end with the $100M Offers method (Alex Hormozi): maximize the value equation, build a stack that makes the price feel obvious, design guarantees straight from real customer objections, and name the offer in customer language. The deliverable is `offer.md` — the context file every copy-, conversion-, lead-magnet- and ads skill inherits.

Respond and produce all deliverables in the user's language. Instructions below are in English; output follows the user.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `icp.md` — Ideal Customer Profile: tiers, firmographics, pains (REQUIRED — the offer is built for the green tier; section 7 of the offer mirrors the tier system)
- `voice-of-customer.md` — verbatim customer language, objections, triggers (REQUIRED — dream outcome is written in their words; objections drive guarantee and bonus design)
- `business-profile.md` — company, services, goals (OPTIONAL — feeds deliverables, capacity, honest scarcity and the guarantee afford-logic check)
- `brand-guidelines.md` — tone, negative rules, banned AI words (OPTIONAL — use if present; Lite continues without it)
- `offer.md` — if it already exists, this is a REDESIGN run: load it, keep what is proven, and improve against the value equation rather than starting blank. If `offer.md` is a **router** (multiple offers, see `references/context-routing.md`), redesign the specific `offer-<slug>.md` the user names, not the index

**Minimum context if files are missing** — ask these and continue:
1. Who is the ideal buyer (role, company type/size) and who is a bad fit you want to turn away?
2. What do those buyers say they want, in their own words — and the 3 most common objections or hesitations you hear before they buy (real phrasing, not guesses)?
3. What do you deliver today, to how many clients per month at most, and how fast does a client see a first result?
4. Roughly what monthly revenue / cash buffer does the business run on? (Only to check that guarantees are affordable — "rather not say" is fine; guarantees are then marked UNVERIFIED.)

Never invent customer objections or phrasing: if the user cannot give real objections, design guarantees from the ones they do give and list the rest as a gap. State in the deliverable which context was missing. Afterwards, suggest `/icp-builder` (for `icp.md`), `/brand-voc` (for `voice-of-customer.md`) and `/business-audit` (for `business-profile.md`) to save the missing files for every future run.

## Method in one paragraph

Value = (Dream outcome x Perceived likelihood of achievement) / (Time delay x Effort & sacrifice). Every design decision either raises the top or shrinks the bottom of that equation. A Grand Slam Offer is one so differentiated it stops being compared on price: right problem for the right (green-tier) customer, a stack of high-value/low-cost solutions, risk reversed by guarantees that answer the actual objections, honest scarcity and urgency, and a name that makes the ideal buyer feel called out.

## Instructions

Work through the phases in order. Interview style: batch 3-5 related questions per turn, offer labeled options where a pick is natural (use the environment's question tool if there is one — AskUserQuestion in Claude Code, option boxes in Claude.ai — otherwise numbered questions in chat), confirm inferences instead of re-asking, cap the interview at 2-3 turns total across all phases.

### Phase 1 — Kickoff (1 turn max)

1. **Which offer?** From the argument if given (e.g. `/brand-offer growth audit`). Design **one offer per run**. If the business has several distinct offers (a ladder or multiple standalone offers), each gets its own `offer-<slug>.md` indexed by an `offer.md` **router** — see `references/context-routing.md`. Confirm which offer this run designs, and whether it is the business's only/first offer (→ a plain `offer.md`) or an addition to a multi-offer set (→ router + sub-file).
2. **New or redesign?** If `offer.md` exists, list what it currently claims and ask what triggered the redesign (poor conversion, price pushback, new capacity, new segment).
3. **Funnel stage and conversion goal** — what traffic does this offer convert (TOF/MOF/BOF) and to what action (booked meeting, trial, purchase)?
4. **Hard commercial facts only the user knows:** current/intended price and billing model, real delivery capacity per month, honest time-to-first-value, and any existing guarantee. Never invent or "suggest" a price as fact — you may present pricing logic, but the number is the user's decision.

### Phase 2 — Harvest the context (silent)

Before asking anything else, extract from the inherited files:

| Source | Pull | Feeds |
|---|---|---|
| `icp.md` §5 emotional layer + §6 green tier | worries, desired identity, green criteria, red disqualifiers | Dream outcome, section 7 (for/not for) |
| `voice-of-customer.md` §2 pains + §3 value drivers | verbatim after-state and praise language | Dream outcome wording, stack component framing |
| `voice-of-customer.md` §4 objections & fears | each objection with its quote and what's behind it | Guarantee design (Phase 4), bonus design, objection table |
| `voice-of-customer.md` §6 diction | words they use / never use | Offer naming, pitch wording |
| `business-profile.md` | services, team, capacity, goals | Stack feasibility, honest scarcity |

Classify what you now hold as Confident / Tentative / Missing. Interview only tentative and missing items.

### Phase 3 — Value equation (build each variable)

Draft all four variables, grounding every line in harvested context or user answers:

1. **Dream outcome (maximize):** the after-state in the customer's own words (quote VoC), one measurable promised result (specific and honest), and the status gain for the buying role (from icp.md emotional layer).
2. **Perceived likelihood (maximize):** the mechanism explained simply (why it works for THEM), proof attached to the promise (only real cases/numbers the user confirms exist — unproven claims go to the proof-gaps list, not the copy), and the risk reversal (points at Phase 4 guarantees).
3. **Time delay (minimize):** time to first value, honest time to full result, and concrete moves that shorten it (onboarding, done-for-you elements, a designed quick win in week one).
4. **Effort & sacrifice (minimize):** the honest list of what the customer must actually do, what you take off their plate, and how switching cost is handled.

If any variable is weak, say so and propose offer changes that fix it (e.g. add a done-for-you component to cut effort) — improving the offer itself beats improving the wording.

### Phase 4 — Stack, enhancers, guarantees, name

**a) Offer stack & pricing.** List every component with what it is, the outcome it drives, and a defensible standalone value (what it would genuinely cost to buy or build separately — inflated fantasy values are banned). Trim components that are high cost to deliver but low perceived value; prefer high-value/low-cost additions. Sum the stack, state the user's price, and anchor it against the cost of the problem, alternatives, and DIY.

**b) Bonuses.** Each bonus must do a job: neutralize a named objection from VoC §4 or solve the next problem the customer will hit after buying. Name each bonus with its own outcome. No filler bonuses.

**c) Scarcity & urgency.** Only if TRUE (verified against real capacity from business-profile.md or user statement): limited client slots, cohort dates, price-change dates. Fabricated countdowns and fake "only 3 left" are a hard stop — an offer document with false scarcity poisons every downstream asset.

**d) Guarantees — designed from objections.** Take the top objections from `voice-of-customer.md` §4 and map each to a guarantee type:

| Objection pattern | Guarantee type to consider |
|---|---|
| "How do I know it works / we tried X before" | Conditional results guarantee (outcome by date, or work free / money back) |
| "Too expensive / risky spend" | Unconditional money-back window, or pay-per-result terms |
| "No time / too much work for us" | Service-level promise (we do X by Y, or Z happens) |
| High-trust service where refunds attract bad-fit buyers | Anti-guarantee ("all sales final, here is why") stated with confidence |

Write the exact wording, the conditions the customer must meet, and the internal logic for why it can be afforded. **Run the afford-logic check (`references/guarantee-check.md`) against `business-profile.md` (or the user's answers) before finalizing** — name the worst-case liability (e.g. "work free until leads flow" = delivery cost × clients who hit the trigger) and compare it to the business's cash/capacity; surface any **RISK** verdict with the number and offer a safer structure (cap it, gate it, or make it pay-per-result). Every guarantee must be operationally honorable — the user confirms each one explicitly before it goes in the file.

**e) Naming.** Draft 2-3 name options using the Hormozi MAGIC checklist — Magnetic reason why, Announce the avatar, Give a goal, Indicate a time interval, Container word (challenge, blueprint, system, sprint, accelerator) — written in the customer diction from VoC §6 and respecting the negative rules in `brand-guidelines.md` if one exists. Not every element is mandatory; clarity beats cleverness.

### Phase 5 — Objection handling and fit boundaries

1. Build the objection table: every VoC §4 objection in the customer's words, answered with offer mechanics (a stack component, guarantee, or proof asset), not spin. An objection with no offer element that neutralizes it is a design gap — flag it and propose a fix.
2. Write "This is for you if / This is NOT for you if" from the icp.md green and red tiers, in customer-facing language. Disqualifying openly is mandatory, not optional.

### Phase 6 — Checkpoint (human in the loop)

Present the draft offer as a compact one-pager in chat: name, one-sentence pitch, value equation highlights, stack table with price, guarantees, scarcity/urgency, for/not for. Ask for confirmation or corrections — especially price, guarantees, and any capacity claims. Only after an explicit yes, write the file.

### Phase 7 — Fill and deliver offer.md

Fill `assets/offer-template.md` section by section (1 Offer summary → 8 Sources & freshness; drop the template's HTML how-to comment) and deliver it as a downloadable file named exactly `offer.md`. In Claude Code, save it in the working-folder root. Then say: **"Add this file to your Claude project so every other Growth OS skill uses it."** (Svenska: "Lägg filen i ditt Claude-projekt så använder alla andra Growth OS-skills den.") Nothing is published or sent anywhere. Rules:

- **Multi-offer businesses use the router pattern** (`references/context-routing.md`): deliver this offer as `offer-<slug>.md` plus a new or updated `offer.md` **router** index (★ the primary offer), as separate downloadable files. A single-offer business gets one plain `offer.md`. Either way, other skills inherit the right file.
- Keep the template's structure and all eight sections; no section deleted.
- Section 5 proof table lists only real, user-confirmed assets with their permission status; everything unproven goes under "Proof gaps".
- Section 8 records which icp.md/voice-of-customer.md versions fed it, today's date, and a review cadence.
- Close by listing the Lite skills that now inherit this file (`/copywriting`, `/cro-audit`, `/leadmagnet-ideate`, `/ads-audit`) and any proof gaps to collect before the boldest claims may be used in copy.

> **Next step in the full version:** `/landingpage-build` and `/ads-create` turn `offer.md` into pages and ads — they are in the Growth OS Skills Pack (246 skills). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

## Output

| Deliverable | File / location | Purpose |
|---|---|---|
| Offer context file | Downloadable `offer.md` (Claude Code: working-folder root) — or `offer-<slug>.md` + an `offer.md` router for multi-offer businesses (`references/context-routing.md`) | Added to the Claude project; inherited by every other Growth OS skill |
| Offer one-pager | in chat (Phase 6 checkpoint) | Human-readable summary for approval and sharing |
| Gap list | in chat | Proof gaps + missing context, each mapped to the skill or action that closes it |

All deliverables in the user's language.

## Quality gates

- **Never invent facts:** no fabricated case studies, results, customer quotes, prices, or capacity numbers. Unproven claims live in "Proof gaps", never in the offer copy.
- **Statistics require a named source + URL.** A number without a source is a hard stop.
- **Scarcity and urgency only if TRUE** and verified with the user. Fake limits are a hard stop.
- **Every guarantee is operationally honorable** and explicitly confirmed by the user, with conditions and afford-logic written down — run the afford-logic check (`references/guarantee-check.md`) against `business-profile.md` or the user's cash/capacity answers; a solvency-risk guarantee is flagged with the number, never shipped silently.
- **Price is the user's decision.** Present anchoring logic; never state an invented price as fact. This skill gives offer mechanics, not financial advice.
- **Standalone values in the stack must be defensible** (real market price of the component), not inflated.
- **Objections come from voice-of-customer.md** (or user-supplied verbatims) — never from imagination.
- **Checkpoint before writing:** the Phase 6 one-pager must be approved before `offer.md` is delivered.
- **Plain, human prose:** no AI-tells (no "delve/leverage/unlock", no rule-of-three spam, no inflated symbolism), and obey the negative rules in `brand-guidelines.md` if one exists. For a deeper pass, run `/humanizer` on the pitch.
- **Max 2-3 interview turns.** Feel like a strategist who read the research, not a form.

## Example

**User:** "Designa vårt erbjudande för growth-audit-tjänsten"

**Flow:** Context loading finds `icp.md` and `voice-of-customer.md` in the Claude project, no existing `offer.md` → Kickoff (in Swedish) confirms the audit offer, BOF/booked-meeting goal, price 25 000 SEK, capacity 6 audits/month → silent harvest maps VoC objection "vi har testat byråer förut och det gav inget" to a conditional results guarantee and the pain quotes to the dream outcome → one interview turn confirms honest time-to-first-value (14 days) and which case studies are approved for use → value equation, 4-component stack with defensible values, one bonus that answers the "no time" objection, true scarcity (6 slots/month), guarantee wording confirmed by user → afford-logic check: conditional guarantee capped at one extra month of work per client → PASS against the cash buffer in `business-profile.md` → Swedish one-pager approved in chat → `offer.md` delivered as a download with two proof gaps flagged (no published review profile; ROI claim lacks a documented case) and the line "Lägg filen i ditt Claude-projekt så använder alla andra Growth OS-skills den."
