---
name: ai-quality-monitoring
description: "Design actionable AI quality, latency, cost, and evaluator-health monitoring. Use when dashboards obscure regressions, sample bias, or failures in the measurement pipeline."
---

# AI Quality Monitoring

Start with the user outcome and decisions operators must make. Separate task success, dependency health, perceived latency, resource cost, and measurement health.

## Define metric contracts

For every metric name the eligible population, numerator, denominator, time window, source, label/version, owner, and action. Keep unresolved targets explicit. A model judge score is an estimate about a quality dimension, not a verified business outcome.

Track latency distributions and their components: queueing, model/tool time, first useful response, and end-to-end completion. Account for parallel work when comparing wall-clock duration with summed span durations. Distinguish reported token use from estimates and unavailable usage; avoid counting parent totals and child calls twice.

Segment quality by task, release, policy/data version, and meaningful user slices with adequate coverage. Keep unbounded IDs out of metric labels. Annotate releases and sampling/evaluator changes so a measurement change is not mistaken for an application regression.

## Alert and investigate

Choose thresholds, observation windows, minimum coverage, and escalation from the operational need. Route alerts to an owner and a diagnostic trace/query. Distinguish service failure, quality drift, traffic-mix shift, missing telemetry, and evaluator outages before proposing a fix.

Monitor export drops, redaction failures without payload disclosure, evaluator lag, invalid scores, and review backlog. Healthy application scores with zero evaluation coverage should be visibly unknown. Deliver metric definitions, dashboard queries, alert/runbook mappings, and synthetic checks that exercise both a real defect and a broken measurement path.

## Sources and adaptation

- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)
- [Sampling](https://opentelemetry.io/docs/concepts/sampling/)
- [Online](https://langfuse.com/docs/evaluation/get-started/online)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
