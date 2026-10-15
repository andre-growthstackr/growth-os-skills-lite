# Context Routing — multi-offer businesses

Growth OS context files (`business-profile.md`, `icp.md`, `offer.md`,
`voice-of-customer.md`) are inherited by every other Growth OS skill. The default assumption
is **one business → one ICP → one offer**. When a business genuinely has more than one offer
(or more than one entity), use the **router pattern** so other skills can inherit the
*right* variant instead of a single blended file.

## When to use a router

Only when the run genuinely surfaces more than one variant:

- **>1 offer** — a product ladder or several standalone offers.
- **>1 entity / brand** — separate brands under one operator.

A single-offer business keeps **one plain `offer.md` and no router**. Do not create a router
for a business that doesn't need one.

## Router file shape

The canonical file (`offer.md`) becomes a short **index**: a one-line note plus a table, and
nothing else — the substance lives in sub-files. Mark exactly one row as the default with **★**.

```
# Offer — Router (multiple offers)

This business runs multiple offers. Skills that inherit `offer.md` must select the right
one for the campaign (see Selection below).

| Offer | File | Use when |
|-------|------|----------|
| ★ Starter (DFY content) | offer-starter.md | education entity · application funnel |
| Audit                   | offer-audit.md   | consulting entity · BOF booked-meeting |
| Retainer                | offer-retainer.md| consulting · existing clients |
```

Sub-file naming — kebab-case slug of the variant: `offer-<slug>.md` (e.g. `offer-starter.md`).

Each sub-file follows the normal offer template (`assets/offer-template.md`) exactly. The
router file itself holds only the index + the Selection note — no offer content. When
variants map to separate entities, slug by entity and name the entity in the "Use when"
column so other skills can filter by entity.

## Where the files live

The router and every sub-file sit **next to each other** wherever the user keeps context:
added to the Claude project's knowledge (Claude.ai / Claude Desktop), or in the working
folder root (Claude Code). Deliver each one as its own downloadable `.md` file with the exact
file name, and tell the user to add all of them to the Claude project.

## Selection — how other skills pick a variant

A skill that inherits `offer.md` and finds a **router** resolves the variant in this order —
**never silently pick**:

1. **Explicit argument** — e.g. `--offer <slug>` if the user passed one.
2. **Ask** — otherwise ask which offer this run targets, listing the router's rows (use the
   environment's question tool if there is one — AskUserQuestion in Claude Code, option boxes
   in Claude.ai — otherwise numbered options in chat).
3. **★ Default** — only if the user defers ("whichever" / "the main one").

Record the resolved variant in the deliverable so the choice is traceable. A skill that reads
a plain (non-router) file uses it directly.
