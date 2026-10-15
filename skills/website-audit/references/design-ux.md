# Design/UX Dimension — Checks & Scoring

A 5-dimension diagnostic scan of the live site. Score each sub-area 0-4, then convert: dimension score /100 = (sum / 20) x 100.

Audit the LIVE site from desktop and mobile views of at least the homepage and one key inner page: screenshots the user uploads, or renders from Claude in Chrome if the user approved it in the permission step. Judge what you can see and verify; with no screenshots, say so, label visual checks "HTML-inferred", and score only what the HTML/CSS reveals (contrast, hover states and layout shift then become "needs manual check").

## 1. Accessibility (0-4)

Check for:
- **Contrast**: text contrast < 4.5:1 (AA) — sample header, body, buttons, links on tinted backgrounds
- **Missing ARIA**: interactive elements without roles/labels/states
- **Keyboard navigation**: missing focus indicators, illogical tab order, keyboard traps
- **Semantic HTML**: broken heading hierarchy, missing landmarks, divs acting as buttons
- **Alt text**: missing or meaningless image descriptions
- **Forms**: inputs without labels, poor error messaging, missing required indicators

Score: 0=fails WCAG A · 1=major gaps · 2=partial effort, significant gaps · 3=WCAG AA mostly met · 4=AA fully met, approaches AAA

## 2. Visual hierarchy & clarity (0-4)

Check for:
- One clear focal point per view; the most important element is visibly the most prominent
- Typography scale: distinct, consistent levels (not 8 near-identical sizes); line length 45-90 chars; line height comfortable
- Spacing rhythm: consistent spacing scale, related items grouped, sections breathe
- Alignment: elements on a grid, no near-miss misalignments
- Cognitive load: can a first-time visitor tell within 5 seconds what this site is, who it is for, and what to do next?

Score: 0=chaotic, no hierarchy · 1=hierarchy unclear on key pages · 2=usable but flat/noisy · 3=clear with minor slips · 4=confident, intentional hierarchy throughout

## 3. Responsive design (0-4)

Check for:
- Fixed widths breaking mobile; horizontal scroll on narrow viewports
- Touch targets < 44x44px
- Text scaling: layout survives larger text sizes
- Missing tablet/mobile variants; images not responsive
- Mobile CTA visible without scrolling on key pages

Score: 0=desktop-only · 1=some breakpoints, many failures · 2=works on mobile, rough edges · 3=responsive, minor issues · 4=fluid on all viewports, proper touch targets

## 4. Consistency & craft (0-4)

Check for:
- Hard-coded one-off colors vs a coherent palette; dark mode (if offered) actually works
- Component consistency: buttons, cards, forms look and behave the same across pages
- Micro-states: hover/focus/active/disabled states exist and are distinct
- Loading, empty and error states handled (where applicable)
- Performance-visible craft: no layout shift on load, no janky animation

Score: 0=no system, everything ad hoc · 1=minimal consistency · 2=partial system, inconsistently applied · 3=consistent, minor drift · 4=tight system, polished states

## 5. Anti-patterns (0-4) — start the report with this verdict

Pass/fail question: **does this look templated or AI-generated?** Look for generic tells and general anti-patterns:
- AI slop tells: default purple/indigo gradient palette, gradient text, glassmorphism-by-default, three-card feature grids with icon+title+blurb, fake hero metrics, generic stock illustration style, interchangeable copy
- General anti-patterns: gray text on colored backgrounds, nested cards, bounce easing, redundant copy ("Welcome to our website"), sliders/carousels hiding key content, walls of centered text

Score: 0=slop gallery (5+ tells) · 1=heavy generic aesthetic (3-4) · 2=some tells (1-2) · 3=mostly clean · 4=distinctive, intentional design

Be brutally honest and specific — name the tells and where they appear.

## Reporting rules

- Tag every issue P0-P3: **P0** blocks task completion · **P1** major difficulty or WCAG AA violation · **P2** annoyance with workaround · **P3** polish
- For each issue: location (page/element), impact on users, standard violated (if any), concrete fix
- Identify systemic patterns ("touch targets too small throughout"), not just one-offs
- Include positive findings — what to keep and replicate
- Never report an issue without explaining why it matters; verify before reporting (no false positives)
