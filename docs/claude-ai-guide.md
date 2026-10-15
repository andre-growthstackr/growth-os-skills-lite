# Growth OS Lite in Claude.ai and Claude Desktop — step by step

This guide gets the 20 Growth OS Lite skills running in Claude.ai (web) or the Claude Desktop app,
and sets up a Claude project so every skill reads your business context automatically.

Checked against the Claude Help Center on 2026-10-15. Claude's settings move from time to time;
if a menu name differs, the linked help articles are the source of truth.

## Before you start

- **Plan:** custom skills are available on Free, Pro, Max, Team and Enterprise plans
  ([Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)).
- **Code execution must be on.** Skills need "Code execution and file creation".
  - Free, Pro, Max: turn it on in **Settings → Capabilities**.
  - Team: on by default for the organization.
  - Enterprise: an Owner enables "Code execution and file creation" and "Skills" in
    **Organization settings → Plugins & skills**. If your organization has turned off
    user-created skills, ask an Owner to upload the skills for everyone instead (see the end of
    this guide).

## 1. Download the skills

Go to the [latest release](https://github.com/andre-growthstackr/growth-os-skills-lite/releases/latest)
and download:

- one zip per skill (e.g. `icp-builder.zip`) — **this is what you upload**, or
- `growth-os-lite-all.zip` — every skill in one archive. Unzip it on your computer, then zip each
  skill folder separately, or just download the individual zips instead.

Each skill zip contains a single folder named after the skill, with `SKILL.md` inside. Do not
unzip and re-zip it with the files at the top level: Claude expects the skill folder at the root
of the zip ([How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)).

Start with these five if you do not want all 20 at once:
`growth-os-lite-start`, `business-audit`, `icp-builder`, `brand-voc`, `brand-offer`.

## 2. Upload each skill

In Claude.ai or Claude Desktop:

1. Open **Customize** in the left sidebar, then **Skills**.
2. Click **+**, then **Create skill**, then **Upload a skill**.
3. Choose the skill's zip file.
4. Repeat for each skill. Every uploaded skill appears in your list with an on/off switch; keep
   the ones you use switched on.

Uploaded skills are personal to your account until you share them, and they are available in
every chat, including chats inside projects.

If an upload is rejected, the most common reasons are a zip with the files at the top level
instead of inside the skill folder, a renamed folder (the folder name must match the skill's
`name`), or a description that is too long for your workspace (see "Known issues" below).

## 3. Create a Claude project for your company

A project keeps your context files in one place so every chat inside it can read them.

1. Click **Projects → New project**. Name it e.g. "Growth OS – Acme".
2. Open a new chat **inside the project** and say: "Kom igång med Growth OS" or
   "Set up Growth OS". The `growth-os-lite-start` skill explains the system and gives you the four
   empty context files.
3. Run the four setup skills in order, one chat each, inside the project:

   | Step | Say | You get |
   |---|---|---|
   | 1 | "Gör en business audit av acme.se" | `business-profile.md` |
   | 2 | "Bygg min ICP" | `icp.md` |
   | 3 | "Ta fram Voice of Customer" | `voice-of-customer.md` |
   | 4 | "Designa vårt erbjudande" | `offer.md` |

4. After each step, download the `.md` file the skill delivers and **add it to the project's
   knowledge** (the project's files panel). From then on every Growth OS skill in that project
   uses it, without you re-explaining your business.

Agencies: create one project per client. Each project holds that client's four files.

## 4. Use the skills

Ask in plain language, in Swedish or English. Examples:

- "Skriv ett LinkedIn-inlägg om varför BRF:er skjuter upp stambyten" → `socialpost-writer`
- "Gör en SEO-audit av acme.se" → `seo-audit`
- "Varför konverterar inte den här sidan?" + a screenshot → `cro-audit`
- "Granska våra Meta-annonser" + a campaign export → `ads-audit`

Not sure which skill fits? Ask "Vilken Growth OS-skill ska jag använda för …?".

## External tools are optional, and you are always asked first

Every skill works with what Claude has built in: web search, reading web pages, and files you
upload. A few skills can use an external connector (for example Firecrawl, DataForSEO, or an
ads-platform server) for better data. Before any skill uses one, it stops and asks you: which
service, what it is for, and what it costs. Say no and the skill continues without it.

Connectors are added in **Customize → Connectors → Add custom connector**
([Custom connectors](https://support.claude.com/en/articles/11175166)). API keys belong in the connector settings, never in a
chat, and a Growth OS skill will never ask for one.

## For Team and Enterprise Owners

To give the whole organization the skills, an Owner can upload each zip in
**Organization settings → Plugins & skills → Add → Upload a skill**. Organization-provisioned
skills are on by default and each member can switch them off
([Manage skills in your organization](https://support.claude.com/en/articles/13119606)). Enterprise
skill scanning, if enabled, reviews each uploaded skill.

## Known issues

- **Description length.** The Help Center lists a 200-character limit for a skill's description,
  while the open Agent Skills specification allows 1024. Growth OS Lite descriptions include both
  Swedish and English trigger phrases and are longer than 200 characters. If an upload is rejected
  for its description, open an issue on GitHub; meanwhile Claude Code and the plugin install are
  unaffected.
- **Websites that block page reading.** Some sites (and review platforms) block Claude's web
  fetch. The skill then asks you to paste the text or upload a screenshot.
