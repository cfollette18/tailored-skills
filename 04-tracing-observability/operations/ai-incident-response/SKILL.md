---
name: ai-incident-response
description: "Investigate production AI failures using correlated evidence across input, retrieval, model, tools, state, and permissions. Use for containment, reproducible diagnosis, targeted fixes, and regression-backed recovery."
---

# AI Incident Response

Separate observed facts, hypotheses, and proposed recovery. Do not begin with a prompt rewrite merely because the visible symptom is a bad answer. Stale sources, wrong state versions, permission filters, schema mismatches, missing results, and timeouts can be the cause.

Use [incident.json](assets/incident.json). Record detection time, affected workflow, severity decision, reporter/owner, affected-user estimate, running release manifest, and controlled evidence references. Keep private traces/customer data out of public artifacts.

Trace one failing request end to end: input → retrieval/filter/version → model invocation → tool/authorization → handoff state → final output. Compare recent code, prompt, model, data, and configuration changes. Locate the first observed divergence and reproduce it in an isolated case.

Complete authorized containment: rollback, feature restriction, dependency isolation, or human routing appropriate to the failure. Record expected consequences and completed side effects that remain. Do not interrupt unrelated active work or replay writes blindly. If a needed action exceeds existing authorization, prepare the concrete change and explain the missing approval.

Make the smallest correction supported by evidence. Run the failing case and relevant regressions; verify staged recovery against agreed criteria. Add an adjudicated recurrence case, document root cause versus contributing factors, assign follow-ups, and verify alerting could detect the same failure. Close only with observed recovery evidence; missing evidence remains open.

## Framework sources

[docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [docs/multi-agent-orchestration.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md), [templates/incident.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/incident.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../../01-software-development/production-ai-framework-map.md).
