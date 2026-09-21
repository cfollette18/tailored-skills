---
name: motion-accessibility-performance
description: Validate and repair reduced-motion handling, keyboard and touch behavior, animation lifecycle, and rendering cost. Use for frontend motion accessibility or performance work; assess actual interactions rather than claiming compliance from CSS alone.
---

# Motion accessibility and performance

Check the moving interface, not just its stylesheet. Inventory CSS transitions/keyframes, WAAPI, animation libraries, SVG/Lottie players, videos, and requestAnimationFrame loops. One CSS media query does not control all of them.

## Reduced motion and meaning

Respect `prefers-reduced-motion` before starting optional motion and react if it changes while motion is active. Stop or settle spatial transitions, decorative loops, and icon drawing. Preserve the correct state and static status labels. A brief opacity change can be suitable; making every animation slower is not a reduced-motion strategy.

In Motion for React, the user preference option reduces transform/layout motion, while other values may still animate. Handle custom path drawing and external players explicitly. With CSS, verify that selectors cover the actual moving elements. Do not make completion of essential business logic depend on an animation event that reduced motion suppresses.

W3C's interaction-animation criterion 2.3.3 is Level AAA; do not mislabel it an AA requirement or claim full WCAG compliance from this check. It supports the practical policy of letting users disable nonessential interaction motion. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html), [MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion).

## Input and focus

Keep the click target still and larger than the visual glyph according to the project's control sizing. Gate decorative mouse-hover behavior using actual pointer events and capability information; `(hover:hover)` describes the primary input, so account for hybrid devices rather than treating it as proof that every pointer can hover. Touch activates on the first tap. Keyboard focus must remain clearly visible without a flourish.

Icon-only controls need an accessible name on the control. Decorative SVG layers should not add duplicate announcements. Tooltips should also work on focus and satisfy applicable dismissible, hoverable, and persistent behavior; handle Escape, avoid blocking content, and retain the control's independent accessible name. A delayed tooltip is not a substitute for a label. [W3C hover/focus content](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html).

During exits, prevent hidden elements from intercepting clicks or retaining keyboard focus. Move focus to a valid destination before hiding/inerting its current container. Check whether the overlay is actually modal before imposing a focus trap.

## Rendering and lifecycle

Prefer transform/opacity for large surfaces. Profile layout changes, filters, shadows, SVG drawing, and canvas at realistic sizes and density. Do not infer compositor-only behavior from the property name alone. Avoid per-frame layout read/write alternation, per-frame React state, and permanent layer promotion across the whole page.

Clean up players, timers, observers, animation handles, and frame callbacks on unmount. Stop decorative work offscreen or in a hidden document when appropriate. Rapid input should replace outdated work, not queue more. Inspect a trace for paint/layout cost and long tasks; record the browser, viewport, device/emulation, and scenario before making performance claims. A 60 Hz frame interval is about 16.7 ms, not a budget wholly available to JavaScript. [web.dev guide](https://web.dev/articles/animations-guide).

## Verification cases

Exercise normal and reduced motion, a mid-animation preference change, keyboard focus/activation, touch, long hover, hover exit/reentry, rapid reversal, resize, and navigation away during playback. Confirm state correctness and useful static information in each case. Use existing browser checks plus live inspection; frame screenshots help visual diagnosis but do not establish assistive-technology support or production performance.

Report what was verified and any remaining coverage gaps. Accessibility improvements are ordinary implementation work; do not ask the user whether basic reduced-motion support is wanted.
