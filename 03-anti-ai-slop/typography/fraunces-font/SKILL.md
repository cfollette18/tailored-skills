---
name: fraunces-font
description: Implement Fraunces for expressive editorial headings or brand accents while retaining professional reading hierarchy.
---

# Fraunces

Implement Fraunces for expressive editorial headings or brand accents while retaining professional reading hierarchy.

## Fit and typography

Fraunces offers optical size, softness, and wonk controls in its full variable design. For a professional product, start with a restrained treatment and reserve strongly expressive forms for titles. Do not use unusual settings indiscriminately in dense tables or tool logs.

Check the installed file for `opsz`, `SOFT`, and `WONK` before setting them: default Fontsource imports may not contain every custom axis. Use separate real italic assets when needed. Compare the result at actual heading sizes; softness and wonk are optional design decisions, not universal anti-slop settings.

## Acquisition and loading

Use the self-hosted Fontsource package `@fontsource-variable/fraunces` with the project's package manager. Version 5.3.0 was checked on 2026-09-21; use the project's lockfile and verify the current package's exports when integrating.

```sh
npm install @fontsource-variable/fraunces
```

```js
import '@fontsource-variable/fraunces';
```

```css
:root { font-family: "Fraunces Variable", serif; }
button, input, textarea, select { font: inherit; }
```

The root declaration is an example for a primary family. For report-only or code-only use, scope the family to that surface. The package uses SIL OFL 1.1 and allows commercial use; preserve its license when redistributing assets. Check the installed CSS for the exact family name, weight range, glyph subset, style, and axis coverage. Import a separate italic entry only if the package actually provides it and the product uses it. Avoid loading the same font again from a remote stylesheet.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://fraunces.undercase.xyz/
- https://fontsource.org/fonts/fraunces/use
- https://fontsource.org/docs/getting-started/install
