#!/usr/bin/env node
/**
 * generate-catalog-index.js — creates combined index from all .catalogues/*.json
 */
import fs from "node:fs"
import path from "node:path"

console.log("=== Catalog Index Generation ===")
const dir = path.resolve(process.cwd(), ".catalogues")
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"))
const index = { catalogs: {}, generated_at: new Date().toISOString() }
for (const f of files) {
  const data = JSON.parse(fs.readFileSync(path.join(dir, f), "utf-8"))
  index.catalogs[data.catalog_name] = {
    file: f,
    items: data.total_items ?? 0,
    verified: data.verified_count ?? 0,
    version: data.version ?? "1.0.0"
  }
}
fs.writeFileSync(path.join(dir, "index.json"), JSON.stringify(index, null, 2))
console.log(`Index written: ${files.length} catalogs`)
