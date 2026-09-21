---
name: radix-icons
description: Implement compact interface iconography with Radix Icons, especially toolbars, menus, and dense controls. Use when Radix Icons is chosen or already used; using Radix UI primitives alone does not require changing a project's icon family.
---

# Radix Icons

Radix Icons is a compact interface set. Inspect the existing layout before choosing it: the library is particularly useful when controls need clear small glyphs, rather than large decorative illustrations.

## Package and geometry

Use `@radix-ui/react-icons` for React and import individual named components. The family is designed on a 15×15 grid. Start with its native dimensions; inspect any scaling at the intended display size. Do not assume that enlarging a toolbar icon produces an appropriate hero illustration.

```tsx
import { MagnifyingGlassIcon } from '@radix-ui/react-icons';

<button aria-label="Search research">
  <MagnifyingGlassIcon width={15} height={15} aria-hidden="true" focusable="false" />
</button>
```

Check the [official catalog and React usage](https://www.radix-ui.com/icons) and the installed package exports for names. Use SVG `width`/`height` and inherited color. Do not assume a `size`, `weight`, or Phosphor-style provider API. Avoid generic stroke overrides: the drawings may encode their shapes as filled paths.

## Product fit

Select one coherent family for a given interface region. If a necessary domain-specific icon is absent, use a text label, an existing deliberate product symbol, or discuss a broader library choice when the missing coverage affects the task. Do not silently mix several libraries to approximate one symbol.

Keep glyphs optically aligned with text. Separate glyph size from target size: a 15 px symbol does not justify a 15 px button. Preserve padding and keyboard focus, label icon-only controls, and hide SVGs that duplicate visible text.

Keep selection and status visible in the enclosing control; use any filled/outline variants only if those exports actually exist and their relationship makes sense. Match the app's tone through typography, spacing, and color rather than decorating every icon with a badge or gradient.

## Verification

Build/typecheck to catch guessed exports and incompatible props. Inspect dense controls at native browser zoom, including hover, disabled, selected, and mobile states. Use existing interaction tests to confirm that icon-only controls retain their accessible names. During a migration, remove old icon-specific CSS and dependencies only after their last consumer is gone. Preserve custom brand marks and unrelated UI behavior.
