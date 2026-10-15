# Technical Dimension — Checks & Scoring

Crawl-based technical health check of the live site. Score this dimension 0-100.

## Sub-areas and weights

| Sub-area | Weight |
|---|---|
| Crawlability & indexability | 25% |
| Core Web Vitals / speed | 30% |
| Security | 15% |
| Mobile & rendering | 20% |
| URL & redirect hygiene | 10% |

## 1. Crawlability & indexability (25%)

- `robots.txt` exists, is valid, and does not accidentally block important paths (`Disallow: /` on production is a Critical finding)
- XML sitemap exists, is referenced from robots.txt, returns 200, contains only canonical 200-status URLs
- Canonical tags present, self-referencing on unique pages, no canonical chains or cross-domain mistakes
- No accidental `noindex` on money pages; check both meta robots and `X-Robots-Tag` header
- Internal links resolve (sample crawl): flag 404s, redirect chains > 2 hops, orphan pages
- AI crawler access: check robots.txt rules for GPTBot, ClaudeBot, PerplexityBot, Google-Extended; note `llms.txt` presence (opportunity, not a failure)

## 2. Core Web Vitals / speed (30%)

Measure with the best available source (in order): PageSpeed Insights via web fetch of the public, keyless API (`https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile`); if that fails, PageSpeed Insights results the user pastes or screenshots from pagespeed.web.dev; DataForSEO Lighthouse only if the user approved DataForSEO in the permission step. No source available = CWV "not measured" (score the remaining sub-areas and re-normalize; never estimate the numbers). Page weight and obvious causes (huge hero images, many third-party scripts) can still be inferred from the HTML and labeled "heuristic".

| Metric | Pass | Warning | Fail |
|---|---|---|---|
| LCP | < 2.5s | 2.5-4.0s | > 4.0s |
| INP | < 200ms | 200-500ms | > 500ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |
| TTFB | < 800ms | 0.8-1.8s | > 1.8s |
| Page weight | < 2MB | 2-5MB | > 5MB |

Common causes to check: uncompressed hero images (recommend WebP/AVIF), render-blocking CSS/JS, un-preloaded fonts, third-party scripts (chat widgets, heatmaps, tag bloat), no lazy loading below the fold.

QA bar: PageSpeed score >= 90 is the target for landing pages.

## 3. Security (15%)

- HTTPS enforced; HTTP redirects to HTTPS; no mixed content
- Security headers: HSTS, X-Content-Type-Options, Content-Security-Policy (missing CSP = Medium, not Critical)
- No exposed staging/dev subdomains indexed
- Valid, non-expiring-soon TLS certificate

## 4. Mobile & rendering (20%)

- Viewport meta tag present and correct
- Content parity between mobile and desktop (mobile-first indexing)
- No JavaScript-only content that fails without rendering: check whether the primary content is present in the raw HTML from web fetch (compare with what the user sees, or with the rendered page if a rendering server was approved)
- Interstitials/popups do not block content on load
- Tap targets at least 44x44 CSS px (WCAG 2.2 AAA; Google recommends 48x48) with >= 8px spacing (overlaps with design dimension; report here only if it blocks crawl/render)

## 5. URL & redirect hygiene (10%)

- Clean, readable, lowercase URLs; hyphens not underscores; no session IDs or tracking params in canonical URLs
- One canonical host (www vs non-www, trailing slash) with 301s from variants
- Redirect chains <= 1 hop; no redirect loops
- 404 page returns actual 404 status (not soft-404 200)

## Crawl configuration

```
Max pages: 100 with an approved crawler, about 25-30 with web fetch (full audit) / 25 (single-dimension quick pass)
Respect robots.txt: yes
Follow redirects: yes (max 3 hops)
Timeout per page: 30s
```

If the user approved Firecrawl in the permission step, use its map + scrape for discovery and rendered content. Otherwise use web fetch: `robots.txt` → XML sitemap → homepage → internal links, page by page on key templates (home, one service/product page, one blog post, contact). Without a crawler the sample is smaller (about 25–30 pages); say so in the report.

## Severity mapping

- **Critical**: blocks indexing or breaks the site (noindex on money pages, robots.txt blocking all, site down, cert expired)
- **High**: CWV fails, redirect loops, mixed content, mobile content missing
- **Medium**: missing sitemap entries, header gaps, chain redirects, heavy pages
- **Low**: llms.txt missing, minor URL cosmetics
