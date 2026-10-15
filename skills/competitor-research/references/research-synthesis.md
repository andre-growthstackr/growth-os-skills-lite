# Synthesis, Competitor Matrix & Battle Cards

After ALL waves complete, synthesize the raw findings into matrix-first outputs and deep-dive deliverables. This step creates the real analytical value — it connects dots across data sources to surface opportunities that individual research pieces can't reveal on their own.

Read `output-schemas.md` before writing. `competitor-matrix.md` is the primary artifact and must be produced before the longer report.

## Synthesis Protocol

### Before Writing

1. Read ALL raw files in `{project-name}/raw/` before writing anything
2. Look for patterns across sources — what themes repeat?
3. Identify contradictions between sources and explain which you trust more
4. Connect the dots: pricing gaps + customer complaints + hiring signals + ad angle gaps + SEO whitespace = opportunities

### Cross-Wave Connections to Look For (the high-value insights from combining data)

- **Complaint + Pricing = Opportunity:** Customers complain about a feature AND the competitor charges a premium for it → undercut with better value
- **Hiring + Product Direction = Threat:** Competitor hiring AI engineers + recent AI mentions in changelog → they're coming for that space
- **Churn Signal + Switching Cost = Wedge:** People want to leave but data portability is hard → build easy migration as a differentiator
- **Content Gap + Demand = Quick Win:** Nobody ranks for a term buyers clearly search for → own it early (demand = search volume when DataForSEO was approved; otherwise SERP evidence such as "People also ask" and forum questions, labeled "volume not measured")
- **Review Pattern + Missing Feature = MVP Feature:** Multiple competitors lack something customers want → build it first
- **Funding + Team Size = Reality Check:** Well-funded competitor with 100+ engineers → don't compete on features, compete on focus
- **Ad Angle Saturation + VoC Gap = Messaging Opening:** Everyone advertises the same outcome while customer language points elsewhere → own the underused message
- **Changelog Cadence + Pricing = Threat:** Competitor shipping fast and charging more → prepare feature comparison and value defense

### Confidence Rating

Rate every major claim:
- **High:** Multiple Tier 1/2 sources agree, recent data
- **Medium:** Some evidence but gaps, or sources partially disagree
- **Low:** Limited data, mostly inferred, or data older than 12 months

## Required Core Outputs

Create these before the deep-dive report:

- `competitor-matrix.md`
- `ad-library-intelligence.md`
- `seo-content-landscape.md`
- `feature-changelog-tracker.md`

Use the exact schemas in `output-schemas.md`.

### Matrix Rules

`competitor-matrix.md` must include rows for: positioning, target, pricing, features (top 3), feature/changelog signal, ad angle, Meta Ads Library signal, LinkedIn Ads Library signal, Google Ads Transparency signal, keywords (top 3), content pillars, proof/social proof, CTA/sales motion, and data gaps.

After the matrix, add `The Gap — three openings nobody addresses` (Swedish: `Lucka — tre öppningar ingen adresserar`) with exactly three gaps. Each gap must include evidence and confidence.

Do not create vague gaps such as "nobody is customer-centric." A valid gap sounds like "No competitor addresses Swedish onboarding for sub-20-person teams" or "Everyone pushes enterprise demo CTAs, but no one offers a fast self-serve comparison path for ops managers."

## Output File: competitors-report.md

Structure:

