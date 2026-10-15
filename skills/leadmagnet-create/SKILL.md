---
name: leadmagnet-create
description: "Produces the chosen lead magnet plus opt-in outline and delivery emails. Use for: skapa leadmagneten, bygg min lead magnet, create the lead magnet, build my lead magnet."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: leads-os
  source: "lead-magnets (anthropic-skills)"
---

# Lead Magnet Create

Produce a decided lead magnet: the finished asset, an opt-in page outline, and the delivery emails. This is the production half of the lead magnet pipeline — strategy and concept selection happen in `/leadmagnet-ideate`; this skill builds what was chosen.

Respond and produce deliverables in the user's language. SKILL instructions are in English; output follows the user.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `icp.md` — Ideal Customer Profile: tiers, firmographics, pains (REQUIRED — the asset solves their problem)
- `offer.md` — offer, pricing, guarantees, proof (REQUIRED — the magnet must bridge to it)
- `voice-of-customer.md` — verbatim customer language (OPTIONAL but strongly preferred — headlines and copy are weaker without it; say so)
- `business-profile.md` — company, services, goals (OPTIONAL)
- `brand-guidelines.md` — tone, negative rules, banned words (OPTIONAL — use if present; Lite continues without it and uses neutral, clean styling)

**Minimum context if files are missing** — ask these and continue:
1. Who is the magnet for? (role, company type, the one problem it solves for them)
2. What do you sell, and what should the reader do after the magnet (book a call, start a trial, reply)?
3. How do your customers describe the problem in their own words? (paste a quote or two if you have them)
4. Any facts, numbers or examples from your own work the asset may use?

Use the answers for this run only and say in the deliverable which context was missing.
Afterwards, suggest `/icp-builder` (saves `icp.md`), `/brand-offer` (saves `offer.md`) and
`/brand-voc` (saves `voice-of-customer.md`) so every future run inherits them.

## Inputs

This skill expects a **decided magnet concept**: format + topic + target funnel stage. Sources, in order:

1. The concept report from `/leadmagnet-ideate` (`lead-magnet-concepts.md`, uploaded or pasted in chat).
2. The argument (e.g. `/leadmagnet-create SEO audit checklist`).
3. Ask the user. If they have no concept yet, offer to run `/leadmagnet-ideate` first — do not improvise strategy here.

Confirm before producing: format, working title, target ICP tier and funnel stage (TOF/MOF/BOF), and the conversion goal after opt-in (nurture, call, trial). One clarifying round maximum. Use the environment's question tool if there is one (AskUserQuestion in Claude Code, option boxes in Claude.ai); otherwise ask numbered questions in chat.

## Instructions

Work through the three stages in order. After each stage, show the deliverable and get a "looks good" before moving on — cheap corrections early beat expensive rework late.

### Stage 1 — Produce the asset

1. Read `references/format-guide.md` for the chosen format's structure and guidelines (ebooks/guides, checklists, cheat sheets, templates, swipe files, mini-courses, quizzes, calculators, webinars).
2. Route by format:
   - **Checklist / cheat sheet / guide / template / swipe file** → write the full content. Follow the format guide's structure. Apply core principles: one specific problem, consumable in under 30 minutes, immediately actionable, natural bridge to the offer (solves a problem the product also solves).
   - **Email mini-course** → write all 3-5 lesson emails in full.
   - **Quiz / assessment / calculator / grader** → write the complete build-ready spec per the format guide: every question or input with answer options, scoring or formula step by step, result bands with copy and recommendations, and which ICP criterion each input qualifies. Assumptions in any formula come from the user or a cited source + URL. The user can build it in a quiz/form tool or spreadsheet, or ask Claude to turn the spec into an interactive page.
   - **Webinar** → write the outline, talking points per section, and the closing CTA.
3. Copy quality gates (hard rules):
   - Use voice-of-customer language in the title and body where `voice-of-customer.md` exists.
   - Apply humanizer principles to all copy — no AI tells (inflated symbolism, rule-of-three spam, "delve/leverage/unlock", em dash overuse, negative parallelisms). For long-form assets, offer a final pass with `/humanizer`.
   - **Fact-check every statistic and factual claim:** find the source with web search, open it with web fetch, and keep the number only if the page confirms it — cite source name + URL inline. If you cannot verify it, cut it. Numbers the user supplied about their own business are labeled as theirs.
   - Respect the negative rules in `brand-guidelines.md` if that file exists.
