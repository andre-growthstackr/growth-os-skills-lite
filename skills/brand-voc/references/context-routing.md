# Context Routing — multi-ICP / multi-offer / multi-entity businesses

Growth OS context files (`business-profile.md`, `icp.md`, `offer.md`,
`voice-of-customer.md`) are inherited by every other Growth OS skill. The default assumption
is **one business → one ICP → one offer**. When a business genuinely has more than one ICP,
offer, or entity (e.g. a dual-entity company running consulting + education), use the
**router pattern** so other skills can inherit the *right* variant instead of a single
blended file.

## When to use a router

Only when a foundation skill genuinely surfaces more than one variant:

- **>1 ICP** — distinct firmographics or go-to-market motion (e.g. account-based consulting
  vs demand-gen course buyers).
- **>1 offer** — a product ladder or several standalone offers.
- **>1 entity / brand** — separate brands under one operator.
- **>1 audience** for VoC — when offers/ICPs address different customer bases.

A single-variant business keeps **one file and no router**. Do not create a router for a
business that doesn't need one.

## Router file shape

The canonical file (`icp.md` / `offer.md` / `voice-of-customer.md`) becomes a short **index**:
a one-line note plus a table, and nothing else — the substance lives in sub-files. Mark
exactly one row as the default with **★**.

```
# Offer — Router (multiple offers)

This business runs multiple offers. Skills that inherit `offer.md` must select the right
one for the campaign (see Selection below).

| Offer | File | Use when |
|-------|------|----------|
| ★ Starter (DFY content) | offer-starter.md | education entity · application funnel |
| Audit                   | offer-audit.md   | consulting entity · booked-meeting funnel |
| Retainer                | offer-retainer.md| consulting · existing clients |
```

Sub-file naming — kebab-case slug of the variant:

- ICPs → `icp-<slug>.md` (e.g. `icp-education.md`, `icp-consulting.md`)
- Offers → `offer-<slug>.md` (e.g. `offer-starter.md`)
- VoC → `voice-of-customer-<audience>.md` (e.g. `voice-of-customer-agencies.md`)

Each sub-file follows the **normal template** for that artifact exactly. The router file
itself holds only the index + the Selection note — no profile content. When variants map to
separate entities, slug by entity (`icp-consulting.md`) and name the entity in the "Use when"
column so other skills can filter by entity.

## Where the files live

The router and every sub-file sit **next to each other**: deliver each as its own
downloadable `.md` file and add all of them to the same Claude project (Claude.ai / Claude
Desktop). In Claude Code, save them side by side in the working-folder root. No subfolders.

## Selection — how other skills pick a variant

A skill that inherits `icp.md` / `offer.md` / `voice-of-customer.md` and finds a **router**
must resolve the variant in this order — **never silently pick**:

1. **Explicit argument** — `--icp <slug>` / `--offer <slug>` if the user passed one.
2. **Ask** — otherwise ask which entity / offer / ICP this run targets, listing the router's
   rows (use the environment's question tool if there is one — AskUserQuestion in Claude Code,
   option boxes in Claude.ai; otherwise numbered questions in chat).
3. **★ Default** — only if the user defers ("whichever" / "the main one").

Record the resolved variant in the deliverable so the choice is traceable. A skill that reads
a plain (non-router) file uses it directly.

## Foundation skills that WRITE routers

- `icp-builder` — writes an `icp.md` router + `icp-<slug>.md` per ICP when the interview
  surfaces more than one distinct ICP or a dual-entity business.
- `brand-offer` — writes an `offer.md` router + `offer-<slug>.md` per rung for a laddered or
  multi-offer business.
- `brand-voc` — writes a `voice-of-customer.md` router + `voice-of-customer-<audience>.md`
  per audience when mining more than one customer base.

Always set a sensible ★ default. It is used only when the user defers ("the main one"), never as a silent pick.
