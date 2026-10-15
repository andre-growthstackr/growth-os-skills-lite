---
name: brand-positioning
description: >
  Market positioning strategy using April Dunford's 5+1 framework, enriched with
  JTBD discovery, Moore's positioning statement, and Neumeier's Onliness Test.
  Inherits ICP and competitor research as inputs, runs competitive-alternatives
  and market-category research, and produces a complete positioning document,
  positioning statements, competitive alternatives map, category analysis, and
  messaging implications. Use when user says "positionering", "hur ska vi
  positionera oss", "differentiera oss från konkurrenterna", "hitta vår unika
  position", "positioneringsdokument", "positioning", "positioning statement",
  "differentiation strategy", "unique value proposition", "market category".
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: brand-os
---

# Brand Positioning

Market positioning strategy that produces a complete positioning document, Moore + Neumeier positioning statements, a competitive alternatives map, market category analysis, and messaging implications. Built on April Dunford's framework, enriched with JTBD discovery, stress-tested with Neumeier's Onliness Test and an optional devil's-advocate critique.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `icp.md` — Ideal Customer Profile (tiers, firmographics, pains) — OPTIONAL, strongly recommended: seeds Best-Fit Customers and JTBD discovery
- `voice-of-customer.md` — verbatim customer language, objections, triggers — OPTIONAL: seeds the language map and Value Themes
- `offer.md` — offer, pricing, guarantees, proof — OPTIONAL: feeds Unique Attributes and value anchoring
- `business-profile.md` — company, services, goals — OPTIONAL: feeds intake
- Competitor research outputs (from `/competitor-research`): `competitor-matrix.md`, `competitors-report.md`, `battle-cards/`, `pricing-landscape.md`, or any competitor matrix the user has — OPTIONAL, strongly recommended: seeds the competitive alternatives map
- `brand-guidelines.md` — tone, negative rules (banned AI words), any existing positioning/narrative — OPTIONAL (use if present; Lite continues without it): existing positioning becomes a hypothesis to test

**Minimum context if files are missing** — no file is hard-required (the intake and research phases cover gaps). If nothing is found, the four Round 1 intake questions in step 1 are the minimum context: product in one sentence, problem and for whom, what customers do instead today, and who your best existing customers are. Ask them and continue.

If BOTH `icp.md` and competitor research are missing, tell the user output quality will be lower and offer to run `/icp-builder` and/or `/competitor-research` first; if they decline, continue and flag the gap in the deliverables. Never invent brand/customer facts. Afterwards, suggest `/icp-builder`, `/brand-voc` or `/competitor-research` for whichever input was missing, so every future run inherits it.

**Router-aware — position ONE motion at a time.** If `icp.md` (or `offer.md`) is a **router** (an index pointing to several `icp-<slug>.md` / `offer-<slug>.md` variants), resolve which one this run targets before positioning: take an explicit `--icp <slug>` / `--offer <slug>` argument, else ask which entity / motion / ICP to position for (listing the router's rows — use the environment's question tool if there is one, AskUserQuestion in Claude Code or option boxes in Claude.ai, otherwise numbered options in chat), else use the ★ default. Company-level positioning that blends two distinct motions is a known failure mode — scope the whole deliverable to the selected variant and name it in the output.

### Language

Respond and produce deliverables in the user's language. Instructions and reference files stay in English; output follows the user.

---

## How It Works

```
CONTEXT LOAD → INTAKE → RESEARCH DEPTH → RESEARCH (2 waves, run in sequence) → CHECKPOINT → SYNTHESIS (Dunford 5+1) → VALIDATION → VERIFICATION → (optional) DEVIL'S-ADVOCATE CRITIQUE
```

Understand the product and its customers, research competitive alternatives and market context, then build positioning through Dunford's 5+1 components. Everything runs in this one conversation; typical runtime 20-30 minutes.

Read `references/honesty-protocol.md` at the start of every session.

---

## Instructions

### 1. Intake

Short and focused — 1-2 rounds of questions. The goal is enough context to research alternatives and build positioning.

**Check inherited context first.** If context files or competitor research exist (see Context loading above):

- Extract the product description, known competitors, and customer pain points
- Use competitor profiles and battle cards to seed the competitive alternatives map
- Pull any existing positioning work (e.g. from `brand-guidelines.md`, a strategy doc or the website the user points to) as a starting hypothesis to test, not a conclusion to keep
- Use ICP tiers and VoC language to inform JTBD discovery and Best-Fit Customers

