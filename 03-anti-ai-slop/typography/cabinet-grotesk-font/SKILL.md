---
name: cabinet-grotesk-font
description: Implement Cabinet Grotesk when it is selected for a branded web interface or editorial headings. Preserve an explicit request to use it throughout an app; do not silently substitute a quieter body font.
---

# Cabinet Grotesk

Implement Cabinet Grotesk when it is selected for a branded web interface or editorial headings. Preserve an explicit request to use it throughout an app; do not silently substitute a quieter body font.

## Fit and typography

Cabinet has pronounced stroke contrast at heavier weights. Start with 400 for reading, 500–600 for controls, and 600–700 for headings, then judge the actual layout. Avoid thin weights for small labels. The official variable file has a `wght` axis from 100 to 900.

The checked family has no italic cut and no `tnum` feature. Do not invent an italic file or claim `font-variant-numeric: tabular-nums` makes its numerals equal-width. For prose emphasis, deliberately permit synthetic oblique with `font-synthesis: style`, or choose a real italic companion when the product permits it. For financial tables, right-align numeric columns; introduce a tabular-capable companion only if the task calls for strict digit alignment.

## Acquisition and loading

Get the official download from [Fontshare](https://www.fontshare.com/fonts/cabinet-grotesk). The archive includes `Fonts/WEB/fonts/CabinetGrotesk-Variable.woff2`, a stylesheet, and `License/FFL.txt`. Use the supplied WOFF2 without modification. No npm package is required; do not invent a Fontsource package for this family.

The checked archive uses ITF Free Font License 2.0 (17 Aug 2026), permitting personal/commercial app use and self-hosting. It is not an open-source license. Keep the supplied license with local assets. Do not redistribute font files through the skills repo or a public source repository, subset/convert them, or expose them as a third-party font-selection service. For reproducible projects, fetch official assets into an ignored directory at setup/build time, verify hashes, retain the license, and reuse the local cache. Review an upstream change before refreshing pins. A CDN is an alternative when the product accepts that runtime dependency.

```css
@font-face {
  font-family: "Cabinet Grotesk";
  src: url("/fonts/cabinet-grotesk/CabinetGrotesk-Variable.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
:root { font-family: "Cabinet Grotesk", system-ui, sans-serif; }
button, input, textarea, select { font: inherit; }
```

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://www.fontshare.com/fonts/cabinet-grotesk
- https://www.fontshare.com/licenses
- https://api.fontshare.com/v2/fonts/download/cabinet-grotesk
