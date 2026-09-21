---
name: newsreader-font
description: Implement Newsreader for content-rich reading surfaces, research reports, or an explicitly requested serif interface.
---

# Newsreader

Implement Newsreader for content-rich reading surfaces, research reports, or an explicitly requested serif interface.

## Fit and typography

Newsreader was designed for continuous on-screen reading. Scope it to report titles, summaries, and narrative analysis when paired with a sans-serif interface. Preserve compact controls and code typography unless their redesign is requested.

Use an optical-size-capable file for mixed title and paragraph sizes, with `font-optical-sizing: auto`; check the installed entry because variable packages may offer several axis subsets. Load its real italic for quotations and emphasized analysis. Judge paragraph width and line-height using real multi-paragraph content, not only a display heading.

## Acquisition and loading

Use the self-hosted Fontsource package `@fontsource-variable/newsreader` with the project's package manager. Version 5.3.0 was checked on 2026-09-21; use the project's lockfile and verify the current package's exports when integrating.

```sh
npm install @fontsource-variable/newsreader
```

```js
import '@fontsource-variable/newsreader';
```

```css
:root { font-family: "Newsreader Variable", serif; }
button, input, textarea, select { font: inherit; }
```

The root declaration is an example for a primary family. For report-only or code-only use, scope the family to that surface. The package uses SIL OFL 1.1 and allows commercial use; preserve its license when redistributing assets. Check the installed CSS for the exact family name, weight range, glyph subset, style, and axis coverage. Import a separate italic entry only if the package actually provides it and the product uses it. Avoid loading the same font again from a remote stylesheet.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://github.com/productiontype/Newsreader
- https://fontsource.org/fonts/newsreader/use
- https://fontsource.org/docs/getting-started/install
