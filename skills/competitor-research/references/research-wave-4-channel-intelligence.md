# Wave 4: Channel & Ad Library Intelligence

Read `source-router.md` and `research-principles.md` first.

**How to run these passes:** run each pass yourself, one after another, in this conversation. If your environment can run subagents you may parallelize (one pass per subagent); otherwise run the passes in sequence — same depth, just slower. Each block below is the brief for one pass. "Save to" means: in Claude Code, write the notes to that path under `work/reports/`; in Claude.ai, keep them as working notes in the conversation. Raw notes feed synthesis — they are never shown as deliverables.

This wave captures the live channel surface: Meta Ads Library, LinkedIn Ads Library, Google Ads Transparency, and content/SEO.

Save raw outputs to:

- `{project-name}/raw/ad-library-intelligence-raw.md`
- `{project-name}/raw/seo-content-raw.md`

## Evidence Log

Ad-library findings must be reproducible. Maintain an evidence log inside `ad-library-intelligence-raw.md`: for every capture, record the library URL/search query and capture date, and reference the evidence next to the finding — a screenshot the user uploaded, a screenshot taken with Claude in Chrome (only if the user approved it in the permission step; in Claude Code save it to `{project-name}/raw/evidence/{competitor}-{platform}-{date}.png`), or enough verbatim ad text from a web fetch that another person could re-find and verify the ad. A finding without an evidence trail drops to Low confidence.

For deeper per-platform analysis (copy/creative/messaging-theme frameworks, TikTok/Microsoft/Apple coverage, spend estimation rules), read `ads-deep-dive.md` — mandatory when the run scope is `ads`.

## Universal Ad Library Fields

For every competitor and platform, capture:

- **Checked:** yes/no
- **Source:** Web fetch / User screenshot / Server ({name}, approved)
- **Captured:** YYYY-MM-DD
- **Country/market:** {market}
- **Search method:** advertiser name / payer name / keyword / page / domain / advertiser ID
- **Active ads found:** exact number if visible, estimate/range if manually counted, or `Unknown`
- **Formats:** static / video / carousel / text / search / display / YouTube / other
- **Dominant angle:** the repeated strategic message
- **Primary hooks:** 3-5 repeated hooks or headlines, verbatim where possible
- **CTA pattern:** demo / free trial / contact sales / download / learn more / buy now / other
- **Landing pages:** destination URLs or page types
- **Repeated claims:** proof, outcomes, category claims, urgency, offers
- **Limitations:** what the platform did not show
- **Confidence:** High / Medium / Low

If no ads are found, distinguish:

- `No ads found in checked source`
- `Could not access source`
- `Advertiser identity unclear`
- `Blocked / rate-limited`
- `Manual search inconclusive`

## Research pass D1: Meta + LinkedIn Ads Library

```
Research task: Capture social ad-library intelligence for competitors in {product category}
Context: {product summary from intake}
Competitors: {list from Wave A}
Market: {country/language}

ROUTE:
- Meta Ad Library: web fetch of the public library URL (see source-router.md);
  if it does not render, ask the user for screenshots or pasted ad text.
- LinkedIn Ad Library: same — web fetch first, then user screenshots.
- Claude in Chrome or Apify only if the user approved that server in the
  permission step (recorded in the source plan).

For EACH competitor:

## {Competitor Name} — Meta Ads Library
- **Checked:** yes/no
- **Source:** Web fetch / User screenshot / Server ({name}, approved)
- **Captured:** {date}
- **Search query/page:** {query, page name, or URL}
- **Market filter:** {country}
- **Active ads found:** {number/range/unknown}
- **Dominant creative formats:** {static/video/carousel/etc.}
- **Dominant angle:** {one sentence}
- **Primary hooks/headlines:**
  - "{verbatim hook}" — {ad/date if visible}
  - "{verbatim hook}"
  - "{verbatim hook}"
- **CTA pattern:** {pattern}
- **Landing page pattern:** {URLs or page types}
- **Repeated claims/offers:** {claims}
- **Notable absence:** {what they are not saying}
- **Limitations:** {no spend/no full targeting/sample only/etc.}
- **Confidence:** High / Medium / Low

## {Competitor Name} — LinkedIn Ads Library
- **Checked:** yes/no
- **Source:** Web fetch / User screenshot / Server ({name}, approved)
- **Captured:** {date}
- **Search query/advertiser:** {query}
- **Country/date filters:** {filters}
- **Ads found:** {number/range/unknown}
- **Advertiser/payer names:** {names if visible}
- **Dominant formats:** {single image/video/document/etc.}
- **B2B message angle:** {one sentence}
- **Primary hooks/headlines:**
  - "{verbatim hook}"
  - "{verbatim hook}"
  - "{verbatim hook}"
- **CTA pattern:** {demo/webinar/report/contact/etc.}
- **Landing page pattern:** {URLs or page types}
- **EU targeting/impression fields:** {visible fields or Not visible}
- **Restricted ads:** {yes/no/unknown}
- **Notable absence:** {what they are not saying}
- **Limitations:** {history limited/fields absent/blocked/etc.}
- **Confidence:** High / Medium / Low

After all competitors:

## Social Ad Angle Matrix
| Competitor | Meta Angle | LinkedIn Angle | CTA | Format Bias | Notable Absence | Confidence |
|---|---|---|---|---|---|---|
| {name} | | | | | | |

## Cross-Competitor Social Ad Gaps
- {gap} — evidence from {competitors/sources}
- {gap}

## Data Gaps
- {platform/competitor} — {reason} — {how to fill}
```

