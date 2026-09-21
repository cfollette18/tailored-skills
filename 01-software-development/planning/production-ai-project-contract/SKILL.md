---
name: production-ai-project-contract
description: "Plan or assess a production AI workflow across evaluation, observability, data foundations, orchestration, and governance. Use to turn a proposed AI use case into an owned project contract and evidence-based milestone plan."
---

# Production AI Project Contract

Start from the business workflow, not a model or vendor selection. Identify whether the user wants a plan, design review, release assessment, or incident investigation. Use available project evidence before asking questions; ask only for missing decisions that change the next useful step.

## Define the contract

Use [project.json](assets/project.json) as a draft structure. Define the user, start/completion conditions, business and technical owners, permitted and forbidden actions, data owners, escalation route, and constraints. Leave unknown values null and record the unresolved decision beside them.

Make the business metric reproducible: numerator, denominator, time window, exclusions, and source. A completed chat is not automatically a resolved customer problem. Pair the business outcome with quality, latency, cost per successful outcome, safety, and human workload. Do not invent release thresholds or assign a convenient default owner.

## Assess five responsibilities

Use this canonical order for presentation: **Evaluation, Observability, Data foundations, Orchestration, Governance**. It is a taxonomy, not a fixed implementation sequence or five-service architecture. For each, record the current evidence, gap, consequence, responsible role, dependency, and acceptance exercise.

Choose the smallest end-to-end milestone that can be evaluated and diagnosed. Multiple agents, embeddings, graph databases, and a new runtime need evidence of benefit; none is required by this framework. Compare candidate configurations on the same cases before recommending a stack change.

## Deliver

Produce the draft contract, a five-pillar assessment, a prioritized dependency-aware backlog, and explicit open decisions. Separate known facts, user requirements, assumptions, and recommendations. Cite the supplied framework section supporting consequential recommendations. Record the framework version used. A plan or structurally valid contract is not a production-readiness approval; preserve null thresholds until the accountable owner decides them.

## Framework sources

[START_HERE.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/START_HERE.md), [docs/pillars.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/pillars.md), [docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [templates/project.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/project.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
