---
name: code-anti-slop
description: Prevent over-abstraction, defensive boilerplate, narrating comments, and inconsistent patterns in agent-generated code. Use during review or before merge.
version: 1.0.0
author: tailored-skills
license: MIT
metadata:
  hermes:
    tags: [code-quality, review, anti-slop, refactoring]
    related_skills: [simplify-code]
---

# Code Anti-Slop

Use when diffs look **LLM-shaped**: unnecessary wrappers, comments that narrate the obvious, duplicate utilities, or architecture that doesn't match the repo.

Adapted from vera `simplify-code` reviewer patterns and common agent failure modes.

## Slop tells in code

| Pattern | Example | Fix |
|---------|---------|-----|
| Narrating comments | `// increment counter` above `count++` | Delete comment |
| Defensive null checks | `if (user && user.id)` after validated input | Trust types/guards |
| `as any` escape hatches | Bypassing errors instead of fixing types | Narrow types properly |
| One-use abstractions | `HelperUtils.processData()` called once | Inline |
| Mirror hierarchies | Interface + abstract class + impl for 3 methods | Flatten |
| Try/catch swallow | `.catch(() => {})`, empty except | Log or propagate |
| Config explosion | 12 new env vars for one feature | Reuse existing config |
| Inconsistent style | New file ignores repo conventions | Match surrounding code |

## Checklist before merge

- [ ] **Scope minimal** — Diff solves stated problem only
- [ ] **Reuse first** — Existing utils/functions used before new ones
- [ ] **Names match domain** — Project terminology, not generic `Manager`/`Handler`/`Service` unless repo uses them
- [ ] **Comments explain why** — Not what the code obviously does
- [ ] **Error paths real** — No silent failures on hot paths
- [ ] **Tests meaningful** — Assert behavior, not implementation trivia
- [ ] **No drive-by refactors** — Unrelated cleanup in separate commit

## Before / after

### Over-abstraction

**Before (slop):**
```typescript
class DataProcessorFactory {
  createProcessor(type: string): IDataProcessor {
    return new GenericDataProcessor(type);
  }
}
// used once
const processor = new DataProcessorFactory().createProcessor("json");
processor.process(data);
```

**After:**
```typescript
processJson(data);
```

### Narrating comments

**Before:**
```python
# Loop through users
for user in users:
    # Check if user is active
    if user.active:
        # Send email to user
        send_email(user)
```

**After:**
```python
for user in users:
    if user.active:
        send_email(user)
```

### Defensive slop

**Before:**
```typescript
function getName(user: User | null | undefined): string {
  if (!user) return "";
  if (!user.profile) return "";
  if (!user.profile.name) return "";
  return user.profile.name;
}
// caller already validated user
```

**After:**
```typescript
function getName(user: User): string {
  return user.profile.name;
}
```

## Review pass (5 minutes)

1. **Altitude check** — Is this the simplest structure that works?
2. **Duplication scan** — `git grep` for similar logic added elsewhere
3. **Comment audit** — Delete every comment that restates the next line
4. **Type audit** — Remove `any` / `@ts-ignore` introduced in diff
5. **Convention audit** — Imports, naming, error handling match file neighbors

## When abstraction is warranted

- Logic reused **≥2 times** with same contract
- Boundary crossing (API layer, external SDK) needs isolation
- Test requires seam — but prefer testing public behavior

## References

- `01-software-development/simplify-code` (multi-reviewer slop patterns)
- [Code quality PR study](https://smoothui.dev/blog/ai-design-slop) (AI PRs: 1.7× issues cited in UI slop literature)
- YAGNI / minimal diff principles
