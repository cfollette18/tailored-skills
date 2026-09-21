---
name: semantic-color-theming
description: Implement a shared semantic color system across frontend surfaces and interaction states. Use when establishing a product theme, migrating a palette, or replacing scattered color literals; adapt to the selected brand and framework.
---

# Semantic color theming

Start with the owner's chosen direction and inventory the existing surfaces, controls, states, charts, and brand assets. A reference brand supplies inspiration, not permission to replace the product's identity, typography, or behavior. Keep this workflow independent of a particular palette or frontend framework.

## Define roles before editing components

Separate palette primitives from semantic roles. A small useful role set includes canvas, raised/subtle surfaces, primary/secondary/muted text, decorative/control borders, primary action and its label, selected background and label, focus, links, success, warning, danger, disabled treatment, and overlay. Add a role when a real component needs different behavior, not for every old hex value.

Use the project's existing token system where possible. CSS custom properties, theme objects, or design-token files are valid implementations. Give components semantic names such as `action`, not names that assume it will always be blue. Define foreground and background as deliberate pairs; brand accents may need a darker UI derivative for small labels.

## Migrate by meaning

Map each declaration by its component role and state. A text color and a border can share an old hex value but need different tokens. Do not perform a blind global hue replacement. Review navigation, chats, forms, tables, dialogs/backdrops, empty/loading/error states, settings, integration screens, and responsive variants.

Check hover, focus, selected, active, disabled, and validation states explicitly. A selected tab may inherit white text while a later hover rule gives it a pale background. Input placeholders are text, and transparent child backgrounds require checking the actual ancestor surface. Use currentColor for ordinary icons where appropriate.

Keep success/warning/danger semantics separate from brand accents, and retain labels or recognizable symbols. Preserve third-party logos and required provider-owned sign-in styling as documented exceptions. Product assets such as wordmarks, favicons, and browser chrome should use the product theme; track any duplicated export colors with a lightweight consistency check.

## Keep the system maintainable

Remove replaced color literals and obsolete rules rather than piling on a second override stylesheet. Scope any dark theme only when requested or already supported; do not assume inverting the light palette works. Record where tokens live, how to add a role, and which exceptions are intentional.

Use existing build/browser checks plus representative rendered-state inspection. When the theme will be maintained over time, add a small check for undefined tokens, accidental component literals, important contrast pairs, and mirrored brand colors. Verify behavior and actual pairings, not just that a named variable appears in source.

## References

- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
