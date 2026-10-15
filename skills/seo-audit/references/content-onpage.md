# On-page, content and image checklists

Condensed from claude-seo (MIT). Severity tags: `[C]` Critical, `[H]` High, `[M]` Medium,
`[L]` Low, `[I]` Info. Check every sampled page; record how many pages fail each check.

## Part A — On-Page SEO (On-Page score)

### Titles and meta descriptions
- `[C]` Title tag missing on key pages (homepage, main service/product/category pages).
- `[H]` Duplicate titles across different sampled pages.
- `[M]` Title outside 30–60 characters, primary topic not near the start, or stuffed
  ("Plumbing - Plumber - Plumbing Services").
- `[M]` Meta description missing or duplicated.
- `[L]` Meta description outside 120–160 characters or without a reason to click.

### Headings
- `[H]` No H1, or several H1s, on key pages.
- `[M]` H1 does not match the page's intent; skipped levels (H2 → H4); headings used for styling.

### Internal linking (needs nav analysis or a crawl export)
- `[H]` Key pages not linked from navigation or any sampled page (orphan risk).
- `[M]` Thin internal linking: guide is 3–5 links on a service page, 5–10 in a 1 500-word article,
  links from category pages to all children.
- `[M]` Generic anchors ("click here", "read more") on important links.

### Social and meta
- `[L]` Missing Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) or Twitter Card tags.
- `[I]` `meta keywords` present (ignored).

## Part B — Content Quality (Content score)

### Topical coverage floors (guides, not targets; word count is not a ranking factor)

| Page type | Floor (words) |
|---|---|
| Homepage | 500 |
| Service / feature page | 800 |
| Location page (primary) | 600, with ≥ 60% unique content |
| Location page (secondary) | 500 |
| Blog post / guide | 1 500 |
| Product page | 400 (300 for simple products) |
| Category page | 400 of unique intro, not only listings |
| About page | 400 |
| Landing page | 600 |

- `[H]` Key pages clearly below their floor **and** not answering the query (thin content).
- `[C]` Doorway pattern: location or programmatic pages where only the city/keyword changes
  (swap test: swap the city name and the page still reads fine). At 30+ such pages, flag a
  warning; at 50+ treat as Critical.
- `[M]` Near-duplicate copy across sampled pages of the same template.

### E-E-A-T (score each factor 0–25 in the report, citing on-page signals)
- **Experience:** original data, case studies with numbers, photos from real work, process detail.
- **Expertise:** named authors with bios and credentials, technical depth that fits the audience,
  sourced claims.
- **Authoritativeness:** citations from or mentions in recognized outlets, awards, memberships,
  client logos with substance.
- **Trustworthiness:** contact page, physical address or company details, privacy policy, terms,
  reviews/testimonials, dates, HTTPS.

Checks:
- `[H]` No trust basics on the site (no contact details, no company information, no privacy policy).
- `[H]` Articles on health, finance, legal or safety topics (YMYL) without a named, qualified author.
- `[M]` Articles without any author attribution or date.
- `[M]` Generic, interchangeable copy with no specifics, examples or first-hand detail (the
  low-quality AI-content pattern raters are told to flag).
- `[M]` Fast-changing topics not updated in 12+ months.
- `[L]` Claims and statistics without sources; no multimedia where it would help.

### Readability (quality indicator, not a ranking factor)
- `[L]` Long paragraphs (5+ sentences), average sentences over ~25 words, walls of text without
  subheads or lists, reading level far above the audience.

### Search experience (intent match)
For each key template, search its main query with web search and look at what ranks:
- `[H]` Page type mismatch: the results are guides and the page is a sales page (or the reverse),
  or results are local packs and the page has no local signals.
- `[M]` The page does not answer the question the query implies in the first screen.

## Part C — Images (Images score)

- `[H]` More than half of the content images on sampled pages lack `alt` (site-wide escalation
  applies automatically).
- `[M]` Some content images lack `alt`; alt text is a file name, "image", or keyword-stuffed.
  Good alt: 10–125 characters describing the image. Decorative images: `alt=""`.
- `[M]` Images over 500 KB (only if size is visible from headers, the PSI report, or the user).
- `[M]` `<img>` without `width`/`height` (or CSS aspect ratio) above the fold (CLS risk).
- `[L]` Images 200–500 KB; JPEG/PNG where WebP/AVIF would do; below-the-fold images not lazy-loaded.
  Do not flag missing `loading="lazy"` when a JS lazy-loader is present (`data-src`, lazysizes,
  Perfmatters, EWWW).
- `[L]` Hero/LCP image lazy-loaded (it should load eagerly, ideally with `fetchpriority="high"`).
