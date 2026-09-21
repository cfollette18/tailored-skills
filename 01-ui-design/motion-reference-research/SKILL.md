---
name: motion-reference-research
description: Analyze a reference website or supplied screen recording to reconstruct interface motion, timing, triggers, and implementation options. Use for frame-by-frame motion research and fidelity studies; distinguish observed behavior from inferred code and proposed adaptations.
---

# Motion reference research

Use the supplied reference and the user's stated attraction as the starting point. Inspect the live interaction when available; use a recording when authentication, reproducibility, or a fleeting gesture limits access. Do not claim to have operated a signed-in interface when only its landing page or public code was inspected.

## Build an evidence record

Record capture date, viewport/recording dimensions, duration, frame timestamps, the interaction region, and which states are visible. A video's nominal `r_frame_rate` can be misleading for variable-frame-rate screen recordings. Use decoded presentation timestamps for timing. A resampled 20 fps filmstrip may duplicate or omit original frames; label it accordingly.

Crop to the interaction under study. Retain the original privately and keep unrelated account/conversation content out of shareable research. Do not publish the recording just because it was supplied for analysis. Preserve provenance through a source hash and descriptive capture ID rather than embedding personal filesystem paths in a reusable skill.

Use [scripts/extract_motion_frames.py](scripts/extract_motion_frames.py) when a repeatable local extraction is useful. It requires Python 3.11+, ffmpeg, and ffprobe, samples by actual source timestamps, writes cropped frames and a contact sheet, and records timestamp provenance. See [the extraction guide](references/extraction.md) for arguments and limitations.

## Separate three kinds of claim

1. **Observed:** dots appear, a glyph narrows edge-on, a page folds, a check redraws, a tooltip appears beside a stationary control.
2. **Source-confirmed:** a specifically identified public component uses an animation player, static fallback, or spring configuration. Restrict the claim to that component and capture date.
3. **Proposed:** CSS 3D transforms, SVG paths, masks, WAAPI, springs, or authored timelines that could reproduce the appearance. State when parameters are starting points.

Do not uniquely infer easing curves, spring constants, implementation libraries, pointer-to-feedback latency, or loop policy from a short compressed recording. Report intervals and uncertainty. A flattened icon might be 3D rotation or a 2D vector shape change. A successful download of a generic animation wrapper does not prove every sidebar icon uses it.

## Reconstruct the choreography

For each interaction, identify the trigger, moving subparts, anchored parts, order of motion, visible action window, settled state, interruption behavior, and accompanying surface/tooltip/page change. Mark absent evidence explicitly: a hover recording may not show sidebar collapse, keyboard focus, long-hover replay, touch, or reduced motion.

Compare the reference with the target product's icon family and task frequency. Preserve the semantic gesture rather than copying unrelated branding. Distinguish immediate functional feedback from a longer optional decorative sequence. Build a small isolated comparison when it helps assess the proposal; keep the production app unchanged if only research is requested.

Deliver timestamped observations, primary source links, implementation choices with tradeoffs, a target-specific mapping, and acceptance checks. Slow motion helps explain mechanics; judge the result at normal speed and actual size.
