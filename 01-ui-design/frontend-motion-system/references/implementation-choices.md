# Implementation choices

| Tool | Good fit | Constraint |
|---|---|---|
| CSS transitions | Hover surfaces, simple two-state transforms, quiet selection | Preserve interruption by changing the target, not remounting the element |
| CSS keyframes | Known one-shot glyph gesture | Explicitly manage retriggering and reduced motion |
| Web Animations API | Small timelines, playback controls, cancellation | Retain animation handles and clean them up; canceled `finished` promises reject |
| Motion for React | Shared selection, layout continuity, component enter/exit | Use the installed version's API; avoid wrapping the whole app in layout animation |
| Lottie | Authored multishape vector sequences | Lazy-load if warranted, keep a static fallback, manage frame/segment playback |
| Native View Transition API | Snapshot transitions where browser support and interaction semantics fit | Feature-detect and verify focus, navigation, and rapid updates; it is not a universal drop-in for live component animation |

CSS and WAAPI can coexist with React without setting component state on every frame. Keep authoritative selection in application state, and let the animation layer interpolate presentation.

For a WAAPI reversal, `reverse()` changes playback direction on the current animation. For arbitrary new targets, capture the current visual value before cancellation or use an interpolator that retargets. Never assume canceling alone commits an intermediate style. Catch cancellation rejections when awaiting `finished`, and prevent stale promise handlers from changing current state. [MDN reverse](https://developer.mozilla.org/en-US/docs/Web/API/Animation/reverse), [MDN WAAPI](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API).

Motion's `layout` animates layout changes; `layoutId` connects matching elements across states. It uses transforms, which can distort child text unless the structure accounts for that. Keep a moving selection layer separate from the label whenever possible. Use a scoped layout group to avoid unrelated matching IDs. [Motion layout](https://motion.dev/docs/react-layout-animations).

Springs are not a duration in disguise. Stiffness, damping, mass, distance, velocity, and termination thresholds affect settling. A highly damped spring can work for a selection indicator; tune visually under interruption. If consistent elapsed time is required, a tween may be the clearer choice. [Motion transitions](https://motion.dev/docs/react-transitions).

`MotionConfig reducedMotion="user"` handles transform/layout reduction, but other animated properties can remain. Custom SVG drawing, Lottie, CSS, and WAAPI need their own policy. [Motion accessibility](https://motion.dev/docs/react-accessibility).

Favor transform and opacity for large moving surfaces; rendering cost depends on the affected area and actual paint/composition path. A width transition or tiny SVG repaint is not automatically unacceptable, but it needs inspection on realistic content. Do not claim “GPU accelerated” simply because an animation uses a library. [web.dev performance](https://web.dev/articles/animations-guide).
