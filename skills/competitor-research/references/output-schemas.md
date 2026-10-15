# Output Schemas

Use these schemas during synthesis. The core outputs come first; deep-dive outputs support them.

Every deliverable starts with:

```markdown
# {Title}: {project/product}
*Skill: competitor-research | Mode: baseline/compare | Generated: {date}*
```

Every deliverable ends with:

```markdown
## Data Gaps
- {gap}

## Red Flags
- {flag}

## Yellow Flags
- {flag}

## Sources
- [{source label}] {url or description} — captured {date} — confidence {High/Medium/Low}
```

## `competitor-matrix.md`

This is the core artifact. Keep it compact enough to feed directly into positioning work.

Language: deliverables follow the user's language. If the user works in Swedish, name the file
`konkurrent-matris.md`, use Swedish labels (Positionering, Målgrupp, Pris, Annonsvinkel, Sökord),
and title the gap section `Lucka — tre öppningar ingen adresserar`.

```markdown
# Competitor Matrix: {category/product}
*Skill: competitor-research | Mode: baseline | Generated: {date}*

## Scope
- **ICP:** {buyer/pain}
- **Market:** {geo/language}
- **Competitors:** {3-5 primary competitors}
- **Source mix:** web search + web fetch {yes/no}, user uploads {what}, optional servers {approved/declined/not available per server}, Meta {route}, LinkedIn {route}, Google Ads Transparency {route}
- **Not measured:** {metrics that need a declined/unavailable server, e.g. search volume, backlinks}

## Matrix
| Signal | {Comp A} | {Comp B} | {Comp C} | {Comp D} | {Comp E} |
|---|---|---|---|---|---|
| Positioning | {tagline/claim + source} | | | | |
| Target | {buyer/segment} | | | | |
| Pricing | {exact tiers/model/discounts or data gap} | | | | |
| Features (top 3) | {feature 1; feature 2; feature 3} | | | | |
| Feature/changelog signal | {recent releases/cadence} | | | | |
| Ad angle | {dominant cross-platform angle} | | | | |
| Meta Ads Library signal | {active count/angle/hooks/source/confidence} | | | | |
| LinkedIn Ads Library signal | {angle/hooks/source/confidence} | | | | |
| Google Ads Transparency signal | {themes/platforms/source/confidence} | | | | |
| Keywords (top 3) | {keyword 1; keyword 2; keyword 3} | | | | |
| Content pillars | {pillar themes} | | | | |
| Proof/social proof | {logos, reviews, metrics, case studies} | | | | |
| CTA/sales motion | {demo/free trial/contact sales/etc.} | | | | |
| Data gaps | {most important missing data} | | | | |

## The Gap — three openings nobody addresses
1. **{Concrete gap}** — {why it matters}. Evidence: {matrix rows/sources}. Confidence: High/Medium/Low.
2. **{Concrete gap}** — {why it matters}. Evidence: {matrix rows/sources}. Confidence: High/Medium/Low.
3. **{Concrete gap}** — {why it matters}. Evidence: {matrix rows/sources}. Confidence: High/Medium/Low.
```

Rules:

- Exactly three gaps.
- Gaps must be falsifiable and tied to source data.
- If a gap depends on incomplete ad-library data, confidence cannot be High.

## `ad-library-intelligence.md`

```markdown
# Ad Library Intelligence: {category/product}
*Skill: competitor-research | Mode: baseline | Generated: {date}*

## Platform Coverage
| Competitor | Meta Checked | LinkedIn Checked | Google Checked | Biggest Limit |
|---|---|---|---|---|
| {name} | yes/no | yes/no | yes/no | {limit} |

## Competitor Breakdowns
### {Competitor}

#### Meta Ads Library
- **Source/Captured/Confidence:** {label}
- **Active ads found:** {number/range/unknown}
- **Dominant angle:** {angle}
- **Hooks:** "{hook}", "{hook}", "{hook}"
- **CTA/landing page:** {pattern}
- **Limitations:** {limits}

#### LinkedIn Ads Library
- **Source/Captured/Confidence:** {label}
- **Dominant B2B angle:** {angle}
- **Hooks:** "{hook}", "{hook}", "{hook}"
- **Advertiser/payer:** {if visible}
- **EU targeting/impressions:** {visible fields or Not visible}
- **Limitations:** {limits}

#### Google Ads Transparency
- **Source/Captured/Confidence:** {label}
- **Advertiser identity:** {identity}
- **Platform mix/formats:** {mix}
- **Copy themes:** {themes}
- **Destination pages:** {pages}
- **Limitations:** {limits}

## Cross-Platform Patterns
- {pattern}

## Channel Gaps
- {gap}
```

## `seo-content-landscape.md`

```markdown
# SEO & Content Landscape: {category/product}
*Skill: competitor-research | Mode: baseline | Generated: {date}*

## SEO Matrix
| Competitor | Top Keywords | Top Pages | Content Pillars | Comparison Pages | Backlink/Authority Signal | Gap |
|---|---|---|---|---|---|---|
| {name} | | | | | | |

## Keyword Opportunities
| Topic/Keyword | Current Owner | Search Signal | Why It Matters | Confidence |
|---|---|---|---|---|
| {topic} | {competitor/none} | {sampled rank; volume/CPC only from an export or approved server, else "not measured"} | {reason} | {confidence} |

## Content Whitespace
- {opportunity}
```

## `feature-changelog-tracker.md`

```markdown
# Feature & Changelog Tracker: {category/product}
*Skill: competitor-research | Mode: baseline | Generated: {date}*

## Feature Matrix
| Feature/Capability | {Comp A} | {Comp B} | {Comp C} | Evidence |
|---|---|---|---|---|
| {feature} | Strong/Adequate/Weak/Missing/Unknown | | | {sources} |

## Recent Product Movement
| Competitor | Recent Shipped Features | Cadence | Direction Signal | Confidence |
|---|---|---|---|---|
| {name} | {features + dates} | weekly/monthly/rare/unknown | {AI/platform/integrations/etc.} | {confidence} |

## Product Gaps
- {gap}
```

## `competitor-diff.md`

Read `snapshot-compare.md` for the full schema. Use this compact top-level shape:

```markdown
# Competitor Diff: {category/product}
*Skill: competitor-research | Mode: compare | Baseline: {date} | Current: {date}*

## Executive Summary
- {most important change}
- {risk}
- {opportunity}

## Changes by Signal
| Signal | Competitor | Previous | Current | Impact | Confidence |
|---|---|---|---|---|---|
| Pricing | | | | | |
| Features/changelog | | | | | |
| Ad angle | | | | | |
| SEO/content | | | | | |

## Recommended Actions
1. {action}
2. {action}
3. {action}
```
