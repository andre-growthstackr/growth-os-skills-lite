---
name: seo-geo
description: "Optimizes pages for AI search (ChatGPT, Perplexity, AI Overviews) and checks AI crawler access. Use for: optimera för AI-sök, GEO, synas i ChatGPT, AI search optimization."
license: MIT
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: web-os
  source: "claude-seo v1.9.9 (AgriciDaniel, MIT)"
---

# AI Search / GEO Optimization

Analyze and optimize a page or site for Generative Engine Optimization (GEO/AIO): becoming a cited source in AI Overviews, ChatGPT web search, Perplexity, and Bing Copilot.

Respond and produce deliverables in the user's language.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `business-profile.md` — company, services, goals (OPTIONAL — helps judge which queries and entities matter)
- `icp.md` — Ideal Customer Profile (OPTIONAL — helps prioritize which AI answers the brand should appear in)

**Minimum context if files are missing** — ask these in one message and continue (use the
environment's question tool if there is one, AskUserQuestion in Claude Code or option boxes in
Claude.ai; otherwise numbered questions in chat):
1. Which URL (page or site) should I analyze?
2. What is the brand name, and who are 2–3 competitors you lose to?
3. Which 3–5 questions do your buyers ask an AI assistant or Google before they buy?
4. Which market and language should the AI answers be checked in?

If the user skips the questions, base the analysis purely on the page/site itself and derive
candidate queries from its headings (say so). Never invent business or customer facts.
Afterwards, suggest `/business-audit` or `/icp-builder` if those files were missing.

## External tools — ask first

This skill works fully without external servers: web fetch of the page, `robots.txt`,
`/llms.txt` and the sitemap; reading the HTML for schema and rendering checks; web search to
probe AI-style answers and brand mentions; and answers the user pastes or screenshots from
ChatGPT, Perplexity or Google AI Overviews. Follow `references/mcp-permission.md` before the
first call (ask once per run, only if the server is already connected).

| Server (optional) | Used for | Requires | Built-in path (no MCP) |
|---|---|---|---|
| DataForSEO | Scraping ChatGPT web-search answers for target queries; LLM-mention counts, top cited domains and pages for the brand | DataForSEO account, paid credits | Web search on each target query to see which sources surface; the user runs 3–5 target prompts in ChatGPT / Perplexity / Google and pastes or screenshots the answers; brand-mention footprint via web search (Wikipedia, Reddit, YouTube, LinkedIn) |

Metrics that exist ONLY with the server (reported as "not measured" when declined, never
estimated): LLM-mention counts and share of voice, AI-search volume for queries, ChatGPT
citation frequency across many queries, and top cited domains/pages per LLM. Without it, AI
visibility is reported as a qualitative manual probe ("cited in 1 of 4 checked answers"), not as
a metric.

## Why GEO matters (course framing)

