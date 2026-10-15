# Templates and outline skeleton

Read in Phase 1.5 (template selection) and Phase 3 (outline).

## Template selection

Auto-detect the content type from the topic and search intent, then shape the outline to match:

| Signal | Template |
|--------|----------|
| "How to…", process, steps | how-to-guide |
| "Best X", "Top N", list | listicle |
| Client result, before/after, metrics | case-study |
| "X vs Y", comparison, alternatives | comparison |
| Broad topic, comprehensive guide | pillar-page |
| "Is X worth it", product evaluation | product-review |
| Opinion, prediction, industry take | thought-leadership |
| Expert quotes, multi-source collection | roundup |
| Code walkthrough, tool demo, technical | tutorial |
| Breaking news, algorithm update, event | news-analysis |
| Survey results, experiment, original data | data-research |
| Q&A, knowledge base, "What is X" | faq-knowledge |

Tell the user which template was selected (or that none matched and the generic skeleton below
applies). The template dictates section order, heading patterns, and word-count balance — not
the writing rules, which are constant.

Template shape hints:
- **how-to-guide / tutorial** — numbered steps as H2s or H3s, prerequisites up front, one
  checklist or summary table near the end.
- **listicle / roundup** — one H2 per item, same internal structure per item, a comparison
  table early for scanners.
- **comparison / product-review** — verdict first, comparison table, criteria-by-criteria H2s,
  "who should pick which" section.
- **case-study / data-research** — the result and the number first, then context, method,
  what changed, what the reader can copy.
- **pillar-page** — broad answer first, one H2 per subtopic, each ending in an
  `[INTERNAL-LINK]` to a deeper post.
- **thought-leadership / news-analysis** — the claim or the news in one paragraph, then why it
  matters, evidence, counter-argument, what to do now.
- **faq-knowledge** — the definition in 40–60 words, then question-shaped H2s.

## Inline brief (Phase 1 output — show it to the user)

```
Topic:            [one line]
Reader:           [from icp.md or the user's answer]
Search intent:    [informational / commercial / comparison / navigational]
Primary keyword:  [phrase] · secondary: [2–4 phrases]
Angle:            [the one point this post makes that the top results don't]
Information gain: [the real data point, opinion or first-hand story the user supplied]
Template:         [name]
Length / format:  [~words] · [markdown / MDX / HTML]
CTA:              [one action, from offer.md or the user]
```

## Generic outline skeleton

```
# [Title as a question — includes the primary keyword]

## Introduction (100–150 words)
- Hook with a surprising, sourced statistic
- Problem / opportunity statement
- What the reader will learn

> Key Takeaways (3–5 bullets, 40–60 words total, self-contained, 1 sourced stat)

## H2 [question] (300–400 words)
- Answer-first paragraph (40–60 words, stat + source)
- Supporting evidence · [IMAGE] · [CITATION CAPSULE] · [INTERNAL-LINK]

## H2 [question] (300–400 words)
- Answer-first paragraph · [CHART: type + data] · analysis · [CITATION CAPSULE]

## H2 [statement, for heading variety] (300–400 words)
- Answer-first paragraph · real example or [ORIGINAL DATA] / [PERSONAL EXPERIENCE]

## H2 [question] (300–400 words)
- Answer-first paragraph · [CHART] · step-by-step · [INTERNAL-LINK]

## [CTA — single, contextual, placed after value delivery]

## FAQ (3–5 Q&A, 40–60-word answers, with a sourced stat where one is honestly available)

## Conclusion (100–150 words) — recap + next step + [INTERNAL-LINK]
```

Pace visual markers (`[IMAGE]`, `[CHART]`, `[VIDEO]`, `[CALLOUT]`) every 300–500 words and
never place two of the same type back to back.

Content type before channel: this produces a *blog article* — a format that is later adapted to
other channels with `/content-repurpose`, not a channel-specific post.
