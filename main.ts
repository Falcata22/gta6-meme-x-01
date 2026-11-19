// main.ts — entrypoint for the gta6-meme-x-01 bounty.
//
// The whole job is to hand the house our post: copy POST.json from the
// repository into the output directory so the grader can read it.
// Nothing else is written; the run must be byte-for-byte repeatable.

import {
  copyFileSync,
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  rmSync,
} from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(botDir, "POST.json");
const target = join(outDir, "POST.json");

if (!existsSync(source)) {
  throw new Error(`POST.json not found in bot directory: ${source}`);
}

// Empty the output directory without removing the directory itself:
// the grader may run as a user who cannot recreate a deleted /output.
mkdirSync(outDir, { recursive: true });
for (const name of readdirSync(outDir)) {
  rmSync(join(outDir, name), { recursive: true, force: true });
}

copyFileSync(source, target);

// Sanity-check what we just wrote: it must be a JSON object naming
// an X post URL, otherwise the entry would be invalid downstream.
const posted = JSON.parse(readFileSync(target, "utf8")) as unknown;
if (
  typeof posted !== "object" ||
  posted === null ||
  typeof (posted as { url?: unknown }).url !== "string" ||
  !(posted as { url: string }).url.startsWith("https://x.com/")
) {
  throw new Error(`POST.json does not name an x.com post URL: ${target}`);
}
