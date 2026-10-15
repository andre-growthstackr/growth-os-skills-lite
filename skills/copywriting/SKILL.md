---
name: copywriting
description: "Conversion copy in the buyer's own words: pages, ads, emails, CTAs. Use for: skriv copy, skriv om vår startsida, skriv en rubrik, write copy, write landing page copy, write a headline."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: design-os
---

# Copywriting — VoC-Driven Copy Engine

Writes copy with the customer's own words instead of the brand's. Pragmatic peer voice,
never agency pitch. This is the central copy engine of Growth OS Lite: other skills (for
example `/socialpost-writer`, `/blog-write`, `/leadmagnet-create`) can pass a format and
its constraints; this skill supplies the method and the voice.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `voice-of-customer.md` — verbatim customer language, pains, objections, triggers, diction
  (REQUIRED — the raw material of every line; if missing, collect real customer language with
  the questions below)
- `icp.md` — Ideal Customer Profile: tiers, firmographics, pains (OPTIONAL — sharpens audience
  and vocabulary tier)
- `offer.md` — offer, pricing, guarantees, proof (OPTIONAL — the only allowed source of proof
  points, prices and guarantees besides the user)
- `business-profile.md` — company, services, goals (OPTIONAL)
- `brand-guidelines.md` — tone and negative rules such as banned words (OPTIONAL — use if
  present; Lite continues without it and uses the default tone profile)

**Minimum context if files are missing** — ask these and continue (use the environment's
question tool if there is one, AskUserQuestion in Claude Code or option boxes in Claude.ai;
otherwise numbered questions in chat):
1. Paste 3–5 real things customers have said or written: reviews, emails, sales-call notes,
   support tickets, survey answers. (Or give me a public review page and I'll pull quotes
   with web search / web fetch and cite each source.)
2. In the buyer's words: what problem made them start looking, and what had they already tried?
3. What is the most common objection or hesitation you hear before someone buys?
4. Who is the reader (role, company type) and what is the one action the copy should drive?
5. Any words or claims that are off-limits for your brand?

Use only what the user gives or what you can cite. If none of the answers contain real
customer language, say so plainly, write the draft, and mark it "not VoC-anchored — validate
with real customer quotes before using". Afterwards, suggest `/brand-voc` to save a full
`voice-of-customer.md` for every future run (and `/icp-builder` or `/brand-offer` if those
files were missing too).

## Core principle

Copy problems are research problems. The buyer's own phrasing of the pain — collected in
`voice-of-customer.md` — is the raw material. Use it verbatim or near-verbatim as often as
you can. Never paraphrase away a powerful formulation because it feels "too raw": the
rawness is exactly what makes copy stop sounding like an agency and start sounding like a
peer who has sat in the same chair.

The winning voice is an experienced peer, not a vendor pitching. When in doubt, lean
toward "we know how this feels" over "we have the solution".

## Scope as argument

The first argument selects the format; the rest is the topic or brief. **Rewriting an existing
page?** First read the current copy: web fetch the URL, or ask the user to paste the text or
upload a screenshot. Keep what already works, and rewrite against it.

| Invocation | Behavior |
|---|---|
| `/copywriting` | Ask which format and topic, then proceed |
| `/copywriting hero [topic]` | Hero section / headline block |
| `/copywriting ad [platform] [topic]` | Ad copy (Meta, LinkedIn, Google...) |
| `/copywriting email [topic]` | Cold or nurture email |
| `/copywriting landing [topic]` | Full landing page copy |
| `/copywriting post [topic]` | Social post |
| `/copywriting script [topic]` | Sales or video script lines |
| `/copywriting cta [topic]` | CTAs and microcopy |
| `/copywriting objection [objection]` | Objection handler |

In Claude.ai (no slash commands) the user just asks, e.g. "write three ad hooks for LinkedIn
about X"; infer the format the same way. Read only the matching section of
`references/formats.md` for format-specific structure. When another Growth OS skill routes
copy through this one, it passes the format and any platform constraints (character limits,
policy rules) as part of the brief.

## Instructions

Respond and produce deliverables in the user's language. Keep VoC quotes in their
original language — do not translate a verbatim quote into marketing-speak.

1. **Load context** (block above). From `voice-of-customer.md` (or the quotes collected in
   chat) extract the parts you will draw from: pains, value drivers, objections and fears,
   triggers, and language and diction. If `brand-guidelines.md` exists, extract its tone
   description and every negative rule (banned words, banned characters, banned
   constructions).
2. **Build the banned list** for this task. Union of: brand-guidelines negative rules (if the
   file exists) + words the user said are off-limits + the VoC "words they never use" list +
   the generic AI-tell list in Quality gates below. This list is a hard filter, not a
   preference.
3. **Set the tone profile.** Map the brand's tone onto the four NNGroup dimensions using
   `references/tone-dimensions.md`. If `brand-guidelines.md` defines tone, derive the
   profile from it; otherwise use the reference defaults, calibrated by the VoC tone
   observations, and say so in the delivery.
4. **Identify the trigger or pain** the copy must address. Pick it from the VoC pains or
   triggers — a concrete, sourced one. Never a generic pain you assume.
5. **Select 1–3 verbatim quotes or fragments** from the VoC material to work into the copy,
   verbatim or with minimal repackaging. These anchor the peer voice.
6. **Draft.** Use the three core templates below when the format fits; for full formats
   follow the matching playbook in `references/formats.md`. Keep the buyer's perspective
   ("stop being blindsided in the Monday meeting"), not the vendor's ("we help you gain
   management's trust"). For short formats (headline, hook, CTA) produce 3 variants; for
   long formats produce 1 draft plus 2 alternative angles for the opening.
