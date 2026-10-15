# Wave 1: Competitor Profiles + Web/Pricing/Product Intelligence

Read `source-router.md` and `research-principles.md` first.

**How to run these passes:** run each pass yourself, one after another, in this conversation. If your environment can run subagents you may parallelize (one pass per subagent); otherwise run the passes in sequence — same depth, just slower. Each block below is the brief for one pass. "Save to" means: in Claude Code, write the notes to that path under `work/reports/`; in Claude.ai, keep them as working notes in the conversation. Raw notes feed synthesis — they are never shown as deliverables.

---

## Research pass A1: Competitor Deep-Dives + Web/Product Surface

```
Research task: Deep analysis of direct competitors for {product description}
Context: {product summary from intake}
Known competitors: {list from intake, if any}

RESEARCH PROTOCOL — identify and profile 3-5 direct competitors in Standard mode, or 5-8 direct competitors plus 2-3 adjacent solutions in Deep mode:

ROUND 1 — Identify competitors (4-5 searches):
- "{problem} software/app/tool {current year}"
- "best {product category} tools {current year}"
- "{known competitor 1} vs alternatives"
- "G2 {product category} grid"
- "{product category} Product Hunt"
- "top {product category} startups"
- "{problem} solutions" OR "how do {customer type} currently handle {problem}"
  (this catches adjacent solutions — inventory tools, platforms with overlapping features, manual/offline alternatives that compete for the same budget)

ROUND 2 — Deep-dive each competitor (2-3 searches per competitor):
- Visit their website: capture positioning, features, messaging, social proof
- Capture homepage, pricing, product/features, docs/release notes/changelog, and blog/resource index: if the user approved Firecrawl in the permission step, scrape them with it; otherwise web fetch each page (ask for a screenshot if a page is gated or does not render)
- "{competitor name} review G2 Capterra"
- "{competitor name} crunchbase funding"
- "{competitor name} linkedin employees" (team size signals)
- "{competitor name} changelog" or "{competitor name} updates {current year}"

ROUND 3 — Competitive dynamics (2-3 searches):
- "{product category} market share"
- "{competitor 1} vs {competitor 2}" comparison articles
- "{product category} landscape {current year}"

For EACH competitor, build a complete profile:

## {Competitor Name}
- **Website:** {url} | **Founded:** {year} | **HQ:** {location}
- **Team size:** {estimate from LinkedIn/Crunchbase} | **Funding:** {total raised, last round, lead investors}
- **Stage:** bootstrapped / seed / Series A / Series B+ / public | **Estimated revenue:** {if available, or proxy}

### Product
- **Tagline:** {their actual tagline/positioning statement}
- **Core offering:** {what they sell in one sentence}
- **Key features:** {top 5-8 features}
- **Feature evidence:** {source URLs and capture dates for the feature claims}
- **Recent releases/changelog:** {recent shipped features, dates, and cadence if public}
- **Tech stack signals:** {any public info}
- **Integrations:** {key integrations}
- **Platform:** {web / mobile / desktop / API}

### Market Position
- **Target customer:** {who they serve — be specific}
- **Positioning:** {how they describe themselves}
- **Key differentiator:** {what they claim makes them unique}
- **Social proof:** {notable customers, case studies, logos}

### Traction Signals
- **G2/Capterra:** {review count and average rating}
- **Product Hunt:** {launch date, upvotes}
- **Social media:** {follower counts, engagement level}
- **Job postings:** {number and type}
- **Web traffic signals:** {only from an approved server, a user export, or a public press mention with URL; otherwise "not measured"}
- **Notable customers:** {logos or case studies}

### Strengths
- {strengths 1-3 — based on evidence, not speculation}

### Weaknesses
- {weaknesses 1-3 — based on reviews, gaps, complaints}

### Threat Level: Low / Medium / High
- {why — with evidence}

---

After all profiles:

## Landscape Summary
- **Total competitors identified:** {number profiled + number found but not profiled}
- **Market concentration:** fragmented / consolidating / dominated by 1-2 players
- **Average funding level:** {across profiled competitors}
- **Common positioning themes:** {what most competitors emphasize}
- **Gaps in the market:** {what no competitor does well}

## Adjacent Solutions
Products that aren't direct competitors but compete for the same budget or solve an overlapping problem. These matter because customers often choose "good enough" adjacent tools over a dedicated solution.
- {adjacent solution 1} — what it does, how it overlaps, why someone might pick it instead
- {adjacent solution 2}
Include: broader platforms with partial feature overlap, manual/offline alternatives, tools from adjacent categories that could expand into this space.

## Data Gaps
- [What you couldn't find and why it matters]

Save to: {project-name}/raw/competitor-profiles.md
Also save raw web/product capture notes to: {project-name}/raw/web-pricing-product-scrape.md
Also save changelog/release notes findings to: {project-name}/raw/feature-changelog-raw.md
```

