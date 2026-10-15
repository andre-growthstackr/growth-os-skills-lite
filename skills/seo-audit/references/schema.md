# Schema / structured data checklist (Schema score)

Condensed from claude-seo (MIT), status as of early 2026. Severity tags: `[C]` `[H]` `[M]` `[L]` `[I]`.

## Detection
1. JSON-LD: `<script type="application/ld+json">` blocks (preferred format).
2. Microdata: `itemscope`, `itemprop`. 3. RDFa: `typeof`, `property`.
Note if JSON-LD is injected by JavaScript (only visible in a rendered view): time-sensitive markup
(Product, Offer) should be in the initial HTML.

## Checks
- `[H]` Invalid JSON-LD (parse errors), missing `@context`/`@type`, placeholder text
  ("[Business Name]"), or missing required properties on key templates.
- `[H]` No structured data anywhere in the sample.
- `[M]` Homepage without `Organization` (or the right `LocalBusiness` subtype for local firms).
- `[M]` Template without its expected type: `Product` + `Offer` on product pages, `Article` /
  `BlogPosting` on posts, `BreadcrumbList` on deep pages, `Service` on service pages,
  `LocalBusiness` on location pages, `Person`/`ProfilePage` on author pages.
- `[M]` Deprecated types still in use (see table) or Microdata only.
- `[L]` Missing recommended properties (`logo`, `sameAs`, `image`, `dateModified`, `aggregateRating`
  with real reviews), relative URLs, dates not ISO 8601, `http://schema.org` instead of https.
- `[I]` FAQPage on a commercial site: no Google rich result (restricted to government and health
  authorities since Aug 2023), but it can still help AI answers. Do not ask to remove it.

## Type status

| Status | Types |
|---|---|
| Active — recommend | Organization, LocalBusiness (+ subtypes), WebSite, WebPage, BreadcrumbList, Service, Product, ProductGroup, Offer, Review, AggregateRating, Article, BlogPosting, NewsArticle, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, SoftwareApplication, WebApplication, DiscussionForumPosting |
| Restricted | FAQPage (rich results only for government/health authority sites) |
| Deprecated — never recommend | HowTo (Sept 2023), SpecialAnnouncement (July 2025), CourseInfo, EstimatedSalary, LearningVideo, ClaimReview, VehicleListing (retired June 2025), Practice Problem, Dataset (retired late 2025) |

E-commerce: `MerchantReturnPolicy` needs `returnPolicyCountry` (required since March 2025).

## Validation checklist (per block)
1. `@context` is `https://schema.org`. 2. `@type` valid and not deprecated. 3. Required properties
present. 4. Value types correct. 5. No placeholders. 6. Absolute URLs. 7. ISO 8601 dates.
8. Image URLs resolve. 9. Facts match what is visible on the page.

Suggest the user confirm with Google's Rich Results Test (search.google.com/test/rich-results)
and the Schema.org validator (validator.schema.org).

## Fix snippets
When recommending a block, give ready-to-paste JSON-LD filled with real values from the page or
`business-profile.md`. Anything not known stays an explicit placeholder for the user, never an
invented value. Minimal Organization example:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company name]",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "sameAs": ["[LinkedIn URL]"]
}
```
