---
name: streaming-chat-lifecycle
description: Implement or repair agent-chat event rendering, persistence, replay, cancellation, and turn-scoped tool state. Use when connecting a chat UI to a real stream or fixing duplicate messages, stale spinners, lost drafts, and reconnect behavior.
---

# Streaming chat lifecycle

Preserve the user's conversation across asynchronous work. Inspect the current transport and persistence model first. Reuse the application's runtime and account handling; this skill does not call for replacing the model provider or adding a second agent harness.

## Separate state domains

Distinguish conversation identity, turn/run identity, individual tool calls, and local UI state. Tool cards are projections of durable events; expansion and scroll position are local interaction state. A completed tool does not finish the turn. A lost connection does not prove the model stopped. A closed browser does not necessarily cancel the job.

Read [event contract](references/event-contract.md) when defining an adapter or reducer. Read [transport and recovery](references/transport-and-recovery.md) when wiring streaming, persistence, or stop behavior. These are portable recommendations; adapt them to the target backend's real guarantees.

## Render from observed events

Persist before broadcast when the product promises replay. Use stable event identities to deduplicate, and correlate tool results with conversation/turn/call identity. Buffer or reconcile results that arrive before their start. Keep terminal status explicit. Old unfinished tools must not become Working merely because a follow-up turn is active.

Public commentary, tool activity, and final assistant output are different event types. Namakan streams tool/commentary events and delivers the final answer on completion. If the target provider supports prose deltas, add message identity and finalization semantics instead of appending each delta as a separate answer. Do not expose private reasoning callbacks to fill perceived gaps.

## Preserve interaction

Keep drafts when switching workspaces or opening an artifact. Retain the reader's position when inspecting earlier content; auto-follow only near the bottom or after the user's own send. Show a jump-to-latest control when new content accumulates off screen. Inline tool expansion must not force bottom scroll. Guard against late events from a previously opened conversation.

Keep sending, running, stopping, reconnecting, failed, cancelled, and completed states distinct. Disable duplicate submissions while the request is being accepted; do not automatically retry a side-effecting tool on a network timeout. A retry policy must match the operation's idempotency and backend guarantees.

For tool-card UX use [inline-tool-call-ui](../inline-tool-call-ui/SKILL.md); for accurate waiting language use [agent-progress-summaries](../agent-progress-summaries/SKILL.md).

## Verify without live actions

Use a fixture transport for duplicated/out-of-order events, two parallel calls, reused call IDs in different turns, reconnect gaps, an old interrupted turn followed by a new one, stop during a call, and reload after completion. Test the actual persistence/stream boundary separately when changing it. Clean up streams, subscriptions, timers, observers, and animations on unmount. Do not create real messages, integrations, or training examples merely to validate presentation.