4. End the asset with a CTA toward the offer (book a call, start trial — per the confirmed conversion goal).
5. Deliver the full asset in chat and as a downloadable `<slug>.md` (Claude Code: save to `work/lead-magnets/<slug>.md`). For a designed PDF, the user can paste the markdown into Google Docs, Word, Canva or Notion and export.

### Stage 2 — Opt-in page outline

Write a short, ready-to-use outline for the page or form where people sign up — five lines, in customer language:

1. **Headline** — names the outcome. Clear beats clever.
2. **Subheadline** — who it is for + what they get, one sentence.
3. **What's inside** — 3-5 concrete takeaways from the asset.
4. **Form** — minimum fields for the funnel stage: email only for TOF; add name for personalization; add company/role only for MOF/BOF where qualification matters. Every extra field adds friction.
5. **CTA + trust** — button says what they get ("Get the checklist"), never "Submit"; one real proof point (from `offer.md` or the user) and a "no spam" line. Never fabricate social proof or download counts.

Add one line for the **thank-you page**: confirm delivery ("check your inbox"), give instant access via a link on the page too, and offer the next step per the conversion goal.

### Stage 3 — 3-email delivery sequence

Write the sequence as outlines with subject line + 3-5 bullet body + CTA (write email 1 in full):

1. **Email 1 — Delivery (immediately):** subject names the asset; link first, no fluff before the goods; one "do this first" tip; soft next step.
2. **Email 2 — Use it (day 2-3):** one quick win or common mistake related to the asset; reply prompt ("What's your biggest blocker with X?").
3. **Email 3 — Bridge (day 5-7):** connect the problem the asset solved to the offer; one proof point from `offer.md`; clear CTA per the conversion goal.

For email mini-courses, the lessons from Stage 1 are the sequence — add the send schedule (one lesson every 1-2 days) instead. Every email includes an unsubscribe line. For a full nurture sequence beyond these three, `/copywriting` can write more emails.

> **Next step in the full version:** `/landingpage-build` builds the full opt-in page, `/crm-nurture` writes the complete nurture sequence, and `/leadmagnet-tool` builds quizzes and calculators as working tools — all in the Growth OS Skills Pack (246 skills). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

## Output

Deliver everything in chat and as downloadable `.md` files (Claude Code: save under `work/lead-magnets/` in the working folder):

| File | Contents |
|---|---|
| `<slug>.md` | The lead magnet itself — finished content, or the build-ready spec for an interactive magnet |
| `<slug>-launch-kit.md` | Opt-in page outline + thank-you line + 3-email delivery sequence + launch checklist |

Close the launch kit with a short **launch checklist**: what is ready, what the user still needs to set up themselves (page, form, email tool), and a suggested first A/B test (headline or number of form fields). Add a data-sources line (e.g. "Statistics verified via web fetch of 3 sources; context: icp.md, offer.md; no VoC available").

This skill never publishes pages, sends emails, or writes to any CRM or email tool. Setting it live is the user's step.

## Quality gates

- Never hardcode or assume a client brand — everything comes from the loaded context files or the user's answers.
- No invented statistics, download counts, or testimonials. Every statistic has source + URL; unverified numbers are cut.
- Humanizer principles on all user-facing copy; respect brand negative rules when `brand-guidelines.md` exists.
- The asset bridges to the offer — a magnet that captures emails but leads nowhere fails.
- The form asks for the minimum fields for the funnel stage.
- `references/benchmarks.md` is qualitative; never quote a conversion rate or cost figure to the user unless you found and cited a current source.

## Example

**User**: `/leadmagnet-create checklista för teknisk SEO-audit` (after `/leadmagnet-ideate` picked this concept for green-tier SaaS marketers, TOF)

**Flow**:
1. Loads `icp.md`, `offer.md`, `voice-of-customer.md` from the Claude project. Confirms: checklist, TOF, goal = nurture toward the audit service.
2. Stage 1: writes a 15-point technical SEO checklist in Swedish, grouped in 3 sections, VoC phrasing in the title; one statistic about page speed is verified via web fetch and cited with URL, another unverifiable one is cut; ends with a CTA to the audit offer. Delivers `teknisk-seo-checklista.md`. Gets approval.
3. Stage 2: five-line opt-in outline (headline, subheadline, 4 takeaways, email-only form, "Hämta checklistan" + no-spam line) + thank-you line.
4. Stage 3: delivery email in full + outlines for emails 2 and 3. Delivers `teknisk-seo-checklista-launch-kit.md` with the launch checklist.
5. Ends: "Everything is ready to set up in your own page builder and email tool — nothing has been published or sent."
