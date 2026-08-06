# rules/ — portable agent rules

Numbered category directories hold **project-agnostic** `.mdc` rule files. Copy subsets into your agent profile or project without editing paths or codenames.

## Loading rules

### Hermes

Rules merge from several scopes (project wins over profile for conflicting rules):

| Scope | Path |
|-------|------|
| Project | `<cwd>/.hermes/rules/*.mdc` |
| Profile | `~/.hermes/profiles/<profile-name>/rules/*.mdc` |
| User (legacy) | `~/.hermes/rules/*.mdc` |

Within each directory, files load in natural sort order. Use zero-padded prefixes on **category directories** (`01-`, `02-`, …) so related rules stay grouped when you copy a whole folder.

### Cursor

Copy chosen `.mdc` files into `.cursor/rules/` at the repo root (or your global Cursor rules directory). Cursor reads frontmatter (`description`, `alwaysApply`, `globs`) from each file.

## Category map

| Dir | Purpose |
|-----|---------|
| `01-security-and-secrets/` | Never hardcode secrets, tokens, or machine-specific paths |
| `02-portability/` | Skills, rules, and docs must work for any clone |
| `03-research-workflow/` | Reproducible research and ML discipline |
| `04-anti-ai-slop/` | Ban generic output patterns in code, UI, and prose |
| `05-ui-craft/` | Agnostic UI quality — composition, type, spacing |
| `06-agent-discipline/` | Long-session agent hygiene (cache, context, hooks) |

## Copying subsets into a profile

```bash
# Example: copy security + portability into a Hermes profile
PROFILE=default
mkdir -p ~/.hermes/profiles/$PROFILE/rules
cp rules/01-security-and-secrets/*.mdc ~/.hermes/profiles/$PROFILE/rules/
cp rules/02-portability/*.mdc ~/.hermes/profiles/$PROFILE/rules/

# Example: copy anti-slop + UI craft into a Cursor project
mkdir -p .cursor/rules
cp rules/04-anti-ai-slop/*.mdc .cursor/rules/
cp rules/05-ui-craft/*.mdc .cursor/rules/
```

Edit frontmatter `appliesTo` if you scope rules to a named profile.

## File format

```markdown
---
description: One-line trigger (keep short)
appliesTo: optional scope (e.g. all-sessions, default-profile)
alwaysApply: true
---

# Title

Action-shaped body in markdown.
```

Project-local rules belong in `<project>/.hermes/rules/` (Hermes) or `.cursor/rules/` (Cursor) — not in this repo.
