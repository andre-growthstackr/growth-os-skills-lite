# Conditional passes (run only when the business type calls for them)

Findings from these passes are reported in their own sections and also feed the scored categories
named in brackets. Severity tags: `[C]` `[H]` `[M]` `[L]` `[I]`. Condensed from claude-seo (MIT).

## Business type detection (from homepage, nav, footer, schema, `business-profile.md`)

| Type | Signals |
|---|---|
| Local service | Street address or service-area text, phone in header, map embed, "near me" or city terms, `LocalBusiness` schema |
| E-commerce | Cart, product grids, prices, `Product`/`Offer` schema, checkout links |
| SaaS / software | Pricing tiers, "free trial", "sign up", integrations, docs/app subdomain |
| Publisher / content-led | Blog or magazine as main nav, categories, authors, dates |
| B2B services / agency | Services, case studies, "book a call", team pages |

Local sub-type: **brick-and-mortar** (visible address), **service-area business** (areas served, no
address), or **hybrid**. Service-area businesses skip the address and map checks.

## Local pass (local service detected)

- **NAP consistency** [Content]: compare business Name, Address, Phone between the footer/contact
  page and the `LocalBusiness` JSON-LD. `[H]` if they conflict, `[M]` if NAP is not in HTML text.
- **Local on-page** [On-Page]: `[M]` key service pages lack city/area in title or H1; `[M]` no
  dedicated page per core service; `[L]` no `tel:` click-to-call link in the header on mobile.
- **Location pages** [Content]: apply the doorway swap test from `references/content-onpage.md`.
  Unique local content: local photos, area-specific testimonials and FAQs, local team.
- **Local schema** [Schema]: `[M]` generic `LocalBusiness` where a subtype fits (Restaurant,
  Dentist, LegalService, Plumber, AutoDealer…); `[L]` missing `geo`, `openingHoursSpecification`,
  `telephone`, `areaServed` (service-area businesses); multi-location: one `LocalBusiness` per
  location page with its own `@id`.
- **Google Business Profile and reviews** (not scored, observations only): use web search for the
  business name + city to see whether a profile, star rating and review count are publicly visible,
  and whether Bing Places, Apple Business Connect and the main industry directories list it. Report
  what you saw with URLs. Never invent review counts or ratings.
- Not possible without paid data: local-pack positions, geo-grid rankings. Report as not measured.

## E-commerce pass (shop detected)

- [Schema] `[H]` product pages without `Product` + `Offer` (price, currency, availability);
  `[M]` no `MerchantReturnPolicy` or shipping details; variants without `ProductGroup`.
- [Content] `[M]` manufacturer-copy product descriptions repeated across products; `[M]` category
  pages with no unique intro text.
- [Technical] `[M]` faceted/filter URLs indexable without canonical or noindex; `[L]` out-of-stock
  handling unclear (removed pages returning 404 without redirect to the category).
- [Images] product images without descriptive alt text.

## Content-strategy pass (blog, guides or a content hub detected)

- Group sampled articles by topic. `[M]` [Content] isolated posts with no pillar page or internal
  links between related posts; `[M]` two or more posts targeting the same query (cannibalization
  risk; confirm with a `site:` web search for the query).
- `[L]` no author pages; no updated dates on older evergreen posts.
- Recommend a pillar + cluster structure for the 1–3 strongest topics. To write the posts, hand
  off to `/blog-write`.

## Previous audit comparison (only if the user uploads an earlier audit report)

Compare category scores and the open Critical/High items with the earlier report. List what was
fixed, what is still open, and what is new. Do not compare against anything you cannot see.
