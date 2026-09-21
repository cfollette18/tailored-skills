---
name: free-font-selection
description: Choose and integrate free commercial-use fonts for distinctive or restrained professional interfaces, reports, and technical text. Use for font shortlists or typography changes when cost must be zero; respect an already selected family.
---

# Free fonts for deliberate product typography

Choose based on the reading task, the product's identity, and actual rendered specimens. A font is not inherently AI slop, and a familiar family is not automatically a bad choice. If the user selected a family, integrate it rather than reopening the decision. Preserve the existing icon family and product behavior during a font change.

## Researched families

The table is a routing guide, not a ranking of objective quality. Read only the relevant family guide. All listed families have free commercial-use distributions; paid alternatives such as Haffer, Roobert, Oracle, Cinetype, Diatype, and Söhne are outside this shortlist.

| Family | Direction | Useful role | License |
|---|---|---|---|
| [Cabinet Grotesk](../cabinet-grotesk-font/SKILL.md) | Distinctive sans | Expressive headings and branded interfaces | ITF FFL 2.0 |
| [Uncut Sans](../uncut-sans-font/SKILL.md) | Distinctive sans | Subtly distinctive all-purpose interface | OFL 1.1 |
| [Bricolage Grotesque](../bricolage-grotesque-font/SKILL.md) | Distinctive sans | Expressive headings and brand typography | OFL 1.1 |
| [Ranade](../ranade-font/SKILL.md) | Distinctive sans | A characterful alternative for headings and interfaces | ITF FFL 2.0 |
| [IBM Plex Sans](../ibm-plex-sans-font/SKILL.md) | Quiet professional sans | Technical research and dense interfaces | OFL 1.1 |
| [Instrument Sans](../instrument-sans-font/SKILL.md) | Quiet professional sans | A softer modern product interface | OFL 1.1 |
| [Source Sans 3](../source-sans-3-font/SKILL.md) | Quiet professional sans | Dense controls and long research text | OFL 1.1 |
| [Switzer](../switzer-font/SKILL.md) | Quiet professional sans | Versatile neutral product interface | ITF FFL 2.0 |
| [Newsreader](../newsreader-font/SKILL.md) | Editorial serif | Research reports and sustained reading | OFL 1.1 |
| [Source Serif 4](../source-serif-4-font/SKILL.md) | Editorial serif | Formal reports and extended analysis | OFL 1.1 |
| [Fraunces](../fraunces-font/SKILL.md) | Expressive serif | Editorial titles and selective brand accents | OFL 1.1 |
| [IBM Plex Mono](../ibm-plex-mono-font/SKILL.md) | Technical companion | Code, tool names, identifiers, and aligned data | OFL 1.1 |

## Choose for the actual surface

- For a distinctive interface, compare Uncut Sans and Ranade on navigation, controls, and paragraphs. Use Cabinet Grotesk when its stroke contrast fits the brand, including throughout the app if requested.
- For restrained professional reading, compare IBM Plex Sans, Instrument Sans, Source Sans 3, and Switzer. Select by readability and proportions, not an unsupported claim that a font is rare or overused.
- For editorial reports, compare Newsreader and Source Serif 4. Fraunces and Bricolage Grotesque offer more expression for headings; do not force their most unusual settings into dense data.
- Use IBM Plex Mono where character alignment helps. A technical companion is optional, not a requirement to add a third family.

Start with one primary family. Add a companion only for an identifiable reading or information role. Use a small specimen with a heading, paragraph, sidebar item, button, italic emphasis, and financial values such as `$1,234.56`, `−12.4%`, `0.00`, and `2026–2030`. Check ambiguous glyphs, long company names, and required languages. Let the user's taste and the specimen decide.

## Acquisition and integration decisions

Free price is separate from open-source permission. OFL families can be redistributed under their license terms. Fontshare's Cabinet Grotesk, Ranade, and Switzer use ITF FFL: obtain official copies, retain the license, and keep the font binaries outside source repositories. Their supplied webfonts can be self-hosted for the product. Do not turn them into a selectable-font service for third-party content creation. The individual guides describe verified sources and packages; do not invent package names.

Use self-hosted WOFF2 when practical. Confirm actual styles and axes before declaring weight ranges or setting optical size, width, or custom axes. Choose a deliberate treatment for italics if the family has none. Inspect OpenType capabilities before relying on tabular numerals; CSS cannot add glyph features that are absent. Right-align financial columns regardless.

Review real body text at comfortable sizes and contrast, not only a large title. Keep line lengths and vertical spacing coherent; avoid tiny all-caps labels, aggressive tracking, or a different font on every card. These are design starting points, not reasons to override the user's requested direction.

Run the project's existing build/browser checks, verify the downloaded face actually renders, and inspect desktop/mobile wrapping. Keep this scoped to typography; no model calls or research mutations are needed to validate a font migration.
