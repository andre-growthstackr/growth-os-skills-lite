---
name: competitor-research
description: "Competitor profiles, pricing, review sentiment, messaging and ad gaps. Use for: analysera våra konkurrenter, konkurrentanalys, competitor research, analyze our competitors."
metadata:
  author: GrowthStackr
  version: 1.0.0
  pack: growth-os-lite
  module: brand-os
---

# Competitor Research

Competitive intelligence that produces a living matrix, not a static PDF. Focus on **what nobody does** (the gap) — never on imitating. Identify what competitors do, what they claim, what customers actually experience, and what they leave open.

Respond and produce deliverables in the user's language. Instructions here are English; if the user works in Swedish, deliverables use Swedish titles and labels (e.g. `konkurrent-matris.md`, `Lucka — tre öppningar ingen adresserar`).

## Context loading (always first)

Follow `references/context-loading.md`: look in the Claude project / this chat first, then the
working folder (Claude Code), then ask.

- `icp.md` — Ideal Customer Profile: tiers, firmographics, pains (OPTIONAL — used to choose competitors that share the same buyer and pain, not generic top-of-mind category names)
- `voice-of-customer.md` — verbatim customer language, objections, triggers (OPTIONAL — used to cross-check ad-angle saturation: messages customers use that no competitor advertises are the strongest gap candidates)
- `offer.md` — offer, pricing, guarantees, proof (OPTIONAL — used to benchmark competitor pricing against the user's own offer in the pricing landscape)
- `business-profile.md` — company, services, goals, market (OPTIONAL — answers product/category and geography)
- `brand-guidelines.md` — tone, negative rules (OPTIONAL — use if present; Lite continues without it)
- An earlier `competitor-matrix.md` or `competitor-snapshot-*.json` from a previous run (OPTIONAL — switches the default to compare mode)

**Minimum context if files are missing** — ask these and continue:
1. What do you sell, in one sentence, and to whom (buyer role / company type)?
2. Which market — country and language?
3. Which competitors do you already know of (names or URLs)? "Not sure" is fine — research will find them.
4. Full baseline, or one dimension only (`ads`, `seo`, `content`, `pricing`, or one competitor)?

Never invent brand/customer facts. Afterwards, suggest `/icp-builder` (for `icp.md`) and `/brand-voc` (for `voice-of-customer.md`) so the next run picks competitors and gaps against real buyers and real customer language.

## External tools — ask first

This skill works fully without external servers: web search, web fetch of public pages and ad libraries, screenshots and exports the user uploads, and a short interview cover every step. Follow `references/mcp-permission.md` before the first call to any server below — ask once per server per run, and only for servers that are already connected.

| Server (optional) | Used for | Requires | Built-in path (no MCP) |
|---|---|---|---|
| Firecrawl | Cleaner capture of competitor homepage, pricing, features, changelog and blog index (Wave 1, Wave 4 content) | Firecrawl account and credits, connected in Claude's connector settings | Web fetch of each page; web search with `site:` queries for changelog and blog; user screenshot if a page is gated or does not render |
| DataForSEO | Ranked keywords, search volume, keyword difficulty, CPC, backlinks, traffic estimates, normalized Google Ads Transparency data (Wave 4) | DataForSEO account and paid credits | Manual SERP sampling with web search; Google Ads Transparency Center via web fetch or user screenshots; an export the user uploads from an SEO tool they already use |
| Apify | Bulk capture from the Meta and LinkedIn ad libraries (Wave 4, `ads` scope) | Apify account and paid usage | Meta Ad Library and LinkedIn Ad Library viewed via web fetch; if they do not render, user screenshots or pasted ad text |
| Claude in Chrome | Browsing the script-heavy ad-library and Transparency Center pages and taking evidence screenshots (Wave 4) | The Claude in Chrome extension installed and connected | Web fetch of the public library URLs (listed in `references/source-router.md`); user screenshots with filters visible |

**Only measured with a server or a user export:** search volume, keyword difficulty, CPC, backlink / referring-domain counts, domain authority, organic traffic estimates, and full ranked-keyword lists. When the user declines and has no export, these are reported as **"not measured"** — never estimated. Everything else in this skill (matrix, ad angles and hooks, pricing, sentiment, GTM, the three gaps) is fully available on the built-in path.

## Operating Modes

- **baseline** (default): build the first snapshot of the competitive landscape → `competitor-matrix.md` plus deep-dive deliverables, and a snapshot file the user keeps.
- **compare**: the user brings back an earlier snapshot (or matrix); rerun the same source set once and report what changed in pricing, features, changelog, ad angles, active ad counts, SEO/content, and positioning.

Default to **baseline** unless the user asks to update, compare against last run, or see what changed. Lite never schedules, automates or monitors in the background: each run is a one-off snapshot the user can rerun whenever they want (see `references/snapshot-compare.md`).

```
BASELINE: INTAKE -> PERMISSION + SOURCE PLAN -> RESEARCH WAVES (in sequence) -> CHECKPOINT -> SYNTHESIS -> VERIFICATION -> SNAPSHOT FILE
COMPARE:  LOAD EARLIER SNAPSHOT -> RERUN SOURCE SET -> NEW SNAPSHOT -> COMPARE -> competitor-diff.md -> FLAGS
```

## Scope as Argument

`/competitor-research` accepts an optional argument that narrows the run:

| Argument | Run | References to read |
|---|---|---|
| *(none)* | Full baseline: all four waves, all deliverables | Full table below |
| `{company name or URL}` | Single-competitor deep dive: all waves scoped to that competitor, ends in one battle card + matrix column | Full table, scoped |
| `ads` | Ad-library dimension only: Meta + LinkedIn + Google (+ TikTok/Microsoft/Apple where relevant) with evidence log, messaging themes, gaps | `source-router.md`, `research-wave-4-channel-intelligence.md`, `ads-deep-dive.md`, `output-schemas.md` |
| `seo` | SEO/content dimension only: ranking presence, top pages, comparison content, content pillars, whitespace | `source-router.md`, `research-wave-4-channel-intelligence.md` (pass D2), `output-schemas.md` |
| `content` | Content and owned-audience dimension: blog cadence, content pillars, resources/webinars, social/community, content gaps | `research-wave-3-gtm-signals.md`, `research-wave-4-channel-intelligence.md` (D2 content), `output-schemas.md` |
| `pricing` | Pricing dimension only: tiers, value metrics, pricing psychology, switching costs, whitespace | `research-wave-1-profiles-pricing.md` (pass A2), `research-synthesis.md` (pricing-landscape schema) |

Arguments combine: `/competitor-research ads pricing` runs both dimensions. A scoped run still requires the honesty protocol, source labels, and the standard deliverable footer. Read only the references the scope requires (progressive disclosure).

## Reference Map

Read only what the current phase needs:

| File | When to read | Purpose |
|------|-------------|---------|
| `references/context-loading.md` | Start of session | Where to find context files; what to do when they are missing |
| `references/honesty-protocol.md` | Start of session | Claim labels, anti-fabrication, confidence discipline |
| `references/mcp-permission.md` | Before the first call to any external server | The permission step and its rules |
| `references/source-router.md` | Before source collection | Built-in and optional routes per signal, public ad-library URLs, source labels |
| `references/research-principles.md` | Before research | Source quality tiers, cross-referencing, data gaps |
| `references/research-scaling.md` | After intake | Light/Standard/Deep scope selection |
| `references/research-wave-1-profiles-pricing.md` | Wave 1 | Web, pricing, profiles, product surface |
| `references/research-wave-2-sentiment-mining.md` | Wave 2 | Reviews, forums, customer language |
| `references/research-wave-3-gtm-signals.md` | Wave 3 | GTM, sales motion, hiring, funding, partnerships |
| `references/research-wave-4-channel-intelligence.md` | Wave 4 | Meta, LinkedIn, Google Ads Transparency, SEO/content, evidence log |
| `references/ads-deep-dive.md` | Scope `ads`, or deeper Wave 4 | Copy/creative/messaging frameworks, TikTok/Microsoft/Apple, spend estimation rules |
| `references/output-schemas.md` | Synthesis | Exact deliverable shapes |
| `references/research-synthesis.md` | Synthesis | Cross-wave pattern matching, report/battle-card schemas |
| `references/snapshot-compare.md` | End of baseline (snapshot file) and compare mode | Snapshot format and change-report protocol |
| `references/verification-pass.md` | After synthesis | Verification checks |

## Instructions

### 1. Intake

Keep intake short — use inherited context before asking questions. Also look for an earlier `competitor-matrix.md` or `competitor-snapshot-*.json` (uploaded, in the Claude project, or in the working folder) — they switch the default to compare mode.

Ask only for missing essentials (the minimum-context questions above), in one short message. Use the environment's question tool if there is one (AskUserQuestion in Claude Code, option boxes in Claude.ai); otherwise ask numbered questions in chat.

Track the run: project, mode, date, language, research depth, data routes, checklist. In Claude Code, save `work/reports/{project-name}/intake.md` and `PROGRESS.md`; in Claude.ai, keep a short progress note in the conversation.

### 2. Permission + source plan

Read `references/source-router.md`. Check which of the servers in the table above are actually connected. For each connected server the chosen scope would use, run the permission step from `references/mcp-permission.md` **once, before its first call** — one message can cover several servers, each with its use, requirement and built-in alternative. A server that is not connected is never requested mid-run; take the built-in path and mention at the end what it would have added.

Then record the plan (Claude Code: `{project-name}/source-plan.md`; Claude.ai: a short note in chat): which routes are used per signal, which servers were approved/declined/not available, and which metrics are therefore **not measured**.

Ad-library and Transparency Center pages are often rendered by script, so web fetch may return little. Ask the user once, early, whether they can supply screenshots (one per competitor and library, filters visible) or pasted ad text, and continue with the other waves meanwhile.

Every ad-library claim carries: `Source: Web fetch | User screenshot | User export | Server ({name}, approved)`, `Captured: YYYY-MM-DD`, `Confidence: High | Medium | Low`, `Limitations: ...`.

### 3. Research depth

Read `references/research-scaling.md`. Score complexity, recommend Light (2-3 competitors, compact matrix) / Standard (3-5 competitors, all four waves — the default) / Deep (5-8 direct + 2-3 adjacent, all deliverables + battle cards). Show the user the recommendation; manual override always wins.

### 4. Baseline research waves

Read `references/research-principles.md` first. Run the four waves one after another in this conversation (if your environment can run subagents you may parallelize the passes within a wave; otherwise run them in sequence — same depth, just slower). Skip waves outside the requested scope.

1. **Wave 1 — Profiles + web/pricing/product** → `raw/competitor-profiles.md`, `raw/pricing-intelligence.md`, `raw/web-pricing-product-scrape.md`, `raw/feature-changelog-raw.md`. If the user approved Firecrawl, use it for the page captures; otherwise web fetch each page.
2. **Wave 2 — Customer sentiment** → `raw/review-mining.md`, `raw/forum-mining.md` (praise, complaints, feature requests, churn signals, verbatim language). Web search + web fetch.
3. **Wave 3 — GTM and strategic signals** → `raw/gtm-analysis.md`, `raw/strategic-signals.md` (sales motion, hiring, funding, partnerships, product direction). Web search + web fetch.
4. **Wave 4 — Channel and ad-library intelligence** → `raw/ad-library-intelligence-raw.md`, `raw/seo-content-raw.md` + evidence log. Ad libraries: if the user approved Claude in Chrome or Apify, use it; otherwise web fetch the public Meta Ad Library, LinkedIn Ad Library and Google Ads Transparency Center pages, and use the user's screenshots where they do not render. SEO: if the user approved DataForSEO, use it; otherwise manual SERP sampling with web search plus any export the user uploads.

Raw notes are inputs to synthesis, not deliverables: in Claude Code they live under `work/reports/{project-name}/raw/`; in Claude.ai keep them as working notes in the conversation.

If a library cannot be accessed and the user has no screenshots, create an explicit data gap. Never infer active ads from blog posts, social posts, or generic search results.

### 5. Checkpoint (human in the loop)

Before synthesis, show the user: competitors profiled, sources captured, ad libraries checked or blocked, biggest visible changes, major data gaps, and what is "not measured". Ask whether to add/remove a competitor. If the user wants speed, proceed after stating assumptions.

### 6. Synthesis

Read `references/output-schemas.md` and `references/research-synthesis.md`. Produce core outputs first:

- `competitor-matrix.md` — competitors as columns; rows: positioning, target, pricing, features (top 3), feature/changelog signal, ad angle, Meta/LinkedIn/Google Ads library signals, keywords (top 3), content pillars, proof, CTA/sales motion, data gaps
- `ad-library-intelligence.md`, `seo-content-landscape.md`, `feature-changelog-tracker.md`

The matrix ends with **The Gap — three openings nobody addresses**: exactly three concrete, falsifiable opportunities tied to matrix evidence, each confidence-rated. Never generic claims like "more customer-centric".

Then deep-dive outputs (Standard/Deep): `competitors-report.md`, `feature-comparison-matrix.md` (feature ratings vs. your product — distinct from the core `competitor-matrix.md`), `pricing-landscape.md`, `battle-cards/{competitor}.md`. Every deliverable ends with Data Gaps, Red Flags, Yellow Flags, Sources.

### 7. Verification

Read `references/verification-pass.md` and run the checks yourself: claim labels present, no internal contradictions, confidence consistent with evidence, matrix rows complete, exactly three gaps each citing at least two observations (or explicitly Low confidence), every ad-library claim carries Source/Captured/Confidence/Limitations, and no server-only metric appears without its server or an export. Pause and show the user any critical issues before finishing.

### 8. Snapshot file (and compare mode)

Read `references/snapshot-compare.md`. End every baseline by delivering the snapshot file (Claude.ai: downloadable `competitor-snapshot-{YYYY-MM-DD}.json`; Claude Code: `snapshots/{YYYY-MM-DD}/competitor-snapshot.json`) and tell the user: "Keep this file. Rerun `/competitor-research` whenever you want an update and upload it — I'll report what changed."

In compare mode, load the earlier snapshot, rerun the same source set once, write a new snapshot and `competitor-diff.md`. If the user asks for weekly or monthly monitoring, explain that Lite runs on demand only — nothing is scheduled, automated, sent or posted — and suggest a rerun cadence they put in their own calendar.

## Output

Deliver the core matrix and the gap analysis in chat, and every file below as a downloadable `.md` file. In Claude Code, save them under `work/reports/{project-name}/`. Nothing is published, sent or synced.

| File | Content |
|---|---|
| `competitor-matrix.md` | Core matrix + three-gap analysis (sv: `konkurrent-matris.md`) |
| `ad-library-intelligence.md` | Per-platform ad intelligence with evidence log |
| `seo-content-landscape.md` | SEO matrix, keyword opportunities, content whitespace (volumes/backlinks "not measured" unless a server was approved or an export provided) |
| `feature-changelog-tracker.md` | Feature matrix + recent product movement |
| `competitors-report.md` | Full report: players, opportunities, risks, moats |
| `feature-comparison-matrix.md` | Feature ratings vs. your product, gap analysis, differentiation paths |
| `pricing-landscape.md` | Tiers, value metrics, psychology, switching costs, whitespace |
| `battle-cards/{competitor}.md` | One-page sales battle cards (Standard/Deep) |
| `competitor-snapshot-{date}.json` | Comparable signals for the next rerun |
| `competitor-diff.md` | Change report (compare mode only) |

Scoped runs deliver only the files their dimension covers, always including the matrix rows they can fill. Suggest adding `competitor-matrix.md` to the Claude project so `/brand-positioning` can seed its competitive alternatives map from it.

## Quality gates

- **Honesty protocol is non-negotiable** (`references/honesty-protocol.md`): label claims `[Data]` / `[Estimate]` / `[Assumption]` / `[Opinion]`, date every source, declare gaps instead of filling them, acknowledge competitor strengths, rate threats honestly.
- **Statistics require a source + URL.** A number without a source is a hard stop, not a footnote. Never invent keyword volumes, spend figures, review counts, or market shares.
- **Server-only metrics are "not measured" without the server or an export** — never estimated.
- **Ad libraries are partial visibility**, not media-buying dashboards: never infer spend, targeting, or performance unless the platform exposes it; ad count is an activity signal, not a budget signal; every finding needs its evidence-log trail.
- **Find the gap, don't imitate.** Every deliverable must push toward what nobody does; exactly three gaps in the matrix, each evidence-backed.
- **Marketing claims are competitor claims**, not verified facts — label them as such.
- **Read-only and on demand.** No server is used without a yes; nothing is scheduled, posted or sent.
- **Deliverables follow the user's language**; references and instructions stay as written.

## Example

**User:** `/competitor-research ads` — "Vad kör våra konkurrenter för annonser? Vi säljer bokföringssystem till småföretag i Sverige."

**Flow:** Load `icp.md` from the Claude project (SME buyer confirmed; competitors chosen that target the same buyer). Read `source-router.md`, `research-wave-4-channel-intelligence.md`, `ads-deep-dive.md`. No external servers are connected, so no permission question is needed: web fetch the Meta Ad Library, LinkedIn Ad Library and Google Ads Transparency Center pages for 4 competitors; two pages do not render, so ask once for screenshots and the user uploads six. Extract verbatim hooks, CTAs, formats, and landing pages with `Source: Web fetch` or `Source: User screenshot` on each. Build the messaging theme matrix, flag that no competitor advertises the "slipp kvittohögen" pain that dominates `voice-of-customer.md`, and deliver `ad-library-intelligence.md` in Swedish with three evidence-backed gaps, keyword CPC marked "not measured", Data Gaps/Red Flags/Yellow Flags/Sources at the end, and a `competitor-snapshot-{date}.json` to upload on the next rerun.
