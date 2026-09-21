---
name: streamline-icons
description: Select and integrate Streamline icon assets into an interface, including family consistency, SVG/JSX exports, and existing license provenance. Use when Streamline is requested or supplied assets come from Streamline; do not invent an npm package or assume premium asset access.
---

# Streamline icons

Use the specific Streamline family and assets available to the project. Treat Streamline as a design asset workflow unless the user's installed tooling provides a verified integration.

## Choose and obtain the assets

Inspect existing assets, design references, and any recorded license first. Select a consistent family and treatment. Core is a useful starting point for compact interface controls; Sharp can fit a more angular technical product. These are design choices, not mandatory preferences. See the [family overview](https://blog.streamlinehq.com/the-streamline-icon-system/).

The [official React workflow](https://site.streamlinehq.com/free/icons-for-react) supports copying SVG or JSX into the project. Do not fabricate a universal `streamline-react` package or install a similarly named third-party package as if it were official. Verify newer tooling against current first-party documentation if needed.

Use supplied exports or assets the user can access. Keep the family, asset name, source URL, and applicable license alongside the project's existing asset records. Check the actual asset terms before committing redistributable files; free and premium assets have different conditions. Consult the current [free](https://help.streamlinehq.com/en/articles/5354376-streamline-free-license) or [premium](https://help.streamlinehq.com/en/articles/5354366-streamline-premium-licenses) terms as applicable. Do not copy a premium preview or purchase access without authorization. If access is missing, finish the integration structure and identify the exact asset still needed.

## Integrate without distorting the drawings

Keep the export's viewBox, aspect ratio, and intended line/fill treatment. For monochrome assets, use `currentColor` on the relevant paths or strokes; do not erase intentional multicolor artwork. Translate SVG attributes to JSX correctly, or use the project's established SVG loader. Avoid global CSS that changes all paths indiscriminately.

Use small, named components or local SVG files for the selected assets. Do not import the full downloaded catalog into the client bundle. Preserve required notices and attribution in the form the asset license requires.

Choose pictograms for concrete actions; decorative sparkles and colored containers are not a substitute for clear labels. Keep glyph sizes consistent within a control family, give icon-only buttons accessible names, and hide redundant SVGs. Ensure repeated SVGs do not create conflicting gradient/mask IDs.

## Verify

Check the files render without clipping or missing internal references, that all local imports resolve, and that currentColor behaves in active and disabled states. Inspect a desktop and mobile control at actual size. Run the existing build and relevant interaction checks. Report any unavailable assets plainly; do not claim an integration is complete while it still uses unidentified placeholders.
