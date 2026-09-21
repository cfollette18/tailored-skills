---
name: iconoir-icons
description: Implement or migrate interface icons with Iconoir, including React SVG sizing, shared stroke defaults, and accessible icon controls. Use for an explicit Iconoir choice or an existing Iconoir interface.
---

# Iconoir icons

Use Iconoir for a consistent line-icon treatment. Start from the app's actual icon consumers and visual scale; preserve its branding and interaction semantics.

## Correct API

For React, install or reuse `iconoir-react`. Components use PascalCase names derived from the catalog. Verify names against installed exports before swapping another library's components.

These are SVG components: use `width` and `height`, not an assumed `size` prop. The documented defaults use `currentColor`, 1.5em dimensions, and a 1.5 stroke width. `IconoirProvider` accepts `iconProps` for shared defaults. Consult the [official React package guide](https://github.com/iconoir-icons/iconoir/tree/main/packages/iconoir-react) for the installed release.

```tsx
import { Check, IconoirProvider } from 'iconoir-react';

<IconoirProvider iconProps={{ width: 20, height: 20, strokeWidth: 1.5, color: 'currentColor' }}>
  <span><Check aria-hidden="true" focusable="false" />Saved</span>
</IconoirProvider>
```

Import individual components. Check peer dependencies when upgrading React; use the existing package manager and update its lockfile rather than ignoring incompatibilities.

## Design and migration

Start around 20–24 px for navigation, then evaluate small details at the actual display size. If a glyph becomes illegible in a compact control, choose a simpler glyph or adjust the control; do not automatically thicken every icon.

Use one stroke treatment across a component family. Iconoir does not share Phosphor's `weight` API: never assume `weight="fill"` works. Represent selection with the control's existing background, color, or indicator unless a suitable distinct variant is verified.

Map concepts to recognizable actions and objects. Preserve specific icons for documents, spreadsheet outputs, and source retrieval instead of using sparkles for every assistant feature. Prefer quiet, monochrome presentation when the requested style is understated; elaborate icon cards are not a requirement of this library.

Put accessible names on icon-only buttons, and hide adjacent decorative SVGs. Preserve hit areas, focus rings, RTL behavior where relevant, and reduced-motion loading states. Remove obsolete library-specific CSS only where its consumers have changed.

Verify every migrated export through a build/typecheck and inspect a representative toolbar, navigation state, and mobile view. Use existing interaction checks when available. Remove the previous dependency only if no remaining consumers need it. Do not change app behavior or replace the logo as a side effect of an icon migration.
