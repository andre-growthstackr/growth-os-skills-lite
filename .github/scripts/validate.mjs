#!/usr/bin/env node
// Growth OS Lite validator — zero-dep. Enforces the standalone-skill rules the README claims.
// Usage: node .github/scripts/validate.mjs [--skill <name>]
// Exit 1 on any error; warnings never fail the build.

import { readFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { join, relative, extname } from "node:path";

const ROOT = process.cwd();
const errors = [];
const warns = [];
const err = (m) => errors.push(m);
const warn = (m) => warns.push(m);
const read = (p) => readFileSync(join(ROOT, p), "utf8");

const EXPECTED_SKILLS = 20;
const VERSION = "1.0.0";
const MODULES = new Set(["meta", "brand-os", "design-os", "web-os", "leads-os", "conversion-os", "content-os", "ads-os"]);
// Non-skill slash commands that may legitimately appear (Claude Code built-ins).
const COMMAND_ALLOWLIST = new Set(["plugin", "mcp", "config", "agents", "permissions", "help", "compact", "skills"]);
const TEXT_EXT = new Set([".md", ".json", ".yml", ".yaml", ".mjs", ".js", ".py", ".txt", ".svg", ".html", ".csv"]);
const CANONICAL = ".github/scripts/canonical";
const PERMISSION_HEADING = "## External tools — ask first";

// Terms this validator bans are assembled from parts so the validator itself stays clean.
const BANNED_DB = new RegExp(["air", "table"].join(""), "i");
const BANNED = [
  [new RegExp(["pip", "\\s+install"].join(""), "i"), "package install instruction"],
  [new RegExp(["play", "wright"].join(""), "i"), "browser-automation dependency"],
  [/(paste|klistra in|enter|provide|ange|share|skicka)\b[^.\n]{0,40}\b(api[ -]?key|api-nyckel|access token|secret key)/i, "asks the user for an API key"],
  [/[A-Z]{3,}_API_KEY/, "API key environment variable"],
];
// Anything that names an external MCP server or the MCP mechanism itself.
const MCP_TERMS = /\bMCP\b|mcp__|firecrawl|dataforseo|claude in chrome|apify/i;

const only = (() => {
  const i = process.argv.indexOf("--skill");
  return i > -1 ? process.argv[i + 1] : null;
})();

const walk = (dir) => {
  const out = [];
  for (const e of readdirSync(join(ROOT, dir))) {
    if ([".git", "node_modules", "dist"].includes(e)) continue;
    const p = join(dir, e);
    if (statSync(join(ROOT, p)).isDirectory()) out.push(...walk(p));
    else out.push(p);
  }
  return out;
};
const isText = (p) => TEXT_EXT.has(extname(p)) || p.endsWith("LICENSE") || p.endsWith("LICENSE.txt");

const frontmatter = (text) => {
  const m = text.match(/^---\n([\s\S]*?)\n---/);
  return m ? m[1] : null;
};
// Minimal YAML reader for `description:` (plain, quoted, or folded `>` / literal `|` block).
const readDescription = (fm) => {
  const lines = fm.split("\n");
  const i = lines.findIndex((l) => /^description:/.test(l));
  if (i < 0) return null;
  const head = lines[i].replace(/^description:\s*/, "");
  if (/^[>|][-+]?\s*$/.test(head)) {
    const body = [];
    for (let j = i + 1; j < lines.length && /^\s+\S|^\s*$/.test(lines[j]); j++) body.push(lines[j].trim());
    return body.join(" ").replace(/\s+/g, " ").trim();
  }
  return head.replace(/^["']|["']$/g, "").trim();
};

// ---------- 1. Skill inventory ----------
const skillDirs = readdirSync(join(ROOT, "skills")).filter((d) => {
  const p = join(ROOT, "skills", d);
  return statSync(p).isDirectory() && !d.startsWith(".");
});
for (const d of readdirSync(join(ROOT, "skills"))) {
  if (d.startsWith(".")) err(`skills/${d}: hidden folders are not allowed (no shared .core in Lite)`);
}
const skillSet = new Set(skillDirs);
if (skillDirs.length !== EXPECTED_SKILLS) err(`expected ${EXPECTED_SKILLS} skills, found ${skillDirs.length}`);
for (const banned of ["_shared", "agents", "hooks", "_workspace-starter"]) {
  if (existsSync(join(ROOT, banned))) err(`${banned}/ must not exist in Lite`);
}

const canonical = (name) => (existsSync(join(ROOT, CANONICAL, name)) ? read(`${CANONICAL}/${name}`) : null);
const CANON_PERMISSION = canonical("mcp-permission.md");
const CANON_CONTEXT = canonical("context-loading.md");
if (!CANON_PERMISSION) err(`${CANONICAL}/mcp-permission.md missing`);
if (!CANON_CONTEXT) err(`${CANONICAL}/context-loading.md missing`);

// Reference-file names: every file in any Lite skill's references/, plus the full pack's shared
// and ads-backend reference names (a bare mention of one of these means "load this file").
const KNOWN_REFERENCE_NAMES = new Set([
  "PLATFORMS.md", "README-core.md", "additional-platforms.md", "agent-pattern.md", "amazon-audit.md",
  "apple-audit.md", "automation-tier-classifier.md", "benchmarks.md", "bidding-strategies.md",
  "budget-allocation.md", "carousel-cover-art-direction.md", "cockpit-publish.md",
  "compliance-requirements.md", "compliance.md", "content-os-flow.md", "context-loading.md",
  "context-routing.md", "contract.md", "conversion-tracking.md", "copy-frameworks.md",
  "creative-source-registry.md", "deck-export.md", "gaql-notes.md", "google-audit.md",
  "google-creative-specs.md", "growth-os-model.md", "guarantee-check.md", "image-providers.md",
  "linkedin-audit.md", "linkedin-b2b-playbook.md", "linkedin-creative-specs.md", "mcp-integration.md",
  "meta-ai-stack.md", "meta-audit.md", "meta-creative-specs.md", "microsoft-audit.md",
  "microsoft-creative-specs.md", "outbound-os-flow.md", "output-paths.md", "pinterest-audit.md",
  "platform-specs.md", "principles.md", "prompt-patterns.md", "reddit-audit.md", "scoring-system.md",
  "snapchat-audit.md", "status-contract.md", "style-memory.md", "thinking-framework.md",
  "tiktok-audit.md", "tiktok-creative-specs.md", "voice-to-style.md", "workflow-pattern.md",
  "x-audit.md", "youtube-audit.md", "youtube-creative-specs.md", "mcp-permission.md",
  ...skillDirs.flatMap((d) =>
    existsSync(join(ROOT, "skills", d, "references")) ? readdirSync(join(ROOT, "skills", d, "references")) : []),
]);

const moduleCounts = {};
for (const dir of skillDirs) {
  if (only && dir !== only) continue;
  const base = `skills/${dir}`;
  if (!existsSync(join(ROOT, base, "SKILL.md"))) { err(`${base}: missing SKILL.md`); continue; }
  const skillText = read(`${base}/SKILL.md`);
  const fm = frontmatter(skillText);
  if (!fm) { err(`${base}/SKILL.md: no frontmatter`); continue; }

  // ---------- 2. Frontmatter ----------
  const name = (fm.match(/^name:\s*(\S+)/m) || [])[1];
  if (name !== dir) err(`${base}/SKILL.md: name '${name}' != folder '${dir}'`);
  const desc = readDescription(fm);
  if (!desc) err(`${base}/SKILL.md: missing description`);
  else if (desc.length > 200) err(`${base}/SKILL.md: description is ${desc.length} chars (max 200, the Claude.ai upload limit)`);
  const ALLOWED_KEYS = new Set(["name", "description", "license", "allowed-tools", "compatibility", "metadata"]);
  for (const k of [...fm.matchAll(/^([A-Za-z][\w-]*):/gm)].map((m) => m[1]))
    if (!ALLOWED_KEYS.has(k)) err(`${base}/SKILL.md: top-level frontmatter key '${k}' is rejected by Claude.ai uploads`);
  if (desc && /[<>]/.test(desc)) err(`${base}/SKILL.md: description must not contain < or >`);
  if (!/^\s{2}author:\s*GrowthStackr/m.test(fm)) err(`${base}/SKILL.md: metadata.author missing/wrong`);
  if (!/^\s{2}pack:\s*growth-os-lite\s*$/m.test(fm)) err(`${base}/SKILL.md: metadata.pack must be growth-os-lite`);
  if (!new RegExp(`^\\s{2}version:\\s*["']?${VERSION.replace(/\./g, "\\.")}["']?\\s*$`, "m").test(fm))
    err(`${base}/SKILL.md: metadata.version must be ${VERSION}`);
  const mod = (fm.match(/^\s{2}module:\s*(\S+)/m) || [])[1];
  if (!mod || !MODULES.has(mod)) err(`${base}/SKILL.md: module '${mod}' not in enum`);
  else moduleCounts[mod] = (moduleCounts[mod] || 0) + 1;
  const lineCount = skillText.split("\n").length;
  if (lineCount > 500) warn(`${base}/SKILL.md: ${lineCount} lines (aim for under 500; move detail to references/)`);

  const files = walk(base).filter(isText);
  let mcpMentioned = false;
  for (const rel of files) {
    const text = read(rel);
    const relInSkill = relative(base, rel);

    // ---------- 3. Self-contained paths ----------
    for (const [re, why] of [[/\.\.\//, "'../'"], [/_shared\//, "'_shared/'"], [/\.core\//, "'.core/'"]]) {
      if (re.test(text)) err(`${rel}: path outside the skill folder (${why})`);
    }
    if (extname(rel) === ".md") {
      for (const m of text.matchAll(/(?<![\w./-])((?:references|assets|scripts)\/[A-Za-z0-9_.\/-]+\.(?:md|py|json|csv|txt|svg|html))/g)) {
        if (!existsSync(join(ROOT, base, m[1]))) err(`${rel}: referenced file '${m[1]}' does not exist in ${base}/`);
      }
      // Bare file names (`compliance.md`) that are shared reference files elsewhere must exist here too.
      const local = new Set(walk(base).map((p) => p.split("/").pop()));
      for (const m of text.matchAll(/`([A-Za-z0-9_.-]+\.md)`/g)) {
        if (KNOWN_REFERENCE_NAMES.has(m[1]) && !local.has(m[1]))
          err(`${rel}: mentions reference file '${m[1]}' that is not in ${base}/`);
      }
    }

    // ---------- 4. Skill references must resolve or sit in an upsell block ----------
    if (extname(rel) === ".md") {
      text.split("\n").forEach((line, n) => {
        const upsell = /^\s*>/.test(line) && /Growth OS Skills Pack/.test(line);
        for (const m of line.matchAll(/(?:^|[\s(`"'*])\/([a-z][a-z0-9]*(?:-[a-z0-9]+)*)(?![\w./-])/g)) {
          const cmd = m[1];
          if (skillSet.has(cmd) || COMMAND_ALLOWLIST.has(cmd) || upsell) continue;
          err(`${rel}:${n + 1}: '/${cmd}' is not a Lite skill and is not inside an upsell block`);
        }
      });
    }

    // ---------- 5. MCP mentions ----------
    if (relInSkill !== "references/mcp-permission.md" && MCP_TERMS.test(text)) mcpMentioned = true;

    // ---------- 6. Scripts must be offline, stdlib-only calculators ----------
    if (extname(rel) === ".py") {
      const STDLIB = new Set(["json", "math", "sys", "argparse", "csv", "statistics", "re", "datetime", "collections", "typing", "dataclasses", "pathlib", "decimal", "fractions", "textwrap", "__future__", "itertools", "functools", "enum"]);
      for (const m of text.matchAll(/^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w., ]+))/gm)) {
        const mods = (m[1] || m[2]).split(",").map((s) => s.trim().split(/\s+/)[0].split(".")[0]);
        for (const x of mods) if (x && !STDLIB.has(x)) err(`${rel}: imports '${x}' (scripts must be offline, stdlib-only calculators)`);
      }
    }
  }

  // Context-loading copies must match the canonical text.
  const ctxPath = `${base}/references/context-loading.md`;
  if (existsSync(join(ROOT, ctxPath)) && CANON_CONTEXT && read(ctxPath) !== CANON_CONTEXT)
    err(`${ctxPath}: differs from ${CANONICAL}/context-loading.md`);

  if (mcpMentioned) {
    const permPath = `${base}/references/mcp-permission.md`;
    if (!existsSync(join(ROOT, permPath))) err(`${base}: mentions MCP/external servers but has no references/mcp-permission.md`);
    else if (CANON_PERMISSION && read(permPath) !== CANON_PERMISSION) err(`${permPath}: differs from ${CANONICAL}/mcp-permission.md`);
    const body = skillText.slice(skillText.indexOf("\n---", 4) + 4);
    const h = body.indexOf(PERMISSION_HEADING);
    const firstMention = body.search(MCP_TERMS);
    if (h < 0) err(`${base}/SKILL.md: mentions MCP/external servers but has no '${PERMISSION_HEADING}' section`);
    else {
      if (firstMention > -1 && firstMention < h) err(`${base}/SKILL.md: an MCP server is mentioned before the '${PERMISSION_HEADING}' permission step`);
      const sectionEnd = body.indexOf("\n## ", h + PERMISSION_HEADING.length);
      const section = body.slice(h, sectionEnd < 0 ? undefined : sectionEnd);
      if (!section.includes("references/mcp-permission.md")) err(`${base}/SKILL.md: permission section must point to references/mcp-permission.md`);
      const rows = section.split("\n").filter((l) => /^\|/.test(l));
      const header = rows[0] || "";
      if (!/Built-in path/i.test(header)) err(`${base}/SKILL.md: permission table needs a 'Built-in path' column`);
      else {
        const col = header.split("|").map((c) => c.trim()).findIndex((c) => /Built-in path/i.test(c));
        const data = rows.slice(2);
        if (!data.length) err(`${base}/SKILL.md: permission table has no servers listed`);
        for (const r of data) {
          const cell = (r.split("|")[col] || "").trim();
          if (!cell || /^[-–—]$/.test(cell)) err(`${base}/SKILL.md: server row without a built-in path: ${r.trim()}`);
        }
      }
    }
  }
}

// ---------- 7. Repo-wide banned content ----------
const SELF = ".github/scripts/validate.mjs";
for (const rel of walk(only ? `skills/${only}` : ".").filter(isText)) {
  if (rel === SELF) continue;
  const text = read(rel);
  if (BANNED_DB.test(text) || BANNED_DB.test(rel)) err(`${rel}: mentions a banned content-database integration`);
  for (const [re, why] of BANNED) if (re.test(text)) err(`${rel}: ${why}`);
}

// ---------- 8. Manifests and inventory sync ----------
if (!only) {
  const plugin = JSON.parse(read(".claude-plugin/plugin.json"));
  const market = JSON.parse(read(".claude-plugin/marketplace.json"));
  const codex = JSON.parse(read(".codex-plugin/plugin.json"));
  const numIn = (s) => Number((String(s).match(/(\d+)\s+(?:[\w-]+\s+){0,3}skills/i) || [])[1]);
  if (plugin.name !== "growth-os-skills-lite") err(`plugin.json name must be growth-os-skills-lite`);
  if (market.name !== "growth-os-lite") err(`marketplace.json name must be growth-os-lite`);
  if (market.plugins?.[0]?.name !== plugin.name) err(`marketplace plugin entry name != plugin.json name`);
  for (const [label, v] of [["plugin.json", plugin.version], ["marketplace entry", market.plugins?.[0]?.version], [".codex-plugin", codex.version]])
    if (v !== VERSION) err(`${label} version ${v} != ${VERSION}`);
  for (const [label, d] of [["plugin.json", plugin.description], ["marketplace entry", market.plugins?.[0]?.description], [".codex-plugin", codex.description]])
    if (numIn(d) !== skillDirs.length) err(`${label} description says ${numIn(d)} skills, ${skillDirs.length} on disk`);
  if (codex.skills !== "./skills/") err(`.codex-plugin skills path must be ./skills/`);

  const readme = read("README.md");
  const badge = Number((readme.match(/badge\/skills-(\d+)-/) || [])[1]);
  if (badge !== skillDirs.length) err(`README skills badge ${badge} != ${skillDirs.length}`);
  const badgeVersion = (readme.match(/badge\/version-([\d.]+)-/) || [])[1];
  if (badgeVersion !== VERSION) err(`README version badge ${badgeVersion} != ${VERSION}`);
  for (const s of skillDirs) if (!readme.includes(`\`${s}\``)) err(`README does not list skill '${s}'`);

  const startDir = "skills/growth-os-lite-start";
  if (existsSync(join(ROOT, startDir))) {
    const startText = walk(startDir).filter(isText).map(read).join("\n");
    for (const s of skillDirs) if (!startText.includes(`\`${s}\``) && s !== "growth-os-lite-start") err(`growth-os-lite-start does not route to '${s}'`);
  } else err(`${startDir} missing`);

  for (const t of ["business-profile.md", "icp.md", "voice-of-customer.md", "offer.md"])
    if (!existsSync(join(ROOT, "templates", t))) err(`templates/${t} missing`);
}

// ---------- report ----------
console.log(`Inventory: ${skillDirs.length} skills${only ? ` (checked: ${only})` : ""}`);
console.log(`Modules: ${Object.entries(moduleCounts).sort((a, b) => b[1] - a[1]).map(([k, v]) => `${k} ${v}`).join(" · ")}`);
for (const w of warns) console.log(`WARN  ${w}`);
for (const e of errors) console.log(`ERROR ${e}`);
console.log(errors.length ? `\n${errors.length} error(s)` : "\nAll checks passed");
process.exit(errors.length ? 1 : 0);
