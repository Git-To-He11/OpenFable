# AI Provider Cheat Sheet — Project Zero (2026-10-02)

Keys live in **`~/.zcode/provider-keys.env`** (chmod 600) and the repo's gitignored
`C:\Projects\Quantum CLI\.env`. Never commit them. Rotate both files together.

---

## 1. Live verification results (2026-10-02, `/models` endpoint)

| Provider | Status | Notes |
|---|---|---|
| Abliteration AI | ✅ 200 | 3 models. **Real model ID is `abliterated-model-large-v2`** (not `abliterated-large-v2`) |
| opencode Zen | ✅ 200 | 85 models (`claude-fable-5`, `claude-opus-5-5`, …) |
| Agnes 2–7 | ✅ 200 | 12 models each; catalog includes `agnes-3.0-flash`, `agnes-2.5-pro-alpha`, `agnes-video-2.5-flash` — confirm `Agnes-2.6-flash` exists per account before relying on it |
| Agnes 1 | ❌ 401 | The UUID-format key is rejected — repair/replace this key |
| Agnes 4 vs 7 | ℹ️ | Genuinely distinct accounts (different model availability) despite similar keys |
| Venice AI | ✅ 200 | 128 models. Look up the exact ID for "Qwen 3.6 Plus Uncensored" in the list before first use |
| OpenRouter | ✅ 200 | 464 models, `vendor/model-slug` IDs |
| Xiaomi (MiMo) | ❌ 401 | OpenAI endpoint rejects the key — retry against the Anthropic endpoint `…/anthropic` before escalating |
| HF Inference Endpoint | ⚠️ 503 | URL + token format accepted; endpoint is **paused** — resume it in the HF console, then re-verify |
| LM Studio (local) | ⚠️ 000 | Not running. Start LM Studio server, then `GET http://localhost:1234/v1/models` |

## 2. How to switch providers per tool

### ZCode (this tool)
- Session model: switch in the ZCode UI/model picker (user-controlled; agents never change it).
- Subagents: pass a registered model via `subagent_model` on Agent/Workflow calls.
- Repo/AI-Supervisor work: use the **provider-rotation skill** (`/provider-rotate`) — it loads
  `~/.zcode/provider-keys.env`, pre-checks the next candidate's `/models`, and edits the
  gitignored `.env` accordingly.

### opencode
- Config lives at `~/.config/opencode/` (present on this machine). Register providers in its
  config (JSON) or run `opencode auth login` for native key registration; switch with
  `opencode models` / the model flag. **Status: config write is a registered task** in
  `TASKS_CHECKLIST.md` Phase 7 — keys are already stored in the env file above.

### mimocode
- **Not installed** (uninstalled 2026-09-28). Per the task rules: skipped, noted here.
  Re-install, then mirror the opencode provider block into its config.

### Manual quick-test of any provider
```bash
set -a; . ~/.zcode/provider-keys.env; set +a
curl -s -m 8 -H "Authorization: Bearer $AGNES_API_KEY_5" "$AGNES_BASE_URL/models" | head -c 400
```

## 3. Rotating keys later
1. Generate/obtain the new key at the provider's console.
2. Update `~/.zcode/provider-keys.env` **and** the repo `.env` (both, always).
3. `chmod 600 ~/.zcode/provider-keys.env` after editing.
4. Re-run the verification table in §1 (curl `/models`, expect 200).
5. Check rotation history at `~/.zcode/logs/provider-rotation.log`.
6. **Already-flagged for rotation:** the legacy Abliteration key (`ABLITERATION_KEY` in repo
   `.env`) — cut over to `ABLITERATION_API_KEY`, then delete the legacy var. Agnes-1's key is
   rejected and needs replacement. The admin master code exposed in legacy docs is compromised
   and must be rotated at first deployment (see `TASKS_CHECKLIST.md` Phase 15).

## 4. Rules honored
- No key values are committed to git anywhere; the repo `.env` is gitignored (line 12).
- Keys never appear in skills, docs, or logs — env files only.
