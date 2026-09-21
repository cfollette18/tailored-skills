---
name: motion-quality-review
description: Audit existing interface motion for generic effects, visual discontinuity, repetition, misleading status, and delayed interaction. Use when reviewing animation quality or comparing an implementation with a reference, rather than introducing a new motion system.
---

# Motion quality review

Review behavior before changing style. Identify the user task, the reference if supplied, and the motions actually encountered. An animation can be technically smooth yet wrong for a frequently repeated workflow.

## Inspect three speeds and two usage patterns

Watch once at normal speed, inspect slow motion for discontinuities, then repeat at normal speed. Exercise both deliberate use and rapid interruption: hover across several rows, reverse a drawer, choose a third tab before the second settles, and navigate by keyboard and touch.

Classify findings by consequence:

- **Functional:** delayed input, wrong final state, lost focus, hidden controls still focusable, stale completion callback, accidental repeat action.
- **Motion quality:** glyph jump at handoff, distorted text, shifted click target, clipping, unearned overshoot, unrelated effects happening together.
- **Preference/performance:** motion continues with reduced motion enabled, repeated background loops, expensive rendering or visible frame drops.
- **Reference fidelity:** wrong moving part, wrong order, wrong resting state, or a claimed exact duration unsupported by evidence.

## Check the choreography

Separate the animation of the surface, indicator, glyph, text, and page. Check that their order is intentional and that a slower decorative layer does not block functional response. A shared moving selection background should not also move each row's label. Verify text remains legible throughout selection, especially across dark and light surfaces.

Icon animation should preserve the surrounding box and end in the expected silhouette. Inspect pointer exit during motion, reentry, a click while hovered, and page unmount. Hover plus click should not play the same flourish twice. Long hover should not create an unintended infinite loop.

For reference matching, use timestamped frames and label confidence. “Looks like a page turning” is an observation; “uses rotateX” is an implementation hypothesis unless source inspection confirms it. Treat product-specific source code as evidence for the inspected component, not every component in that product.

## Report useful findings

For each material finding provide the affected file/component or recording interval, the observed behavior, its consequence, and the smallest repair. Prioritize correctness and responsiveness before aesthetic preferences. Avoid an arbitrary numeric taste score.

Validate the repair through the same interaction that revealed the problem. A final screenshot or passing build does not verify motion. Record any missing browser, touch, reference, or assistive-technology coverage. When the task is review-only, deliver findings without silently rewriting the app.

Primary references: [NN/g](https://www.nngroup.com/articles/animation-purpose-ux/), [Good vs Great Animations](https://emilkowal.ski/ui/good-vs-great-animations), [web.dev rendering guidance](https://web.dev/articles/animations-guide), and [W3C interaction animation](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html). Provenance is in `SOURCE.json`.
