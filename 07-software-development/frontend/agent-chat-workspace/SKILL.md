---
name: agent-chat-workspace
description: Build or adapt a calm agent chat workspace with a focused conversation, anchored composer, inline tool activity, and responsive navigation. Use when replicating Namakan's chat look and feel for another product or composing these patterns into a new AI interface.
---

# Agent chat workspace

Reproduce the interaction hierarchy, then adapt the product identity. This pattern comes from the owner-approved Namakan chat: a light workspace, a narrow reading column, compact user bubbles, open assistant prose, useful activity updates, and tool details that expand below their own controls. It is a product pattern, not a mandate to use Namakan's names, palette, financial tools, provider, or framework.

## Start with the target product

Inspect its shell, router, tokens, conversation store, stream, and existing components. Identify what the user does, what outputs they revisit, and which tools are visible. Keep the existing stack and functional behavior unless the task calls for a change. A visual port does not authorize new accounts, model providers, paid requests, or deployment.

Specify the small adaptation surface: product identity, navigation destinations, useful starter prompts, optional composer controls, tool labels/purposes, output types, and mobile breakpoint. Prefer a working vertical slice—send, observe a tool, read a response, reopen the conversation—over a static landing page.

## Preserve the hierarchy

- **Shell:** quiet navigation with recent conversations; stable main area. Keep destinations tied to user outcomes. Internal methodology/debug catalogs do not need permanent top-level navigation. Namakan's owner removed the Frameworks destination and researcher-ready sidebar indicator; apply the underlying simplification rather than banning those concepts in every product.
- **Welcome:** a restrained identity, short outcome-oriented heading, composer, and a few distinct prompts that seed the draft. Do not auto-submit a paid/action-bearing request when a suggestion is clicked.
- **Conversation:** user messages in compact, right-aligned soft surfaces; assistant answers as readable prose on the main canvas. Keep long tables/code within the reading column. Avoid enclosing every paragraph in a card.
- **Composer:** match the reading width. Anchor it beneath the scrollable transcript once a conversation starts. Keep the draft while switching views. A small send control becomes a clearly labelled stop control while work is active.
- **Activity:** compact tool rows between messages. Each has an adjacent public progress sentence; clicking reveals a short purpose/result below the row. Preserve reading position instead of opening a competing right sidebar.

Use [visual specification and source map](references/namakan-reference.md) for dimensions, token roles, exact source-file locations, and the distinction between observed implementation and recommended adaptations.

## Apply the relevant companion

- Tool disclosure geometry and state: [inline-tool-call-ui](../inline-tool-call-ui/SKILL.md).
- Public “thinking traces,” useful cadence, and accurate copy: [agent-progress-summaries](../agent-progress-summaries/SKILL.md).
- Streaming, replay, cancellation, and stale events: [streaming-chat-lifecycle](../streaming-chat-lifecycle/SKILL.md).
- Use the retained [restrained color guide](../../../anti-ai-slop/color/restrained-color-design/SKILL.md) and [motion quality guide](../../../anti-ai-slop/motion/motion-quality-review/SKILL.md) when those aspects need work. The visual reference below covers the relevant shell and motion values; do not impose a full redesign on a narrow request.

## Portable reference

Open [chat-workspace-reference.html](assets/chat-workspace-reference.html) in a browser. It is a self-contained, editable fixture with no dependencies, network requests, credentials, or real conversations. It demonstrates empty/completed/running/failed/stopped states, inline disclosure, elapsed activity, a responsive drawer, and two example token palettes. Its controls explicitly identify it as a demo. Replace the scripted transport with the target product's event adapter; never ship simulated progress as real work.

The reference deliberately uses system typography and text branding. For Namakan's exact typography/icon direction, use the existing [Cabinet Grotesk](../../../anti-ai-slop/typography/cabinet-grotesk-font/SKILL.md) and [Phosphor](../../../anti-ai-slop/icons/phosphor-icons/SKILL.md) guides. No product logo, font binary, or proprietary motion asset is bundled.

## Verify the port

Use the [replication checks](references/replication-checks.md). Check realistic long content, active tools, failures, saved chats, keyboard operation, reduced motion, and a narrow viewport. Validate with fictional fixtures; report separately what was verified against the actual provider. Finish with the implementation, relevant checks, and any functional limits—not just a mockup.
