---
name: socialpost-writer
description: >
  Writes the copy for a single image post (hook + body + CTA) and adapts that one
  post to each channel's native norms — LinkedIn, Instagram, and X/Twitter — instead
  of writing channel-first. Builds from your content pillars and the reader's own
  words in voice-of-customer.md, runs the /copywriting frameworks for the hook and
  body, and finishes with a /humanizer pass so nothing reads AI-written. Enforces
  brand negative rules (banned AI words, forbidden characters). Use when user says
  "skriv ett LinkedIn-inlägg", "bildinlägg-copy", "skriv en caption till bilden",
  "text till mitt inlägg", "social post copy", "write a LinkedIn post", "image post
  caption", "Instagram caption", "X post", "hook body cta for a post", "socialpost",
  "/socialpost-writer". Content-type before channel. Does NOT design the image,
  build carousels, or write long video scripts.
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: content-os
  source: "NEW"
---

# Socialpost Writer — the image-post copywriter

Write the copy that rides with an image post — **hook + body + CTA** — then adapt that one post to each channel you publish on. The image stops the scroll; the copy does the converting. This skill owns the words, not the picture.

**Content type before channel.** You write ONE post — one idea, one angle, one point of view — and then reshape it to LinkedIn, Instagram, and X norms. You do not write three unrelated posts. The angle is constant; the length, line rhythm, hashtag load, and CTA style change per surface.

**Respond and produce deliverables in the user's language.** All copy follows the user's language; verbatim customer quotes stay in their original language. Default to Swedish when the brand context is Swedish.

Questions: use the environment's question tool if there is one (AskUserQuestion in Claude Code, option boxes in Claude.ai); otherwise ask numbered questions in chat.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the working folder (Claude Code), then ask.

