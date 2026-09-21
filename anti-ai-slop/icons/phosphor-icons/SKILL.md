---
name: phosphor-icons
description: Implement or migrate interface icons using Phosphor, including React imports, visual weights, semantic icon selection, and accessible controls. Use when Phosphor is selected or a project requests a Phosphor migration; do not replace another established icon family without that scope.
---

# Phosphor icons

Build a consistent icon vocabulary for the product. Inspect existing imports, icon-bearing controls, and dependency versions before editing. Preserve the user's brand marks and genuine service logos unless their redesign is requested.

## Package and rendering

Use `@phosphor-icons/react` for React. Check actual exports in the installed version; do not translate another library's names by guesswork. Prefer named imports and the current `*Icon` component names. Use the package's `Icon` type for component maps. Avoid namespace imports or a runtime lookup of the entire catalog.

Phosphor provides `thin`, `light`, `regular`, `bold`, `fill`, and `duotone` weights. Set shared defaults through `IconContext`; use `weight`, not CSS `stroke-width` or `fill` overrides, to change the drawing. Remove inherited stroke styling from the previous library. For React Server Components, use the documented SSR entry point and explicit props; the client context is not available there.

```tsx
import { IconContext, ChartLineUpIcon } from '@phosphor-icons/react';

<IconContext.Provider value={{ size: 20, weight: 'regular', color: 'currentColor' }}>
  <button aria-label="View projections">
    <ChartLineUpIcon aria-hidden="true" focusable="false" />
  </button>
</IconContext.Provider>
```

See the [official React guide](https://github.com/phosphor-icons/react) for version-specific imports and SSR support.

## Visual decisions

For a restrained workspace, start with Regular at 18–20 px in navigation and a smaller consistent size in dense controls. Treat these as starting points, not requirements for every product. Inspect the rendered result at actual size.

Choose imagery by action: a chart for projections, a document for reports, a calculator for calculations, and a connection symbol for integrations. A sparkle is not a universal agent/status symbol. Prefer text for a concept that has no recognizable pictogram.

Use monochrome icons inheriting their control's color. A selected navigation item may use Fill alongside its existing selected background and accessible state. Avoid unrelated weight changes, decorative gradients, or a colored tile behind every glyph. Keep purposeful status colors and product-specific exceptions.

Label icon-only buttons on the button; hide redundant SVGs from assistive technology. Keep the click target larger than the glyph, and retain visible keyboard focus. Loading icons need a textual status and reduced-motion support.

## Finish the migration

Check navigation, tool activity, menus, loading/stop states, downloads, empty states, and mobile controls. Build/typecheck and use the project's existing browser checks. Inspect selected and unselected states at desktop/mobile sizes. Remove the old dependency only after all consumers are migrated; update the lockfile. Do not invoke a paid model just to test icon rendering.
