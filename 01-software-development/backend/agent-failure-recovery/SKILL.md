---
name: agent-failure-recovery
description: "Design bounded retries, circuit breakers, degradation, and compensation for agent or tool dependencies. Use when preventing retry loops, handling partial side effects, or defining restart and recovery behavior."
---

# Agent Failure Recovery

Separate dependency containment from side-effect recovery. Retrying a failed call, failing fast on an unhealthy service, and compensating a completed action solve different problems.

Use [circuit-breaker-policy.json](assets/circuit-breaker-policy.json). Define closed/open/half-open behavior, which failures count, threshold, cooldown, probe policy, owner, and enforcement point. Record transition events with the calls that caused them. The talk's five failures and sixty seconds are examples, not production defaults; thresholds stay unresolved until an owner decides them.

Choose degradation in advance: reduced functionality, acceptably fresh cached data with meaningful scope, or human escalation. A gateway timeout/rate limit is not automatically a stateful circuit breaker. Enforce budgets in runtime code and distinguish dependency failure from a permanent schema/authorization error that blind retries cannot repair.

For side-effecting workflows, inventory each execute action and its actual compensation. Keep durable completed-step and recovery progress. In a sequential chain, compensate dependents before prerequisites; branching flows need dependency-aware recovery. Compensation is application logic, not a distributed database rollback. It can fail, needs idempotency/retry bounds, and must preserve unrelated concurrent work.

Identify irreversible actions explicitly and apply the product's authorized gate, ordering, or accepted-risk policy. Check the existing session's authorization before asking again. Do not equate cancellation with undo. On uncertain completion, reconcile by idempotency key or external state before replaying a write.

Deliver the breaker/degradation policy, action/compensation map, irreversible boundaries, and failure tests: timeout, rate limit, repeated failure, half-open success/failure, worker restart, duplicate execution, partial compensation failure, and unavailable escalation owner.

## Framework sources

[docs/multi-agent-orchestration.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md), [docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [templates/circuit-breaker-policy.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/circuit-breaker-policy.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
