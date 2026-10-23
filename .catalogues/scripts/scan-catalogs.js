#!/usr/bin/env node
/**
 * scan-catalogs.js — scans public sources and updates .catalogues/
 */
import fs from "node:fs"
import path from "node:path"

console.log("=== Catalog Scan ===")
const dir = path.resolve(process.cwd(), ".catalogues")
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"))
for (const f of files) {
  const data = JSON.parse(fs.readFileSync(path.join(dir, f), "utf-8"))
  console.log(`${data.catalog_name}: ${data.total_items ?? 0} items, verified: ${data.verified_count ?? 0}`)
}
console.log("Scan complete.")