Tell the user: "I found existing context (list files). I'll use it as a starting point for positioning analysis." Skip redundant intake questions. Go straight to research if inherited data is sufficient.

**What to ask (only for gaps):**

Round 1 — Core context:
- What's your product? (one sentence is fine)
- What problem does it solve and for whom?
- What do your customers do today instead of using you? (alternatives, workarounds, doing nothing)
- Who are your best existing customers? (describe them, not demographics)

Round 2 — Sharpening (only if needed):
- How is your product different from the alternatives you mentioned?
- Have you tried positioning before? What didn't work?
- Are there competitors you're often compared to?

Don't over-interview. If the user gives a clear description upfront, move to research.

**Output:** a brief intake summary — product, problem, alternatives, customers, and which inherited context files were used. Project name: kebab-case.

Track progress: project name, skill name (`brand-positioning`), start date, language, research mode (Live / Knowledge-Based), and a phase checklist. In Claude Code, save these as `work/reports/{project-name}/intake.md` and `PROGRESS.md`, update PROGRESS.md after each phase, and resume from the last incomplete phase if it already exists. In Claude.ai, keep the intake summary and a short progress note in the conversation.

### 2. Research Depth Assessment

> Read `references/research-scaling.md` for the complexity scoring matrix, tier definitions, wave configurations, and the user communication template.

1. Score three factors from intake: market breadth (1-3), known competitors (1-3), geographic scope (1-3)
2. Sum (range 3-9) and map to a tier: Light (3-4), Standard (5-7), Deep (8-9)
3. Present the Research Depth table to the user (exact template in `research-scaling.md`)
4. Wait for user response: **light**, **deep**, or **ok**
5. Record the selected tier in the progress note

The tier determines research passes per wave and search rounds per pass in step 3.

### 3. Research (two waves, run in sequence)

**How it runs:** you run every research pass yourself, one after another, in this conversation, using the briefs in the wave files. If your environment can run subagents you may parallelize the passes within a wave; otherwise run the waves in sequence — same depth, just slower.

**Web search:** this skill needs live data (built-in web search and web fetch; no external tools needed). If web search is unavailable or denied, fall back to **Knowledge-Based Mode**: use training data, mark all findings with **[Knowledge-Based — verify independently]**, reduce confidence ratings by one level, and note the mode in the deliverable (and in PROGRESS.md when working in Claude Code).

> Read `references/research-principles.md` before starting any wave — source quality tiers, cross-referencing rules, data gaps.

**Wave 1: Competitive Alternatives & Customer Context** — read `references/research-wave-1-alternatives.md` for the research briefs.

- **A1: Alternative Mapping (JTBD lens)** — Map ALL competitive alternatives, not just direct competitors: direct competitors, adjacent tools competing for the same budget, manual processes, spreadsheets, hiring someone, doing nothing / status quo. For each: what job does the customer hire it for, where does it fall short, what triggers switching? Seed with inherited competitor research instead of re-discovering it.
- **A2: Customer Intelligence** — Mine voice-of-customer data: reviews, forums, communities. Extract pain points, exact customer language, what "better" means, best-fit customer profile, switching triggers. Build a **language map**. Seed with inherited `voice-of-customer.md` and `icp.md`; research fills gaps and validates.

**Wave 2: Market Frame & Trends** — read `references/research-wave-2-market-frame.md` for the research briefs.

- **B1: Market Category Analysis** — Identify 3-5 candidate categories. For each: buyer expectations, leaders, competitive dynamic, maturity. Apply Dunford's category types: head-to-head, big fish/small pond, or category creation. Assess which frame makes the unique strengths matter most.
- **B2: Trend & Timing Analysis** — Identify relevant trends (technology, behavior, regulation). For each: real or hype, effect on buyer expectations, does it strengthen or weaken the positioning? Assess timing — early, on-time, or late to the trend. Only include trends that genuinely change how buyers evaluate solutions.

Each pass produces raw notes (`alternative-mapping.md`, `customer-intelligence.md`, `market-categories.md`, `trends-timing.md`) — in Claude Code saved under `work/reports/{project-name}/raw/`, in Claude.ai kept as working notes in the conversation. Raw notes are inputs to synthesis, never deliverables.

### 4. Post-Research Checkpoint

Before synthesis, present in ONE message: the alternative landscape (counts of direct / adjacent / status quo), the strongest customer pains, and the most promising category candidates. Ask: "Does this align with your expectations? Anything to adjust before I synthesize the positioning?"

### 5. Positioning Synthesis (Dunford 5+1, in order)

