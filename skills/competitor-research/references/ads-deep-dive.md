# Ads Deep-Dive: Competitor Ad Intelligence

Read this file when the run scope is `ads`, or during Wave 4 when the user wants deeper ad analysis than the core Meta/LinkedIn/Google capture. It extends `research-wave-4-channel-intelligence.md` — the universal ad-library fields and evidence-log rules there still apply.

## Data Sources per Platform

| Source | Platform | What You Can Find |
|--------|----------|------------------|
| Google Ads Transparency Center | Google | Active ads, formats, geo targeting, ad history |
| Meta Ad Library | Meta/Instagram | All active ads, creative, copy; spend ranges only for political/social ads |
| LinkedIn Ad Library | LinkedIn | Active ads by advertiser/payer/keyword/country; EU ads may show targeting and impression estimates |
| TikTok Creative Center | TikTok | Top ads by industry/country/objective, trending creative and hashtags — no per-advertiser library |
| Microsoft Ads | Microsoft | Limited public data; Auction Insights from an owned account |
| Apple Ads (App Store) | Apple | Search tab ads, Today tab ads, Custom Product Page variants |

How to access them: web fetch the public library or tool page; if it does not render, ask the user for screenshots (filters visible) or pasted ad text. Claude in Chrome or Apify only if the user approved that server in the permission step (`source-router.md`). Data from the user's own ad accounts (e.g. Auction Insights) comes only as an export the user uploads.

Platform notes:

- **Meta:** filter by advertiser, country, platform, date range. Creative clustering means near-duplicate ads may be suppressed — assess conceptual diversity, not just ad count.
- **Google:** search Transparency Center by advertiser name or domain; search competitor brand terms live to see triggered ads. Auction Insights (impression share, overlap rate, outranking share) is only available from the user's own account — use it only if the user uploads that export.
- **LinkedIn:** search by company name; less data than Meta. Check whether competitors sponsor external thought leaders (Thought Leader Ads).
- **TikTok:** no advertiser lookup — use Creative Center for industry-level trends and top ads; check competitor Shop presence where relevant.
- **Apple:** search competitor brand terms in the App Store; note Today tab presence and product-page ad variants.

## Analysis Framework

### 1. Ad Copy Analysis

For each competitor, document: **headlines** (primary value propositions), **CTAs** (free trial / demo / buy now / learn more), **offers** (pricing, discounts, trials), **tone** (professional / casual / urgent / educational / emotional), **USPs** emphasized, and **pain points** addressed. Quote hooks verbatim.

### 2. Creative Strategy Analysis

- **Formats used:** image, video, carousel, collection, document
- **Visual style:** photography, illustration, UGC, stock, branded
- **Video approach:** studio quality vs UGC vs animated
- **Creative volume:** number of active ads (testing-velocity signal, NOT a budget signal)
- **Refresh frequency:** how often new creatives appear

### 3. Messaging Theme Matrix

Categorize competitor messaging and mark each theme Primary / Secondary / Absent:

| Theme | {Comp A} | {Comp B} | {Comp C} | Your Brand |
|-------|----------|----------|----------|------------|
| Price/Value | | | | |
| Quality/Premium | | | | |
| Speed/Convenience | | | | |
| Trust/Authority | | | | |
| Innovation | | | | |

Rows are a starting set — replace with the themes actually present in the captured ads. The empty or thin columns/rows are gap candidates.

### 4. Keyword Intelligence (Google/Microsoft/Apple)

- Brand keyword bidding: are competitors bidding on the user's brand?
- Keyword overlap: which non-brand terms do both target?
- Keyword gaps: terms competitors target that the user does not (and vice versa)
- Keyword data: if the user approved DataForSEO, use it; otherwise use a user-uploaded export or manual SERP sampling with web search (search competitor brand and category terms and note which ads appear), labeled Medium/Low confidence. Search volume and CPC without an export or approved server are "not measured"

### 5. Spend Estimation (handle with care)

Public libraries rarely show spend. Only offer directional estimates, always labeled `[Estimate]` with the math shown:

```
Estimated Monthly Spend ≈ Impressions × CPM / 1000   (when impressions are visible, e.g. EU fields)
Estimated Monthly Spend ≈ Clicks × CPC              (only with CPC from a user export or an approved server — never a guessed CPC)
```

Never present an estimate as fact. Never treat ad count as budget. If nothing supports an estimate, write a data gap instead.

## Gap & Opportunity Identification

The output of the ads dimension is the gap list — what nobody does:

- **Platform gaps:** platforms competitors are NOT on or visibly underinvest in
- **Messaging gaps:** pain points and value propositions NO competitor's ads address (cross-check against `voice-of-customer.md` — customer language nobody advertises is the strongest opening)
- **Audience gaps:** segments, geos, or funnel stages competitors' visible ads neglect
- **Creative gaps:** formats and styles missing from the landscape (video, UGC, document ads, interactive)

Each gap needs evidence (which libraries were checked, what was absent) and a confidence rating.

## Competitive Response Playbook

Include in the deliverable when relevant:

**If competitors bid on the user's brand:** run defensive brand campaigns (low CPC, high CTR), use sitelinks to pricing/reviews, lead copy with unique differentiators, and evaluate bidding on competitor terms within platform rules.

**If the user is outspent:** compete on efficiency — long-tail keywords competitors ignore, exact match precision, retargeting over prospecting, creative quality over volume.

## Ads-Scope Deliverable

When scope is `ads`, produce `{project-name}/ad-library-intelligence.md` (schema in `output-schemas.md`) extended with:

- Messaging Theme Matrix (section 3)
- Keyword overlap/gap table (section 4)
- Gap & opportunity list with evidence and confidence
- Competitive response recommendations

Standard footer applies: Data Gaps, Red Flags, Yellow Flags, Sources.
