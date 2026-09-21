---
name: motion-anti-slop
description: Choose purposeful animation and remove generic motion patterns when an interface feels overanimated, templated, or disconnected from its brand. Use for motion direction and anti-slop redesign; preserve explicitly requested expressive references.
---

# Motion anti-slop

Give each movement a reason tied to the interaction: acknowledgement, state, spatial continuity, or a deliberately chosen moment of character. Preserve the owner's preferred aesthetic. Restraint does not mean deleting expressive icons the owner specifically likes.

## Diagnose the mismatch

Inspect the interface in motion, at normal speed, through a repeated task. Still screenshots cannot establish easing, timing, interruption, or hover behavior. Distinguish what you observed, what source code confirms, and what you recommend.

Common problems include identical bounce on unrelated icons, every card lifting on hover, repeated page-entry staggers, idle navigation pulsing, enormous entrance offsets, slow opacity ramps over useful text, and animation that delays the action. Treat these as contextual findings, not an aesthetic blacklist: a marketing sequence and an analyst's daily navigation have different needs.

For each proposed change, name the trigger, moving part, semantic purpose, stable part, completion state, interruption behavior, and reduced-motion alternative. Delete or simplify motion whose explanation is only “it looks premium.”

## Separate response from expression

Selection, focus, and content availability should respond immediately. A small decorative icon gesture may continue after the action is accepted. Do not turn “keep interface transitions short” into a universal 300 ms cap on authored icon timelines, or turn a 650 ms icon reference into a 650 ms navigation delay.

The owner's Muse reference demonstrates this distinction: a stationary rail contains different internal gestures for chat, search, feed, ideas, goals, and library. The local shapes change while their click targets stay still. Apply the principle to the product's existing icon family and domain; do not replace every symbol with Muse's symbols. The detailed observation is in the sibling frontend skill's [Muse study](../../01-ui-design/animated-interface-icons/references/muse-sidebar-study.md) when the full collection is available. This skill remains usable on its own.

## Make the smallest expressive choice

- Animate an icon's meaningful part: check, page, lens, line, connector, or internal dots. Keep the surrounding label and row anchored.
- Use one coherent movement per interaction. Stagger parts only when their order conveys the gesture; avoid adding delays to every item in a list.
- Avoid perpetual motion in idle navigation. Loading and real progress need their own explicit status semantics.
- Keep a clear resting silhouette. Repeated hover should not leave a half-drawn glyph or accumulated transforms.
- Preserve the product's palette, typography, icon weights, and density. An animation reference is not permission for a full rebrand.
- Make frequent keyboard navigation immediate. Touch must work without first revealing a hover state.

## Deliver

Show the existing behavior and proposed behavior at the same size and normal speed. Use slow playback only to diagnose mechanics. Report the few changes that materially improve the interaction, with evidence and remaining uncertainties. Do not add dependencies, redesign unrelated pages, or publish anything merely because this skill is invoked.

Read [motion judgment](references/motion-judgment.md) when choosing between expressive and quiet variants or reviewing contradictory motion advice. Provenance is in `SOURCE.json`.