- The AI era raised the quality floor: content supply exploded, so **information gain** is required — original data, first-hand experience, and real opinions layered on top of any AI draft.
- **Brand mentions are the new backlinks** (Reddit, forums, news, review sites). Traffic is not the only goal — AI citations produce "primed leads" who already trust the brand before they visit.
- Citability = direct answers first (no fluff in the opening paragraph), authors with E-E-A-T signals, statistics + expert quotes + source URLs (up to +40% citation rate, GEO study 2024, https://arxiv.org/abs/2311.09735), and clean technical hygiene (JSON-LD schema, canonicals, OG tags, llms.txt, WebP).

## What drives AI citations (qualitative)

The upstream skill carried market statistics without source URLs; Lite keeps only the
direction. If the user wants a figure, find a current source with web search and cite its URL.

- **Brand mentions matter alongside backlinks.** Presence on YouTube, Reddit, Wikipedia, LinkedIn,
  review sites and news is a strong signal for AI answers; links alone are a weaker one.
- **Platforms cite different sources.** Google AI Overviews lean on pages that already rank;
  ChatGPT and Perplexity lean more on encyclopedic and community sources. Optimize per platform.

## Instructions

1. **Fetch the target.** Take the URL from the argument or the user's message (or ask). Fetch the page with web fetch, plus `robots.txt` and `/llms.txt` at the domain root. If the URL is unreachable, follow Error Handling — never guess site content.
   **Permission step:** if DataForSEO is connected, ask now, once (see External tools). No or no answer = built-in path for the whole run.
2. **Score the five GEO criteria** below (weighted). For each, list concrete strong/weak findings with quoted passages from the page.
3. **Check AI crawler access** against the crawler table; report allowed vs blocked.
4. **Check llms.txt, rendering and schema by reading the HTML.** Note llms.txt presence/quality. Check whether the key content is present in the raw HTML (AI crawlers do NOT execute JavaScript — server-side rendering is critical) and extract JSON-LD blocks (`<script type="application/ld+json">`) to list the schema types present. If your fetch tool returns converted text without scripts or markup, say "not verifiable from this fetch" and ask the user to paste the page source or a Rich Results Test result; never assume.
5. **Assess brand mention footprint** (Wikipedia, Reddit, YouTube, LinkedIn) with web search; cite the URLs found.
6. **Assess information gain.** Flag content that merely restates what is already everywhere; identify where original data, first-hand experience, or a defensible opinion could be added — this is what earns citations.
7. **Probe AI answers.** If the user approved DataForSEO, use its ChatGPT scraper on the target queries and its LLM-mention search and top-domains tools for mention tracking. Otherwise run a manual probe: web search each of the 3–5 target queries and note which domains and page types surface (Google AI Overviews draw mostly from top-ranking pages), and ask the user to paste or screenshot the answers ChatGPT / Perplexity / Google AI Overviews give for the same queries. Record per query: brand cited yes/no, competitors cited, source types. Label it "manual probe, n queries" and list the server-only metrics as "not measured".
8. **Write the report** per the Output section, with platform breakdown and prioritized fixes.

---

## GEO Analysis Criteria

Score each criterion 0–100 with this rubric, then weight: **90** = every strong signal present,
no weak ones · **70** = most strong signals, one or two weak · **50** = mixed · **30** = mostly
weak · **10** = criterion essentially absent. Quote the evidence behind each score. Platform
readiness scores reuse the same criterion scores, weighted toward each platform's focus in
*Platform-Specific Optimization*; state the weights you used.

### 1. Citability Score (25%)

**Optimal passage length: 134-167 words** for AI citation.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (can be extracted without context)
- Direct answer in first 40-60 words of section
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere (information gain)

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

**Strong signals:**
- Clean H1->H2->H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials (E-E-A-T)
- Publication date and last-updated date
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**AI crawlers do NOT execute JavaScript.** Server-side rendering is critical.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt` for these AI crawlers:

| Crawler / token | Owner | Purpose |
|---------|-------|---------|
| OAI-SearchBot | OpenAI | Indexing for ChatGPT search results |
| ChatGPT-User | OpenAI | Fetches pages when a ChatGPT user asks |
| GPTBot | OpenAI | Model training |
| Claude-SearchBot | Anthropic | Indexing for Claude's search results |
| Claude-User | Anthropic | Fetches pages when a Claude user asks |
| ClaudeBot | Anthropic | Model training |
| PerplexityBot | Perplexity | Indexing for Perplexity answers |
| Perplexity-User | Perplexity | Fetches pages when a Perplexity user asks |
| Google-Extended | Google | robots.txt token controlling Gemini training use (AI Overviews use regular Googlebot) |
| CCBot | Common Crawl | Training datasets |
| Bytespider | ByteDance | Training / AI products |

Crawler names change; confirm the current list on each vendor's documentation page with web
search before reporting a block as a problem.

**Recommendation:** for AI-search visibility, allow the search and user-fetch agents (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User) and Googlebot. Blocking training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot) is a business choice that does not remove the site from AI search answers; record it, do not flag it as an error.

---

## llms.txt Standard

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
```
# Title of site
> Brief description

## Main sections
- [Page title](url): Description
- [Another page](url): Description

## Optional: Key facts
- Fact 1
- Fact 2
```

**Check for:**
- Presence of `/llms.txt`
- Structured content guidance
- Key page highlights
- Contact/authority information

---

## RSL 1.0 (Really Simple Licensing)

Standard (December 2025) for machine-readable AI licensing terms.

**Backed by:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Check for:** RSL implementation and appropriate licensing terms.

---

## Platform-Specific Optimization

| Platform | Key Citation Sources | Optimization Focus |
|----------|---------------------|-------------------|
| **Google AI Overviews** | Pages that already rank in the top results | Traditional SEO + passage optimization |
| **ChatGPT** | Wikipedia, Reddit, authoritative sites | Entity presence, authoritative sources |
| **Perplexity** | Reddit, Wikipedia, community discussions | Community validation, discussions |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

---

## Output

Deliver the report in chat and as a downloadable `<domain>-geo-analysis.md` (in Claude Code, save under `work/geo/`). Nothing is published or changed on the site. The report contains:

0. **Data sources** (e.g. "web fetch of page, robots.txt, llms.txt + web search probe of 4 queries + 2 user screenshots (no MCP used)") and a **Not measured** list
1. **GEO Readiness Score: XX/100**
2. **Platform breakdown** (Google AIO, ChatGPT, Perplexity readiness scores, plus the probe results per platform where checked)
3. **AI Crawler Access Status** (which crawlers allowed/blocked)
4. **llms.txt Status** (present, missing, recommendations — include a ready-to-use template if missing)
5. **Brand Mention Analysis** (presence on Wikipedia, Reddit, YouTube, LinkedIn)
6. **Passage-Level Citability** (optimal 134-167 word blocks identified)
7. **Information Gain Assessment** (where original data/experience/opinion is missing)
8. **Server-Side Rendering Check** (JavaScript dependency analysis)
9. **Top 5 Highest-Impact Changes**
10. **Schema Recommendations** (for AI discoverability)
11. **Content Reformatting Suggestions** (specific passages to rewrite)

Deliver the report in the user's language.

---

## Recommendations Playbook

### Quick Wins

1. Add "What is [topic]?" definition in first 60 words
2. Create 134-167 word self-contained answer blocks
3. Add question-based H2/H3 headings
4. Include specific statistics with sources (statistics + quotes + source URLs: up to +40% citations, GEO study 2024)
5. Add publication/update dates
6. Implement Person schema for authors
7. Allow key AI crawlers in robots.txt

### Medium Effort

1. Create `/llms.txt` file
2. Add author bio with credentials + Wikipedia/LinkedIn links
3. Ensure server-side rendering for key content
4. Build entity presence on Reddit, YouTube
5. Add comparison tables with data
6. Implement FAQ sections (structured, not schema for commercial sites)

### High Impact

1. Create original research/surveys (unique citability = information gain)
2. Build Wikipedia presence for brand/key people
3. Establish YouTube channel with content mentions
4. Implement comprehensive entity linking (sameAs across platforms)
5. Develop unique tools or calculators
6. Seed brand mentions where AI answers source from (Reddit threads, review sites, industry forums) — earned, never astroturfed

## Quality gates

- Never invent statistics or scores without inspecting the actual page — every finding must reference observed content.
- Every statistic in the deliverable requires a source + URL found during the run; otherwise it is cut.
- If robots.txt or llms.txt cannot be fetched, report that explicitly instead of assuming.
- AI visibility is a measured metric only with an approved server; otherwise it is a labeled manual probe. Never estimate mention counts or citation rates.
- No external server is called without a yes in this run.
- Recommendations must be specific to the analyzed page (quote the passage to change), not generic advice.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again. |
| AI crawlers blocked by robots.txt | Report exactly which crawlers are blocked and which are allowed. Provide specific robots.txt directives to add for enabling AI search visibility. |
| No llms.txt found | Note the absence and provide a ready-to-use llms.txt template based on the site's content structure. |
| No structured data detected | Report the gap and provide specific schema recommendations (Article, Organization, Person) for improving AI discoverability. |

## Example

**User:** `/seo-geo https://example.com/guide-to-crm`

**Flow:** Fetch page + robots.txt + llms.txt → score 5 criteria with quoted evidence → check crawler access (finds GPTBot blocked) → note llms.txt missing, read JSON-LD (Article only, no Person/Organization) → flag zero original data (low information gain) → no server connected, so manual probe: web search 4 buyer questions, user pastes 2 ChatGPT answers (brand cited in 0 of 4) → deliver `example-com-geo-analysis.md` with score 58/100, platform breakdown, robots.txt fix, llms.txt template, LLM-mention counts listed as "not measured", and 5 prioritized changes including one original-data suggestion.
