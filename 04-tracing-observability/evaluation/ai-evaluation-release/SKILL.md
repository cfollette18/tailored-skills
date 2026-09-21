---
name: ai-evaluation-release
description: "Design representative AI evaluation cases, calibrated checks, and evidence-based release comparisons. Use for agent-quality regression suites and release decisions, including tool behavior, unavailable judges, and subgroup failures."
---

# AI Evaluation and Release

Evaluate the business behavior and the execution path. Fluent prose alone is not a passing outcome. Inspect the existing workflow, authoritative sources, and failure history before changing a prompt or score.

## Build cases and checks

Use [evaluation-case.json](assets/evaluation-case.json). Each case names input/context, required and forbidden behavior, authorized tools, expected escalation, evidence, owner, and provenance. Cover ordinary, ambiguous, missing/stale/conflicting data, dependency failure, unauthorized, and repeated requests.

Separate development, regression, and held-out release sets. Preserve old case versions when policies change; adjudicated real failures can become regressions without silently rewriting the historical expectation. Protect private cases and trace data from public repositories.

Use deterministic checks for verifiable constraints, semantic rubrics against supplied evidence, and behavioral checks over authorization, repeated actions, required steps, errors, and tool budgets. Calibrate any model judge against domain-reviewed examples and record disagreement. Missing, malformed, or unavailable judge output is an evaluation error or unresolved state, never a pass. Self-reported model confidence is not a calibrated probability.

## Compare and decide

Pin candidate and baseline configurations, case set, prompts, model identifiers, tools, retrieval snapshot, judge versions, time, and costs. Compare identical cases, show subgroup failures as well as aggregates, and distinguish infrastructure failure from quality failure. Use focused tests while developing, then the agreed release suite for promotion.

Request owner decisions for thresholds, sample sizes, zero-tolerance categories, and exception policy when needed for an actual release decision. Until then, produce the supported results and unresolved decisions. A waiver needs owner, rationale, expiry, and compensating controls. Do not treat catalog/schema validation as proof of agent quality.

Deliver case definitions, check/rubric versions, comparison results, failure categories, and the supported release disposition. If using Langfuse or another product, consult the available vendor-specific skill/docs for API implementation; this guide does not prescribe a platform or create remote datasets automatically.

## Framework sources

[docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [docs/pillars.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/pillars.md), [templates/evaluation-case.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/evaluation-case.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../../01-software-development/production-ai-framework-map.md).
