---
name: graph-execution-tracing
description: "Correlate graph nodes, branches, checkpoints, resumes, and replay attempts. Use to diagnose stateful agent workflows in LangGraph or an equivalent graph runtime."
---

# Graph Execution Tracing

Keep the logical graph separate from the execution evidence. A node name can execute repeatedly; identify each attempt by run, graph namespace, node/task, and attempt. Preserve parent checkpoint and branch ancestry where available.

## Reconstruct state transitions

For each node capture the input state version, selected route, output state version, duration, and terminal disposition. Prefer state hashes and controlled references over copying entire memory into traces. Distinguish pending writes from committed snapshots. A checkpoint records recovery state; a trace records what was observed, and one cannot substitute for the other.

Represent parallel siblings as siblings with explicit merge dependencies. Record the merge/reducer policy when concurrent outputs update the same field. Do not interpret arrival order as business order. Detect stale versions, rejected contracts, and branch conflicts at the boundary where they first appear.

Distinguish initial execution, resume from failure, human response, and deliberate replay. Link a new attempt to the original run and checkpoint; do not overwrite the historical trace. Inspect the first divergent input or state transition before assigning blame to a later answer.

## LangGraph mapping and checks

When LangGraph is selected, inspect thread identity, checkpoint identity, checkpoint namespace, task records, and the installed runtime's snapshot behavior. Review reducers before editing saved state. Replay may invoke models and external tools again; diagnose with read-only inspection or isolated tools unless replay effects are authorized.

Test parallel branches, an interrupted node, failed checkpoint persistence, a resumed attempt, and an altered route. Deliver a correlated execution timeline, state-version lineage, and observed evidence versus hypotheses. Generic graph advice does not imply a particular SDK field or exactly-once execution guarantee.

## Sources and adaptation

- [Checkpoints](https://docs.langchain.com/oss/python/langgraph/checkpointers)
- [Orchestration](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
