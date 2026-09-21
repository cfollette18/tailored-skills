---
name: human-feedback-review
description: "Collect attributable feedback and adjudicate AI outputs with a stable rubric. Use for annotation queues, disagreement review, and turning feedback into reliable evaluation labels."
---

# Human Feedback and Review

Separate product feedback, verified task outcome, and expert quality annotation. A thumbs-down identifies a review candidate; silence is missing feedback, and a satisfied user may still receive an incorrect answer.

## Design the review unit

Attach feedback to the exact answer, turn, tool outcome, or conversation revision reviewed. Record source, timestamp, rubric version, reviewer role or controlled identifier, and supporting evidence. Preserve corrections as versions rather than silently replacing the original label.

Provide reviewers enough input, authoritative context, output, and allowed-action policy to decide. Hide candidate/model identity when it could bias a comparison. Define explicit labels for insufficient evidence, ambiguous policy, and outside expertise. Reviewers should not infer missing evidence from plausible prose.

For new or changing rubrics, independently annotate an overlapping sample, inspect disagreements, and adjudicate before scaling. Distinguish rubric ambiguity from reviewer error. Keep the original labels and the resolved decision so apparent agreement is not manufactured by overwriting dissent.

## Operate the queue

Define selection criteria, routing owner, access controls, and aging/timeout behavior. A review backlog is not approval to execute a proposed action. Operational approval workflows belong in the application's authorization layer; quality review alone does not authorize a tool.

Report review coverage, nonresponse, selection bias, disagreement, and adjudicated failure patterns. Before promoting examples into regression datasets, remove unnecessary personal data and confirm the expected behavior is reproducible. Deliver the rubric, queue contract, attribution fields, and an export with unresolved cases separated from scored cases.

## Sources and adaptation

- [Evals](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Errors](https://langfuse.com/academy/monitoring/error-analysis)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
