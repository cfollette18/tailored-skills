---
name: navigation-and-view-transitions
description: Implement responsive sidebar, tab, drawer, popover, and page transitions with stable focus and interruptible state. Use when adding or repairing navigation motion, especially shared selection indicators and collapsible sidebars.
---

# Navigation and view transitions

Keep navigation useful during motion. Inspect the application's actual state, routing, scroll, focus, and data-loading behavior before adding transitions. Preserve URL/history behavior and drafts; a visual improvement should not remount expensive content or lose user input.

## Selection is separate from hover

Keep persistent selected state distinct from transient hover. A moving selection background can create continuity, but a sidebar does not inherently require one. If used, render a single layer behind stable labels and icons. Measure the actual target bounds, account for scroll and responsive layout, and retarget from the current visual position during rapid input. Do not animate each row's layout independently.

Use semantic state appropriate to the widget. Site navigation normally uses links with `aria-current`; an actual tab widget needs the corresponding tab roles, panel association, and keyboard pattern. Do not add tab semantics merely because the owner calls sidebar items “tabs.”

Update selection and load/show content immediately. Optional icon choreography runs independently. Frequently repeated keyboard movement should not wait for the indicator. Avoid a long exit-before-enter sequence that serializes every page click.

## Sidebar and drawer geometry

Decide whether the surface pushes content, overlays it, or collapses to a rail; these are different layouts. Preserve the intended final geometry and reading position. A transform can move an overlay cheaply, but it does not reclaim layout space for a collapsing desktop sidebar. A width/grid transition may be reasonable on a small layout; profile realistic content. FLIP/shared layout is another option, with text-distortion checks.

Manage visibility across exit: a surface cannot both disappear immediately through `display:none` and animate visibly out. Remove its interactive descendants from focus when closed, and transfer focus before making the currently focused subtree inert. Modal drawers need correct modal semantics and focus containment; desktop navigation is not automatically a modal.

Use the surface's real origin. Popovers should emerge from their trigger; a side drawer should maintain edge continuity. Usually 140–280 ms is a useful starting range, with large surfaces near the upper end. These are recommendations, not measured Muse values.

## View changes and content

For sibling workspaces, an immediate replacement or a short opacity transition often preserves speed. Use directional motion only when the information hierarchy warrants it. Keep a stable shell. Do not replay list staggers, charts, or streamed paragraphs on every route change. Keep loading skeletons truthful and transition independently of network latency.

If using Motion, scope shared layout IDs and keep labels outside the transformed selection layer. If using the native View Transition API, feature-detect and verify snapshot behavior, rapid navigation, and reduced motion. Avoid combining several competing route-transition engines.

## Validate

Try A→B→C rapidly, A→B→A before settlement, repeated collapse/expand, resize while moving, a scrolled navigation list, keyboard activation, and mobile. Confirm the final selected state, content, focus, and URL agree. With reduced motion enabled, navigation remains complete and readable with immediate geometry or minimal opacity.

Primary references: [Motion layout](https://motion.dev/docs/react-layout-animations), [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API), [origin and easing](https://emilkowal.ski/ui/good-vs-great-animations). Provenance is in `SOURCE.json`.
