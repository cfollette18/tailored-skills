---
name: frontend-motion-system
description: Establish reusable motion roles, timing tokens, easing, and interruption rules for an existing frontend. Use when building or consolidating product-wide animation behavior; adapt to the current stack and brand rather than prescribing a visual redesign.
---

# Frontend motion system

Inspect existing motion, routing, state ownership, reduced-motion handling, and installed libraries. Build on that system. For a few transitions, CSS or the Web Animations API may be sufficient; use an existing motion library when it solves real orchestration or layout problems.

## Specify roles before durations

Separate immediate input feedback, selection continuity, entering/leaving surfaces, optional icon expression, and genuine ongoing progress. Each needs a trigger, affected properties, end state, cancellation policy, and static alternative. Components should consume named roles instead of unrelated timing literals.

Use these as initial tuning ranges, not universal limits or measurements from a reference:

| Role | Starting duration | Notes |
|---|---|---|
| Press, hover surface | 80–140 ms | State recognition starts immediately |
| Selection indicator | 150–220 ms | Retarget from the current position |
| Popover or small panel | 140–220 ms | Origin follows the actual trigger |
| Drawer or sidebar | 200–280 ms | Keep the rest of the page stable |
| Optional icon gesture | 350–700 ms | Only when desired; never gates navigation |
| Page switch | Instant or 100–160 ms opacity | Avoid repeated entrance choreography |

For a calm product UI, a starting entrance curve is `cubic-bezier(.22,1,.36,1)`; an on-screen movement may benefit from a balanced ease-in-out. Color hover can use `ease`. These are proposed tokens. Do not attribute them to Muse or another reference without measurement or source evidence.

Read [implementation choices](references/implementation-choices.md) when deciding between CSS, WAAPI, a spring, shared layout, and authored vector animation.

## Preserve continuity and state

Update application state independently of animation completion. Retarget or cancel outdated animations; do not queue them. A completion callback must not restore an obsolete tab or reopen a dismissed surface. Register and clean up animations, observers, timers, and event handlers with component lifetime.

Keep the product's existing icons and theme. Prefer separate layers for moving indicators and stable text. Avoid `transition: all`, blanket layout animation, per-frame React state, and permanent `will-change` on every element. Treat SVG line drawing and measured layout changes as scoped exceptions to a transform/opacity preference, then profile them.

Respect reduced motion in CSS and JavaScript, including one-shot icon engines. An already-running animation must settle to a coherent state when the preference changes. Keep semantic state, labels, and focus visible without motion.

## Verify the system

Build/typecheck where relevant, then inspect representative interactions at actual size. Exercise reversal, rapid repeat input, keyboard focus, touch, reduced motion, and unmount. Profile the dense screen the user actually works in. Report the implemented roles and tested behavior rather than promising a universal frame rate.
