# SEO Health Score (0–100) — scoring table

The score is arithmetic on observed findings, not a feeling. Every deduction cites the check, the
evidence (tag, header, value, URL) and how many sampled pages it affects. Do the math by hand in
the report (or with code execution if available); the formula below is all there is.

## 1. Category weights

| Category | Weight | Checklist |
|---|---|---|
| Technical SEO | 22% | `references/technical.md` sections 1–6 |
| Content Quality | 23% | `references/content-onpage.md` part B |
| On-Page SEO | 20% | `references/content-onpage.md` part A |
| Schema / Structured Data | 10% | `references/schema.md` |
| Performance (Core Web Vitals) | 10% | `references/technical.md` section 7 |
| AI Search Readiness | 10% | `references/ai-search.md` |
| Images | 5% | `references/content-onpage.md` part C |

Backlinks, rankings and traffic are **not** part of the score: they depend on paid or account data
the audit may not have. When measured, they are reported in their own section.

## 2. Category score (all categories except Performance)

Each category starts at **100**. For every failed check, deduct once (per check, not per page):

| Severity | Deduction | Meaning |
|---|---|---|
| Critical | −30 | Blocks indexing, causes a penalty risk, or breaks the site for search engines |
| High | −15 | Significantly limits rankings or visibility for important pages |
| Medium | −7 | Clear optimization gap |
| Low | −3 | Nice to have |
| Info | 0 | Noted, not scored |

- Floor at 0.
- **Site-wide escalation:** if a High or Medium issue affects ≥50% of the sampled pages of a key
  template (homepage, service/product, category, article, location), raise it one severity level.
  Never escalate beyond Critical.
- **Not checked ≠ passed.** A check you could not run (for example image file sizes when web fetch
  does not return them) gets no deduction, is listed under Limitations, and counts toward the
  confidence label below.

Severity per check is given in each checklist file (`[C]`, `[H]`, `[M]`, `[L]`, `[I]`).

## 3. Performance score (metric-based)

Use field data (CrUX, 75th percentile) when available, otherwise lab data. Say which.

| Metric | Good → 100 | Needs improvement → 60 | Poor → 20 |
|---|---|---|---|
| LCP | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| INP (field) | ≤ 200 ms | 200–500 ms | > 500 ms |
| TBT (lab stand-in for INP) | ≤ 200 ms | 200–600 ms | > 600 ms |
| CLS | ≤ 0.1 | 0.1–0.25 | > 0.25 |

Performance score = average of the three metric points (LCP, INP or TBT, CLS), using the mobile
result. If only some metrics were measured, average those. If **no** metric was measured, the
category is "not measured": it is excluded and the weights are renormalized (below). FID is retired;
never report it.

## 4. Overall score

```
SEO Health Score = Σ (category score × weight) ÷ Σ (weights of scored categories)
```

Example with Performance not measured: weights in play = 90%. A site scoring Technical 70,
Content 62, On-Page 78, Schema 40, AI 55, Images 85 gives
(70×22 + 62×23 + 78×20 + 40×10 + 55×10 + 85×5) ÷ 90 = 5 901 ÷ 90 = **65.6 → 66**.
Show this line in the report so the reader can check it.

## 5. Bands

| Score | Band | Read |
|---|---|---|
| 90–100 | Excellent | Maintain and test |
| 75–89 | Good | A handful of clear lifts |
| 60–74 | Needs improvement | Several fixable gaps |
| 40–59 | Poor | Structural work needed |
| 0–39 | Critical | Fundamentals broken (indexing, HTTPS, content) |

## 6. Confidence label (always printed next to the score)

| Label | When |
|---|---|
| High | Crawl export or ≥ 25 URLs fetched, performance measured, ≥ 80% of checks run |
| Medium | 10–24 URLs fetched, or performance not measured, or 60–79% of checks run |
| Low | < 10 URLs fetched, or < 60% of checks run, or JS-rendered site read only from raw HTML |

## 7. Priority of actions

| Priority | Definition | Fix within |
|---|---|---|
| Critical | Blocks indexing or causes penalties | Immediately |
| High | Significantly impacts rankings | 1 week |
| Medium | Optimization opportunity | 1 month |
| Low | Nice to have | Backlog |

Quick wins = High or Medium findings that are a template, tag or copy change (no rebuild).
