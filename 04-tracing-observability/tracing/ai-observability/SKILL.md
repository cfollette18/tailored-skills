---
name: ai-observability
description: "Design correlated, privacy-aware traces and operational diagnostics for an AI workflow. Use to connect retrieval, model, tools, guardrails, handoffs, and final outcomes or diagnose why an agent request failed."
---

# AI Observability

Make a failed request reconstructable from observable actions. Private chain-of-thought is neither required evidence nor a substitute for operation/version metadata. Inspect current instrumentation before adding another telemetry layer.

Use [trace.json](assets/trace.json) as a contract sketch. Correlate ingress, retrieval, model invocation, tool execution, guardrails, handoffs, and final outcome with stable request/workflow/span IDs. Connect the trace to the release manifest.

For retrieval, retain document/version/filter/index references. For tools, record operation, argument classification, authorization outcome, duration, error category, retries, and idempotency key where applicable. For model calls, capture model/prompt versions, tokens, termination reason, and a labelled cost estimate. Public chat progress is a presentation of selected events, not the complete operator trace.

Redact before export. Use controlled evidence references and hashes where full payload retention is inappropriate. Define access and retention by data category; answer-serving content and telemetry may share infrastructure but have different policies. Never copy customer traces or credentials into the skills/framework repository.

Define alert condition, window, affected workflow, owner, baseline comparison, relevant trace IDs, and recent changes. Ask for unknown operating thresholds instead of manufacturing production defaults. Runtime code, not a prompt, enforces time/retry/cost budgets. Decide what happens if telemetry itself fails.

Acceptance exercise: inject a dependency failure in a controlled test, find the request, isolate the failed operation, verify the fallback, and identify its owner. Deliver a trace-field map, instrumentation gaps, alert ownership, and observed diagnostic evidence. Use current documentation and the installed observability skill for SDK changes; this contract does not authorize sending data to a new service.

## Framework sources

[docs/pillars.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/pillars.md), [docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [templates/trace.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/trace.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../../01-software-development/production-ai-framework-map.md).
