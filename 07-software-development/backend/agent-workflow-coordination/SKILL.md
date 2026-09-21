---
name: agent-workflow-coordination
description: "Choose explicit coordination, event-driven workers, or a hybrid for an agent workflow. Use when defining dependencies, human handoffs, durable states, and recovery ownership; do not add agents solely for autonomy aesthetics."
---

# Agent Workflow Coordination

Start with the smallest workflow that meets the task. Additional agents introduce distributed-state and delivery problems; inspect consistency and execution order before attributing failures to prompts.

## Choose ownership of coordination

Central orchestration fits complex dependencies and a need to reconstruct execution: the coordinator owns graph/state/retries/cancellation while workers receive inputs and return outputs. Choreography fits independent reactions and frequent new subscribers when the team can trace propagation, replay, duplicates, and eventual consistency. A hybrid can combine independent events with compensation. These choices depend on the workflow, not a universal vendor recommendation.

Draw or describe the actual dependency graph, including parallel branches, side effects, joins, and review queues. Agents do not need to call each other directly. Distinguish sibling results from sequential versions; a join must state how branches merge.

## Specify operational behavior

Define pending, running, awaiting-review, succeeded, failed, and cancelled states; correlation IDs; deadlines; duplicate handling; cancellation propagation; and restart recovery. Use explicit versioned inputs and enforce contracts at consumer boundaries. Name who persists transitions and resolves conflicts.

A human review step needs a queue, owner, supporting evidence, response objective, and timeout disposition. Approval binds to the concrete action and inputs; changed inputs may invalidate it. Silence is not approval. Keep existing user authorizations and actual host permissions authoritative.

Deliver a coordination decision with trade-offs, state/dependency model, handoff/side-effect inventory, and fault exercises. Test duplicate delivery, partial completion, worker restart, and unavailable reviewers. More agents are justified only by a measurable benefit, and a design for delegation does not itself authorize spawning agents in the current task.

## Framework sources

[docs/multi-agent-orchestration.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md), [docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
