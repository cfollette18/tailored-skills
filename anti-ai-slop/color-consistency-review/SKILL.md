---
name: color-consistency-review
description: Audit and repair color drift across an existing frontend, including component states, feature-specific styles, and brand assets. Use when a product feels visually inconsistent or after a palette migration; preserve documented exceptions.
---

# Color consistency review

Find where the product's intended color roles diverge in implementation. This is a focused consistency review, not permission to redesign the brand or adopt a particular palette.

## Inspect the whole color surface

Locate the canonical tokens and compare them with component CSS, inline styles, framework theme objects, SVG fills, logos/favicons, browser theme-color, portals, dialogs, and feature-specific stylesheets. Review all supported themes and viewports in scope. Search is useful for finding candidates, but a literal color is not automatically wrong: provider assets and generated data visualizations can be legitimate exceptions.

Group findings by role: unintended old-theme remnants, duplicate shades serving the same purpose, one token serving incompatible purposes, unreadable state combinations, and documented external-brand colors. Prioritize broken reading or interactions over cosmetic differences.

Check common drift traps: feature screens imported outside the main stylesheet, selected text inheriting a hover background, disabled elements retaining active emphasis, semantically different statuses sharing one accent, logos with hardcoded colors, input defaults supplied by the browser, and translucent overlays that change contrast.

## Repair narrowly

Map product colors to existing semantic roles where they fit. Introduce a new role only for a distinct need. Remove superseded declarations instead of accumulating overrides. Keep complete approved wordmarks and preserve other brand constraints; recoloring does not authorize cropping or rebuilding a logo.

Record exceptions with a concrete owner or requirement, such as a provider's sign-in button. Do not use exceptions as a general escape hatch for one-off component tints. Avoid recoloring third-party brand marks just to make a screenshot uniform.

## Verify and hand off

Inspect representative normal, hover, focus, selected, disabled, success, and failure states. Measure actual foreground/background pairs and examine the app at desktop/mobile sizes. Reuse existing fixtures to avoid external side effects.

Summarize corrected drift, intentional exceptions, and any untested surfaces. A lightweight token/literal/asset check is useful when it prevents the same drift from recurring; do not equate that static check with a full visual or accessibility review.

## References

- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
