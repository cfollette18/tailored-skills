---
name: ranade-font
description: Implement Ranade when selected as a free alternative for a modern interface or its headings.
---

# Ranade

Implement Ranade when selected as a free alternative for a modern interface or its headings.

## Fit and typography

Judge its proportions in the real sidebar, controls, and content rather than only a large specimen. Begin with Regular for paragraphs and Medium for interface hierarchy; let the shapes provide the character before adding tight tracking.

The official archive provides both variable upright and variable italic files, plus static cuts. Register italic separately under the same CSS family when prose uses emphasis. Derive the weight range from the supplied CSS; do not assume every variable font reaches 900.

## Acquisition and loading

Get the official download from [Fontshare](https://www.fontshare.com/fonts/ranade). The archive includes `Fonts/WEB/fonts/Ranade-Variable.woff2`, a stylesheet, and `License/FFL.txt`. Use the supplied WOFF2 without modification. No npm package is required; do not invent a Fontsource package for this family.

The checked archive uses ITF Free Font License 2.0 (17 Aug 2026), permitting personal/commercial app use and self-hosting. It is not an open-source license. Keep the supplied license with local assets. Do not redistribute font files through the skills repo or a public source repository, subset/convert them, or expose them as a third-party font-selection service. For reproducible projects, fetch official assets into an ignored directory at setup/build time, verify hashes, retain the license, and reuse the local cache. Review an upstream change before refreshing pins. A CDN is an alternative when the product accepts that runtime dependency.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://www.fontshare.com/fonts/ranade
- https://www.fontshare.com/licenses
- https://api.fontshare.com/v2/fonts/download/ranade
