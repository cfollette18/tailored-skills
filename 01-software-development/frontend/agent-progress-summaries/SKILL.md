---
name: agent-progress-summaries
description: Add frequent, useful public activity summaries to agent chat, including the UI often called thinking traces. Use when users want clearer progress under tool calls, live elapsed time, or concise explanations of what an AI is doing without exposing private reasoning.
---

# Agent progress summaries

Help the user understand what operation is underway and what has actually returned. “Thinking traces” in this UI means public activity summaries, not private chain-of-thought, hidden prompts, or a reconstructed internal monologue. Never present generated narration as observed model reasoning.

## Choose trustworthy inputs

Use tool start/end events, verified operation names, safe argument fields, known result metadata, and the harness's explicitly public commentary channel. Prefer a small deterministic description catalog for frequent operations. If public model commentary already exists, preserve it as commentary; do not repurpose a private reasoning stream.

Examples and adaptation guidance are in [activity catalog](references/activity-catalog.md). Keep templates outside visual components so another product can change tools and language without replacing chat layout.

## Cadence tied to work

1. On request acceptance, show a short processing state.
2. On each actual tool start, show its purpose-based activity beneath that card.
3. While a call remains active, update elapsed time at a low cadence; Namakan uses five seconds. A timer is a local duration display, not a heartbeat from the model or evidence of another completed step.
4. On an actual result, replace the wait with the observed outcome. Do this immediately, without minimum spinner time.
5. Between calls, show a neutral ongoing state plus finished-call count when helpful. Count terminal events, not assumed stages or an invented total.
6. End the active state on the observed terminal turn event. Stop stale timers when reopening old chats or moving to another turn.

Do not rotate through “analyzing / verifying / synthesizing” on a timer. Do not append an endless transcript line every few seconds. Update a compact existing status; append narrative only when there is new meaningful information. A long-running operation can say it is still running, or that no recent activity has been received, without claiming the provider is healthy.

## Keep language calibrated

Distinguish “request finished,” “returned N items,” and “operation succeeded.” Use the strongest statement the result contract supports. Tool completion does not prove correctness, review approval, publication, or successful delivery. Failed calls get clear, safe summaries; missing information stays missing. Do not expose arbitrary source text, credentials, signed URLs, or provider exceptions through a purpose string.

An optional server-supplied purpose should use a bounded public field with explicit provenance and a fallback. Reusing another model to summarize every result adds latency/cost and can invent intent; do that only if the product requires it and the summaries can be checked against events.

## Accessible progress

Announce meaningful status changes through a focused polite live region. Keep seconds ticking outside that announcement to avoid constant speech. Do not make the entire transcript a live region or depend on a spinner/color to carry state. WAI's [status-message guidance](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) explains the programmatic-announcement requirement; batching and cadence here are product recommendations.

Verify that paused/failed/completed turns stop looking active, elapsed time freezes when a call ends, and a new turn does not revive earlier interrupted calls. Test with a controllable clock and event fixtures, not delays or paid inference. Use [inline-tool-call-ui](../inline-tool-call-ui/SKILL.md) for card presentation and [streaming-chat-lifecycle](../streaming-chat-lifecycle/SKILL.md) for reliable state.
