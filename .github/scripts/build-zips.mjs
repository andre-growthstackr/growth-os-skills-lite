#!/usr/bin/env node
// Builds one zip per skill (skill folder at the zip root, as Claude.ai expects)
// plus dist/growth-os-lite-all.zip with every skill folder. Zero-dep: uses the system `zip`.
// Usage: node .github/scripts/build-zips.mjs

import { readdirSync, statSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { join, resolve } from "node:path";
import { execFileSync } from "node:child_process";

const ROOT = process.cwd();
const SKILLS = join(ROOT, "skills");
const DIST = resolve(ROOT, "dist");

const skills = readdirSync(SKILLS).filter(
  (d) => !d.startsWith(".") && statSync(join(SKILLS, d)).isDirectory() && existsSync(join(SKILLS, d, "SKILL.md")),
);
if (!skills.length) {
  console.error("No skills found");
  process.exit(1);
}

rmSync(DIST, { recursive: true, force: true });
mkdirSync(DIST, { recursive: true });

const zip = (out, entries) =>
  execFileSync("zip", ["-r", "-q", "-X", out, ...entries, "-x", "*.DS_Store", "*__pycache__*"], { cwd: SKILLS, stdio: "inherit" });

for (const s of skills) {
  zip(join(DIST, `${s}.zip`), [s]);
  console.log(`dist/${s}.zip`);
}
zip(join(DIST, "growth-os-lite-all.zip"), skills);
console.log(`dist/growth-os-lite-all.zip (${skills.length} skills)`);
