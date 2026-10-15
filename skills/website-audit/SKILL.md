---
name: website-audit
description: >
  Holistic website audit across four dimensions — technical health, SEO/AI-search
  readiness, design/UX, and conversion — merging crawl-based SEO auditing, a
  five-dimension design diagnostic, and landing-page conversion analysis with
  the friction model (interactive/cognitive/emotional). Produces a scored audit
  report plus a prioritized action plan (impact x effort). Scope one dimension or
  run all four. Use when user says "granska min hemsida", "audita min webbplats",
  "webbplatsanalys", "hälsokoll på sajten",
  "audit my website", "website audit", "site health check", "review my site",
  "check my whole site". For a single page that is not converting, use cro-audit.
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: web-os
  source: "claude-seo/seo-audit v1.9.9 + impeccable/audit + ads-landing v1.5 (merged)"
---

# Website Audit

Audit a live website across four dimensions — technical, SEO, design/UX, conversion — and deliver a scored report with a prioritized action plan. The conversion lens throughout is the friction model: every conversion finding is tagged **interactive**, **cognitive**, or **emotional** friction.

**Respond and produce all deliverables in the user's language.** Internal reasoning and file structure stay as specified here.

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `icp.md` — who the site must convince (OPTIONAL — sharpens the conversion and content assessment)
- `voice-of-customer.md` — customer language and objections (OPTIONAL — used to judge jargon vs customer language and whether top objections are answered)
- `offer.md` — offer, pricing, guarantees (OPTIONAL — used to judge value proposition and pricing clarity)
- `business-profile.md` — company, services, goals (OPTIONAL — helps detect business type and the main conversion goal)
- `brand-guidelines.md` — colors, typography, tone (OPTIONAL — use if present for on-brand consistency checks in the design dimension; Lite continues without it)

**Minimum context if files are missing** — ask these in one message and continue (use the
environment's question tool if there is one, AskUserQuestion in Claude Code or option boxes in
Claude.ai; otherwise numbered questions in chat):
1. Which URL should I audit, and which dimensions (all four, or technical / SEO / design / conversion)?
2. What is the site's main conversion goal (book a call, request a quote, buy, sign up)?
3. Who is the main audience (role, company type or consumer segment)?
4. Is paid or campaign traffic sent to a specific landing page? If so, what does the ad promise?

