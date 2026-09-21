---
name: online-ai-evaluation
description: "Score observed production operations asynchronously with explicit eligibility, sampling, and deduplication. Use when monitoring AI quality on live traffic or historical traces."
---

# Online AI Evaluation

Define the operation or conversation that receives the score, the decision it informs, and the available evidence. Prefer verified outcomes or deterministic checks when possible. Use a calibrated judge only for qualities that need semantic assessment.

## Select and score the correct unit

Inspect representative matching traces before enabling a selector. Pin operation names/types, environment, completion state, and exclusions. Avoid scoring both a parent summary and every child as independent answers. Exclude evaluator-generated traces from recursively triggering the same evaluation.

Use a stable target revision plus evaluator version as a deduplication key. Distinguish first scoring, retry after infrastructure failure, and intentional re-scoring under a new version. Preserve historical scores instead of silently overwriting the measurement definition.

Define when an operation is ready: completed output, available retrieval evidence, or a declared conversation window. Late events may require a revised score. Missing/redacted evidence should produce an explicit unresolved state rather than a fabricated pass or fail.

## Keep the service and measurement observable

Set asynchronous queue concurrency, retry limits, cost controls, and backlog handling. Report eligible, selected, attempted, valid, failed, and pending counts. Sampled scores need a known selection policy; review-only failures cannot estimate overall quality.

Keep observational scoring separate from inline blocking controls. A delayed verdict cannot undo an already executed action. Deliver selector/evaluator versions, a sample audit, score lineage, coverage/lag dashboard, and the change procedure. Live configuration changes use the destination project's existing authorization, not authority implied by this skill.

## Sources and adaptation

- [Online](https://langfuse.com/docs/evaluation/get-started/online)
- [Evals](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
