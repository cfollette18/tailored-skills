---
name: source-serif-4-font
description: Implement Source Serif 4 for professional report typography and substantial reading surfaces.
---

# Source Serif 4

Implement Source Serif 4 for professional report typography and substantial reading surfaces.

## Fit and typography

Use Source Serif 4 for a formal, readable report voice. It pairs naturally with Source Sans 3, but a second family is optional. Keep financial tables compact and align their numeric columns; a serif does not supply table structure by itself.

The family has optical-size designs. Use a file containing `opsz` with `font-optical-sizing: auto` when available; otherwise select the intended text or display cut. Do not mix Source Serif Pro and Source Serif 4 names or pretend the weight-only entry includes every axis. Load real italics and verify the font in any separate PDF renderer before promising export parity.

## Acquisition and loading

Use the self-hosted Fontsource package `@fontsource-variable/source-serif-4` with the project's package manager. Version 5.3.0 was checked on 2026-09-21; use the project's lockfile and verify the current package's exports when integrating.

```sh
npm install @fontsource-variable/source-serif-4
```

```js
import '@fontsource-variable/source-serif-4';
```

```css
:root { font-family: "Source Serif 4 Variable", serif; }
button, input, textarea, select { font: inherit; }
```

The root declaration is an example for a primary family. For report-only or code-only use, scope the family to that surface. The package uses SIL OFL 1.1 and allows commercial use; preserve its license when redistributing assets. Check the installed CSS for the exact family name, weight range, glyph subset, style, and axis coverage. Import a separate italic entry only if the package actually provides it and the product uses it. Avoid loading the same font again from a remote stylesheet.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://github.com/adobe-fonts/source-serif
- https://fontsource.org/fonts/source-serif-4/use
- https://fontsource.org/docs/getting-started/install