> Read `references/research-synthesis.md` for the synthesis protocol and `references/frameworks.md` for the Dunford/Moore/Neumeier/JTBD/Ries reference.

The sequence matters — each step builds on the previous:

1. **Competitive Alternatives** — from Wave 1. What would customers use if the product didn't exist? Positioning is always relative.
2. **Unique Attributes** — what the product has that alternatives lack. Specific and honest: features, architecture, team expertise, business model, speed.

   **PAUSE — user input required.** Present the research-derived attributes. Ask the user to confirm, add, or remove before proceeding. The founder knows capabilities research can't surface.

3. **Value Themes** — translate each attribute into a customer outcome (attribute → "so what?" → value). Group into 2-3 themes. Use customer language from the Wave 1 language map / VoC file.
4. **Best-Fit Customers** — who cares most about the value themes? Define by characteristics that make them care, not demographics. They should be reachable, recognizable, and willing to pay. Cross-check against `icp.md` green tier; flag any mismatch to the user rather than silently overriding either.
5. **Market Category** — choose the frame that makes the value obvious. Present 3-5 options with trade-offs, recommend one.
6. **Trend Overlay (optional)** — only if a genuine trend strengthens the positioning. Forced trend alignment is worse than none.

### 6. Validation (two stress tests)

**Neumeier Onliness Test:**

> Basic: "Our [product] is the only [category] that [differentiator]."
> Extended: "Our [product] is the only [category] that [differentiator] for [target] who [need] in [context]."

If "only" feels like a stretch, the positioning is too weak. Iterate.

**Ries/Trout Mental Ladder:** simple enough to remember? Claims one clear rung? Is that rung available (not owned by a competitor)? Explainable in one sentence?

If either test fails, revisit the 5+1 components. Don't ship weak positioning.

### 7. Verification pass

> Read `references/verification-pass.md` for the full protocol.

Run the verification pass **V1** yourself, re-reading every deliverable with critical eyes (if your environment can run subagents you may hand it to one): unlabeled claims, internal contradictions, confidence rating consistency, missing data gaps, missing flags, stale data, duplicate-source false corroboration, plus positioning-specific checks (statement vs. research data, JTBD vs. customer intelligence, cross-deliverable coherence, validation test integrity). Produce `verification-report.md`.

- Critical issues → pause, present to the user, ask: fix first or proceed as-is?
- Only warnings/info → one-line summary.

### 8. Optional: devil's-advocate critique

After verification, offer one harder stress test, run in this conversation: critique the positioning in turn as three voices — **system thinker** (does it hold together across offer, ICP and category?), **pragmatist** (can sales and marketing use it on Monday?), **contrarian** (where would a sharp competitor or skeptical buyer break it?) — with the rule "prove every line or cut it." Recommend it especially for crowded markets, category creation candidates, or when the Onliness Test only barely passed. Show the critique, let the user accept or reject each point, and fold accepted outcomes back into the deliverables.

> **Next step in the full version:** `/brand-audit` runs this as a multi-round debate and `/brand-messaging` turns the positioning into a full messaging house — both are in the Growth OS Skills Pack (246 skills). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

### 9. Hand the positioning to other skills (with approval)

Nothing is written into existing context files silently. Offer two options and act only on an explicit yes:

- **Add `positioning-statement.md` to the Claude project** (Claude Code: keep it in the working folder) so skills like `/copywriting`, `/website-audit` and `/thought-leadership` can use the category label, onliness statement and messaging direction.
- **If a `brand-guidelines.md` exists**, show the exact positioning text you would add or replace in it, and on approval deliver the updated `brand-guidelines.md` as a downloadable file for the user to swap in. Never overwrite existing brand context without an explicit yes.

---

## Output

Deliver the files below in chat and as downloadable `.md` files. In Claude Code, save them under **`work/reports/{project-name}/`** in the working folder (every `{project-name}/` path in the reference files is relative to that). Nothing is published or sent anywhere. Every deliverable starts with `# {Title}: {product}` followed by `*Skill: brand-positioning | Generated: {date}*`, and ends with Red Flags, Yellow Flags, and Sources sections (templates in `references/research-synthesis.md`).

