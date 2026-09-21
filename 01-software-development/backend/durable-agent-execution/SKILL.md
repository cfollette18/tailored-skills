---
name: durable-agent-execution
description: "Design restartable stateful agent workflows with checkpoint boundaries, idempotency, and bounded recovery. Use when adopting LangGraph-like persistence or handling worker failures."
---

# Durable Agent Execution

Identify durable state, nondeterministic work, external effects, and the places execution can stop. Define logical workflow identity separately from attempt and checkpoint identity.

## Choose recovery semantics

Select checkpoint granularity and persistence behavior based on acceptable lost work and latency. A process-memory store supports local experiments, not recovery after a process restart. Version state schemas and define migration or incompatibility handling for old checkpoints.

Make state transitions and effect receipts explicit. Isolate nondeterministic calls and side effects so replay policy can be controlled. Use stable idempotency keys for repeatable external operations and record the provider's receipt. A checkpoint does not make an external API exactly-once; failures between an effect and recording its receipt need reconciliation.

For fan-out, preserve branch ancestry and define merge/reducer semantics. Successful sibling work, partially persisted writes, and a committed global checkpoint are different states. Do not assume a restart rolls back successful external work.

## Verify with failures

Exercise a crash before and after a side effect, lost acknowledgement, duplicate delivery, failed checkpoint write, cancellation, and restart on a changed schema. Bound attempts and elapsed time; classify retryable versus terminal errors. Use compensations only for effects that actually have a valid compensating operation.

When using LangGraph, inspect the installed checkpointer, durability mode, and replay behavior. Nodes after a replay point can execute again. Deliver a state/recovery contract and isolated fault-injection evidence, with residual reconciliation cases explicit. Link runtime attempts to observability records without storing hidden reasoning or unnecessary private state.

## Sources and adaptation

- [Checkpoints](https://docs.langchain.com/oss/python/langgraph/checkpointers)
- [Orchestration](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
