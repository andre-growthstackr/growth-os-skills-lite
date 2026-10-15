---
name: growth-os-lite-start
description: "Start here: Growth OS Lite setup, the 4 context files, and which skill to use. Use for: kom igång med Growth OS, vilken skill ska jag använda, set up Growth OS, what can Growth OS do."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: meta
---

# Growth OS Lite — start, help and routing

Get a new user from zero to their first useful result, and route any goal to the right Lite
skill. Three modes: **set up** (first time), **route** (the user names a goal), **browse** (the
user asks what is in the pack).

**Respond in the user's language** (Swedish or English). Instructions are English for
robustness.

## Context check (silent, always first)

Follow `references/context-loading.md` to check which of the four context files already exist
(Claude project / this chat, then the working folder in Claude Code). Use the result to tailor
the answer: never tell someone to create a file they already have.

## Mode 1 — Set up (first run, or "kom igång")

1. **Explain Growth OS in five lines** (in the user's language):
   - Growth OS is GrowthStackr's system for B2B marketing and lead generation, packaged as skills.
   - You describe your business once, in four context files.
   - Every skill reads those files, so you never re-brief Claude.
   - Lite has 20 skills: brand foundation, copy, website/SEO, lead magnets, CRO, content, ads audit.
   - Everything stays in Claude; external tools are optional and always asked for first.
2. **Recommend a Claude project.** In Claude.ai or Claude Desktop: create a project (e.g.
   "Growth OS – <company>") and work inside it, so the context files sit in the project's
   knowledge and every chat sees them. In Claude Code: work in one folder per company; the files
   live in its root.
3. **If all four files already exist**, skip the rest of this mode: confirm what you found in one line each
   and go straight to Mode 2 ("What do you want to get done first?"). Otherwise:
   **hand out only the missing empty context files** from `assets/` as downloadable files with these exact
   names: `business-profile.md`, `icp.md`, `voice-of-customer.md`, `offer.md`. Say that they do not
   need to be filled in by hand: the setup skills below fill them through an interview. (In Claude
   Code, only write them to the working folder if the user asks; never overwrite existing files.)
4. **Show the setup order** and what each step delivers:

   ```
   business-audit  →  icp-builder  →  brand-voc  →  brand-offer
   business-profile.md   icp.md      voice-of-customer.md   offer.md
   ```

   About 20–40 minutes each, interview-driven. After each one: "Add the file to your Claude
   project so every other Growth OS skill uses it."
5. **Offer the first step**: "Want to start with `business-audit` now? Give me your website URL."
   If they already have some files, start at the first missing one.

## Mode 2 — Route a goal

Match the goal to 1–3 Lite skills using `references/skill-index.md`. Give, for each: the skill
name, one line on why, and a ready-to-send example prompt in the user's language. Then:

- If the skill needs context that is missing (per the context check), say which setup skill to
  run first, or that the skill will ask 3–5 quick questions instead.
- If the goal is a **full-version feature** (see the "Not in Lite" table in
  `references/skill-index.md`), say so plainly in one line, then offer the closest Lite skill
  that still helps. Never pretend a Lite skill does something it does not.

Common routes (full list in the index):

| Goal | Lite route |
|---|---|
| "Jag behöver fler leads" / "I need more leads" | `leadmagnet-ideate` → `leadmagnet-create`; foundation first if missing |
| "Skriv LinkedIn-inlägg" / "Write LinkedIn posts" | `socialpost-writer` (single posts) or `thought-leadership` (founder authority) |
| "Varför konverterar inte sidan?" | `cro-audit`, then `copywriting` for the rewrites |
| "Hur mår min sajt?" | `website-audit` (overview) → `seo-audit` (deep SEO) → `seo-geo` (AI search) |
| "Låter AI" / "sounds like AI" | `humanizer` |
| "Granska våra annonser" | `ads-audit` |
| "Vilka är våra konkurrenter?" | `competitor-research`, then `brand-positioning` |
| "Skriv ett blogginlägg" | `blog-write`, then `content-repurpose` for LinkedIn/newsletter versions |

## Mode 3 — Browse

Show the 20 skills grouped by module (from `references/skill-index.md`), one line each. Do not
dump the whole index file; lead with the modules and offer to explain any skill.

## How to run a skill

- **Claude.ai / Claude Desktop:** just ask in plain language ("bygg min ICP") or name the skill
  ("kör icp-builder"). The skill must be uploaded and switched on under Customize → Skills.
- **Claude Code:** the same, or type the slash form, e.g. `/icp-builder`.

## Lite vs full version

When the user asks what the full version adds, answer from this list, without numbers that are
not here:

> **Full version:** the Growth OS Skills Pack has 246 skills, a 10-agent specialist team, 5 gated multi-agent workflows, Outbound OS (lists, buying signals, cold email, LinkedIn sequences), Design OS, style memory per format, ads planning/launch/optimization, and live data via integrations. See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

Mention the course "AI för Leadsgenerering" and the free community AI Growth Sverige only when
the user asks how to learn more, or asks for help beyond the skills: both are linked from
https://www.growthstackr.io/.

## Rules

- Always end with one concrete next step: a skill name and an example prompt.
- Never invent features, prices, or results. Never claim a full-version skill exists in Lite.
- This skill writes nothing except the four empty context files, and only when asked.
