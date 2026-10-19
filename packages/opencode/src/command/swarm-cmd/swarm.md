---
name: swarm
description: Spawn a massive parallel subagent swarm for enterprise-grade parallel execution with verified quality gates
---

# /swarm

Spawn a massive swarm of intelligent, persistent, thorough AI subagents running simultaneously in parallel to complete all tasks quickly with verified, production-grade quality.

## Activation
- Message contains `/swarm` (any text after colon is the mission briefing)
- Or explicitly asks to "spawn a swarm", "run agents in parallel", "swarm of subagents"

## Protocol

### Phase 0 — Mission Intake (Commander, alone, fast)
1. Read mission after `/swarm:` and expand with standing context
2. Produce **Swarm Plan**:
   - Complete task list, each with one-line acceptance criterion
   - Dependencies between tasks
   - **File ownership map** — every file path assigned to EXACTLY ONE implementer
   - Swarm size: 3–12 implementers (never spawn for a 30-second task)
   - Quality gates: real build/test commands, lint/typecheck, rendered-output review

### Phase 1 — Parallel Dispatch (one message, many Agent calls)
- Launch ALL independent implementers **in a single message with multiple Agent invocations**
- Each agent brief is self-contained (subagents start fresh):
  1. Role + single task with acceptance criterion
  2. Full context: repo path, AGENTS.md rules verbatim, key file paths, API signatures
  3. **File ownership list** — "you may create/modify ONLY these paths"
  4. Hard constraints (never weaken a check; no simulated code; immutable key files)
  5. Verification duty: exact command + output to paste as proof
  6. Report format: changes, files touched, evidence, open risks

### Phase 2 — Integration (Commander, alone)
1. Collect reports. Cross-check: union of touched files covers mission? No file conflicts?
2. Run integration steps (build → typecheck → lint → test)
3. Run **full-project gates** yourself — per-agent partial checks don't prove integrated whole

### Phase 3 — Verification & Repair Loop
1. Spawn **verifier** (read-only: code-reviewer, silent-failure-hunter, visual-judge)
2. Check: acceptance criteria met, no mocks/stubs, no weakened checks, no regressions
3. If fails: dispatch targeted repair agent with exact evidence + minimal scope, re-run gate
4. Repeat until gate passes **with printed evidence**

### Phase 4 — Closing Report
- Accomplishments with evidence lines
- Verification evidence: build result, test counts, artifact paths
- Anything deferred/failed — stated plainly
- Next steps only after deliverable is done

## Anti-Patterns (invalidate the swarm)
- ❌ Launching agents one-by-one when independent
- ❌ Two agents editing same file — partition ownership instead
- ❌ Accepting "done" from subagent without running gate yourself
- ❌ Vague briefs ("improve the code") instead of owned tasks with criteria
- ❌ Simulating verification ("this should pass") instead of running it
- ❌ Stopping mid-mission to ask "should I continue?"

## Example
```
/swarm Fix Android build, add network dashboard, push signed release
```

## Source
- Macro: `packages/opencode/src/skill/macro/swarm.yaml`
- Skill: `skills/swarm/SKILL.md`