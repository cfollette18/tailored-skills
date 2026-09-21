# Icon recipes and implementation traps

These are reconstruction strategies, not a claim about Muse's internal per-icon implementation.

| Gesture | Moving parts | Practical implementation | Stable parts |
|---|---|---|---|
| Chat dots | Three internal dots | Opacity/scale or short vertical movement with small local offsets | Bubble outline and control |
| Search turn | Lens/handle group | A short 3D-like turn, or authored vector compression | Icon center and hit target |
| Feed sheet | Foreground page and internal lines | Layered SVG with a folding/page-turn timeline; Lottie for complex shape changes | Rear page or rail position |
| Ideas filament | Internal curved line | Normalized stroke reveal, optional retract, inside bulb | Outer bulb |
| Goals check | Check stroke and small box tilt | Check draws after a bounded rotation and settles | Outer control geometry |
| Library shapes | Separate small shapes | Staggered shape-local flatten/turn/recover | Overall grid positions |
| Projection chart | Graph segment | Stroke reveal or mask on the line | Chart axes |
| Framework book | Page group | Hinge around the spine; preserve legible silhouette | Spine and opposite page |
| Connector | Two halves | Small approach/settle with neutral styling | Control location and actual account state |

## Drawn paths

For a true stroked path, normalize `pathLength="1"`, use a unit dash length, and animate dash offset from 1 to 0. Multiple subpaths can reveal unexpectedly; split sequential strokes when their order matters. Restore the complete static path for reduced motion. [MDN pathLength](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/pathLength).

Filled icon outlines need a mask or authored stroke counterpart. Do not expose the entire filled silhouette as an animated stroke and call it a line reveal. Do not use fill/regular weight swapping as an uncontrolled geometry morph.

## Origins and 3D-like turns

Explicitly set `transform-box` and `transform-origin` for SVG groups. Verify the browser's SVG/CSS transform behavior at the target size. A flattened frame in a recording supports a turning interpretation; it does not prove the original used CSS `rotateY` or `rotateX`. An authored path animation can create the same result.

When copying an icon into clipped halves, retain unique clip/mask IDs per instance. Do not let separate sidebar instances reference each other's masks. Check seams and stroke weight at intermediate frames.

## Authored vector playback

Lottie can render vector timelines exported as JSON. A useful wrapper provides a static fallback, lazy loading, explicit playback, a completion callback, and a controlled reset. Cache shared assets rather than re-fetching them on each hover. Stop idle work and clean up the player. [Lottie Web](https://github.com/airbnb/lottie-web), [format reference](https://lottiefiles.github.io/lottie-docs/).

Muse's public bundle included a general icon wrapper with these capabilities, but this does not establish the asset or playback policy used by every recorded sidebar icon. See the research provenance before attributing specifics.

## Handoff and cancellation

Ensure the first animated frame matches the visible resting icon. The final frame should match the static fallback, or make a brief intentional handoff. A crossfade does not repair substantially mismatched silhouettes. If canceling mid-gesture, settle from the current visual state rather than resetting invisibly and starting another timeline.

CSS reduced-motion rules do not cancel JavaScript playback automatically. React to preference changes and settle active players. Avoid using a tiny duration as the only fallback when application logic incorrectly depends on `animationend`; repair the state ownership instead.
