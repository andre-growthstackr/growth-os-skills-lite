# Growth OS Lite — skill index (20 skills)

"Reads" lists the context files a skill inherits (★ = most important). Every skill runs without
them too: it then asks 3–5 quick questions.

## Start

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `growth-os-lite-start` | Setup, the four empty context files, routing | — | "Kom igång med Growth OS" / "Where do I start?" |

## Brand OS — the foundation (run these first, in this order)

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `business-audit` | `business-profile.md` from website research + interview | — | "Gör en business audit av acme.se" / "Map my business" |
| `icp-builder` | `icp.md`: tiers, firmographics, triggers, TAM/SAM | business-profile | "Bygg min ICP" / "Build my ideal customer profile" |
| `brand-voc` | `voice-of-customer.md`: verbatim pains, objections, triggers | ★icp | "Ta fram Voice of Customer" / "Mine our customer language" |
| `brand-offer` | `offer.md`: value stack, pricing logic, guarantees, naming | ★icp, ★voc | "Designa vårt erbjudande" / "Design our offer" |
| `brand-positioning` | Positioning statement, category, differentiation, messaging hierarchy | ★icp, voc, offer | "Positionera oss" / "Sharpen our positioning" |
| `competitor-research` | Competitor profiles, pricing, sentiment, messaging gaps | business-profile, icp | "Analysera våra konkurrenter" / "Research our competitors" |

## Design OS — copy

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `copywriting` | Conversion copy for pages, ads, emails, CTAs | ★voc, icp, offer | "Skriv om vår startsida" / "Write landing page copy" |
| `humanizer` | Rewrites text so it stops sounding AI-written | voc (optional) | "Det här låter AI, fixa det" / "Humanize this text" |

## Web OS

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `website-audit` | Website audit: SEO, technical, design/UX, conversion, prioritized fixes | business-profile, icp, offer | "Granska vår hemsida" / "Audit our website" |
| `seo-audit` | SEO Health Score (0–100) and a prioritized SEO action plan | business-profile | "Gör en SEO-audit" / "Full SEO audit of acme.com" |
| `seo-geo` | Optimization for AI search (ChatGPT, Perplexity, AI Overviews) | business-profile | "Optimera för AI-sök" / "Optimize for AI search" |

## Leads OS

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `leadmagnet-ideate` | Ranked lead-magnet ideas matched to ICP and offer | ★icp, voc, offer | "Ge mig idéer på leadmagneter" / "Lead magnet ideas" |
| `leadmagnet-create` | The finished lead magnet (guide, checklist, template, scorecard…) | ★icp, voc, offer | "Skapa leadmagneten" / "Build the lead magnet" |

## Conversion OS

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `cro-audit` | Conversion audit of a page or funnel (URL or screenshots), scored, with fixes | icp, voc, offer | "Varför konverterar inte sidan?" / "CRO audit of this page" |

## Content OS

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `blog-write` | A researched, SEO- and AI-search-ready blog post | icp, voc, business-profile | "Skriv ett blogginlägg om X" / "Write a blog post about X" |
| `socialpost-writer` | LinkedIn (and other social) posts | ★voc, icp | "Skriv ett LinkedIn-inlägg om X" / "Write a LinkedIn post" |
| `content-repurpose` | One piece of content turned into many formats | voc, icp | "Gör om inlägget till flera format" / "Repurpose this post" |
| `thought-leadership` | Founder-led authority posts and a point-of-view series | icp, voc | "Hjälp mig bygga thought leadership" / "Founder-led LinkedIn content" |

## Ads OS

| Skill | Delivers | Reads | Example prompt (sv / en) |
|---|---|---|---|
| `ads-audit` | Read-only ad-account audit from exports/screenshots, scored, with an action plan | business-profile, offer | "Granska våra annonser" / "Audit my Meta and Google ads" |

## Not in Lite (answer honestly, then offer the closest Lite skill)

| Goal | Full version has | Closest Lite skill |
|---|---|---|
| Cold email, LinkedIn outreach sequences, lead lists, buying signals | Outbound OS | `copywriting` (one email), `icp-builder` (who to target) |
| Landing page build, funnels, CRM nurture | Leads OS build skills | `copywriting` + `cro-audit` |
| Carousels, newsletters, YouTube, short video | Content OS format skills | `content-repurpose` (text versions) |
| Brand guidelines, brand book, visual design | Brand OS + Design OS | `brand-positioning` |
| Launching or optimizing ad campaigns | Ads OS (plan, create, launch, optimize) | `ads-audit` |
| Analytics dashboards, attribution, A/B test statistics | Conversion OS | `cro-audit` |
| Style memory that learns your format per content type | Style memory | Paste 1–2 examples into the chat each time |
| Multi-agent campaigns with approval gates | 10 agents + 5 workflows | Run the Lite skills in sequence |

> All of the above are in the Growth OS Skills Pack (246 skills). See https://github.com/andre-growthstackr/growth-os-skills-lite#lite-vs-full
