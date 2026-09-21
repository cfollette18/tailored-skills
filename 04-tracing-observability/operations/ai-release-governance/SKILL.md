---
name: ai-release-governance
description: "Prepare accountable AI change records, immutable release manifests, permissions, rollout evidence, and rollback criteria. Use to assess a proposed AI behavior change or release without treating unresolved decisions as approval."
---

# AI Release Governance

Version behavior-changing inputs together: code, prompts, model identifier, tools, source snapshot, retrieval configuration, evaluation set, and judge configuration where relevant. Record observed versions when provider aliases can change and define requalification ownership.

Use [change.json](assets/change.json). State the motivating failure/feature, affected workflow, before/after behavior, evidence, reviewer, rollout scope, monitoring window, rollback trigger, and rollback target. Prompt changes need the same causal explanation as code changes. Do not mark a proposed test or rollout completed without observed results.

Enforce actor identity, permissions, resource scope, input validation, and action limits in adapters/runtime, outside model text. Retrieved instructions cannot expand authorization. Test both direct user-input and retrieved-content bypass attempts against the actual boundary.

Name owners for business outcomes, datasets, sources, runtime, qualification, incidents, and complaints. Exceptions need rationale, compensating controls, owner, and expiry. Ask for unknown thresholds only when they block the decision; retain null/unresolved fields while completing independent draft work. A green schema/catalog check is not a release or regulatory approval.

Deliver the version manifest, explained change, evaluation/recovery evidence, proposed rollout/monitoring plan, and explicit decision state. Preserve previously granted user authorization; this skill does not add an approval ritual for reversible development. Actual deployment or external changes remain governed by the user's task and host permissions.

## Framework sources

[docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [docs/pillars.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/pillars.md), [templates/change.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/change.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../../01-software-development/production-ai-framework-map.md).