| File | Contents |
|---|---|
| `positioning-doc.md` | Executive summary (positioning in 3 sentences), the 5+1 components with evidence, strength assessment per component (Strong / Moderate / Needs Work), strategic recommendations, data gaps and limitations |
| `positioning-statement.md` | Moore template ("For [target] who [need], [product] is a [category] that [benefit]. Unlike [alternative], we [differentiator]."), Neumeier Onliness statement (basic + extended), 30-second elevator pitch, tagline candidates with a "Possible Misread" column, one-liner variants per channel, freemium positioning if applicable |
| `competitive-alternatives.md` | All alternatives (direct, adjacent, manual, status quo); per alternative: job hired for, strengths, shortcomings, switching triggers; unique attributes vs. each |
| `market-category-analysis.md` | 3-5 candidate categories with buyer expectations, category type assessment, recommendation with reasoning, implementation notes, red/yellow flags |
| `messaging-implications.md` | Messaging hierarchy, exact category label, value anchor, customer language vs. category language map, words to use/avoid, social proof guidelines, freemium positioning if applicable |
| `verification-report.md` | Verification pass findings |
| `raw/` | Raw research notes (Claude Code only; never shown as deliverables) |

---

## Quality gates

1. **Honesty protocol is binding** (`references/honesty-protocol.md`): label every claim, quantify where possible, declare gaps. No aspirational positioning — position on what the product IS today. Research wins over narrative.
2. **Statistics require source + URL.** A number without a source is a hard stop, not a footnote. Knowledge-based findings are labeled as such.
3. **Never invent brand/customer facts.** Missing context is surfaced ("no VoC data — objections section omitted"), never papered over.
4. **Validation tests must pass** (Onliness + Mental Ladder) before deliverables are finalized. Weak positioning doesn't ship.
5. **Category creation is flagged as high risk** by default. Most companies can't afford to educate a market — default to existing categories or subcategories unless evidence is overwhelming.
6. **Copy quality:** taglines, one-liners, and messaging follow humanizer principles (no AI-tells, no "unlock/leverage/delve", no rule-of-three spam) and any negative rules in `brand-guidelines.md`.
7. **Human in the loop:** unique attributes confirmed by the user (step 5.2), critical verification issues surfaced (step 7), and context files are only updated after explicit approval (step 9).

**Anti-patterns to challenge** (full table in `references/honesty-protocol.md`):

| Anti-pattern | What to say |
|---|---|
| "We're for everyone" | "If you're for everyone, you're for no one. Who cares MOST?" |
| Feature-based positioning | "Customers don't buy features. What outcome do they get?" |
| Aspirational positioning | "Position on what you deliver today, not the roadmap." |
| Category-of-one | "New categories cost millions. Is there an existing frame?" |
| Copycat positioning | "You can't out-position the leader — find genuinely different ground." |

---

## Reference files

Read only what the current phase needs (progressive disclosure):

| File | When | Purpose |
|---|---|---|
| `references/honesty-protocol.md` | Session start | Full honesty protocol + anti-patterns |
| `references/research-scaling.md` | After intake | Complexity scoring, tiers, wave configurations |
| `references/research-principles.md` | Before research | Source quality, cross-referencing, data gaps |
| `references/research-wave-1-alternatives.md` | Wave 1 | Research briefs: alternatives + customer intel |
| `references/research-wave-2-market-frame.md` | Wave 2 | Research briefs: categories + trends |
| `references/research-synthesis.md` | After waves | Synthesis protocol, Dunford process, validation, messaging |
| `references/frameworks.md` | During synthesis | Dunford/Moore/Neumeier/JTBD/Ries reference |
| `references/verification-pass.md` | After synthesis | Verification protocol + skill-specific checks |
| `references/context-loading.md` | Session start | Where to find context files and what to do when they are missing |

---

## Examples

**Example 1 — with inherited context (Swedish user):**

> User: "/brand-positioning — hur ska vi positionera vår bokningsplattform?"
>
> The skill finds `icp.md`, `voice-of-customer.md`, and `competitor-matrix.md` (from `/competitor-research`) in the Claude project. It confirms: "Jag hittade befintlig kontext (icp.md, voice-of-customer.md, competitor-matrix.md) och använder den som utgångspunkt." Intake shrinks to two gap questions, research depth lands on Standard (score 6), the two waves run one after another, and after the checkpoint it synthesizes the 5+1 components — pausing for the user to confirm unique attributes. Deliverables are written in Swedish. The Onliness Test barely passes, so it runs the devil's-advocate critique, folds in two accepted points, and suggests adding `positioning-statement.md` to the Claude project.

**Example 2 — cold start (English user):**

> User: "Help me figure out how we're different from competitors."
>
> No context files exist. The skill warns that ICP and competitor research would improve the output and offers `/icp-builder` and `/competitor-research` first. The user declines, so intake runs in full, research runs in Live mode with web search, and the positioning document flags the missing ICP as a data gap instead of guessing.
