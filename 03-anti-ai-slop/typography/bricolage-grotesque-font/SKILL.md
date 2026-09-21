---
name: bricolage-grotesque-font
description: Implement Bricolage Grotesque for expressive headings or a deliberately characterful interface, respecting any requested body-text use.
---

# Bricolage Grotesque

Implement Bricolage Grotesque for expressive headings or a deliberately characterful interface, respecting any requested body-text use.

## Fit and typography

Its width and optical-size design can produce very different personalities. For a professional research product, begin at normal width and moderate weights, with greater expression in titles. Do not compress paragraphs just to make them fit.

The upstream design has weight, width, and optical-size axes and no italics. Verify which axes the chosen Fontsource entry actually includes before setting custom values; a weight-only build will not supply the full design space. Use `font-optical-sizing: auto` when the loaded file supports `opsz`. Preserve semantic emphasis by allowing intentional synthetic oblique or using an approved italic companion.

## Acquisition and loading

Use the self-hosted Fontsource package `@fontsource-variable/bricolage-grotesque` with the project's package manager. Version 5.3.0 was checked on 2026-09-21; use the project's lockfile and verify the current package's exports when integrating.

```sh
npm install @fontsource-variable/bricolage-grotesque
```

```js
import '@fontsource-variable/bricolage-grotesque';
```

```css
:root { font-family: "Bricolage Grotesque Variable", sans-serif; }
button, input, textarea, select { font: inherit; }
```

The root declaration is an example for a primary family. For report-only or code-only use, scope the family to that surface. The package uses SIL OFL 1.1 and allows commercial use; preserve its license when redistributing assets. Check the installed CSS for the exact family name, weight range, glyph subset, style, and axis coverage. Import a separate italic entry only if the package actually provides it and the product uses it. Avoid loading the same font again from a remote stylesheet.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://ateliertriay.github.io/bricolage/
- https://fontsource.org/fonts/bricolage-grotesque/use
- https://fontsource.org/docs/getting-started/install
