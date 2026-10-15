---
name: blog-write
description: "Writes a researched, sourced blog post ready for Google and AI answers. Use for: skriv ett blogginlägg, skriv en artikel, write a blog post, write an article about."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: content-os
  source: "blog-write"
---

# Blog Writer — new article generation

Writes a complete blog article from a topic, brief, or outline. Every article targets the two
surfaces that matter in 2026: Google organic ranking (relevance + authority) and AI-assistant
citation (extractable, sourced, quotable).

The rule that makes this skill different from a generic "write me a post": AI has collapsed the
cost of an average draft, so the quality floor is now **information gain** — original data, a
real opinion, or first-hand experience layered on top of the AI draft. A post with none of that
does not rank and does not get cited. This skill refuses to ship without it.

Respond and produce all deliverables in the user's language. The instructions below are in
English; the finished article follows the user's language.

Questions: use the environment's question tool if there is one (AskUserQuestion in Claude Code,
option boxes in Claude.ai); otherwise ask numbered questions in chat.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `icp.md` — Ideal Customer Profile: tiers, firmographics, pains (REQUIRED — audience, angle,
  and search intent are guesses without it)
- `voice-of-customer.md` — verbatim customer language, objections, triggers (OPTIONAL —
  sharpens headlines, FAQ questions, and the answer-first framing to the words buyers use)
- `offer.md` — offer, pricing, guarantees, proof (OPTIONAL — informs the single contextual CTA
  and any product-comparison framing)
- `business-profile.md` — company, services, goals, author E-E-A-T (OPTIONAL — background,
  author attribution, and internal-link targets)
- `brand-guidelines.md` — tone and banned words / characters (OPTIONAL — use if present; Lite
  continues without it and applies the banned-tells list in `references/writing-rules.md`)

**Minimum context if files are missing** — ask these and continue:
1. Who is the reader (role, company type, the problem that brings them to this post)?
2. What question should the post answer, and which keyword or phrase would they search?
3. What real data point, opinion, or first-hand story can we add (the information gain)?
4. What is the one action the reader should take at the end (offer, lead magnet, contact)?
5. Who is the author, and why should the reader trust them on this topic?

Never invent brand, customer, or product facts. Never invent statistics. Afterwards, suggest
`/icp-builder` (and `/brand-voc`, `/brand-offer`, `/business-audit` for the optional files) to
save the missing files for every future run.

## External tools — ask first

This skill works fully without external servers: research and fact-checking run on built-in web
search and web fetch. Follow `references/mcp-permission.md` before the first call.

| Server (optional) | Used for | Requires | Built-in path (no MCP) |
|---|---|---|---|
| Firecrawl | Searching for and scraping statistic sources and top-ranking articles, including JavaScript-heavy pages | A Firecrawl account (uses credits) | Web search + web fetch; if a page cannot be fetched, pick another source or ask the user to paste the text |

Metrics that only exist with a server: none — Firecrawl only improves page retrieval. Search
volume and keyword difficulty are not measured by this skill; if the user asks, say "not
measured" and never estimate them.

Ask once per run, at the start of Phase 2, and only if Firecrawl is already among your tools.

## Style bar

`references/blog-style-exemplar.md` is the quality bar (structure, intro style, formatting), not
the output identity. Ask once, in Phase 1: "Do you have 1–2 articles whose style you like? Paste
or link them." If yes, extract concrete rules (length, intro style, heading pattern, tone) and
apply them on top of the bar — the user's style wins. If no, use the bar.

> **In the full version:** the Growth OS Skills Pack learns your blog style and remembers it across runs, per format. See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

## Scope (argument)

The argument is the topic, optionally followed by audience, primary keyword, and output format:

- `/blog-write "speed-to-lead for B2B SaaS"` → ask for the missing inputs in Phase 1
- `/blog-write "AI Overviews and CTR" CMOs "ai overviews ctr" MDX` → all inputs pre-filled
- If the user pastes a brief or outline, use it and skip the matching questions

---

## Steps

### Phase 0: Surface targeting