---

## Research pass A2: Pricing Intelligence

```
Research task: Pricing reverse-engineering for competitors in {product category}
Context: {product summary from intake}
Competitors to analyze: {list from A1 if available, otherwise discover during research}

RESEARCH PROTOCOL:

ROUND 1 — Capture pricing pages (1 search per competitor):
- Visit each competitor's pricing page directly
- Screenshot or capture: tiers, prices, feature lists, CTAs
- Note: annual vs monthly pricing, currency, any free tier
- Capture hidden/custom pricing language, "contact sales" thresholds, usage limits, seat limits, and package names

ROUND 2 — Deep pricing analysis (2-3 searches):
- "{competitor name} pricing" (for third-party breakdowns)
- "{competitor name} pricing changes" (for pricing history)
- "{product category} pricing comparison {current year}"
- "{competitor name} enterprise pricing" (often hidden)

ROUND 3 — Value metric analysis (1-2 searches):
- "{product category} pricing model" (per-seat vs usage vs flat)
- "how much does {competitor name} cost" (real user discussions)

For EACH competitor, analyze:

## {Competitor Name} — Pricing Breakdown

### Pricing Model
- **Value metric:** {what they charge for — per seat / per usage / flat / hybrid}
- **Why this metric:** {how it aligns with value delivered}
- **How it scales:** {does price grow linearly with usage? Are there volume discounts?}
- **Visibility:** public / partially hidden / enterprise only / custom only
- **Capture source:** {URL, date, Source label}

### Tier Structure
| | {Tier 1} | {Tier 2} | {Tier 3} | {Enterprise} |
|---|----------|----------|----------|-------------|
| Price (monthly / annual / annual discount) | | | | |
| Key features (top 3) | | | | |
| Key limits | | | | |
| Target persona | | | | |

### Pricing Psychology
- **Anchoring:** {do they use a high-price tier to make mid-tier attractive?}
- **Decoy effect:** {is there a tier designed to push people to a specific plan?}
- **Charm pricing:** {$49 vs $50? $99 vs $100?}
- **Social proof on pricing:** {which tier is "most popular"?}
- **Free tier strategy:** {what's free and what's gated?}
- **Annual lock-in:** {discount size, refund policy}

### Switching Costs
- **Technical:** {data export? API migration? Integration rewiring?}
- **Contractual:** {annual contracts? Cancellation penalties?}
- **Emotional / data portability:** {brand loyalty? Learning curve? Easy data export?}

---

After all competitors:

## Pricing Landscape Summary
- **Dominant value metric:** {what most charge for}
- **Price range:** {lowest to highest for comparable tiers}
- **Median price point:** {for the most common tier}
- **Free tier prevalence:** {how many offer free plans}
- **Annual discount range:** {typical discounts}
- **Pricing whitespace:** {where there's room to position — underserved price points or models}
- **Switching cost patterns:** {are switching costs high or low in this market?}

## Data Gaps
- [Competitors with hidden/custom pricing]
- [Enterprise pricing that couldn't be found]
- [Pricing pages blocked, region-specific, or requiring login]

Save to: {project-name}/raw/pricing-intelligence.md
```

---

## Matrix Extraction Notes

Wave 1 must produce enough normalized data to fill these `competitor-matrix.md` rows:

- Positioning
- Target
- Pricing
- Features (top 3)
- Feature/changelog signal
- Proof/social proof
- CTA/sales motion
- Data gaps

If a field cannot be found, write an explicit data gap with source attempts. Do not leave the matrix cell blank.
