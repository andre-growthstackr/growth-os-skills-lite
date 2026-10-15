# AI Search Readiness checklist (AI Search score)

How likely ChatGPT search, Perplexity, Google AI Overviews / AI Mode and Copilot are to find,
understand and cite the site. This is the audit-level check; for a full GEO analysis run `/seo-geo`.
Severity tags: `[C]` `[H]` `[M]` `[L]` `[I]`.

## Access
- `[H]` robots.txt blocks AI search/retrieval crawlers (`OAI-SearchBot`, `ChatGPT-User`,
  `PerplexityBot`, `Claude-SearchBot`/`Claude-User`) without a stated business reason. Blocking
  training-only crawlers (`GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`) is a business choice:
  report it as `[I]`.
- `[H]` Key content only exists after JavaScript runs (most AI crawlers do not render JS).
- `[L]` No `/llms.txt` file (example.com/llms.txt). Emerging convention, low impact: Low at most.

## Citability (check key pages)
- `[M]` No answer-first passages: questions the page targets are not answered in the first
  40–60 words under a clear heading.
- `[M]` No quotable, specific facts (numbers, definitions, comparisons) with a source.
- `[L]` Comparative information in prose where a table or list would be extractable.
- `[L]` Headings are clever rather than descriptive (a model cannot tell what the section answers).

## Entity clarity
- `[M]` The brand is not clearly defined: no About page with who/what/where, no `Organization`
  schema with `sameAs` links to official profiles.
- `[L]` Authors not defined as entities (no author pages, no `Person` schema).

## Off-site signals (web search only; never estimate counts)
- Search the brand name plus the main category. Note whether it appears in third-party lists,
  reviews, Reddit/forum threads, press, Wikipedia/Wikidata. Report what you found as observations
  with URLs. Not scored (no reliable count without a paid tool), but feeds recommendations.
