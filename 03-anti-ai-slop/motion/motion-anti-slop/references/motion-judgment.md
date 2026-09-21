# Motion judgment

“AI slop” is an informal critique, not a measurable animation technology. Evaluate a concrete failure: unmotivated repetition, mismatched tone, delayed work, weak geometry, inaccessible motion, or an incoherent combination of effects.

## Choose against the actual task

| Situation | Useful choice | Common mistake |
|---|---|---|
| Repeated sidebar navigation | Immediate state, anchored labels, optional one-shot icon character | Replaying the full page entrance every click |
| Inspecting a financial value | Exact value and cursor feedback immediately | Springing a value behind the pointer |
| Drawer from a known edge | Short directional movement that preserves its origin | Scaling the entire application or moving from an unrelated edge |
| A rare celebratory action | A bounded expressive gesture if the brand supports it | Making the same flourish mandatory for routine saves |
| Hovering across a dense list | Stable hit targets, quiet surface feedback | Moving the hovered element away from the pointer |
| Known loading work | Honest status text with optional motion | Endless idle pulse that implies background work |

These are design recommendations, not measured laws.

## Evidence behind the recommendations

[Nielsen Norman Group](https://www.nngroup.com/articles/animation-purpose-ux/) frames motion as feedback, state communication, navigation continuity, and signification. Attention is a limited resource; motion can also distract from the task.

[Emil Kowalski on frequency](https://emilkowal.ski/ui/you-dont-need-animations) explains why a rare flourish may be enjoyable while repeated functional navigation should feel immediate. Apply that reasoning to the user's workflow rather than copying a blanket prohibition.

[Carbon](https://carbondesignsystem.com/elements/motion/overview/) separates productive and expressive motion. Its duration scale includes 70, 110, 150, 240, 400, and 700 ms for different purposes. This is a design-system example, not a timing standard for every application.

## Resolve apparent contradictions

- **“Keep it under 300 ms” versus Muse's longer icons:** keep feedback and navigation short; allow a bounded, nonblocking gesture inside an icon when explicitly desired.
- **“Never bounce” versus a characterful checkbox:** a small authored settle can suit the icon; a generic elastic spring on every control usually does not.
- **“Prefer opacity and transforms” versus a drawn check:** localized SVG drawing can be appropriate. Inspect paint and frame cost; a small repaint is not equivalent to a full-screen blur.
- **“Use a spring” versus exact matching:** a spring is an implementation choice. A recording does not reveal stiffness or damping uniquely. Match the visible trajectory and interruption behavior.
- **“Avoid stagger” versus sequential dots:** ordering meaningful subparts is different from delaying every row or paragraph.
- **“Blur makes it polished”:** first fix timing, geometry, and continuity. Blur is an optional small-surface treatment, not a default cover for poor transitions.

Checked against primary sources on 2026-09-21. Keep product examples contextual when transferring this guidance.
