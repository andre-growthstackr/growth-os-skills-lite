---
name: content-repurpose
description: >
  Turns one piece of content into many by adapting it across content types — LinkedIn
  post, X thread, newsletter, email, short-video script, longform video script,
  carousel slide text, blog — never channel-first. Preserves the core message while
  adapting format, length, and platform norms, keeps the voice VoC-driven with the
  /copywriting principles, and runs a humanizer pass. Human in the loop twice: approve
  the repurpose plan before production, approve drafts before distribution. Use when
  user says "repurpose", "repurpose content", "turn this blog into", "atomize content",
  "spin this into a thread", "återanvänd innehåll", "gör om bloggen till", "dela upp
  innehållet", "gör en video av inlägget", "skriv om till nyhetsbrev".
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: content-os
  source: "blog-repurpose"
---

# Content Repurpose — One Source, Many Content Types

Takes a single finished (or drafted) piece of content and adapts it into other content
**types**, preserving the core message while re-fitting format, length, and platform norms.
One research cycle feeds many pieces: a blog becomes a LinkedIn post, a thread, a newsletter
section, an email, a short-video script, and carousel slide text — all delivered as finished
text in this skill.

**Content-type before channel.** You produce a *format* (a short-video script, a carousel, a
newsletter), not a channel-specific post. A short-video script serves Reels, TikTok, and
YouTube Shorts alike; a carousel serves LinkedIn and Instagram alike. Split the work per
content type, never per channel.

**Respond and produce all deliverables in the user's language.** Match the language of the
source content and the user's request; the instructions below are in English for the model,
the output is not.

