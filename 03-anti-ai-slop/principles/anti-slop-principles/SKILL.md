---
name: anti-slop-principles
description: Consolidated guardrails against generic AI output in UI, writing, code, and agent artifacts. Use before shipping or when output feels templated, hedgy, or interchangeable.
version: 1.0.0
author: tailored-skills
license: MIT
metadata:
  hermes:
    tags: [quality, craft, anti-slop, review, taste]
    related_skills: [design-anti-slop, writing-anti-slop, code-anti-slop, agent-artifact-anti-slop]
---

# Anti-Slop Principles

Use this skill when output feels **generic, interchangeable, or "AI-made"** — before shipping UI, prose, code, or agent artifacts (skills, plans, commits).

## Core idea

AI defaults to the **statistical center** of its training data: safe fonts, purple gradients, three-card grids, hedged copy, over-abstracted code, and bloated plans. Slop is not one mistake — it is **convergence on defaults** when constraints are missing.

**Fix upstream:** supply concrete constraints *before* generation. Editing slop afterward fights the model's defaults compound-by-compound.

Sources: [What is AI slop?](https://uxskill.laithjunaidy.com/what-is-ai-slop.html), [Why AI Design Looks Generic](https://superdesign.dev/blog/why-ai-design-looks-generic), [SmoothUI anti-slop loop](https://smoothui.dev/blog/ai-design-slop), [Rottoways fix guide](https://rottoways.com/blog/fix-ai-slop-website).

---

## Universal checklist (all domains)

Before accepting output, verify:

- [ ] **Specificity** — Names real features, files, metrics, or user actions; no placeholder uplift.
- [ ] **Constraint trace** — Decisions tie to stated brand, audience, stack, or acceptance criteria.
- [ ] **Restraint** — Fewer elements, fewer adjectives, fewer abstractions than first draft.
- [ ] **Asymmetry / variance** — Not every section uses the same template rhythm.
- [ ] **Evidence** — Claims backed by repo state, design tokens, tests, or cited sources.
- [ ] **Second pass** — One dedicated critique pass with an explicit "anti-slop" bar.

### Build → critique → fix loop

1. Generate with explicit **avoid list** and **acceptance bar**.
2. Critique against domain checklist below.
3. Fix the **highest-impact** slop tell first.
4. Re-check; stop when bar passes or budget is hit.

---

## Domain routing

| Domain | Skill | When |
|--------|-------|------|
| UI / design | `design-anti-slop` | Landing pages, dashboards, components, motion |
| Writing | `writing-anti-slop` | Docs, marketing, PR descriptions, agent replies |
| Code | `code-anti-slop` | Refactors, new modules, agent-generated diffs |
| Agent artifacts | `agent-artifact-anti-slop` | Skills, plans, commits, handoff docs |

Load the smallest relevant sub-skill; do not paste all checklists into context unless auditing end-to-end.

---

## Slop tells (cross-domain)

| Tell | Design | Writing | Code | Artifacts |
|------|--------|---------|------|-----------|
| Default aesthetic | Purple gradient, Inter, 3 cards | "Leverage", "delve", "robust" | Wrapper helpers, `as any` | 47-step plans |
| Symmetry obsession | Centered hero, identical cards | Parallel bullet chains | Mirror class hierarchies | Every section same depth |
| Missing edge cases | No empty/error/focus states | No failure modes | Swallowed errors | No validation step |
| Unearned confidence | "Modern", "seamless" | "Simply", "just" | Premature abstraction | "Comprehensive" scope |

---

## Before/after (meta)

**Before (slop):**
> I'll create a comprehensive, robust solution leveraging best practices to seamlessly improve the user experience with a modern, polished interface.

**After (specific):**
> Add a 404 state to `SettingsPanel` when the API returns empty teams; match existing `EmptyState` spacing (24px) and reuse `Button` variant `secondary`.

---

## Integration with UI skills

For interface work, pair this quality bar with the relevant frontend implementation skill in `01-software-development/frontend/` or the target product’s own component guidance.
