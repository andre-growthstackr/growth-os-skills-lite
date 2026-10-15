# SEO Dimension — Checks & Scoring

Covers content, on-page, schema, and AI-readiness (AIO/GEO) checks. Score this dimension 0-100.

## Sub-areas and weights

| Sub-area | Weight |
|---|---|
| On-page fundamentals | 25% |
| Content quality & E-E-A-T | 30% |
| Schema / structured data | 15% |
| AI search readiness (AIO/GEO) | 20% |
| Images & media | 10% |

## Core lens (apply throughout)

Two levers only: **relevance** (match search intent, one primary keyword per page) and **authority** (links, brand mentions, E-E-A-T). In the AI era the quality floor is higher — content must show **information gain**: own data, own opinions, first-hand experience. Traffic is not the only goal; being cited by AI answers produces "primed leads".

## 1. On-page fundamentals (25%)

- Title tags: unique, 50-60 chars, primary keyword near the front, no duplication across pages
- Meta descriptions: present, 140-160 chars, contain a reason to click
- One H1 per page; logical H2/H3 hierarchy; headings describe content (scannable)
- One primary keyword/intent per page — flag keyword cannibalization (two pages targeting the same query)
- Internal linking: money pages reachable in <= 3 clicks; descriptive anchor text; no orphan pages
- Open Graph + Twitter card tags on shareable pages

## 2. Content quality & E-E-A-T (30%)

- Search intent match: does the page type fit the query type (informational vs commercial vs transactional)?
- Thin content: flag indexable pages with < 300 words of unique substance
- Duplicate/near-duplicate pages
- E-E-A-T signals: named author with bio/credentials, about page, contact details, editorial dates, cited sources
- Information gain check: does the content contain anything a generic AI draft would not (proprietary data, real examples, first-hand experience, named opinions)? Generic rehash = High finding on key pages
- Readability: short paragraphs, plain language for the audience, no wall-of-text sections

## 3. Schema / structured data (15%)

- Detect existing JSON-LD; validate required properties per type
- Expected by page type: Organization/LocalBusiness (site-wide), Article + author (blog), Product + offers/reviews (e-commerce), Service, FAQPage where FAQs exist, BreadcrumbList
- Flag schema that contradicts visible content (risk finding)
- Missing high-value opportunities listed as recommendations with the exact type to add

## 4. AI search readiness — AIO/GEO (20%)

- **Answer-first structure**: first paragraph of key pages answers the query directly, no throat-clearing fluff
- **Citability capsule**: statistics with source URLs and expert quotes — per the Princeton/GT GEO study (2024, "GEO: Generative Engine Optimization", arXiv:2311.09735), adding citations, quotations and statistics improved generative-engine visibility by up to ~40% on some query sets
- AI crawler access (cross-check with technical dimension): GPTBot/ClaudeBot/PerplexityBot not blocked unless intentional
- `llms.txt` present (opportunity)
- Clean extractable structure: definition-style intros, tables, lists, FAQ blocks
- Brand mentions ("the new backlinks"): note presence/absence on Reddit, forums, review sites, news with web search (cite the URLs found). LLM-mention counts only if the user approved DataForSEO in the permission step; otherwise "not measured"

## 5. Images & media (10%)

- Alt text present and descriptive on content images
- Modern formats (WebP/AVIF) and sensible dimensions
- Descriptive filenames; lazy loading below the fold

## Live data enrichment (optional)

If the user approved DataForSEO in the permission step, enrich with real data: ranked keywords for the domain, keyword volumes for target terms, backlink summary, live SERP checks for 2-3 money keywords. Otherwise: spot-check 2-3 money keywords with web search (note that results are personalized and unofficial), use a Search Console export if the user uploads one, and mark rankings, volumes and backlink counts as "not measured". State clearly which findings are heuristic vs measured. Never invent rankings, volumes or backlink counts.

## Severity mapping

- **Critical**: money pages noindexed, mass duplicate titles, schema errors triggering manual-action risk
- **High**: cannibalization on money terms, thin money pages, no answer-first structure on top content, missing Article/Product schema where it drives rich results
- **Medium**: meta description gaps, weak internal linking, missing OG tags, missing FAQ schema
- **Low**: llms.txt, filename cosmetics, minor readability polish
