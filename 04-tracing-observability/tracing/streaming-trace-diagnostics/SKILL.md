---
name: streaming-trace-diagnostics
description: "Diagnose partial, duplicated, delayed, or disconnected AI streams using correlated runtime events. Use when user-visible streaming behavior disagrees with server execution."
---

# Streaming Trace Diagnostics

Separate transport delivery, runtime progress, and durable turn state. A disconnected socket is not proof that the agent stopped; a closed stream is not proof that a result was saved.

## Capture useful events

Record logical turn, execution attempt, event ID/sequence, event kind, source node/call identity, server timestamp, and client receipt timestamp. Keep token events, state updates, tool results, public progress summaries, interrupts, and terminal outcomes distinguishable. Prefer summarized counts and timings to retaining every text fragment.

Measure request queue time, time to first event, time to first useful content, tool wait, final output, and persistence acknowledgement separately. Cross-machine clocks may differ; use monotonic timing for local durations and describe clock uncertainty when joining events.

At reconnect, use the transport's cursor or durable replay contract. Deduplicate by stable event identity scoped to its attempt. State snapshots replace a versioned state; deltas require the expected base. A user retry creates a new attempt even if it repeats the same words.

## Diagnose and verify

Compare server event production with transport delivery and UI application. Exercise disconnect before completion, duplicate delivery, out-of-order events where supported, backpressure, cancellation, and interrupted human review. Confirm exactly one user-visible terminal disposition per attempt after reconciliation.

For LangGraph, inspect the installed streaming API and selected mode/projection; message chunks and graph state events are not interchangeable. Filter internal/debug events before exposing public activity. Describe tool purpose and observed progress without fabricating hidden reasoning or timer-based accomplishments.

Deliver the event contract, a timeline locating the missing boundary, and a regression fixture. Do not enable unrestricted payload debug logging merely to investigate a missing spinner.

## Sources and adaptation

- [Streaming](https://docs.langchain.com/oss/python/langgraph/streaming)
- [Good Traces](https://langfuse.com/docs/observability/best-practices)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
