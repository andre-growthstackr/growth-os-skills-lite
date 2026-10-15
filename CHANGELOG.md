# Changelog

All notable changes to Growth OS Lite are recorded here. Versions follow semantic versioning.

## [1.0.0] — 2026-10-15

First public release of Growth OS Lite, the free edition of the Growth OS Skills Pack.

### Added
- 20 standalone skills across Brand OS, Design OS (copy), Web OS, Leads OS, Conversion OS,
  Content OS, and Ads OS, each runnable on its own in Claude.ai, Claude Desktop, and Claude Code.
- `growth-os-lite-start`: setup, the four empty context files, and goal-to-skill routing.
- Context inheritance without a file system: skills read `business-profile.md`, `icp.md`,
  `voice-of-customer.md`, and `offer.md` from the Claude project, the chat, or the working folder,
  and ask 3–5 questions when a file is missing.
- Permission-first external tools: every optional MCP server is asked for before the first call,
  with a built-in path when declined. Paid-only metrics are reported as "not measured", never
  estimated.
- `ads-audit` rebuilt as a sequential, read-only audit on uploaded exports or screenshots, with
  the Lite scoring rubric (`scripts/score.py`) and the economics calculator (`scripts/admath.py`).
- One zip per skill plus `growth-os-lite-all.zip` on every release.
- Validator (`.github/scripts/validate.mjs`) enforcing standalone folders, resolvable references,
  the permission step, and the inventory.
- Skill descriptions kept at 200 characters or fewer (the Claude.ai upload limit), with Swedish
  and English trigger phrases.
- Templates for the four context files in `templates/`.
- Guide for Claude.ai and Claude Desktop: `docs/claude-ai-guide.md`.
