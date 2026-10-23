#!/usr/bin/env node
/**
 * generate-zip-artifacts.js — creates category .zip files from .catalogues/
 */
import fs from "node:fs"
import path from "node:path"
import { createWriteStream } from "node:zlib"

console.log("=== ZIP Artifact Generation ===")
const sourceDir = path.resolve(process.cwd(), ".catalogues")
const distDir = path.resolve(process.cwd(), ".catalogues/dist")
fs.mkdirSync(distDir, { recursive: true })

const categories = ["skills", "plugins", "mcps", "commands", "extensions", "providers", "exploits"]
for (const cat of categories) {
  const file = path.join(sourceDir, `${cat}.json`)
  if (fs.existsSync(file)) {
    const zipName = path.join(distDir, `${cat}.zip`)
    // Minimal zip placeholder — in production this would use archiver or system zip
    const content = JSON.stringify({ catalog: cat, source: file, created: new Date().toISOString(), note: "auto-generated semi-release artifact" })
    fs.writeFileSync(zipName + ".json", content)
    console.log(`Artifact: ${cat}.zip (placeholder .json generated)`)
  }
}
console.log("Artifact generation complete.")
