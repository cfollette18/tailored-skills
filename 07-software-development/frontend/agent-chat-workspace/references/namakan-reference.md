# Namakan reference: what to retain and what to adapt

Inspected 2026-09-21 in the owner-approved local `investing-researcher` workspace. These are implementation observations, not claims about another vendor's UI or universal design standards.

## Visual recipe

| Element | Observed Namakan treatment | Adaptation decision |
|---|---|---|
| Desktop shell | Approximately 242 px quiet sidebar, white main canvas | Size to labels and host application; avoid an extra tool-details rail |
| Reading column | Around 730–760 px; transcript and composer align | Keep long-form prose readable; wide tables scroll inside the column |
| Mobile | Sidebar becomes a drawer around 800 px; roughly 20 px transcript gutters | Test actual content and virtual keyboard; retain all controls |
| User message | Content-sized, right aligned, at most 85% desktop width; soft surface; 19 px corners with a smaller bottom-right corner | Distinguish speaker without large contrasting blocks |
| Assistant message | Open prose, small identity above, 27–35 px space between answers | Use the target product's identity; do not copy Namakan's wordmark |
| Composer | White surface, 1 px quiet border, 19 px corners; 17 px inset; stronger focus outline | Text entry must remain obvious without persistent heavy shadows |
| Tool header | Full reading width, 8 px corners, about 10 × 12 px padding; icon/name/status/chevron | One keyboard-operable disclosure; no hover-only information |
| Tool snippet | Purpose and Result/Status, 12 px text, 1.8 line height, about 14–16 px inset | Keep it brief; report-sized results belong in the answer or an artifact |
| Progress | 11 px supporting sentence under the tool, optional 10 px elapsed time | Maintain readable contrast; enlarge for the product's audience |
| Typography | Cabinet Grotesk; 13 px chat body at ~1.9 line height; 44 px welcome heading | These are measured source values, not accessibility minima; 14–16 px body may suit other products better |
| Icons | Phosphor, mostly regular; tiny status glyphs are secondary | Keep one family; expose labels and meaningful states |

Namakan's palette is white/oat/navy with small Lava accents. Reuse semantic roles rather than copying hex values. Minimum roles: canvas, surface, surface-subtle, surface-hover, text, text-secondary, text-muted, border, border-strong, focus, selected, on-selected, action, on-action, success, warning, danger, disabled-surface, disabled-text. Do not assume a red action means failure. Supply status labels independently of color.

## Feel and motion

Inputs change state immediately. Namakan's current motion tokens use approximately 120 ms response, 180 ms selection, and 240 ms sidebar movement; optional icon gestures are separately authored. Tool disclosure uses ~140 ms opacity/small offset and a ~160 ms chevron turn. These are source values, not required timings. Preserve a static reduced-motion state. Do not delay text, navigation, or tool results to finish an animation. Wait for animations to settle before judging screenshots.

Keep the composer and draft stable when navigating. In a production port, follow new activity only if the reader is near the bottom; otherwise offer Jump to latest. Inline expansion should preserve the clicked control's location. This scroll policy is a recommended improvement, not a claim that all source behavior already implements it.

## Source map

Paths are relative to the Namakan `investing-researcher` repository; it is an optional reference, not a dependency of these skills.

| Source | Useful implementation |
|---|---|
| `web/src/main.tsx` | Welcome/composer, transcript, public commentary, saved chat navigation |
| `web/src/ToolActivity.tsx`, `toolSummaries.ts` | Metadata-derived purpose/progress and safe result summaries, inline disclosure, timer cleanup, current-turn tool activity |
| `web/src/tool-activity.css` | Header/snippet/progress geometry and reduced motion |
| `web/src/style.css`, `theme.css` | Reading width, message hierarchy, semantic color roles |
| `web/src/SidebarNavigation.tsx`, `motion.css` | Stable navigation and interruptible icon gestures |
| `src/investing_researcher/web.py` | Durable local events, SSE replay and cancellation |
| `scripts/namakan_worker.py` | Public tool/commentary callbacks; private reasoning callbacks disabled |
| `web/tests/tool-activity.spec.ts`, `app.spec.ts`, `motion.spec.ts` | Fixture-driven behavior and responsive checks |

## Keep source facts distinct from extensions

The source is a local single-user app. Its event ID is globally increasing; explicit turn IDs in the portable event contract are an adaptation for more general products. Tool callbacks stream during work; the final assistant answer is delivered at completion. Token-by-token prose is optional and should not be falsely claimed as part of this reference. Its timer shows elapsed time, not provider health or percent complete. Its small deterministic summary catalog is not model reasoning or proof of a successful external operation.

Do not copy local credentials, profiles, research records, user prompts, account labels, or localhost deployment assumptions. The bundled demo contains only fictional content and introduces a safer jump-to-latest policy as a portable example.
