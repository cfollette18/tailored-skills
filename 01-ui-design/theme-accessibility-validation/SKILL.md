---
name: theme-accessibility-validation
description: Validate a frontend color theme using contrast measurements and rendered interaction states. Use for palette migrations, readability checks, and theme regressions across supported screens; report the actual validation scope.
---

# Theme accessibility validation

Validate the rendered theme, including foreground/background combinations introduced by state and inheritance. A palette chart alone does not establish accessibility. This workflow applies to any product, palette, or frontend framework.

## Measure the right pairs

For WCAG AA contrast, ordinary text needs at least 4.5:1. Large text needs at least 3:1: at least 24 CSS px regular or approximately 18.67 CSS px bold. Essential control/state indicators generally need 3:1 against adjacent colors. A faint decorative divider does not automatically need the same ratio as an input boundary needed to identify that control.

Use relative luminance and the unrounded ratio for pass/fail. Resolve token aliases and composite translucent foregrounds/backgrounds before comparing. Do not assume a white label is legible on every vivid brand color. Test a darker action shade or a dark label and measure again. Inactive controls and logos have contrast exceptions, but should still be usable and recognizable.

Inspect body text, secondary labels, placeholders, selected navigation, buttons, links, focus indicators, status labels, alerts, and text selection. Check hover on already-selected controls; nested text or icons can override an otherwise correct parent's color. Review keyboard focus on light and dark surfaces and avoid relying on color alone to communicate success, error, selection, or chart series.

## Validate in context

Exercise the supported desktop/mobile layouts and every major surface affected by the change. Use existing fixtures for states that would otherwise require an external transaction, account connection, or paid model call. Do not initiate those actions just to inspect styling.

Wait for fonts and assets, inspect computed colors and inherited backgrounds, then visually review screenshots. Check text wrapping, zoom, long values, image/logo contrast, and focus visibility. Automated checks identify measurable failures; they do not establish that all content, states, and user journeys comply.

Report the tested surfaces, contrast pairs, and limitations. A passing token check should be described as a token check, not as a complete WCAG certification. Extend persistent checks where they protect a real shared contract; avoid tests that merely duplicate implementation wording.

## References

- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