- `voice-of-customer.md` — verbatim customer language, pains, objections, triggers (REQUIRED — the hook and body are built from the reader's own words, not imagination)
- `content-brand.md` — content mission, **pillars**, and editorial voice rules (OPTIONAL — use if present; Lite continues without it and asks for the pillars instead)
- `brand-guidelines.md` — tone and the **negative rules: banned AI words / forbidden characters** (OPTIONAL — use if present; Lite continues without it; when present its banned list is additive to the forbidden patterns in `references/copy-frameworks.md`)
- `icp.md` — who the reader is, tiers, pains (OPTIONAL — sets vocabulary and the pain framing)
- `offer.md` — the offer, proof, and the lead magnet a CTA might point to (OPTIONAL — makes the CTA concrete instead of "learn more")
- `business-profile.md` — company, services, channels (OPTIONAL — background and which channels the brand actually uses)

**Minimum context if files are missing** — ask these and continue:
1. Who is the post for (role, situation), and what do they struggle with — in their own words if you have them (a customer quote, a review, a sales-call line)?
2. Which 2–4 topics (content pillars) does your brand post about, and which one is this post for?
3. What should the reader do after reading (comment a keyword for a lead magnet, answer a question, click a link, nothing)?
4. Any words, emoji, or characters the brand never uses?

Never invent brand or customer facts. Afterwards, suggest `/brand-voc` (and `/icp-builder`, `/brand-offer`) to save the missing files for every future run.

## Style bar

`references/socialpost-style-exemplar.md` is the quality bar (hook style, line rhythm, length, CTA shape), not the output identity. In Step 1, ask once: "Do you have 1–2 posts whose style you like? Paste, link, or screenshot them." If yes, extract concrete rules and apply them on top of the bar — the user's style wins, field by field. If no, use the bar. If the user gives feedback during the run ("shorter hooks", "drop the emoji"), apply it to every variant.

> **In the full version:** the Growth OS Skills Pack remembers your post style across runs and adds content pillars, angle research and image design (`/content-brand`, `/content-research`, `/socialpost-image`). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

## Arguments

- `/socialpost-writer` — ask for topic, then write for all three channels (default).
- `/socialpost-writer [topic]` — write about that angle for all channels.
- `/socialpost-writer linkedin` (or `instagram` / `x`) — write only that channel's variant.
- Channels are a scope argument — read only the `references/channel-norms.md` sections the scope needs.

## Step 0 — Anchor the post

Read the context. Fix three things before writing a word:

1. **Pillar** — which content pillar or recurring theme this post serves (from `content-brand.md` if present, otherwise from the user's answer; if neither exists, propose 2–3 themes drawn from the ICP pains and VoC and confirm one in Step 1). One post, one pillar.
2. **Angle** — the single point being made (a claim, a lesson, a contrarian take, a story beat). If the user gave a topic, sharpen it to one angle. If not, propose 2–3 angles pulled from VoC pains and ask which one.
3. **The reader's words** — pull the 2–4 most concrete VoC phrases (pains, objections, triggers) that this angle touches. These are the raw material for the hook and body.

## Step 1 — ALWAYS confirm the brief before writing (human in the loop, pass 1)

Before writing anything, present the choices as multiple-choice questions (max 3, pre-filled with smart defaults from the context), plus the one-time style-example question:

1. **Channels** — LinkedIn / Instagram / X / All (default All, unless the argument already set scope).
2. **Angle** — confirm the pillar and angle from Step 0, or pick from the 2–3 proposed.
3. **CTA goal** — comment-keyword CTA (→ DM → lead magnet) / soft engagement (question to the reader) / profile or link click / none. Default to the comment-keyword CTA when `offer.md` names a lead magnet.

If the user already specified everything in their message, skip the questions and write.

## Step 2 — Write the core post: hook + body + CTA (read `references/copy-frameworks.md`)

Write the channel-neutral core first, then adapt in Step 3. Use the `/copywriting` frameworks for the hook and body if that skill is installed; otherwise use the checklist in `references/copy-frameworks.md` — do not free-write.

- **Hook (line 1)** — earns the second line. Pick a proven pattern (VoC pain stated plainly, a specific number, a contrarian claim, an open loop). No warm-up, no "In today's world". The hook must work as the visible preview line before the "…more" cut.
- **Body** — one idea per line, line break after each. Concrete nouns over adjective stacks: tool names, numbers, exact outcomes. Build from the reader's own words. One central analogy at most. Handle the obvious objection inside the body, not after it.
- **CTA** — matches the goal chosen in Step 1. For the comment-keyword CTA: `Kommentera "ORDET" så skickar jag [lead magnet].` (or the user's language) with the payoff in the same sentence. Never "follow for more" begging.

Any statistic in the copy needs a source (from context, the user, or a page you opened with web fetch). Fabricated numbers are a hard stop.

## Step 3 — Adapt to each channel (read `references/channel-norms.md`)

Same angle, native shape. Read only the sections for the chosen channels:

- **LinkedIn** — professional-but-human, hook optimized for the ~140-char "…more" cut, generous line breaks, 0–3 hashtags at the very bottom, CTA usually a comment prompt or lead-magnet keyword.
- **Instagram** — first line is the hook (feed truncates early), warmer and more personal, 3–8 niche hashtags in the first comment or bottom, emoji only if the brand allows them.
- **X/Twitter** — tightest. Single punchy post or a short thread; hook is the whole game; no hashtag clutter (0–1); link/CTA as a reply when a link would suppress reach.

Keep the angle and the core claim identical across all three — only length, rhythm, hashtag load, and CTA placement change.

## Step 4 — Language + humanizer pass (read `references/copy-frameworks.md`)

Verify before delivering: correct grammar (särskrivningar, de/dem, subject–verb), conversational rhythm, reads like a person talking. Every line survives the "would I say this out loud?" test.

Run the humanizer pass on every variant: apply `/humanizer` if it is installed, otherwise strip the forbidden AI patterns in `references/copy-frameworks.md` inline — inflated symbolism, rule-of-three spam, "delve/leverage/unlock" and their Swedish equivalents, em-dash chains, negative parallelisms ("inte bara X — utan Y"). Honor the banned-word / forbidden-character list from `brand-guidelines.md` if it exists, and anything the user named in the minimum-context questions.

## Step 5 — Deliver (human in the loop, pass 2)

Deliver each channel variant in chat as a **draft**, clearly labeled, ready to paste. Also deliver all variants in one downloadable file named `<slug>.md`; in Claude Code, save it as `work/socialpost/<slug>.md` in the working folder. Offer what is most often wanted next: a second hook to A/B test, or `/content-repurpose` to turn the same idea into a carousel, thread, or newsletter section.

**Never schedule, post, or distribute the copy.** Nothing is published from this skill — the user pastes the approved drafts into their own channels or scheduling tool.

## Quality gates (hard rules)

- **One angle, adapted — not three posts.** The core claim is identical across channels.
- **Ladders to a pillar.** Every post serves a named pillar; no random topics.
- **Built from the reader's words.** Hook and body use VoC language; never invented customer facts. If no VoC was available, say so in the delivery.
- **Hook earns the next line.** No warm-up. It must survive the channel's truncation cut.
- **No invented statistics.** Every number is sourced or it is cut.
- **No AI patterns** — no "det handlar inte bara om X, utan Y", no em-dash chains, no symmetrical triads, no "låt oss dyka in", no buzzwords (see the forbidden list in `references/copy-frameworks.md`). Honor `brand-guidelines.md` negative rules when present.
- **Humanizer pass on every variant** before delivery.
- **Human in the loop twice** — confirm the brief before writing, deliver drafts and stop before any scheduling or posting.

## Examples

- `/socialpost-writer "why 95% of AI pilots return zero ROI"` → loads `voice-of-customer.md` and `offer.md` from the Claude project, confirms channels + angle + CTA, verifies the 95% figure's source with web fetch (or cuts it), writes a LinkedIn, Instagram, and X variant of the same take, each in native shape, humanized, with a comment-keyword CTA → delivers `ai-pilots-zero-roi.md`.
- `/socialpost-writer linkedin` with no context files → asks the four minimum-context questions, writes one LinkedIn post optimized for the "…more" cut, notes that no VoC file was available, and suggests `/brand-voc`.

## Related skills (Lite)

- `/copywriting` — the hook and body frameworks applied in Step 2.
- `/humanizer` — deeper AI-tell scrub in Step 4.
- `/content-repurpose` — turns the same idea into other formats.
- `/brand-voc`, `/icp-builder`, `/brand-offer` — create the context files above.

## Skill folder

- `references/channel-norms.md` — LinkedIn / Instagram / X norms, truncation limits, hashtag rules. **Read in Step 3.**
- `references/copy-frameworks.md` — hook/body/CTA frameworks, language rules, forbidden AI patterns. **Read in Steps 2 and 4.**
- `references/socialpost-style-exemplar.md` — the quality bar for post style.
- `references/context-loading.md` — where context files are found and how missing context is handled.
