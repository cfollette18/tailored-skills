---
name: ai-error-analysis
description: "Inspect AI traces and experiment failures to produce an evidence-based failure taxonomy and prioritized fixes. Use when aggregate scores do not explain what is going wrong."
---

# AI Error Analysis

Choose the sampling frame and decision: understanding common failures, investigating a regression, or examining a rare consequential case. Keep representative samples distinct from deliberately selected complaints or failures.

## Read before categorizing

Inspect the task, authoritative context, retrieved data, model output, tool calls, state transitions, and verified outcome. Note the first observed divergence in plain language. Separate observed facts, suspected mechanism, missing evidence, and impact. Do not explain a model failure by inventing private internal reasoning.

Group similar notes into categories that imply different interventions. Split stale source data from retrieval misses, and wrong tool arguments from failed tool execution. Treat evaluator mistakes and missing instrumentation as their own categories. Permit multiple labels when failures have multiple causes, while identifying the primary divergence when supported.

Review ambiguous cases and refine the taxonomy against fresh examples. Preserve category version and example evidence so reclassification can be audited.

## Measure and act

Report counts and denominators within the inspected sample, unknown cases, severity, and sampling limitations. Multiple-label percentages can sum beyond 100%; explain the unit. A failure-enriched review set cannot establish the production failure rate.

For each category choose a code/data/prompt fix, a regression case, a calibrated evaluator, better instrumentation, or continued observation. Tie priority to user impact and observed frequency rather than an arbitrary severity multiplier.

Deliver annotated examples, taxonomy definitions, unresolved hypotheses, and a prioritized backlog with verification evidence required for each fix. Route active production containment through the incident procedure; analysis alone does not authorize replaying tools or changing production state.

## Sources and adaptation

- [Errors](https://langfuse.com/academy/monitoring/error-analysis)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
