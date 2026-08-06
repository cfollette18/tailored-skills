---
name: hermes-profile-layout
description: "Hermes harness layout: rules, learnings, fixes, skills, hooks."
version: 1.0.0
author: tailored-skills
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, profile, harness, rules, learnings, fixes, layout]
    related_skills: [context-loading, agent-shell-hooks, portable-harness-authoring, hermes-agent]
---

# Hermes profile / harness layout

## Overview

Hermes separates **portable harness knowledge** (rules, learnings, fixes, skills,
hooks) from **session memory**. The same directory shape works at user scope
(`${HERMES_HOME:-$HOME/.hermes}`), profile scope
(`${HERMES_HOME:-$HOME/.hermes}/profiles/<name>/`), and project scope
(`$PROJECT_ROOT/.hermes/`).

Use this skill when creating or explaining an agent harness, importing a
profile, or deciding where a new rule/skill/learning belongs.

## Canonical layout

```
${HERMES_HOME:-$HOME/.hermes}/
├── rules/           *.mdc   — persistent rules (system-prompt prefix)
├── learnings/       *.md    — teachable patterns (additive)
├── fixes/           *.md    — known failure-mode corrections (additive)
├── hooks/           <name>/ — gateway hook packages (HOOK.yaml + handler.py)
├── agent-hooks/     *.sh    — shell hooks referenced from config.yaml
├── mcp/                     — MCP server definitions / templates
├── skills/                  — user-local skills
├── memories/                — durable facts (auto-injected; not credentials)
├── plans/           *.md    — persistent run / refactor plans
└── profiles/<name>/         — same layout scoped to one profile
    ├── rules/, learnings/, fixes/, hooks/, mcp/, plans/, skills/
    └── config.yaml          — profile config (hooks:, mcp_servers:, …)

$PROJECT_ROOT/.hermes/       — project-local overlay of the same slots
$PROJECT_ROOT/.hermesrules   — single-file project rules (Hermes)
$PROJECT_ROOT/AGENTS.md      — project briefing (many loaders)
$PROJECT_ROOT/SOUL.md        — optional identity / operating principles
```

## How loading merges (conceptual)

| Slot | Sources (high → low priority for first-wins) | Merge |
|------|-----------------------------------------------|-------|
| Rules / project context | `$PROJECT_ROOT/.hermes/rules/*.mdc`, `.hermesrules`, active profile, `${HERMES_HOME}/rules/` | First-wins for conflicting project context |
| Learnings | project → profile → user `learnings/` | Always additive |
| Fixes | project → profile → user `fixes/` | Always additive |
| Skills | profile import, `${HERMES_HOME}/skills/`, project skills dirs | Indexed by description; body on demand |

Exact loader priority may vary by Hermes version; treat project-local as
highest specificity and keep user-level content portable.

## What belongs where

| Write to… | When |
|-----------|------|
| `rules/` | Always-on behavior ("preserve the prompt cache", "no secrets in repo") |
| `learnings/` | Patterns discovered in the field you want next session |
| `fixes/` | Failure modes you already burned on |
| `skills/` | Multi-step procedures the agent should load on trigger |
| `hooks/` / `agent-hooks/` | Enforcement and observability outside the model loop |
| `AGENTS.md` / project `.hermes/` | Repo-specific paths, rubrics, frozen SHAs, local conventions |
| `memories/` | Stable user preferences — **never** tokens or keys |

## File formats

**Rules (`.mdc`)** — Markdown + optional YAML frontmatter (Cursor-compatible):

```markdown
---
description: one-line trigger — keep under 57 chars
appliesTo: optional-scope
alwaysApply: true
---

# Title

Action-shaped body. Concrete. Checkable.
```

**Learnings / fixes** — plain `.md`. Lead with a one-sentence summary for indexing.

**Naming** — zero-padded prefixes (`00-`, `01-`, …) so load order is explicit.

## Profile import

Ship a profile as a directory with `profile.yaml` plus `rules/`, `skills/`,
`hooks/`, etc., then:

```bash
hermes profile import /path/to/profile-or-skills-tree
```

Or symlink categories into `${HERMES_HOME:-$HOME/.hermes}/skills/`.

## Common pitfalls

1. Putting project-specific checkpoint paths in profile `skills/` — use
   `$PROJECT_ROOT` or project `.hermes/learnings/` instead.
2. Writing credentials into `memories/` or `rules/` — use CLI auth caches
   and env vars (see security skill `credential-tokens-never-in-config`).
3. Mutating rules mid-conversation — invalidates the prompt cache; wait for
   `/reset` or a new session (see `prompt-cache-session-discipline`).
4. Confusing **gateway hooks** (`hooks/<name>/`) with **shell hooks**
   (`agent-hooks/*.sh` via `hooks:` in config) — see `agent-shell-hooks`.

## Verification checklist

- [ ] Layout matches rules / learnings / fixes / skills / hooks separation
- [ ] No personal home paths; placeholders only (`$PROJECT_ROOT`, `$HERMES_HOME`)
- [ ] New always-on guidance is a rule; multi-step workflow is a skill
- [ ] Profile import or symlink path documented for consumers
