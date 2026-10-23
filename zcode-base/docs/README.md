# ZCode-Based OpenFable Rebuild

Architecture-aligned rebuild using `.zcode` design patterns as reference framework.
Not a full 8,800-commit merge — feature/module migration of verified components.

## Verified Components Migrated
- Agent swarm (ruflo-integration/swarm)
- Memory / RAG (ruflo-integration/memory)
- Plugin marketplace (ruflo-integration/plugin-marketplace)
- MCP server bridge (ruflo-integration/mcp-server)
- Provider config fixes (openfable -> opencode, OPENFABLE_* env vars)
- Skill loading (skip duplicates + parse logging)
- Android manifest (file access permissions + runtime request)
- Typecheck: 0 errors
- Git push: clean (b3bead2)

## Source Reference
- Original OpenFable: https://github.com/ProjectZeroDays/OpenFable (commit b3bead2)
- Design reference: `.zcode` upstream patterns (from AGENTS.md reference)
- Ruflo harness: https://github.com/ProjectZeroDays/ruflo (feature/module bridge)
