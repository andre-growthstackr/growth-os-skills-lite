# Dependency map — from the full pack to standalone Lite skills

How each Lite skill depended on the rest of the Growth OS Skills Pack (v3.4.0), and what was done
so the skill runs on its own (one folder, no `_shared/`, no `skills/.core/`, no other skills).

Legend for the "Lite resolution" column: **inlined** = copied into the skill's own
`references/` or `assets/`; **removed** = the step was dropped; **fallback** = replaced by a short
built-in step; **upsell** = one line pointing to the full version; **permission** = optional MCP
server behind the ask-first step in `references/mcp-permission.md`.

All skills that load context now carry `references/context-loading.md` (Lite rules: Claude
project / chat → working folder → ask 3–5 questions). It replaces `_shared/references/context-loading.md`
and the `_shared/context/` lookup.

## Source dependencies (four columns) and Lite resolution

| Skill | `_shared/` files | `skills/.core/` files | Other skills referenced | External tools | Lite resolution |
|---|---|---|---|---|---|
| `growth-os-lite-start` | — (new skill; based on `growth-os-setup` and `growth-os-help`) | — | all 19 Lite skills | — | New. Ships the four templates in `assets/` and a routing index. |
| `business-audit` | references/context-loading, references/cockpit-publish, templates/business-profile-template | — | `/icp-builder`, `/brand-guidelines` | Firecrawl (map, scrape) | Template inlined to `assets/`; cockpit publish removed; Firecrawl → permission, built-in web fetch; `/brand-guidelines` → upsell. |
| `icp-builder` | references/context-loading, references/context-routing, references/cockpit-publish, templates/icp-template | — | — | CRM data (HubSpot, GoHighLevel) | Template + context-routing inlined; cockpit removed; CRM → uploaded export by default, optional CRM server behind permission. |
| `brand-voc` | references/context-loading, references/context-routing, references/cockpit-publish, templates/voice-of-customer-template | — | `/icp-builder` | Firecrawl, Apify, DataForSEO | Template + context-routing inlined; cockpit removed; all three → permission, built-in web search/fetch + uploaded reviews/transcripts. |
| `brand-positioning` | references/context-loading, references/context-routing, references/cockpit-publish | — | `/brand-audit`, `/brand-discovery`, `/competitor-research`, `/icp-builder` | web research (built-in) | Cockpit removed; research "agents" run as sequential passes; `/brand-audit` → inline critique + upsell; `/brand-discovery` removed. |
| `brand-offer` | references/context-loading, references/context-routing, references/guarantee-check, references/cockpit-publish, templates/offer-template | — | `/icp-builder`, `/brand-voc` | — | guarantee-check, context-routing and template inlined; cockpit removed; landing-page/ads-create hand-offs → upsell. |
| `competitor-research` | references/context-loading | — | — | Firecrawl, DataForSEO, Apify, Claude in Chrome, headless browser automation, paid SERP APIs | All MCP → permission with built-in paths (web search/fetch, public ad libraries, screenshots); browser automation and paid API keys removed; recurring monitoring → one-off snapshot compare. |
| `copywriting` | references/context-loading, templates/voice-of-customer-template | — | `/brand-guidelines`, `/brand-voc`, `/humanizer` | — | VoC section map inlined into `references/formats.md`; brand-guidelines optional. |
| `humanizer` | templates/brand-guidelines-template, templates/voice-of-customer-template | — | — | — | Template paths removed; brand-guidelines optional; upstream MIT LICENSE kept. |
| `website-audit` | context lookup only | — | URL path `/offer` (not a skill) | Firecrawl, DataForSEO, PageSpeed Insights, Claude in Chrome | All MCP → permission; PageSpeed via keyless public fetch or pasted result; Apache NOTICE for the impeccable-derived part. |
| `seo-audit` | context lookup only | — | 15 specialist sub-audits (full-pack `seo-*` skills, via subagents) | Google Search Console, GA4, PageSpeed/CrUX, DataForSEO, browser rendering; Python scripts with auth/network | Scripts removed (see below); specialists run as sequential passes with inlined checklists; GSC/GA4/DataForSEO → permission or uploaded export. |
| `seo-geo` | context lookup only | — | — | DataForSEO (LLM mentions, AI search volume) | DataForSEO → permission; built-in web fetch of robots.txt / llms.txt / pages + manual AI-answer probes. |
| `leadmagnet-ideate` | context lookup only | — | `/leadmagnet-tool`, `/landingpage-build`, `/brand-guidelines` | DataForSEO, Firecrawl, CRM mention | Both MCP → permission; unsourced benchmark numbers removed; non-Lite skills → upsell or removed. |
| `leadmagnet-create` | context lookup only | — | `/leadmagnet-tool`, `/landingpage-build`, `/crm-nurture`, `/crm-automation`, `/design-craft`, `/factcheck`, `/brand-guidelines` | CRM wiring (webhooks, GoHighLevel) | CRM wiring removed; landing page + delivery emails as inline outlines; fact-check inline; one upsell line. |
| `cro-audit` | context lookup only | — | — | Claude in Chrome, Firecrawl, PageSpeed | MCP → permission; runs on URL (web fetch) or screenshots; `scripts/score.py` kept as an offline calculator with a manual fallback. |
| `blog-write` | references/style-memory, foundation/style/blog-style, context/style/blog-style, the Content OS sync reference | — | `/blog-brief`, `/blog-outline`, `/blog-factcheck`, `/blog-images`, `/blog-schema`, `/blog-seo`, `/blog-repurpose`, `/seo-keyword`, `/seo-content-brief`, `/content-init`, `/brand-guidelines` | Firecrawl; external content database sync | Content database sync removed entirely; style exemplar inlined; brief/outline/fact-check as inline steps; images/schema/SEO → one upsell; `/blog-repurpose` → `/content-repurpose`. |
| `socialpost-writer` | references/context-loading, references/style-memory, foundation/style/socialpost-style, context/style/socialpost-style, the Content OS sync reference | — | `/content-brand`, `/content-research`, `/socialpost-image`, `/content-init`, `/brand-guidelines` | external content database sync | Sync removed; style exemplar inlined; non-Lite skills → one upsell. |
| `content-repurpose` | references/context-loading, references/content-os-flow, the Content OS sync reference, templates/ | — | `/carousel-build`, `/newsletter-writer`, `/shortform-script`, `/shortform-video`, `/youtube-script`, `/content-calendar`, `/factcheck`, `/content-init`, `/brand-guidelines` | external content database sync | Sync and Content OS flow removed; the skill writes all text formats itself (`references/format-specs.md`); production skills → one upsell. |
| `thought-leadership` | references/context-loading | — | `/brand-guidelines` | — | brand-guidelines optional (was required); one upsell line. |
| `ads-audit` | context lookup only | contract.md, PLATFORMS.md, references/thinking-framework, references/scoring-system, references/benchmarks, references/conversion-tracking, references/compliance, references/budget-allocation, references/*-audit (per platform), agents/audit-* (parallel workers) | `ads-validate/scripts/admath.py` (shared calculator) | ads-platform APIs/MCP (read) | Inlined: 7 primary platform audits, benchmarks, conversion-tracking, compliance, budget-allocation; contract, thinking framework and scoring rewritten for Lite; workers → sequential passes; `admath.py` copied; new `scripts/score.py`; Amazon/Reddit/Pinterest/Snapchat/X → upsell. |

## Removed scripts

| Skill | Script | Why |
|---|---|---|
| `seo-audit` | `scripts/google_auth.py`, `scripts/google_report.py` | Google OAuth + network; replaced by Search Console/GA4 via MCP with permission, or an uploaded export |
| `seo-audit` | `scripts/backlinks_auth.py` | Paid backlink API keys + network; backlinks only via DataForSEO with permission |
| `seo-audit` | `scripts/drift_baseline.py`, `scripts/drift_history.py` | Persistent local state + network fetches; replaced by a re-audit comparison in chat |
| `seo-audit` | `scripts/fetch_page.py` | Network fetcher with third-party packages; replaced by Claude's built-in web fetch |

Kept offline calculators (stdlib only, each with a manual fallback): `cro-audit/scripts/score.py`,
`ads-audit/scripts/score.py`, `ads-audit/scripts/admath.py`.

## Not shipped in Lite

`agents/`, all workflows, `hooks/`, `_shared/` and `skills/.core/` as folders,
`_shared/carousel-core/`, `_workspace-starter/`, all `design-*` skills, the Outbound OS skills,
style memory, and the Content OS references (content database sync, Content OS flow, cockpit
publish, outbound flow).