7. **Run every quality gate** (section below). Fix, do not flag-and-ship: a gate failure
   means rewrite before delivery.
8. **Deliver** per the Output section. If any gate result was borderline, say so
   explicitly rather than delivering silently.

## The three core templates

Proven structures. Use them directly when the format fits; for longer formats use them as
building blocks. Examples are illustrative placeholders — real copy must pull its facts
and quotes from the context files or the user.

### Template 1 — Hero

Structure: `[Specific trigger]. [Buyer's own phrasing of the pain]. [Context, not solution].`

The third sentence is where the peer voice confirms the buyer is not alone. Never jump to
the solution there.

> Illustrative: "The forecast meeting is Thursday. The pipeline number is a guess, again.
> Most of the marketers we talk to are carrying that same number alone."

### Template 2 — Objection handler

Structure: `We know you tried [specific past investment]. It did not work. That is not on you.`

Built to neutralize the "we tried something like this before" objection (VoC objections
section). The concreteness in the first sentence is what makes it land — name the actual
category or vendor type from the VoC data, never an abstract "previous solutions".

> Illustrative: "You have run the campaigns and paid the retainers. It did not move
> pipeline. That is not you failing. The setup was built for a buyer who no longer exists."

### Template 3 — Value formulation

Structure: `[Something that happens this week] — [something that compounds in 6–12 months] — [how it works].`

Binds short-term delivery (which calms a burned buyer) to long-term outcome (which
justifies the investment). Both must be present; either one alone reads as hype.

> Illustrative: "A page that answers the question your sales calls actually start with,
> live this week. The same page keeps pulling in pipeline for years. One research cycle,
> reused everywhere."

## Tone signature (defaults — brand-guidelines.md overrides if present)

- **Concreteness first.** Buyers skim and stop reading at emptiness. Specifics in the
  first sentence, never in the fourth paragraph. No warm-up paragraphs.
- **Specific over vague.** "Many customers" is banned by default: use the real number,
  name, or example from the context files. If no real specific exists, restructure the
  sentence — do not fabricate one.
- **Respect the buyer's diction.** If the VoC shows the buyer mixing languages or using
  English terms (pipeline, CMO, lead), do not force translations they would never say.
- **No hedging.** Cut "maybe", "potentially", "in many cases" unless the buyer's own
  quotes hedge. Directness is the peer signal.
- **The two tests.** If a line would fit a 2015 PowerPoint bullet, cut it. If a colleague
  would say it over coffee, keep it.

## Output

- Deliver copy in chat, in the user's language, with: the copy itself (plus variants),
  which VoC quotes were worked in (with their source), which template or playbook was
  used, and which context was missing (if any).
- Offer it as a downloadable `.md` file. In Claude Code, save to
  `work/copy/<format>-<topic-slug>.md` with a short header: format, audience, VoC quotes
  used, banned-list source, date.
- **This skill never publishes, sends, posts or schedules anything.** The user decides
  where and when the copy goes live.

## Quality gates

Every gate is mandatory on every deliverable. A failed gate means rewrite, not caveat.

1. **Verbatim check.** At least one verbatim or near-verbatim customer formulation from
   the VoC material is worked into the copy. If none fits, you have written agency copy —
   go back to step 4. (Exception: no real customer language was available at all; then the
   delivery carries the "not VoC-anchored" label from Context loading.)
2. **Banned-list check.** Search the draft for every entry on the task's banned list
   (step 2). Zero hits allowed.
3. **Concreteness check.** At least one concrete number, name, or example per paragraph,
   each traceable to a context file or the user's brief. No fabricated numbers, quotes,
   customers, or claims — ever. Statistics require a source and URL or they do not ship.
4. **Humanizer pass.** Strip AI tells: inflated symbolism ("testament to", "stands as"),
   promotional filler ("game-changing", "seamless", "unlock", "delve", "leverage",
   "elevate"), rule-of-three spam, em-dash overuse as a rhetorical tic, negative
   parallelisms ("not just X, but Y"), vague attributions ("experts agree"), and
   superficial "-ing" analysis clauses. If `/humanizer` is installed, run the draft
   through it; otherwise apply these principles inline.
5. **Peer test.** Read the first sentence aloud. Would a colleague say it over coffee, or
   would only an agency write it in a pitch? If the latter, rewrite the opening.
6. **Skim test.** Skim the copy in 3 seconds. The eye must catch concretion (numbers,
   names, the buyer's phrases), not slide over fluff.
7. **Tone check.** Compare against the tone profile from step 3
   (`references/tone-dimensions.md` validation section). Flag any dimension that drifted.

## Examples

**Example 1 — Swedish request, ad hook:**
User: "Skriv en Meta-annons om vår onboarding-tjänst."
Flow: load context → `voice-of-customer.md` and `offer.md` found in the Claude project, no
`brand-guidelines.md` → banned list built from VoC diction + AI-tell list → default tone
profile calibrated by VoC tone observations (stated in delivery) → pain selected from VoC
("onboardingen äter veckor av vår tid" — verbatim, with source) → 3 hook variants drafted
in Swedish using Template 1, each anchored on the verbatim quote → all seven gates run →
delivery in Swedish with quotes and sources listed.

**Example 2 — missing context:**
User: "Write a landing page for our new service."
Flow: no `voice-of-customer.md` found → ask the five minimum-context questions → the user
pastes four review snippets and the top objection → landing page drafted from those quotes
(sources: "user-supplied reviews") → gates run → delivery notes the VoC was a small sample
and suggests `/brand-voc` to build a full `voice-of-customer.md`.
