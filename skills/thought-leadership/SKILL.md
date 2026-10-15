---
name: thought-leadership
description: "Founder-led LinkedIn authority: point of view, stances, post drafts. Use for: bygg thought leadership, positionera mig som expert, thought leadership, founder-led content."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: content-os
---

# Thought Leadership — Executive Authority Program

Audiences smell manufactured opinions instantly, and generic insight is worse than
silence. This skill mines the stances an executive genuinely holds, pressure-tests them
for defensibility, and turns them into a publishing program in the exec's own diction —
with the exec's approval gate built in before anything ships.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `business-profile.md` — company, services, goals (OPTIONAL — anchors stances in what the business sells)
- `icp.md` — who the exec should reach (OPTIONAL — sharpens which stances matter to the audience)
- `voice-of-customer.md` — verbatim customer language, objections, triggers (OPTIONAL — raw material for stances that hit real pains)
- `offer.md` — guarantee, proof, case studies (OPTIONAL — proof for stances)
- `brand-guidelines.md` — tone, positioning, negative rules (OPTIONAL — use if present; Lite continues without it)
- Exec voice samples (real posts, emails, talk transcripts) — requested at runtime (REQUIRED for any ghostwritten draft)

**Minimum context if files are missing** — ask these and continue:
1. Who is the program for? (name, role, company, what the company sells)
2. Who should the exec reach? (role and industry of the audience)
3. What business goal should the program serve? (pipeline, hiring, fundraising, category leadership)
4. Paste 3–5 real pieces of the exec's own writing or speaking (posts, emails, a talk transcript).

Use the answers for this run only and say in the deliverable which context was missing.
Afterwards, suggest `/business-audit` (saves `business-profile.md`), `/icp-builder` (saves `icp.md`)
and `/brand-voc` (saves `voice-of-customer.md`) so every future run inherits them.

## Arguments

| Invocation | Behavior |
|---|---|
| `/thought-leadership` | Ask who the program is for, then interview |
| `/thought-leadership "Anna Berg"` | Build the program for that person |
| `/thought-leadership "Anna Berg" pricing` | Focus the POV mining on that theme |

## Instructions

Respond and produce deliverables in the user's language.

1. **Load context and identify the exec.** Request real voice samples: 3–5 pieces of
   their actual writing or speaking (posts, emails, a talk transcript). No samples
   means the diction profile is never approximated from a job title. Fallback for an exec
   with no writing yet: build the diction profile from their own answers in the POV interview
   (step 2), quoted as spoken, and mark the drafts "voice from interview answers — confirm it
   sounds like you".
2. **POV mining interview.** Ask one question at a time, each with 2–4 pre-filled
   options plus free text. Use the environment's question tool if there is one
   (AskUserQuestion in Claude Code, option boxes in Claude.ai); otherwise ask numbered
   questions in chat. Surface: opinions the exec actually holds, where they disagree
   with industry consensus, and lessons from real failures they will discuss publicly.
   If the user has already answered these in the chat, use those answers instead of
   re-asking. Mined opinions only — fabricating an opinion for a real person is a hard
   stop.
3. **Stance selection — the contrarian-but-defensible test.** A stance qualifies only
   if both halves hold: a meaningful share of industry peers would disagree (rule of
   thumb: roughly a third), AND it can be defended with the exec's own experience or
   data. "Everyone agrees" is content, not leadership; "nobody can defend it" is noise.
   Document the test result per stance.
4. **Format ladder.** Each qualifying stance climbs: LinkedIn posts (test resonance) →
   long-form essay (the argument in full) → talk/podcast angles (the stance as a title
   plus three talking points). Map every selected stance onto the ladder.
5. **Build the diction profile** from the real samples: sentence length, favored words,
   words they never use, how they open, how they disagree. Ghostwritten drafts must
   pass as written by the exec — judged by the exec.
6. **Cadence plan tied to capacity.** Ask how much review time the exec will actually
   give per week — minutes, not aspiration. Plan cadence to that number; a sustainable
   post per week beats a heroic daily fortnight that dies in week three. The plan is a
   suggested rhythm the exec follows themselves — this skill does not schedule anything.
7. **Draft the first pieces:** 2–3 LinkedIn posts from the strongest stance, written in
   the diction profile. Apply humanizer principles (no AI tells, no hype words); for an
   extra pass, offer `/humanizer`. Every draft carries the exec approval gate — nothing
   ships until the named exec approves each piece.
8. **Run the quality gates** below, then deliver per Output.

> **In the full version:** a brand-guidelines skill that saves tone and banned-word rules for every run is in the Growth OS Skills Pack (246 skills). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full

## Output

- **In chat:** the 2–3 LinkedIn post drafts in full, copy-paste ready, each marked
  "draft — needs approval from <person>", followed by a short summary of the program.
- **Downloadable `thought-leadership-<person>-<date>.md`** (Claude Code: save to
  `work/thought-leadership/<person>-<date>.md` in the working folder): mined POV inventory
  with stance-test results, format ladder per stance, diction profile with sample sources,
  cadence plan, and the first drafts with their approval marks. Note which context files
  were missing.
- This skill never posts, schedules or publishes. The exec approves each piece and
  publishes it themselves. For more posts later from an approved stance, use
  `/socialpost-writer`; to turn an essay into other formats, use `/content-repurpose`.

## Quality gates

A failed gate means rewrite, not caveat.

1. Every stance is genuinely held and mined from the interview or samples — fabricating
   opinions for a real person is a hard stop, not a shortcut.
2. No generic listicle content: every planned piece argues a POV or it is cut.
3. The exec approval gate is explicit on every draft ("draft — needs approval from
   <person>").
4. The diction profile is built from real samples only; no samples, no ghostwritten
   drafts.
5. Every stance passes both halves of the contrarian-but-defensible test, with the
   result documented.
6. Statistics in any draft carry a source + URL (verified with web search and web fetch);
   no invented quotes ever.
7. If `brand-guidelines.md` exists, drafts respect its tone and banned-word rules.

## Example

**Example 1 — Swedish:**
User: "Bygg tankeledarskap för vår grundare Anna kring prissättning."
Flow: `business-profile.md` och `icp.md` laddas från Claude-projektet → röstprover begärs
(3 riktiga LinkedIn-inlägg + en föredragstranskription) → POV-intervju, en fråga i taget
med svarsalternativ: var avviker Anna från branschkonsensus? → ståndpunktstest:
"värdebaserad prissättning är fel för tidiga B2B-bolag" — en tydlig andel av branschen
håller inte med, försvarbar med Annas egna kunddata → diktionsprofil från proverna →
3 LinkedIn-utkast i chatten, märkta "utkast — kräver Annas godkännande" → programmet +
utkasten som nedladdningsbar `.md`. Inget publiceras eller schemaläggs.

**Example 2 — no samples, no mined opinions:**
User: "Ghostwrite LinkedIn posts for our CEO, just make him sound smart."
Flow: hard stop on two counts — no voice samples yet (requested) and no mined stances
to write from. The POV interview runs first; without the exec's actual opinions,
nothing is drafted.