```markdown
# Competitive Intelligence Report: {market/product}
*Skill: competitor-research | Generated: {date}*

## Executive Summary
{5 sentences max: market concentration, key finding, biggest opportunity, biggest risk, overall assessment}

## Market Concentration
- **Structure:** fragmented / consolidating / dominated | **Active players:** {count}
- **Funding concentration:** {flowing in or drying up?} | **Entry barriers:** low/medium/high — {why}

## Key Players at a Glance
| Competitor | Stage | Funding | Strength | Weakness | Threat |
|-----------|-------|---------|----------|----------|--------|
| ... | ... | ... | ... | ... | H/M/L |

## Adjacent Solutions & Substitutes
{Broader platforms, manual alternatives, and tools from neighboring categories that compete for the same budget or job.}

## Strategic Opportunities
### Opportunity: {name}
- **What:** {description} | **Evidence:** {data points} | **Confidence:** H/M/L
- **How to exploit:** {specific recommendation}

## Strategic Risks
### Risk: {name}
- **What:** {description} | **Evidence:** {data points} | **Severity:** H/M/L
- **Mitigation:** {how to protect against it}

## Competitive Moat Assessment
| Moat Type | Present in Market? | Who Has It | Strength |
|----------|-------------------|-----------|----------|
| Network effects / Switching costs / Data moat / Brand-trust / Economies of scale | yes/no | {who} | strong/weak |

{Paragraph explaining what this means for a new entrant}

## Data Gaps & Research Limitations
Aggregate all data gaps from raw research files. For each gap: what is missing, why it matters, how to fill it (specific actions the user can take). This section is mandatory — every competitive analysis has blind spots.

## Red Flags
- {flag — things that should worry the user}

## Yellow Flags
- {flag — things to watch}
```

## Output File: feature-comparison-matrix.md

```markdown
# Competitive Feature Matrix: {market}

## Feature Comparison
| Feature | {Your Product} | {Comp 1} | {Comp 2} | {Comp 3} |
|---------|---------------|----------|----------|----------|
| {feature} | {rating} | {rating} | ... | ... |

Rating scale: Strong / Adequate / Weak / Missing / Unknown

## Gap Analysis
Features where no competitor excels (all Weak or Missing):
- {gap} — {opportunity implication}

## Differentiation Opportunities
1. {opportunity — what to build and why}
2. {opportunity}
3. {opportunity}
```

## Output File: pricing-landscape.md

```markdown
# Pricing Landscape: {market}

## Market Pricing Overview
- **Dominant value metric:** {what most charge for} | **Price range:** {lowest — highest}
- **Median price point:** {standard tier} | **Free tier prevalence:** {X of Y offer free}

## Tier-by-Tier Comparison
| | {Comp 1} | {Comp 2} | {Comp 3} |
|---|----------|----------|----------|
| Free tier / Entry / Mid / Top / Enterprise | {price — limits} | ... | ... |

## Value Metric Analysis
| Competitor | Value Metric | Why It Works/Doesn't | Impact on Scaling |
|-----------|-------------|---------------------|-------------------|

## Pricing Psychology in Use
| Tactic (anchoring / decoy tier / charm pricing / annual lock-in) | Used By | How |
|--------|---------|-----|

## Switching Cost Matrix
| Competitor | Technical | Contractual | Emotional | Overall |
|-----------|-----------|-------------|-----------|---------|
| ... | H/M/L | H/M/L | H/M/L | H/M/L |

## Pricing Whitespace
{Underserved segments, untried models, price points nobody occupies}

## Recommendations
- **If competing on price / value / model:** {strategy per path}
```

## Output File: battle-cards/{competitor-name}.md

One battle card per competitor. Keep each to ONE page — quick-reference tools, not research docs.

```markdown
# Battle Card: {Competitor Name}
*Last updated: {date}*

## At a Glance
- **What they do:** {one sentence} | **Founded:** {year} | **Funding:** {total} | **Team:** ~{size}
- **Price:** {range} | **Model:** {value metric} | **Best for:** {their ideal customer}

## Their Strengths (be honest)
- {strength — with evidence}

## Their Weaknesses (your openings)
- {weakness — with evidence from reviews/forums}

## How to Win Against Them
- **When they say "{objection},"** respond: {counter with evidence}
- **Lead with:** {your strongest differentiator vs. this specific competitor}

## When They Win Over You
- {scenario where the competitor is honestly the better choice}

## Their Customers' Top Complaint
"{verbatim quote from review}" — {source}. This matters because: {strategic implication}

## Key Vulnerability
{The single biggest weakness you can exploit — with evidence}

## Churn Signals
- {reason people leave} — frequency: common / occasional

## Watch For
{What this competitor is likely to do next based on strategic signals}
```

## Post-Synthesis Verification

After writing all deliverables and battle cards, run the verification pass in `verification-pass.md`. It checks unlabeled claims, internal contradictions, confidence consistency, and cross-deliverable coherence (battle cards vs. report, matrix vs. profiles, pricing landscape vs. profiles, opportunity/risk traceability).
