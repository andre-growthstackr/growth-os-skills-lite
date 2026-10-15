# Verification Pass Protocol

After synthesis completes, run a **verification pass (V1)** that audits all deliverables for consistency, accuracy, and completeness. This step catches issues that individual research passes and synthesis can miss. Run it yourself in this conversation, with fresh, critical eyes: re-read every deliverable as if someone else wrote it. (If your environment can run subagents you may hand V1 to one; otherwise run it in sequence after synthesis.)

## When to Run

- After synthesis is complete and all deliverable files are written
- Before presenting the final output to the user
- One pass: **V1: Verification**

## Task

V1 reads ALL deliverable files (not raw files) and checks them against the rules below. It produces `verification-report.md` (Claude Code: in the project directory; Claude.ai: shown in chat or as a downloadable file).

## Universal Checks

These apply to every deliverable this skill produces:

### 1. Claims Without Source
Every quantitative claim must have a data label: **[Data]**, **[Estimate]**, **[Assumption]**, or **[Opinion]**. Flag any number, percentage, or factual assertion without a label.

### 2. Internal Contradictions
Cross-check numbers and statements across deliverable files. Flag when:
- The same metric appears with different values in two files
- A claim in one file contradicts a claim in another
- Confidence ratings disagree (e.g., "High confidence" in one file, different data in another suggests Medium)

### 3. Confidence Rating Consistency
Verify that confidence ratings match the evidence:
- A claim with only one Tier 3 source cannot be rated **High**
- A claim with multiple Tier 1 sources should not be rated **Low**
- Every major section must have a confidence rating

### 4. Data Gaps Declared
Every deliverable must have a Data Gaps section. Flag:
- Files missing the Data Gaps section entirely
- Sections where data is clearly thin but no gap is declared
- Gaps mentioned in raw files that didn't make it into the synthesized deliverables

### 5. Flags Present
Every deliverable must end with Red Flags and Yellow Flags sections. Flag:
- Files missing these sections
- Files with "No flags identified" where the content clearly contains risks

### 6. Stale Data
Flag any data point older than 18 months that isn't marked as potentially outdated.

### 7. Duplicate Sources
Flag when the same source is used as "independent corroboration" in multiple places. Two claims both citing the same blog post don't have independent verification.

## Skill-Specific Checks: competitor-research

In addition to the universal checks above, verify:

### Core Matrix Output Checks
- `competitor-matrix.md` exists unless the user explicitly requested deep-dive only.
- Standard mode includes 3-5 primary competitors unless the user selected a different scope.
- `competitor-matrix.md` includes rows for positioning, target, pricing, top features, feature/changelog signal, ad angle, Meta, LinkedIn, Google Ads Transparency, top keywords, content pillars, proof, CTA/sales motion, and data gaps.
- `competitor-matrix.md` has exactly three gap entries ("The Gap" section; "Lucka" in Swedish).
- Each gap is concrete, tied to matrix evidence, and confidence-rated.
- Meta, LinkedIn, and Google ad-library checks exist for every primary competitor, or each missing source is declared as a data gap.
- Every ad-library claim includes Source, Captured date, Confidence, and Limitations.
- No owned-account Google Ads data (e.g. Auction Insights) is treated as public competitor transparency data; it is used only if the user uploaded that export.
- No search volume, keyword difficulty, CPC, backlink or traffic number appears unless it comes from a user export or a server the user approved; otherwise the field reads "not measured".

### Channel Deliverable Checks
- `ad-library-intelligence.md` separates Meta, LinkedIn, and Google findings instead of merging them into a generic paid ads summary.
- `seo-content-landscape.md` distinguishes server or export data from manual SERP sampling and web-fetch observations.
- `feature-changelog-tracker.md` dates recent product movement or marks the date as unavailable.
- `competitor-diff.md`, when present, compares against a named baseline snapshot date and does not report one-off observations or a change of data route as changes.

### Battle Card vs. Report Consistency
- Every competitor in the battle cards must appear in the `competitors-report.md` Key Players table
- Strengths/weaknesses in battle cards must not contradict the competitor profiles in the report
- Threat levels must be consistent between battle cards and the report

### Matrix vs. Profiles Alignment
- Every competitor in `feature-comparison-matrix.md` must have a profile in `competitors-report.md`
- Feature ratings (Strong/Adequate/Weak/Missing) in the matrix must be supported by evidence in the report or battle cards
- Gap analysis items must connect to actual findings, not assumptions

### Pricing Landscape vs. Profiles Consistency
- Pricing data in `pricing-landscape.md` must match pricing mentioned in battle cards
- Value metrics must be consistent across the pricing landscape and competitor profiles
- Switching cost assessments must align between pricing landscape and battle cards

### Cross-Deliverable Coherence
- Strategic opportunities in the report must be supported by evidence from at least two deliverables (e.g., pricing gap + customer complaint)
- Strategic risks must be traceable to specific competitor data
- Moat assessment must reference specific competitors and evidence

## Output: verification-report.md

```markdown
# Verification Report: {project-name}
*Generated: {date}*

## Summary
- **Critical issues:** {count}
- **Warnings:** {count}
- **Info:** {count}

## Critical Issues
Issues that could mislead decision-making. The process pauses here for user review.

### {Issue title}
- **File(s):** {affected files}
- **Section:** {section name}
- **Problem:** {description}
- **Suggested fix:** {how to resolve}

## Warnings
Issues that reduce quality but don't block decisions.

### {Issue title}
- **File(s):** {affected files}
- **Problem:** {description}
- **Suggested fix:** {how to resolve}

## Info
Minor improvements and observations.

- {observation}
- {observation}

## Verification Checklist
- [ ] All quantitative claims labeled
- [ ] No internal contradictions found
- [ ] Confidence ratings consistent with evidence
- [ ] Data gaps declared in all deliverables
- [ ] Red/Yellow flags present in all deliverables
- [ ] No stale data unmarked
- [ ] No duplicate-source false corroboration
- [ ] Battle cards consistent with report (skill-specific)
- [ ] Matrix aligned with profiles (skill-specific)
- [ ] Pricing landscape consistent with profiles (skill-specific)
- [ ] Opportunities backed by multi-source evidence (skill-specific)
- [ ] Competitor matrix exists with exactly three concrete gaps
- [ ] Ad-library findings have Source/Captured/Confidence/Limitations
- [ ] SEO/content and feature/changelog deliverables are present or explicitly scoped out
```

## Flow Control

- **If Critical issues > 0:** Pause. Show the user: "Verification found {N} critical issues that could affect decision-making." List them. Ask: "Should I fix these before continuing, or proceed as-is?"
- **If only Warnings/Info:** Show a one-line summary: "Verification complete: {N} warnings, {N} info items. See `verification-report.md` for details." Continue.
