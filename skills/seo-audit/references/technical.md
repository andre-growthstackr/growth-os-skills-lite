# Technical SEO checklist (sections 1–6 = Technical score, section 7 = Performance score)

Condensed from claude-seo (MIT). Severity tags: `[C]` Critical, `[H]` High, `[M]` Medium,
`[L]` Low, `[I]` Info. Record pass / fail / not checked with evidence (header value, tag snippet,
URL) for every line.

## 1. Crawlability
- `[C]` robots.txt blocks Googlebot from important sections, or `Disallow: /` for all agents.
- `[H]` robots.txt missing (404) or returns 5xx.
- `[H]` No XML sitemap found (check robots.txt `Sitemap:` line, then example.com/sitemap.xml and
  example.com/sitemap_index.xml).
- `[M]` Sitemap not referenced in robots.txt.
- `[M]` Important pages deeper than 3 clicks from the homepage (needs crawl export or nav analysis).
- `[M]` Accidental `noindex` on pages that should rank (meta robots or `X-Robots-Tag` header).
- `[I]` Crawl budget matters only for very large sites (> 10k URLs).

### Sitemap quality (fetch the sitemap; check a sample of its URLs)
- `[M]` Sitemap lists non-200, redirected, noindexed or non-canonical URLs.
- `[M]` HTTP URLs in the sitemap of an HTTPS site.
- `[L]` All `<lastmod>` values identical (not real modification dates).
- `[H]` More than 50 000 URLs in a single file without a sitemap index.
- `[I]` `<priority>` / `<changefreq>` used (ignored by Google).
- Compare sitemap URLs with pages reached through navigation: important pages missing from the
  sitemap `[M]`.

### AI crawler rules in robots.txt
Training crawlers and AI search/retrieval crawlers are different. Blocking a training crawler does
not remove the site from AI answers; blocking a retrieval crawler does.

| Crawler token | Company | Purpose |
|---|---|---|
| `GPTBot` | OpenAI | Model training |
| `OAI-SearchBot` | OpenAI | ChatGPT search index |
| `ChatGPT-User` | OpenAI | Live browsing on user request |
| `ClaudeBot` | Anthropic | Model training |
| `Claude-SearchBot` / `Claude-User` | Anthropic | Search / user-requested retrieval |
| `PerplexityBot` | Perplexity | Search index |
| `Google-Extended` | Google | Gemini training (not Search, not AI Overviews) |
| `Bytespider` | ByteDance | Model training |
| `CCBot` | Common Crawl | Open dataset |

Report what is allowed and blocked. Unintended blocking of search/retrieval crawlers is scored in
`references/ai-search.md`, not here.

## 2. Indexability
- `[H]` Canonical missing or pointing elsewhere on key templates; canonical conflicts with noindex.
- `[M]` Duplicate variants all resolve with 200 (http/https, www/non-www, trailing slash,
  uppercase) instead of redirecting to one version.
- `[M]` Parameter URLs (sorting, filters, tracking) indexable without canonical.
- `[M]` Hreflang errors on multi-language sites (missing return links, wrong codes, no x-default).
- `[M]` Pagination that hides deeper items from crawlers.
- `[L]` Index bloat signals (tag/archive/search-result pages indexable in large numbers).

## 3. Security
- `[C]` No HTTPS, invalid/expired certificate, or HTTP does not redirect to HTTPS.
- `[H]` Mixed content (HTTP resources on HTTPS pages).
- `[M]` `Strict-Transport-Security` (HSTS) missing.
- `[L]` Missing `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`,
  `Referrer-Policy` (one Low per audit, list which are missing).
Headers can only be checked if the fetch tool returns them; otherwise mark "not checked".

## 4. URL structure
- `[H]` Redirect chains (more than 1 hop) or 302 used for permanent moves on key URLs.
- `[M]` Important pages returning 4xx/5xx, or internal links pointing to them.
- `[L]` Non-descriptive URLs (IDs, query strings for content), URLs > 100 characters,
  inconsistent trailing slashes, underscores instead of hyphens.

## 5. Mobile
Google indexes the mobile version of every site (mobile-first indexing is complete).
- `[H]` No `<meta name="viewport">` or a fixed-width viewport.
- `[M]` Content or navigation present on desktop but missing on mobile (needs screenshots or a
  rendered view).
- `[L]` Tap targets under 48×48 px, body text under 16 px, horizontal scroll (needs screenshots).

## 6. JavaScript rendering and IndexNow
- `[H]` Main content, title, canonical, meta robots or structured data only appear after
  JavaScript runs (raw HTML is nearly empty, or a framework shell like an empty root div).
  Google may use either the raw-HTML or the rendered canonical if they differ, may keep a raw-HTML
  `noindex` even if JS removes it, and does not render JS on non-200 pages. Recommend serving these
  elements in the initial HTML.
- `[M]` Canonical or robots directive differs between raw HTML and rendered DOM (needs a rendered
  view; otherwise "not checked").
- `[L]` No IndexNow support (faster discovery on Bing, Yandex, Naver; not used by Google).

## 7. Performance — Core Web Vitals (scored in `references/scoring.md` section 3)

Targets (75th percentile of real users): **LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1.** INP replaced
FID in March 2024; never mention FID.

How to get numbers, in this order (follow the permission step for any server):
1. A PageSpeed/CrUX or DataForSEO Lighthouse server the user approved.
2. Web fetch of the public PageSpeed Insights API for the homepage and one key template, mobile
   strategy, without any key:
   `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<encoded-url>&strategy=mobile`
   Read `loadingExperience` (field data, if the site has enough traffic) and
   `lighthouseResult.audits` (lab: largest-contentful-paint, total-blocking-time,
   cumulative-layout-shift). Never ask the user for a key; if the call fails or is rate-limited,
   go to step 3.
3. Ask the user to run pagespeed.web.dev for the URL and paste a screenshot or the numbers.
4. Otherwise: Performance = "not measured". You may still list **likely** causes seen in the HTML
   (hero image without dimensions or > 500 KB, many render-blocking scripts in `<head>` without
   `async`/`defer`, injected banners), labeled as heuristics, never as measurements.

Record each number with its source and retrieval date.