None of the files are required. When one is missing, run the affected checks generically and
note in the report which assessments would sharpen with context (e.g. "objection coverage judged
generically — run `/icp-builder` and `/brand-voc` for an ICP-specific pass"). Never invent brand
or customer facts.

## External tools — ask first

This skill works fully without external servers: web fetch of the pages, `robots.txt` and
sitemap, web search, the public PageSpeed Insights check, and screenshots or exports the user
uploads. Follow `references/mcp-permission.md` before the first call to any server below (ask
once per server per run, only if the server is already connected).

| Server (optional) | Used for | Requires | Built-in path (no MCP) |
|---|---|---|---|
| Firecrawl | Mapping site URLs and scraping rendered pages at scale (up to 100 pages) | Firecrawl account, uses credits | Web fetch of `robots.txt`, the XML sitemap and the homepage, then follow internal links page by page (25–30 pages, 5–10 deep-analyzed) |
| DataForSEO | Lighthouse lab data, ranked keywords, keyword volumes, backlink summary, live SERP checks, LLM-mention tracking | DataForSEO account, paid credits | PageSpeed Insights (keyless web fetch, or the user pastes or screenshots pagespeed.web.dev results); web search for SERP spot checks and brand mentions; volumes, rankings and backlinks reported as "not measured" |
| Claude in Chrome | Rendering pages at desktop and mobile width, screenshots, form and CTA click-through | Claude in Chrome extension connected | The user uploads desktop + mobile screenshots of the key pages; otherwise visual checks are labeled "HTML-inferred" |

Metrics that exist ONLY with a server (reported as "not measured" when declined, never
estimated): keyword search volumes, ranked keywords and positions, backlink and referring-domain
counts, LLM-mention counts, and full-site crawl coverage beyond the sampled pages. Core Web
Vitals are measured only when PageSpeed Insights (keyless fetch or user-supplied result) or a
server provides them; otherwise "not measured".

## Arguments (scope as argument)

`/website-audit [url] [dimension...]`

- `/website-audit https://example.com` → all four dimensions, full report
- `/website-audit https://example.com seo` → SEO dimension only
- `/website-audit https://example.com design conversion` → two dimensions
- Dimension aliases: `technical`, `seo`, `design` (also `ux`), `conversion` (also `cro`)

In Claude.ai (no slash commands) the user just asks ("audit example.com, focus on conversion").
No URL given? Ask for it (or take it from `business-profile.md` and confirm). Read ONLY the
reference files the scope requires:

| Dimension | Reference |
|---|---|
| technical | `references/technical.md` |
| seo | `references/seo.md` |
| design | `references/design-ux.md` |
| conversion | `references/conversion.md` |

## Instructions

1. **Resolve scope and load references.** Parse URL + dimensions, load the matching reference file(s). Confirm scope in one line before starting.
2. **Permission step.** If any server in the table above is connected and would help this scope, ask once per server now (per `references/mcp-permission.md`). No answer or no = built-in path for the rest of the run.
3. **Fetch and detect.** Fetch the homepage with web fetch. Detect business type (local service, e-commerce, SaaS, B2B services, content/blog, portfolio) — it changes which checks matter (e.g. LocalBusiness schema, product pages, demo funnels). State the detected type.
4. **Crawl a representative sample.** If the user approved Firecrawl, use it to map the site (up to 100 URLs) and scrape the templates. Otherwise fetch `robots.txt` and the XML sitemap, then follow internal links with web fetch: full audit ~25–30 pages discovered, deep-analyze 5–10 representative templates (home, key money page, one content page, contact/form page); single dimension: 3–5 deep. Respect robots.txt; if fetching is blocked or fails, report the limitation and analyze accessible pages only — never guess site content.
5. **Run each in-scope dimension** exactly as its reference file specifies, one dimension at a time. For design and conversion: if the user approved Claude in Chrome, render key pages at desktop and mobile width and take screenshots. Otherwise ask the user to upload desktop + mobile screenshots of the homepage and one key page; if none arrive, judge from HTML and label visual checks "HTML-inferred".
6. **Measure speed and enrich.** Core Web Vitals: try the public PageSpeed Insights API once with web fetch (no key: `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile`). If that fails (quota, blocked fetch), ask the user to run pagespeed.web.dev on the URL and paste the numbers or a screenshot; if they cannot, mark CWV "not measured". If the user approved DataForSEO, use it for Lighthouse, keywords, backlinks and SERP checks; otherwise those metrics are "not measured". Label every metric as measured (with source) vs heuristic.
7. **Score.** Each dimension scores 0-100 per its reference. Overall Website Health Score for full audits:

   | Dimension | Weight |
   |---|---|
   | Technical | 25% |
   | SEO | 25% |
   | Design/UX | 20% |
   | Conversion | 30% |

   Grades: A 90-100 · B 75-89 · C 60-74 · D 40-59 · F below 40. Single-dimension runs report only that dimension's score. A sub-area that could not be measured is excluded and the weights re-normalized; say so next to the score.
8. **Build the action plan (impact x effort).** Collect every finding, then place each in a 2x2:

   | | Low effort | High effort |
   |---|---|---|
   | **High impact** | Quick wins — do first | Strategic projects — plan |
   | **Low impact** | Fill-ins — batch later | Reconsider — usually skip |

   Within each quadrant, order by severity (Critical > High > Medium > Low). Every item: finding, dimension, friction type (conversion items), impact rationale, concrete fix, effort estimate (S/M/L), and a suggested owner (developer, designer, copywriter, marketer) or a Lite skill that helps (`/copywriting`, `/cro-audit`, `/seo-audit`, `/seo-geo`).
9. **Write the report and present a summary.** Deliver the files (Output below), then give the user the executive summary in chat: score(s), top 5 critical issues, top 5 quick wins, data sources used, and next steps.
10. **Human in the loop.** The audit itself is read-only. Never modify, deploy, or publish anything to the site as part of this skill. If the user wants fixes implemented, that is a separate explicit request — wait for a go-ahead.

## Output

Deliver in chat and as two downloadable `.md` files (in Claude Code, save under
`work/website-audit/`):

- `<domain>-website-audit-report.md` — full findings:
  - Executive summary: overall score + grade, per-dimension scores (bar-style visualization), business type detected, top 5 critical issues, top 5 quick wins
  - Data sources line (e.g. "Data: web fetch of 8 pages + PageSpeed Insights + user screenshots (no MCP used)") and a "Not measured" list
  - Anti-patterns verdict (design dimension first — "does this look templated/AI-generated?", honest and specific)
  - Per-dimension sections with sub-scores, findings (severity-tagged; conversion findings friction-tagged), and positive findings worth keeping
  - Systemic patterns (recurring issues, not one-offs)
- `<domain>-website-action-plan.md` — the impact x effort matrix, then a numbered, ordered task list (quadrant → severity) with fix, effort (S/M/L), and suggested owner

Both documents in the user's language.

## Quality gates

- **No invented numbers.** Rankings, traffic, conversion rates, search volumes, backlink counts, and lift percentages appear only when measured or sourced (with URL). Impact estimates without data are directional labels (High/Medium/Low), never percentages.
- **Measured vs heuristic labeled.** Every metric states its source (PageSpeed Insights, user-supplied screenshot/export, an approved server, or "inferred from HTML").
- **Verify before reporting.** No finding without a concrete location and a stated user/business impact. No false positives — if unsure, verify or mark as "needs manual check".
- **Severity discipline.** Critical = blocks indexing/conversion/access. Everything cannot be P0; too many low-priority items is noise — cap Low findings at the genuinely useful.
- **Friction tagging.** Every conversion finding carries interactive/cognitive/emotional.
- **Positive findings required.** Every dimension section names at least one thing that works and should be kept.
- **Permission respected.** No external server is called without a yes in this run.
- **Read-only.** No site changes, deploys, or publishing from this skill.

## Example

**User:** `/website-audit https://acme-consulting.se conversion`

**Flow:** Scope = conversion only → load `references/conversion.md` → context: finds `icp.md` and `voice-of-customer.md` in the Claude project, notes `offer.md` missing → no servers connected, so built-in path → fetches homepage, detects B2B services → fetches sitemap and 4 key pages → asks for desktop + mobile screenshots of home and contact; user uploads them → runs the five conversion sub-areas, tags each finding with friction type, checks objection coverage against VoC objections → scores Conversion 54/100 (D) → delivers `acme-consulting-se-website-audit-report.md` + `acme-consulting-se-website-action-plan.md` in Swedish (user wrote Swedish) → chat summary: score, top issues ("CTA 'Skicka' below fold on mobile — interactive + cognitive friction, High"), quick wins, and the note that offer clarity checks would sharpen after `/brand-offer` builds `offer.md`.