Questions: use the environment's question tool if there is one (AskUserQuestion in Claude Code,
option boxes in Claude.ai); otherwise ask numbered questions in chat.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `voice-of-customer.md` — verbatim customer language, objections, triggers (REQUIRED —
  repurposing without it re-fits the format but loses the buyer's voice)
- `brand-guidelines.md` — tone and negative rules / banned AI words (OPTIONAL — use if present;
  Lite continues without it and applies the banned-tells list in Step 4)
- `icp.md` — Ideal Customer Profile: tiers, firmographics, pains (OPTIONAL)
- `offer.md` — offer, pricing, guarantees, proof, lead magnet (OPTIONAL — makes CTAs concrete)
- `business-profile.md` — company, services, goals, channels (OPTIONAL)

**Minimum context if files are missing** — ask these and continue:
1. Who is this content for, and what problem does it solve for them?
2. How do your customers describe that problem in their own words (a quote, review, or
   sales-call line, if you have one)?
3. What should readers do at the end (lead magnet, booking, reply, follow)?
4. Any words, emoji, or tone the brand avoids?

Never invent brand or customer facts. State in the delivery which context was missing.
Afterwards, suggest `/brand-voc` (and `/icp-builder`, `/brand-offer`) to save the missing
files for every future run.

## The source

The first argument is the source content: an uploaded file, pasted text, a file path (Claude
Code), or a URL. Read a URL with web fetch; if the page cannot be fetched, ask the user to paste
the text. For a video or podcast, ask for the transcript (pasted or uploaded) — this skill does
not transcribe media. Read the source in full before anything else.

Identify its **native type** (blog, longform video/transcript, shortform script, social post,
carousel, newsletter). Repurposing flows in any direction, but the richest sources (a long blog
or a longform transcript) atomize into the most targets; a single social post rarely fills a
longform video.

If the source is thin, say so and offer to expand it first (for an article, run `/blog-write`)
rather than padding a repurpose with filler.

## Scope as argument — target content types

After the source, the remaining arguments select which content **types** to produce. Omit them
and the skill proposes a set based on the source's richness, then asks.

| Target type | What this skill delivers (as text) |
|---|---|
| `linkedin` | LinkedIn post: hook, body, CTA, hashtags (image idea if it is an image post) |
| `thread` | Numbered X thread (or LinkedIn multi-post), one idea per post |
| `newsletter` | Newsletter issue (subject, preview, body, one CTA) or a section for an existing issue |
| `email` | Standalone email: subject, preview, short body, one CTA |
| `shortform` | Short-video script: hook → setup → payoff → CTA with on-screen cues and duration |
| `longform-video` | YouTube-style script outline with retention arc and visual cues |
| `carousel` | 6–10 slides of slide text + caption |
| `blog` | Quick article version here, or hand-off to `/blog-write` for a full SEO article |
| `all` | Every type the source can genuinely support |

Read only the sections of `references/format-specs.md` for the types requested (progressive
disclosure).

## Steps

### Step 1 — Extract the core (message-preserving)

From the source, pull the reusable substance once, so every target draws from the same well:

- **Core message** — the central thesis in 1–2 sentences. This must survive into every target unchanged.
- **Key points** (5–9) — each a standalone claim that can headline a slide, a post, or a section.
- **Statistics** — every data point *with its source and URL*. Statistics without a source do not travel; drop them rather than repeat an unsourced number.
- **Quotes / first-hand experience** — anything that gives information gain (own data, opinion, lived detail). Preserve these; they stop the repurpose from reading like generic AI.
- **Proof** — case snippets, results, named examples.
- **Primary audience** — who this is for (cross-check against `icp.md` tiers if present).

### Step 2 — Propose the repurpose plan → **HUMAN IN THE LOOP #1**

Before producing anything, present a short plan: the core message, the target types you
recommend for this source, and the angle each will take (the same message re-cut for that
format's job — e.g. the blog's strongest "how" section becomes the short-video script's single
payoff; the three best key points become the thread). **Stop and get explicit approval before
production.** Adjust the plan on feedback.

### Step 3 — Write each target type

For each approved target, write the finished text per `references/format-specs.md`, holding the
core message fixed. Keep the voice VoC-driven: use the buyer's phrases from
`voice-of-customer.md` (or the minimum-context answers) in hooks, subject lines, and CTAs. Apply
the `/copywriting` principles if that skill is installed; otherwise follow the hook/body/CTA
rules in the format specs. For a full SEO article, hand the extracted core to `/blog-write`; for
one post adapted to LinkedIn, Instagram and X at once, `/socialpost-writer` does that job.

> **In the full version:** the Growth OS Skills Pack turns these drafts into finished assets — designed carousels, edited short videos, newsletter and YouTube production, and a content calendar. See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

### Step 4 — Quality gates (every piece, before it leaves the skill)

1. **Message preservation.** The core message from Step 1 is intact and recognizable in every target. A repurpose that drifts off-message is a new piece, not a repurpose — flag it.
2. **Source integrity on stats.** Every statistic carries its source + URL. Open each statistic's source URL with web fetch and confirm the number; statistics that arrived without a source were already dropped in Step 1, and anything that cannot be verified is cut. No fabricated numbers, quotes, customers, or claims — ever.
3. **Voice consistency.** All pieces read as the same brand in the buyer's own words, not one voice per platform.
4. **Banned-list check.** If `brand-guidelines.md` exists, search each draft for every banned word and forbidden character. Zero hits. Same for anything the user named in the minimum-context questions.
5. **Humanizer pass.** Apply `/humanizer` if it is installed; otherwise strip AI tells inline — inflated symbolism, promotional filler ("unlock", "delve", "leverage", "seamless", "game-changing"), rule-of-three spam, em-dash overuse, negative parallelisms ("not just X, but Y"), vague attributions ("experts say") — and their equivalents in the user's language.
6. **No-duplication check.** The pieces are genuinely re-fit to their format, not the same text pasted with different line breaks. Each earns its type.

### Step 5 — Deliver → **HUMAN IN THE LOOP #2**

Show every piece in chat, each under a heading with its type and length/duration. Deliver all
pieces together as one downloadable file named `<slug>.md` (one H2 per target type). In Claude
Code, save it as `work/repurpose/<slug>.md` in the working folder (create the folder if needed).

Open the delivery with a summary: core message, pieces produced (type + length/duration), stats
reused across pieces, and any missing context.

**Nothing is published, scheduled, or sent.** This skill produces drafts. The user pastes the
approved pieces into their own channels, email tool, or video editor.

## Examples

**Example 1 — blog → short + newsletter (Swedish):**
User: "Återanvänd den här bloggen till en short och ett nyhetsbrev." (pastes the blog)
Flow: load context (`voice-of-customer.md` found in the Claude project) → read blog → extract
core (message, 7 points, 3 sourced stats) → propose plan (short = the blog's strongest "how" as
one payoff; newsletter = TL;DR + 3 takeaways) → **approval #1** → write the short-video script
with on-screen cues and the newsletter issue with two subject options → six quality gates →
deliver in chat + `bloggslug.md` (Claude Code: `work/repurpose/bloggslug.md`), summary in
Swedish → **hold for approval #2**; nothing is scheduled.

**Example 2 — missing context:**
User: "Repurpose this post into a carousel and a thread."
Flow: no `voice-of-customer.md` found → ask the four minimum-context questions in one message →
continue with the answers → note in the delivery "no VoC file; voice based on your answers" →
suggest `/brand-voc` at the end.

**Example 3 — thin source:**
User: "Turn this one image caption into a full YouTube video."
Flow: read source → too thin to fill a longform script without invention → say so, offer a
short-video script instead, or ask for a richer source (a blog or transcript). Do not pad the
gap with fabricated points.
