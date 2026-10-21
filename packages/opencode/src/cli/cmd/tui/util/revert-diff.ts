import { parsePatch } from "diff"

export function getRevertDiffFiles(diffText: string) {
  if (!diffText) return []

  try {
    return parsePatch(diffText).map((patch: any) => {
      const filename = [patch.newFileName, patch.oldFileName].find((item: any) => item && item !== "/dev/null") ?? "unknown"
      return {
        filename: filename.replace(/^[ab]\//, ""),
        additions: patch.hunks.reduce((sum: any, hunk: any) => sum + hunk.lines.filter((line: any) => line.startsWith("+")).length, 0),
        deletions: patch.hunks.reduce((sum: any, hunk: any) => sum + hunk.lines.filter((line: any) => line.startsWith("-")).length, 0),
      }
    })
  } catch {
    return []
  }
}
