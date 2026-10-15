# Source Router

Use this file before collecting data. The goal is to choose the best permitted source for each signal, label the source honestly, and fall back without fabricating.

**Built-in first.** Every signal below has a built-in route — web search, web fetch, files or screenshots the user uploads, or an interview — and the skill delivers a complete result with those alone. External servers (Firecrawl, DataForSEO, Apify, Claude in Chrome) are optional upgrades, used only after the permission step in `mcp-permission.md` (ask once per server, before its first call, with what it is for, what it requires, and the built-in alternative). A "no" or no answer means the built-in route, without asking again.

## Source Labels

Every ad-library and tool-derived claim must include:

- **Source:** Web fetch / Web search / User screenshot / User export / Server ({name}, approved)
- **Captured:** YYYY-MM-DD
- **Confidence:** High / Medium / Low
- **Limitations:** none / sample only / limited history / blocked / no spend / no impressions / EU-only fields / hidden pricing / unavailable

Use these labels in raw notes and keep them in synthesized deliverables when the claim affects a decision.

## Routing Table

| Signal | Built-in route (always available) | Optional server route (only if approved) | Notes |
|---|---|---|---|
| Homepage positioning | Web fetch of the homepage | Firecrawl scrape | Capture exact tagline, H1, proof logos, CTAs |
| Pricing | Web fetch of the pricing page; user screenshot if it is gated or rendered by script | Firecrawl scrape | Preserve exact amounts, billing cadence, tiers, discounts |
| Features/product pages | Web fetch of product/feature pages | Firecrawl scrape | Capture top features and claims, not only a page summary |
| Docs/changelog/release notes | Web fetch of the changelog; web search `site:{domain} changelog OR "release notes"` | Firecrawl scrape/map | Date every shipped feature signal |
| Blog/resources | Web fetch of the blog index or `sitemap.xml` | Firecrawl map | Read the index first; do not crawl the whole blog unless Deep mode |
| SEO ranked keywords | Manual SERP sampling with web search for 10-20 category queries; user-uploaded export from their own SEO tool | DataForSEO | Use the project's location/language. Sampled positions are Medium/Low confidence |
| Search volume / CPC / keyword difficulty | User-uploaded export (e.g. a CSV from a keyword tool they already use) | DataForSEO | Otherwise **not measured** — never estimated |
| Backlinks / domain authority / traffic estimates | User-uploaded export | DataForSEO | Otherwise **not measured** — never estimated |
| Google Ads Transparency | Web fetch of the Google Ads Transparency Center page for the advertiser; if it does not render, ask the user for screenshots | DataForSEO (Ads Transparency data) or Claude in Chrome | Google Ads API is never the route for competitor transparency |
| Meta Ad Library | Web fetch of the Meta Ad Library search URL; if it does not render, ask the user for screenshots or copied ad text | Claude in Chrome (browse + screenshot) or Apify (ad-library actor) | Never promise spend for commercial ads |
| LinkedIn Ad Library | Web fetch of the LinkedIn Ad Library search URL; if it does not render, ask the user for screenshots | Claude in Chrome or Apify | EU ads may expose extra targeting/impression fields |
| Social/community | Web search; web fetch of public profiles | — (built-in only) | Capture follower counts only with dates |
| Reviews/forums | Web search; web fetch of review pages | — (built-in only) | Tier 3 evidence is useful for sentiment, not hard numbers |

Useful public URLs for web fetch (replace the query):

- Meta Ad Library: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={CC}&q={advertiser}`
- LinkedIn Ad Library: `https://www.linkedin.com/ad-library/search?accountOwner={company}`
- Google Ads Transparency Center: `https://adstransparency.google.com/?region={CC}&domain={domain}`

These pages are often rendered by script and may come back empty through web fetch. That is a normal limitation, not a failure: ask the user once for screenshots (one per competitor and library, with the filters visible) or pasted ad text, and continue with the other sources while you wait.

## Source plan

Before the baseline, record the actual plan (Claude Code: `{project-name}/source-plan.md`; Claude.ai: a short note in chat):

```markdown
# Source Plan: {project}
*Generated: {date}*

## Routes
- Web search: yes/no
- Web fetch: yes/no
- Firecrawl: approved / declined / not available
- DataForSEO: approved / declined / not available
- Apify: approved / declined / not available
- Claude in Chrome: approved / declined / not available
- User uploads/screenshots: {what the user provided}

## Source Routing
| Signal | Route used | Fallback | Status |
|---|---|---|---|
| Web/pricing/features | {web fetch or Firecrawl} | user screenshot | ok / blocked |
| SEO/content | {SERP sampling, export, or DataForSEO} | data gap | ok / partial |
| Meta Ad Library | {web fetch, screenshots, Chrome or Apify} | data gap | ok / blocked |
| LinkedIn Ad Library | {web fetch, screenshots, Chrome or Apify} | data gap | ok / blocked |
| Google Ads Transparency | {web fetch, screenshots, Chrome or DataForSEO} | data gap | ok / blocked |

## Not measured (server declined or unavailable)
- {e.g. search volume, keyword difficulty, backlinks}
```

## Platform-Specific Rules

### Meta Ad Library

The public Meta Ad Library is the default path for commercial competitor research. Capture active ad count, repeated copy, creative format, CTA, landing page, date range if visible, and dominant angle.

Do not claim exact spend or full delivery unless the platform exposes it for that ad type and region.

### LinkedIn Ad Library

The public LinkedIn Ad Library is the default path. Capture advertiser, payer, ad format, country/date filters, restricted status, preview/copy, CTA and landing page when visible.

For EU-targeted ads, capture targeting parameters and estimated impressions if shown. If the field is absent, write `Not visible`, not `None`.

### Google Ads Transparency

Use the public Google Ads Transparency Center (web fetch or user screenshots). If the user approved DataForSEO in the permission step, its Ads Transparency data may be used instead because it is normalized.

Do not use the Google Ads API for public competitor transparency — it only covers accounts the user owns.

### SEO and Content

Default: manual SERP sampling with web search (which competitors appear for which category queries), plus web fetch of competitors' top pages, comparison pages and blog index — clearly marked Medium/Low confidence. If the user uploads an export from an SEO tool they already use, use it and label it `User export`. If the user approved DataForSEO, use it for ranked keywords, search volume, keyword difficulty, domain competitors, traffic estimates, backlinks, and relevant pages. When none of these give a number, write **not measured**.

## Fallback Behavior

If a source fails:

1. Retry with one alternative query or route.
2. Mark the source status in the raw notes.
3. Add a data gap with why it matters.
4. Continue with other sources.

Never replace a failed source with inference. Example: if the Meta Ad Library is blocked and the user has no screenshots, do not infer active ad angles from organic social posts.