Decide which surfaces this post must win before researching. Most posts target three by default:

1. Owned site (organic Google ranking)
2. Search results including AI Overviews
3. AI-assistant citations (ChatGPT, Perplexity, Claude, Gemini, Copilot)

If the same query also surfaces in a community (a Reddit thread, a YouTube comment section),
note it — the post is optimized for extraction here, and a community version can be made
afterwards with `/content-repurpose`. Keep this decision in one line; it shapes length,
citation density, and CTA.

### Phase 1: Brief (inline)

1. Ask only what is missing (max 3–4 questions in one round, defaults pre-filled from the
   context files; never repeat a minimum-context question already answered):
   - Target audience (default from `icp.md`)
   - Primary keyword / search intent. If unknown, run 2–3 web searches on the topic, read the
     top results' titles and headings, and propose a keyword + intent. Search volume is not
     measured — say so if the user asks.
   - Desired word count (default 1,500–2,500 words, matched to what ranks)
   - Format (markdown by default; MDX or HTML if the site needs it)
   - The information-gain material (real data, opinion, or story) and 1–2 style examples
2. Write the brief using the "Inline brief" block in `references/templates-and-outline.md` and
   show it. A quick "ok" is enough to continue.

### Phase 1.5: Template selection

Pick the template from the table in `references/templates-and-outline.md` and tell the user
which one was selected (or that the generic skeleton applies).

### Phase 2: Research

If the user approved Firecrawl in the permission step, use it to search for and scrape sources.
Otherwise use web search to find sources and web fetch to read them. Gather:

1. **6–12 current statistics** (2025–2026 preferred). Search
   `[topic] study 2025 2026 data statistics`. For each, record: the statistic, publisher,
   document title, URL, date, and methodology. Prefer primary and high-authority sources.
   **A statistic with no verifiable source is dropped, not softened** — no exceptions.
2. **What the top 3–5 results cover** — read them, list the common sections, and note what they
   all miss. That gap plus the user's information gain is the angle.
3. **1–3 data visualizations** planned from the researched statistics (optional) — diverse
   chart types, one data story each.
4. **Image plan** — a cover and 3–5 inline image placeholders with alt text (see
   `references/writing-rules.md` 5i).

Never fabricate a number, a source, or a URL to fill a gap. If research comes up short, say so
and narrow the claim to what is verifiable.

### Phase 3: Outline (human approval gate #1)

Draft a structured outline adapted to the selected template, using the skeleton in
`references/templates-and-outline.md`. Mark where each statistic, information-gain marker,
chart, image placeholder, citation capsule, and internal-link zone goes.

**Present the outline and wait for explicit approval before writing.** Do not draft the article
until the user approves the outline.

### Phase 4: Charts (optional)

When the research yields chart-worthy data, build the inline SVG charts per
`references/writing-rules.md` 5j. Skip this phase when the data does not support a chart.

### Phase 5: Content writing

Read `references/writing-rules.md` and write the full article to those rules: frontmatter, Key
Takeaways box, answer-first H2s with the evidence triple, 2–3 information-gain markers, citation
capsules, internal-linking zones, paragraph/sentence/heading rules, image placeholders, charts,
FAQ, and a single CTA. Apply the style bar from the "Style bar" section.

### Phase 6: Quality gates (mandatory — before any delivery)

Run every gate. A failure blocks delivery.

**Structure & sourcing**
1. Every H2 opens with an answer-first paragraph; the major H2s carry a statistic + named source.
2. No paragraph exceeds 150 words.
3. **Fact-check (inline).** For every statistic and every claim about a named company or person:
   open the source URL with web fetch and confirm the number, year, and publisher match the
   draft. Contradicted by a newer source → replace it. Page unreachable or the number is not on
   it → cut the statistic or make the sentence qualitative. **No unsourced numbers.** Every kept
   statistic is listed in the source block with URL and retrieval date.
4. Charts (if any) use diverse types and only verified numbers; image placeholders carry
   descriptive alt text.
