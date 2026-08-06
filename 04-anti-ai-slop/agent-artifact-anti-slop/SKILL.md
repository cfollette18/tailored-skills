---
name: agent-artifact-anti-slop
description: Keep agent-produced skills, plans, commits, and handoffs concise, actionable, and free of template bloat. Use when artifacts feel copy-pasted or over-scoped.
version: 1.0.0
author: tailored-skills
license: MIT
metadata:
  hermes:
    tags: [agents, planning, skills, anti-slop, workflow]
---

# Agent Artifact Anti-Slop

Use when agents produce **bloated plans**, **generic skills**, **novel-length commits**, or **handoff docs** that repeat context without enabling action.

## Slop tells in agent artifacts

### Skills (SKILL.md)
- Frontmatter missing `name` / `description`
- 500 lines restating obvious agent behavior
- No triggers — skill applies to everything
- Duplicates existing skill with different wording
- Hard-coded machine paths (`/home/user/...`)

### Plans
- 40 steps for a 3-file change
- "Investigate" without concrete files/commands
- Risks section listing generic concerns ("may break tests")
- Re-states entire codebase context
- No validation / acceptance criteria

### Commits
- Subject: "Update files" / "Fix issue" / "WIP"
- Body narrates every file touched without **why**
- Multiple unrelated changes bundled

### Handoffs
- "The previous agent did X" without actionable state
- Missing: current branch, failing tests, exact next command
- Copy of entire chat log

## Checklists

### Skill quality
- [ ] Description says **when** to load (triggers), not what agent already knows
- [ ] ≤200 lines unless domain requires references/templates
- [ ] Uses `$PROJECT_ROOT`, `${HERMES_HOME}`, not personal paths
- [ ] One primary job; links to related skills instead of duplicating
- [ ] Examples are **project-shaped**, not lorem ipsum

### Plan quality
- [ ] Goal in one sentence
- [ ] Steps name **files** and **commands**
- [ ] Validation section: how to know done
- [ ] Open questions listed explicitly (not buried)
- [ ] Scope matches user request — no "while we're here"

### Commit quality
- [ ] Subject: imperative, ≤72 chars, states **why** not **what**
- [ ] Body: context only if non-obvious
- [ ] One logical change per commit

### Handoff quality
- [ ] Current state: branch, test status, blockers
- [ ] Next 1–3 actions with exact commands
- [ ] Links to plan file or issue — not chat recap

## Before / after

### Plan step

**Before:**
> 3. Investigate the authentication module and determine the best approach for implementing the requested changes while ensuring compatibility.

**After:**
> 3. Add `rotateRefreshToken()` in `src/auth/tokens.ts`; call from `POST /api/auth/refresh` handler. Test: `npm test auth.test.ts`.

### Skill description

**Before:**
> Comprehensive skill for helping with all aspects of software development including planning, coding, testing, and deployment in a holistic manner.

**After:**
> Write markdown plans to `.hermes/plans/`; no execution. Use when user asks for a plan instead of implementation.

### Commit message

**Before:**
```
Update auth files

- Modified tokens.ts
- Modified refresh route
- Added tests
```

**After:**
```
Rotate refresh tokens on each use

Prevents replay of stolen refresh tokens. Invalidates
old token in DB and sets new HttpOnly cookie.
```

## Portability conventions (this repo)

- `$PROJECT_ROOT` — active workspace root
- `${HERMES_HOME:-$HOME/.hermes}` — Hermes config/skills home
- `$FRONTEND_PROJECT_ROOT` — frontend app subpath when monorepo
- Never commit secrets; reference env var **names** only

## References

- `07-software-development/plan` — plan-mode constraints
- `07-software-development/hermes-agent-skill-authoring` — skill format
- `07-software-development/writing-plans` — plan structure
