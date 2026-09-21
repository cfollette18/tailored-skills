---
name: instrument-sans-font
description: Implement Instrument Sans for a restrained modern product interface or an explicitly requested font migration.
---

# Instrument Sans

Implement Instrument Sans for a restrained modern product interface or an explicitly requested font migration.

## Fit and typography

Treat Instrument Sans as the interface family; Instrument Serif is a different design and is not installed by this package. Start with readable regular text and medium controls instead of decorative typography on every component.

Check the installed font metadata before selecting weights: do not invent ultra-light or black styles beyond the available range. For a stronger identity, first adjust hierarchy, spacing, and content density. Only enable stylistic alternates after confirming they exist and inspecting their effect across common product strings.

## Acquisition and loading

Use the self-hosted Fontsource package `@fontsource-variable/instrument-sans` with the project's package manager. Version 5.3.0 was checked on 2026-09-21; use the project's lockfile and verify the current package's exports when integrating.

```sh
npm install @fontsource-variable/instrument-sans
```

```js
import '@fontsource-variable/instrument-sans';
```

```css
:root { font-family: "Instrument Sans Variable", sans-serif; }
button, input, textarea, select { font: inherit; }
```

The root declaration is an example for a primary family. For report-only or code-only use, scope the family to that surface. The package uses SIL OFL 1.1 and allows commercial use; preserve its license when redistributing assets. Check the installed CSS for the exact family name, weight range, glyph subset, style, and axis coverage. Import a separate italic entry only if the package actually provides it and the product uses it. Avoid loading the same font again from a remote stylesheet.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://github.com/Instrument/instrument-sans
- https://fontsource.org/fonts/instrument-sans/use
- https://fontsource.org/docs/getting-started/install