5. FAQ present (3–5 items); clean heading hierarchy; meta description 150–160 chars with a stat.

**Information gain (hard gate)**
6. At least 2 genuine information-gain markers (`[ORIGINAL DATA]`, `[PERSONAL EXPERIENCE]`,
   `[UNIQUE INSIGHT]`). If the article cannot clear this with real material, stop and tell the
   user it is thin — do not pad with invented data.
7. Citation capsules present in the major H2 sections.
8. 5–10 internal-linking zones marked across intro, H2s, FAQ, conclusion.

**Voice & humanizer pass (hard gate)**
9. Run the humanizer pass: apply `/humanizer` if it is installed, otherwise strip the banned AI
   tells listed in `references/writing-rules.md` inline.
10. Honor `brand-guidelines.md` negative rules if the file exists — remove every banned word or
    character.
11. Natural contractions used where the language allows; at least one rhetorical question every
    200–300 words; sentence-length variance confirmed.

### Phase 7: Delivery (human approval gate #2)

1. Present the finished draft in chat with the summary below. The Phase 6 gates are the first
   reviewer; the user is the approver.
2. Deliver the article as a downloadable file named `<slug>.md` (or `.mdx` / `.html` if the user
   asked for that format). In Claude Code, save it as `work/blog/<slug>.md` in the working
   folder. Nothing is published, scheduled, or pushed to a CMS — the user publishes it.
3. Apply edits on feedback and re-deliver the file.

Summary template:
```
## Blog post complete: [Title]

Template: [name or "generic outline"]
Statistics: [N] sourced (all fact-checked with web fetch) · [N] unique sources · [N] cut
Visuals: cover placeholder · [N] inline image placeholders · [N] SVG charts ([types])
Information gain: [N] markers ([types]) — real material from the user
AI-citation: [N] citation capsules · [N] internal-link zones
Structure: [N] H2s (answer-first) · [N] FAQ items · ~[N] words · [N] min read
Quality: humanizer pass [done] · fact-check [done] · banned-word scan [pass]
Data: [web search + web fetch of N pages / Firecrawl] · Missing context: [list or "none"]

Next: resolve [INTERNAL-LINK] and [IMAGE] placeholders · /content-repurpose to turn the post
into LinkedIn posts, a newsletter section, a thread, or a short-video script
```

> **Next step in the full version:** `/blog-images`, `/blog-schema` and `/blog-seo` (images, JSON-LD and an on-page score) are in the Growth OS Skills Pack (246 skills). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

## Quality gates (summary)

- **Information gain is non-negotiable** — 2+ genuine markers or the post is flagged thin. Never
  fabricate original data or experience.
- **Every statistic is sourced and fact-checked** with web fetch — no invented numbers, ever.
- **Humanizer pass is mandatory**, plus the `brand-guidelines.md` banned-word list when present.
- **Two human gates**: outline approval before writing, draft approval before it is used.
- Output and all prose follow the user's language.

## Example

**User:** `/blog-write "how speed-to-lead affects B2B conversion" CMOs`

1. Finds `icp.md` and `offer.md` in the Claude project; asks only for keyword, format, one
   real client metric, and an optional style example.
2. Shows the inline brief; detects the how-to / data angle → selects `how-to-guide`.
3. Researches 10 statistics with web search + web fetch (each with publisher, title, URL,
   date), reads the top 4 ranking articles, plans a bar chart and a line chart.
4. Presents the outline → **waits for approval**.
5. Writes the article: answer-first H2s, Key Takeaways box, 3 citation capsules, the client
   metric tagged `[ORIGINAL DATA]`, internal-link zones, 2 charts, 4 image placeholders.
6. Fact-checks every statistic with web fetch (cuts one that the source page does not contain),
   runs the humanizer pass (strips "leverage", "game-changer", an em-dash pileup).
7. Presents the draft + summary and delivers `speed-to-lead-b2b.md` (Claude Code:
   `work/blog/speed-to-lead-b2b.md`) → offers `/content-repurpose` for the follow-up pieces.
