---
name: animated-interface-icons
description: Build authored hover and state animations inside interface icons while preserving their icon family, hit target, and meaning. Use for expressive sidebar, toolbar, and action glyphs, including Muse-inspired motion; not for changing the entire product's branding.
---

# Animated interface icons

Make the icon perform a recognizable action. Inspect its vector structure and the requested reference before choosing transforms. Different icons need different anatomy; assigning the same wobble to every glyph misses the point.

For the owner's Muse reference, read [the recording study](references/muse-sidebar-study.md). It includes timestamped icon-only filmstrips, observed gestures, source-code findings, and explicit limits. Read [implementation recipes](references/icon-recipes.md) when building the animation.

## Preserve the icon system

Retain the established viewBox, optical size, weight, baseline, and resting silhouette. Some libraries encode regular icons as filled compound paths: changing CSS stroke width or applying stroke-dashoffset to that filled outline does not produce a clean line-drawing animation. Use compatible stroke geometry, a reveal mask, or separately authored layers. Do not assume any two SVG paths can interpolate without matching topology.

Keep the outer icon box and control hit area fixed. Animate meaningful internal groups: dots in a bubble, a lens, a page, a check, a chart segment, connector halves. Set transform origins deliberately; a page turns around its spine, not the whole SVG's center. Keep labels readable and stationary.

## Define the interaction contract

Use a small explicit lifecycle: resting, playing, settling, resting. Hover starts one gesture on a device that supports it. Long hover does not imply an infinite loop. Do not retrigger on every pointer movement. A click during hover should not duplicate the animation; keyboard activation should perform the action immediately without requiring the flourish. On touch, activate on the first tap.

Choose what happens on early pointer exit: finish a short cycle, smoothly return, or hand off to a matching static frame. Specify it instead of accepting a snap from a canceled animation. Reentry can retarget or restart only after a defined reset; avoid overlapping timelines. Cancel work when the component unmounts or becomes irrelevant.

The static and animated versions must match at handoff. A static fallback should be available before lazy assets load, on errors, and under reduced motion. Avoid empty glyphs while a player initializes. If the motion includes a check or connecting plugs, do not let decorative hover falsely indicate success or a connected account.

## Timing and feedback

Input feedback starts immediately. For a deliberately expressive reference, a roughly 350–700 ms glyph gesture can be appropriate while selection and navigation complete separately. Tune the visible trajectory rather than inventing exact spring values from a video. Keep optional tiny subpart delays local to the icon.

Under reduced motion show the resting or semantically correct final icon. Preserve the accessible button/link name, selected state, and visible focus; mark decorative SVG layers hidden to assistive technology. A tooltip is supplemental, never the sole accessible name.

Inspect actual-size playback, an enlarged slow version, hover exit/reentry, repeated clicks, keyboard, touch, and reduced motion. A smooth enlarged animation can still be illegible at 20 px.
