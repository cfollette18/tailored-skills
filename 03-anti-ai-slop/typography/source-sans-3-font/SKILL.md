---
name: source-sans-3-font
description: Implement Source Sans 3 for readable, professional interfaces and substantial on-screen research text.
---

# Source Sans 3

Implement Source Sans 3 for readable, professional interfaces and substantial on-screen research text.

## Fit and typography

Use Source Sans 3 when reading comfort and compact controls matter more than expressive display typography. Distinctiveness should come from a deliberate layout and information hierarchy, not forced letterspacing.

Keep Source Sans 3 naming consistent; do not mix older Source Sans Pro family names or assets into the same declaration. Source Serif 4 can serve as an optional report companion, but add it only where the product needs an editorial reading surface. Load real italics for emphasized analysis and inspect punctuation, links, and financial tables.

## Acquisition and loading

Use the self-hosted Fontsource package `@fontsource-variable/source-sans-3` with the project's package manager. Version 5.3.0 was checked on 2026-09-21; use the project's lockfile and verify the current package's exports when integrating.

```sh
npm install @fontsource-variable/source-sans-3
```

```js
import '@fontsource-variable/source-sans-3';
```

```css
:root { font-family: "Source Sans 3 Variable", sans-serif; }
button, input, textarea, select { font: inherit; }
```

The root declaration is an example for a primary family. For report-only or code-only use, scope the family to that surface. The package uses SIL OFL 1.1 and allows commercial use; preserve its license when redistributing assets. Check the installed CSS for the exact family name, weight range, glyph subset, style, and axis coverage. Import a separate italic entry only if the package actually provides it and the product uses it. Avoid loading the same font again from a remote stylesheet.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://github.com/adobe-fonts/source-sans
- https://fontsource.org/fonts/source-sans-3/use
- https://fontsource.org/docs/getting-started/install
