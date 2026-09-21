---
name: uncut-sans-font
description: Implement Uncut Sans for a clean interface with understated character, or migrate an existing interface to it when requested.
---

# Uncut Sans

Implement Uncut Sans for a clean interface with understated character, or migrate an existing interface to it when requested.

## Fit and typography

Keep ordinary reading text restrained before exploring alternates. The upstream README documents alternate R (`ss01`), Y/y (`ss02`), Q/Ø/ø (`ss03`), a (`ss04`), and 1/2/4 (`ss05`). Use alternates as a coherent product choice after inspecting their actual glyphs, not as random decoration.

Check company names, tickers, currency symbols, and ambiguous characters such as I/l/1 and O/0 at the actual interface size. The family includes variable fonts; read the downloaded CSS or font metadata for its weight range and available styles rather than guessing from the number of static cuts.

## Acquisition and loading

Download the official files from [the upstream repository](https://github.com/kaspernordkvist/uncut_sans), using its `Webfonts` or variable distribution as appropriate. Retain `LICENSE.txt` (SIL OFL 1.1) with redistributed assets. This permits commercial use; modifications and redistribution remain subject to the OFL and any reserved font names.

Register the supplied WOFF2 with `@font-face`, using one CSS family name, the correct weight range, and separate style declarations where supplied. Prefer self-hosting for a product app. Do not guess an npm package name or reference a raw source file that the bundler cannot serve. Inspect the selected release for exact filenames and available glyphs.

## Verify the integration

Inspect existing font declarations and preserve the user's chosen scope. Set a shared family token or root declaration and make controls inherit it; retain purposeful monospace text. Remove obsolete remote imports only after checking their consumers. Keep a system fallback and `font-display: swap`; preload only a font used immediately.

Build with the project's existing checks. In a browser, wait for `document.fonts.ready`, confirm the intended face is loaded (a CSS family string alone is not proof), and inspect actual glyph rendering. Check desktop/mobile wrapping, narrow controls, long paragraphs, emphasis, currency/percent/minus signs, and missing-glyph fallback. Use existing screenshot checks where available; a typography migration does not require a model call or a new research run.

## Sources

- https://uncut.wtf/sans-serif/uncut-sans/
- https://github.com/kaspernordkvist/uncut_sans
