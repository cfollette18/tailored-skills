---
name: portable-harness-authoring
description: "Write portable harness skills/rules: no personal paths."
version: 1.0.0
author: tailored-skills
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [portability, open-source, skills, rules, harness]
    related_skills: [hermes-agent-skill-authoring, hermes-profile-layout, context-loading]
---

# Portable, agnostic harness authoring

## Overview

An open-source agent harness must work for a stranger who clones the repo —
not only for one developer's laptop. Apply this skill whenever you add or
edit skills, rules, learnings, fixes, hooks, or plans at profile or repo level.

## Placeholders (use these)

| Placeholder | Meaning |
|-------------|---------|
| `$PROJECT_ROOT` | Active workspace / project root |
| `${HERMES_HOME:-$HOME/.hermes}` | Hermes user config and skills home |
| `$HERMES_AGENT_ROOT` | Checkout of the Hermes agent source (if contributing upstream) |
| `$PROJECT_ENV_FILE` | Project env file path (never commit secrets) |
| `$EDGE_HOST` | Remote training/inference host **as an env var**, not a hostname literal |
| `$FRONTEND_PROJECT_ROOT` | Frontend app path in a monorepo |

## Skills

1. **Project-agnostic by default.** Teach procedures without assuming a repo
   name, hostname, or hardware nickname.
2. **Examples use placeholders**, not private codenames.
   - Good: "your project at `$PROJECT_ROOT`"
   - Bad: hard-coded `/home/<user>/...` paths or internal host aliases
3. **Hardware class is OK; nicknames are not.** "Jetson Orin Nano class,
   ~8 GB unified" is portable. A personal hostname is not.
4. **Split portable vs project-local knowledge:**

| Portable (skill / profile rule) | Project-local (repo `.hermes/` or `AGENTS.md`) |
|---------------------------------|-----------------------------------------------|
| How to design an eval rubric | This project's rubric JSON + frozen test SHA |
| QLoRA VRAM estimation | This run's exact checkpoint path |
| Generic teacher-API quirks | Which provider this project uses today |

5. Before saving a skill, ask: "Would this still make sense if every path and
   project name were `$PROJECT_ROOT`?" If not, generalize or move the
   specific part to the project's `.hermes/learnings/`.

## Rules, learnings, fixes

- Same bar as skills: no usernames, home directories, or one-off cron IDs.
- Learnings capture **patterns**, not session state.
- Fixes capture **failure modes**, not one user's incident timestamps.

## Secrets

- Never hardcode API keys, tokens, or session secrets.
- Never persist a chat-pasted token into repo files, skills, or memories.
- Document **login commands** and env var **names**; use placeholders like
  `hf_xxxxxxxxxxxx` in examples.
- Prefer OS keychains / CLI credential caches (`hf auth login`, `gh auth login`).

## Naming

- Prefer generic names: `edge-qlora-pipeline`, `training-studio-api`,
  `eval-rubric-design`.
- If tied to one external tool, name the **tool**, not a private deployment.

## Review checklist (before merging harness content)

- [ ] No `/home/<user>/` paths
- [ ] No real hostnames, IPs, or cron UUIDs
- [ ] No API keys or token-shaped strings (except documented placeholders)
- [ ] Env vars documented; values never inlined
- [ ] Readable by someone who never saw your machines
- [ ] Project-specific numbers live under `$PROJECT_ROOT`, not the profile skill
