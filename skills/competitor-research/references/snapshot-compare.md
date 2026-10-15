# Snapshot Compare (rerun on demand)

Use this file when the user asks what has changed since an earlier competitor run ("what changed since last time", "update the competitor research", "monitor competitors"). Lite does not schedule or automate anything: every run is a **one-off snapshot**, and a comparison is simply a new run that is compared against an earlier snapshot the user brings back.

Do not run compare mode until a baseline snapshot exists. If the user asks for ongoing monitoring, explain this once: "I can't watch competitors in the background. Save the snapshot file I give you, and rerun `/competitor-research` whenever you want an update (monthly is a good default) — upload the snapshot and I'll report what changed." Then run a normal baseline.

## Snapshot file

Every baseline run ends by delivering a snapshot the user keeps:

- **Claude.ai:** a downloadable `competitor-snapshot-{YYYY-MM-DD}.json`. Tell the user: "Keep this file. Next time, upload it with your request and I'll compare."
- **Claude Code:** save it as `work/reports/{project-name}/snapshots/{YYYY-MM-DD}/competitor-snapshot.json`, next to that run's raw notes.

The snapshot is written by hand from the run's findings. It preserves only comparable signals:

```json
{
  "project": "project-name",
  "captured": "YYYY-MM-DD",
  "competitors": {
    "competitor-name": {
      "positioning": {
        "tagline": "",
        "primary_claim": "",
        "cta": "",
        "source": ""
      },
      "pricing": {
        "model": "",
        "entry_price": "",
        "tiers": [],
        "discounts": [],
        "hidden_or_custom": false,
        "source": ""
      },
      "features": {
        "top_features": [],
        "recent_releases": [],
        "changelog_cadence": "",
        "source": ""
      },
      "ads": {
        "meta": {"active_count": "", "dominant_angle": "", "hooks": [], "confidence": ""},
        "linkedin": {"active_count": "", "dominant_angle": "", "hooks": [], "confidence": ""},
        "google": {"ads_found": "", "themes": [], "platform_mix": [], "confidence": ""}
      },
      "seo": {
        "top_keywords": [],
        "top_pages": [],
        "content_pillars": [],
        "comparison_pages": []
      },
      "data_gaps": []
    }
  }
}
```

## How a compare run works

1. Load the earlier snapshot (uploaded file, or the `snapshots/` folder in Claude Code). If the user has only an earlier `competitor-matrix.md`, use that as a lower-confidence baseline and say so.
2. Rerun the same source set for the same competitors (same routes where possible; note any route that changed, e.g. a server approved this time but not last time — a change of route is not a change of competitor).
3. Write the new snapshot.
4. Compare signal by signal and write `competitor-diff.md`.

## Diff Comparison

Compare the new snapshot to the earlier one the user provided.

Track:

- **Pricing:** new tiers, removed tiers, price changes, discount changes, value metric changes, hidden pricing changes.
- **Positioning:** tagline, hero claim, target buyer, CTA, proof changes.
- **Features/changelog:** new launches, removed features, cadence shifts, new integrations, AI/platform bets.
- **Meta Ads Library:** active count change, dominant angle change, new repeated hooks, discontinued hooks, format shift.
- **LinkedIn Ads Library:** B2B angle change, webinar/report/demo pushes, payer/advertiser changes, targeting/impression fields when visible.
- **Google Ads Transparency:** new advertiser identity, platform mix, destination page changes, search/display/YouTube copy themes.
- **SEO/content:** new top pages, lost pages, keyword shifts, comparison content, new content pillars, abandoned topics.
- **Data gaps:** sources newly blocked, newly available, or changed in confidence.

## Impact Rating

Rate each change:

- **High:** likely to affect positioning, pricing strategy, sales objections, or next-quarter content/paid strategy.
- **Medium:** useful watch item, but not urgent.
- **Low:** minor copy/content/format change.

## Output: `competitor-diff.md`

```markdown
# Competitor Diff: {project}
*Skill: competitor-research | Mode: compare | Baseline: {baseline date} | Current: {current date}*

## Executive Summary
- **Biggest competitive move:** {change}
- **Biggest risk:** {risk}
- **Best opening:** {opportunity}

## Change Log
| Signal | Competitor | Previous | Current | Impact | Confidence | Source |
|---|---|---|---|---|---|---|
| Pricing | {name} | {old} | {new} | H/M/L | H/M/L | {source} |
| Feature/changelog | {name} | {old} | {new} | H/M/L | H/M/L | {source} |
| Ad angle | {name} | {old} | {new} | H/M/L | H/M/L | {source} |
| SEO/content | {name} | {old} | {new} | H/M/L | H/M/L | {source} |

## New or Changed Gaps
1. **{gap}** — {evidence}. Confidence: {rating}.
2. **{gap}** — {evidence}. Confidence: {rating}.
3. **{gap}** — {evidence}. Confidence: {rating}.

## Recommended Actions
1. {action tied to a High impact change}
2. {action}
3. {action}

## Data Gaps
- {gap}

## Red Flags
- {flag}

## Yellow Flags
- {flag}

## Sources
- {source}
```


## Suggested rerun cadence (for the user's own calendar)

- Monthly for fast-moving SaaS categories or active paid-media categories.
- Quarterly for slower B2B categories, or when most competitors have static websites and hidden enterprise pricing.

The user decides when to rerun; nothing is scheduled, sent or posted by this skill. Do not report Low-confidence ad-library changes as facts — mark them "needs manual verification".