## Research pass D2: Google Ads Transparency + SEO/Content

```
Research task: Capture Google ad transparency, search visibility, and content landscape for competitors in {product category}
Context: {product summary from intake}
Competitors: {list from Wave A}
Market: {country/language}

ROUTE:
- Google Ads Transparency: web fetch of the Transparency Center page, or user
  screenshots. DataForSEO or Claude in Chrome only if approved in the
  permission step.
- SEO/content: manual SERP sampling with web search + web fetch of top pages,
  comparison pages and blog index; a user-uploaded SEO-tool export if given;
  DataForSEO (ranked keywords, volumes, backlinks) only if approved.
  Volume, difficulty and backlink fields without one of those = "not measured".

For EACH competitor:

## {Competitor Name} — Google Ads Transparency
- **Checked:** yes/no
- **Source:** Web fetch / User screenshot / Server ({name}, approved)
- **Captured:** {date}
- **Advertiser lookup:** {advertiser/domain/query}
- **Advertiser identity:** {name/ID if visible}
- **Ads found:** {number/range/unknown}
- **Platform mix:** Search / YouTube / Display / Shopping / Maps / Unknown
- **Ad formats:** {formats}
- **Copy themes:** {themes}
- **Primary hooks:**
  - "{verbatim copy or close paraphrase}"
  - "{verbatim copy or close paraphrase}"
- **Destination URLs:** {URLs or page types}
- **Offer/CTA pattern:** {pattern}
- **Limitations:** {no exact spend/no keyword mapping/verified advertisers only/etc.}
- **Confidence:** High / Medium / Low

## {Competitor Name} — Content & SEO
- **Source:** SERP sampling / Web fetch / User export / Server ({name}, approved)
- **Captured:** {date}
- **Top ranked keywords:** {top 5-10; volume only from an export or approved server, else "not measured"}
- **Top ranking pages:** {URLs and themes}
- **Comparison pages:** {vs/best/alternatives pages owned}
- **Pillar pages:** {category/solution pages}
- **Blog/resource cadence:** {posts/month or estimate}
- **Backlink/domain signals:** {from an export or approved server, else "not measured"}
- **Content pillars:** {themes they own}
- **Content gaps:** {themes absent or weak}
- **Limitations:** {data unavailable/low confidence}
- **Confidence:** High / Medium / Low

After all competitors:

## Paid Search + SEO Matrix
| Competitor | Google Ads Themes | Top SEO Keywords | Content Pillars | Comparison Content | SEO Gap |
|---|---|---|---|---|---|
| {name} | | | | | |

## Channel Opportunity Map
| Channel | Competitor Saturation | Opportunity Level | Evidence | Confidence |
|---|---|---|---|---|
| Meta ads | High/Medium/Low | High/Medium/Low | | |
| LinkedIn ads | High/Medium/Low | High/Medium/Low | | |
| Google ads | High/Medium/Low | High/Medium/Low | | |
| SEO/content | High/Medium/Low | High/Medium/Low | | |

## Data Gaps
- {source/competitor} — {reason} — {how to fill}
```

## Quality Bar

- Capture concrete hooks, not just "they focus on efficiency."
- Separate ad angles by platform; LinkedIn and Meta often carry different buyer intent.
- Do not infer spend, targeting, or performance unless visible.
- Do not treat ad count as budget. Use it only as activity signal.
- If using web fetch or user screenshots, include enough verbatim text for another person to verify the interpretation.
