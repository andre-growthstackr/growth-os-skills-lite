# Writing rules (Phase 4–5)

Read before drafting. These rules are constant across templates.

## 5a. Frontmatter

```yaml
---
title: "[Question-format title with the primary keyword]"
description: "[Fact-dense, 150–160 chars, includes 1 statistic]"
coverImage: "[URL the user supplied, or IMAGE-PLACEHOLDER]"
coverImageAlt: "[Descriptive sentence]"
ogImage: "[Same as coverImage or a custom OG image]"
date: "YYYY-MM-DD"
lastUpdated: "YYYY-MM-DD"
author: "[Author with E-E-A-T signals]"
tags: ["keyword1", "keyword2", "keyword3"]
---
```

Adapt field names to the site's existing convention (`image`, `hero`, etc.) if the user shows
one. Plain markdown posts without a CMS can drop the frontmatter and put title + meta
description at the top.

## 5b. Key Takeaways box

Immediately after the intro, before the first H2 body: 3–5 bullets, 40–60 words combined,
self-contained, at least one sourced statistic. Label "Key Takeaways" (or the user's language).

## 5c. Answer-first formatting (critical)

Every H2 opens with a 40–60 word paragraph that directly answers the heading's implicit question;
the major H2s also carry at least one statistic with source attribution. Put the year in the prose
("In 2026, …"), not buried in parentheses.

Evidence triple, required at drafting time for every public statistic:
1. **Year anchor in the sentence body** — "In 2026," / "As of Q1 2026,".
2. **Inline citation naming publisher AND document title** — not just a brand.
3. **URL + retrieval date** in a source block at the foot of the post
   (`[Publisher], [Title], retrieved YYYY-MM-DD, [full URL]`).

Quality bar: verified source OR stay qualitative. Unverifiable → drop it. Contradicted by a
newer source → replace it. Never soften vague language to keep an unsourceable number.

## 5d. Information-gain markers (the core requirement)

Distribute at least 2–3 through the article. These lift the post above the AI-average floor and
drive both ranking and citation. Tag each:
- `[ORIGINAL DATA]` — proprietary survey, experiment, A/B test, case-study metric the author
  collected first-hand.
- `[PERSONAL EXPERIENCE]` — first-hand observation, lesson from direct involvement, "when we
  tried X, Y happened".
- `[UNIQUE INSIGHT]` — analysis, contrarian take, or novel connection others have not published.

If the user has supplied none of the above, **ask for it** — one real data point, opinion, or
story before drafting. Never fabricate original data or experience. Render markers as HTML
comments (`<!-- [ORIGINAL DATA] -->`) or visible callouts (`> **Our finding:** …`).

## 5e. Citation capsules

In each major H2, write a 40–60 word self-contained passage an AI system can lift verbatim: one
specific claim + one data point + source attribution, declarative and quotable, inside the
section body.

## 5f. Internal-linking zones

Mark 5–10 per 2,000 words using `[INTERNAL-LINK: anchor text → target description]` in the
intro, each H2, the FAQ, and the conclusion. Descriptive anchor text only — never "click here" or
"read more". If `business-profile.md` lists service or offer pages, point zones at those. The
user resolves the placeholders to real URLs.

## 5g. Paragraph & sentence rules

- Paragraphs 40–80 words (never over 150); lead with the key information.
- Vary sentence length deliberately — mix 8-word and 25-word sentences. Uniform length is the
  loudest AI tell.
- Target Flesch Reading Ease 60–70 (or the equivalent plain-language level in the user's
  language).

## 5h. Heading rules

One H1 (title); H2s for main sections (60–70% phrased as questions); H3s for subsections only,
never skipping a level; the primary keyword appears naturally in 2–3 headings.

## 5i. Images (placeholders)

Lite does not source or generate images. Mark where images belong:
`[IMAGE: what it shows — alt: full descriptive sentence with the keyword]`, placed after an H2
and before its body, spaced evenly, never clustered. Plan a cover (1200×630) and 3–5 inline
images. If the user supplies image URLs, embed them as
`![full descriptive alt sentence](url)`. Never invent an image URL.

## 5j. Charts (optional)

When research yields chart-worthy data (3+ comparable metrics, a trend, a before/after), build
1–3 inline SVG charts per 2,000 words:
1. Pick a chart type using the diversity rule — no repeated types in one post (bar, lollipop,
   donut, line).
2. Build a clean, self-contained `<svg viewBox="0 0 560 380">` with a title, inside a
   `<figure>` with a `<figcaption>` naming the source and year.
3. Distribute charts evenly; never cluster them. Every plotted number is a verified statistic.

## 5k. Videos (optional)

Only when the user supplies a video or one is found by web search and the URL is verified with
web fetch. Lazy-loaded YouTube embed with `aria-label` and a `<noscript>` text fallback; place
after a relevant H2, 500+ words apart from other embeds.

## 5l. FAQ

3–5 items, 40–60-word answers, each containing a statistic where one is honestly available.
Plain `## Frequently Asked Questions` section (or the site's FAQ component if the user shows one).

## 5m. Single CTA

One focused, contextual call-to-action placed after value delivery. Draw the offer from
`offer.md` if present; otherwise use the CTA from the brief.

## Banned AI tells (humanizer pass, Phase 6)

Inflated symbolism, rule-of-three spam, "delve / leverage / unlock / seamless / robust /
tapestry", em-dash overuse, negative parallelisms ("not just X, but Y"), "in today's digital
landscape", "it's important to note", "game-changer" — and their equivalents in the user's
language. Plus every banned word or character in `brand-guidelines.md` if that file exists.
