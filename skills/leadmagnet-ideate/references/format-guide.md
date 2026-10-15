# Lead Magnet Format Guide

Detailed creation guidance for each lead magnet format.

## Contents
- Ebooks & Guides
- Checklists
- Cheat Sheets
- Templates & Spreadsheets
- Swipe Files
- Mini-Courses
- Quizzes & Assessments
- Calculators & Graders
- Webinars & Workshops

---

## Ebooks & Guides

**Best for**: Building authority, deep education, awareness-stage leads

**Structure**:
1. Title page with professional design
2. Table of contents
3. Introduction — frame the problem, set expectations
4. 3-7 chapters — one key concept per chapter
5. Summary — recap key takeaways
6. CTA — next step toward your product

**Guidelines**:
- Ideal length: 10-25 pages (shorter is fine if valuable)
- Include visuals: charts, diagrams, screenshots
- Use callout boxes for key stats or quotes
- End each chapter with a quick takeaway
- Don't pad — density beats length

**Tools**: Canva, Google Docs → PDF, Notion export, Designrr, Beacon.by

---

## Checklists

**Best for**: Process-oriented tasks, quick wins, implementation help

**Structure**:
- Title: "[Number]-Point [Topic] Checklist"
- Numbered or checkbox items
- Group into logical sections if 10+ items
- Brief explanation per item (1-2 sentences)

**Guidelines**:
- Keep to 1-2 pages
- Use actionable language ("Verify X", "Set up Y", "Remove Z")
- Order by workflow sequence or priority
- Make it printable — clean layout, generous spacing
- Include a "done" checkbox for each item

**What works**: Step-by-step processes, audit criteria, launch checklists, setup guides

---

## Cheat Sheets

**Best for**: Reference material, shortcuts, quick-lookup information

**Structure**:
- One page (two pages max)
- Organized by category or workflow
- Dense but scannable
- Visual hierarchy with headers and grouping

**Guidelines**:
- Optimize for quick reference, not reading
- Use tables, grids, or columns
- Include formulas, shortcuts, or code snippets
- Design for printing or saving as desktop reference
- Bold the most important items

**What works**: Keyboard shortcuts, formula references, terminology glossaries, decision matrices

---

## Templates & Spreadsheets

**Best for**: Repeatable processes, planning, tracking

### Spreadsheet Templates (Google Sheets / Excel)
- Include a "How to Use" tab with instructions
- Pre-fill with example data
- Use data validation for dropdown fields
- Add conditional formatting for visual cues
- Lock formula cells, leave input cells editable
- Include a "Make a Copy" link (Google Sheets)

### Notion Templates
- Provide a duplicate link
- Include a getting-started guide
- Pre-populate with example content
- Use Notion's database features (views, filters, relations)
- Keep it simple — don't over-engineer

### Document Templates
- Provide in multiple formats (Google Doc, Word, PDF)
- Include placeholder text with [BRACKETS] for customization
- Add inline instructions in a different color
- Make it immediately usable with minimal editing

**Key principle**: Templates should be usable within 5 minutes of downloading.

---

## Swipe Files

**Best for**: Inspiration, examples, learning from others

**Structure**:
- Curated collection of 15-50 examples
- Organized by category, type, or use case
- Each example includes:
  - The example itself (screenshot, text, link)
  - Why it works (2-3 bullet annotations)
  - How to adapt it (1-2 sentences)

**Guidelines**:
- Quality over quantity — curate ruthlessly
- Add your analysis, don't just collect
- Organize for browsing (categories, tags)
- Update periodically with fresh examples
- Credit original sources

**What works**: Email subject lines, landing pages, ad copy, CTAs, onboarding flows, pricing pages

---

## Mini-Courses

### Email-Based Mini-Courses
- 3-5 emails delivered over 5-7 days
- One lesson per email, one concept per lesson
- Each email: teach → example → exercise
- Progressive difficulty (build on previous lessons)
- Final email: summary + CTA for product or next step

### Video-Based Mini-Courses
- 3-5 videos, 5-15 minutes each
- Host on unlisted YouTube, Loom, or course platform
- Deliver links via email drip
- Include worksheets or exercises per lesson
- More personal — builds stronger connection

**Cadence**: Every 1-2 days. Don't stretch too thin or compress too tight.

**Key principle**: Each lesson should deliver standalone value. If someone only watches lesson 2, they should still learn something useful.

---

## Quizzes & Assessments

**Best for**: Engagement, segmentation, personalized results

**Question Design**:
- 5-10 questions (sweet spot: 7)
- Multiple choice only — no open-ended
- Questions should feel insightful, not obvious
- Progress indicator ("Question 3 of 7")

**Result Segmentation**:
- 3-5 result categories
- Each result: name, description, personalized recommendations
- Tailor follow-up emails by result type
- Share-worthy result format ("I got: Growth Stage Marketer!")

**Implementation**: Gate results behind email capture. The quiz itself is ungated — the personalized results require an email.

**Building it**: `leadmagnet-create` writes the complete quiz spec — questions, answer options, scoring, result pages and follow-up angle per result. Build it in any quiz or form tool, or ask Claude to turn the spec into an interactive page.

---

## Calculators & Graders

**Best for**: BOF/MOF intent, ROI cases, personalized numbers or scores

**Spec structure**:
- Inputs: 3-7 fields, each mapped to a qualification criterion (company size, budget, volume, current tool)
- Formula: every calculation written out step by step, with units and any assumptions labeled as assumptions
- Output: the number or score, what it means, and 2-3 recommendations per result band
- Gate: show a teaser result ungated; the full breakdown or report requires an email

**Guidelines**:
- Assumptions in the formula (rates, prices, averages) come from the user or a cited source + URL — never from memory
- Keep the input screen to one view; fewer fields beat more precision
- Result bands (e.g. low / medium / high) should map to the ICP tiers and the follow-up angle

**Building it**: `leadmagnet-create` writes the complete spec. Build it in a spreadsheet, a form tool with calculations, or ask Claude to turn the spec into an interactive page.

---

## Webinars & Workshops

### Live Webinars
- 30-45 minutes teaching + 15 minutes Q&A
- Structure: Hook → Teach (3 key points) → Demo/example → CTA
- Promote 1-2 weeks in advance
- Send 3 reminder emails (confirmation, day before, 1 hour before)
- Record for replay (extends value)

### Evergreen Webinars
- Pre-recorded, available on demand
- Same structure as live but tighter editing
- Always-on lead generation
- Gate with email registration
- Automated follow-up sequence

**Follow-up**: Send replay link + summary + CTA within 24 hours. Continue with nurture sequence.

**Key principle**: Teach something genuinely useful. A webinar that's just a sales pitch will damage trust.
