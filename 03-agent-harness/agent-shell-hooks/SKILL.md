---
name: agent-shell-hooks
description: "Shell hooks: pre_tool_call block/audit patterns for agents."
version: 1.0.0
author: tailored-skills
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [hermes, hooks, pre_tool_call, security, observability, shell]
    related_skills: [hermes-profile-layout, hermes-agent, native-mcp]
---

# Agent shell hooks (pre/post tool call)

## Overview

Shell hooks are subprocess programs that run around tool or LLM calls. They
receive JSON on stdin and emit JSON on stdout. Use them to **block dangerous
commands**, **inject ambient context**, or **audit** tool use — without growing
the model prompt or relying on the model to refuse.

This skill is harness-agnostic in spirit; examples use Hermes config keys.
Other agents (Claude Code PreToolUse, etc.) share the same idea: matcher +
command + allow/block decision.

## Three mechanisms (do not conflate)

| Mechanism | Where | Role |
|-----------|-------|------|
| **Shell hooks** | `${HERMES_HOME:-$HOME/.hermes}/agent-hooks/*.sh` + `hooks:` in config | Block / inject / audit via subprocess |
| **Gateway hooks** | `${HERMES_HOME:-$HOME/.hermes}/hooks/<name>/` (`HOOK.yaml` + `handler.py`) | Gateway lifecycle observability; usually cannot block tools |
| **Plugins** | profile `plugins/` | In-process agent behavior changes |

Prefer shell hooks for terminal safety and audit. Prefer gateway hooks for
startup/shutdown messaging. Prefer plugins when you must replace agent logic.

## Config shape (Hermes)

In `${HERMES_HOME:-$HOME/.hermes}/config.yaml` or a profile `config.yaml`:

```yaml
hooks:
  pre_tool_call:
    - matcher: "terminal"
      command: "${HERMES_HOME:-$HOME/.hermes}/agent-hooks/block-rm-rf.sh"
      timeout: 5
  post_tool_call:
    - matcher: "terminal"
      command: "${HERMES_HOME:-$HOME/.hermes}/agent-hooks/audit-terminal.sh"
      timeout: 10
  pre_llm_call:
    - command: "${HERMES_HOME:-$HOME/.hermes}/agent-hooks/prepend-today.sh"
      timeout: 5
```

Use env-expanded or absolute paths under `$HERMES_HOME`. Do not hardcode
`/home/<user>/...`.

## Wire protocol (shell hooks)

**Input (stdin):** JSON object including at least:

- `tool_name` — e.g. `terminal`
- `tool_input` — tool arguments (e.g. `{ "command": "..." }`)
- `session_id` — optional correlation id

**Output (stdout):**

| Intent | Example |
|--------|---------|
| Allow / no-op | `{}` |
| Block | `{"action":"block","message":"reason for the user/agent"}` |
| Inject context (`pre_llm_call`) | `{"context":"Today is …"}` |

Keep scripts **predictable**: same trigger → same effect. Fail open or fail
closed deliberately — document which. A crashing hook must not take down the
agent process (trap errors; emit `{}` or an explicit block).

## Pattern catalog

### 1. Block destructive terminal commands (`pre_tool_call`)

- Match `tool_name == terminal`
- Inspect `tool_input.command` for high-risk patterns (`rm -rf` on `/`, `$HOME`,
  `--no-preserve-root`, etc.)
- On match: emit `action: block` with a clear remediation message
- On safe: emit `{}`

### 2. Audit log (`post_tool_call`)

- Append one JSONL line to `${HERMES_HOME:-$HOME/.hermes}/logs/<name>.jsonl`
- Never block; never log secrets (redact token-shaped strings if present)
- Include `ts`, `session_id`, `tool_name`

### 3. Ambient context injector (`pre_llm_call`)

- Emit low-rate facts (UTC date, git branch, `$PROJECT_ROOT`) via `context`
- Do **not** dump large files — that belongs in rules/skills loading
- Avoid mutating the **system** prompt mid-session (cache discipline)

## Authoring rules

1. Observers by default; only pre-tool / pre-verify hooks should block.
2. No personal paths in committed hook samples — use `$HERMES_HOME` /
   `$PROJECT_ROOT`.
3. Timeouts stay small (seconds). Hooks run on the hot path.
4. Side effects go through documented APIs or local logs — not ad-hoc network
   calls from the hook unless that is the product feature.
5. Gateway hooks: failing handler must not break gateway startup; return
   empty ack when idle.

## Gateway hook package layout

```
${HERMES_HOME:-$HOME/.hermes}/hooks/<name>/
├── HOOK.yaml    # event + config schema
└── handler.py   # hook(event, config, **kwargs)
```

Typical events: `gateway:startup`, `gateway:shutdown`, `agent:start`,
`agent:stop`, `message:incoming`, `message:outgoing`.

## Verification checklist

- [ ] Hook path resolves under `$HERMES_HOME` or the active profile
- [ ] `pre_tool_call` blocker covered by a safe and an unsafe dry-run payload
- [ ] Audit path is mode-safe and outside the git repo (or gitignored)
- [ ] No tokens or home directories in hook source committed to a public tree
