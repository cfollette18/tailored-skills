---
name: distributed-agent-tracing
description: "Instrument causally connected agent, model, retrieval, and tool work across services and background jobs. Use when traces split, nest incorrectly, or double-count operations."
---

# Distributed Agent Tracing

Define a trace boundary from the operation users wait for. Keep session, logical run, execution attempt, span, and tool-call identities distinct. A conversation can group several turn traces; retries remain separate attempts within the same logical operation.

## Build the instrumentation contract

Map the entry point, orchestrator, each model invocation, retrieval, tool execution, queue boundary, and final outcome. Give spans stable operation names and put request identifiers in attributes. Capture the actual model/tool version, duration, status, usage availability, and safe evidence references. Record public actions and outcomes; hidden model reasoning is not required telemetry.

Use the runtime's context carrier for synchronous and asynchronous calls. Inject/extract context at HTTP and queue boundaries; verify what survives serialization and worker restart. For fan-in or resumed work with several causal predecessors, record links instead of inventing a single parent or keeping one span open indefinitely. Context correlation never grants access to the referenced resource.

Inspect existing automatic instrumentation before adding wrappers. One model invocation should have one accountable usage record; distinguish retries, parent summaries, and cache hits so costs are not counted twice. Treat tool calls that return application-level errors as failed operations even when the transport succeeded.

## Verify and deliver

Exercise a nested call, parallel siblings, a queue hop, retry, cancellation, and export failure. Inspect parent relationships and attempt IDs at the receiving backend, not only in process logs. Ensure exporter shutdown has a bounded flush and telemetry failure does not create unbounded request delays.

Deliver a boundary/attribute map, synthetic trace evidence, export configuration, and known gaps. Map this contract to OpenTelemetry or the selected platform only after inspecting its installed integration and current conventions; vendor field names belong in the adapter.

## Sources and adaptation

- [Context](https://opentelemetry.io/docs/concepts/context-propagation/)
- [Good Traces](https://langfuse.com/docs/observability/best-practices)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
