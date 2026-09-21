---
name: agent-trajectory-evaluation
description: "Evaluate tool selection, arguments, state transitions, and task outcomes across an agent execution. Use when a good final answer can hide an incorrect or unauthorized path."
---

# Agent Trajectory Evaluation

Choose the evaluation unit: final outcome, one decision, or the whole observable trajectory. Score these separately so a correct answer cannot conceal a failed workflow.

## Define acceptable behavior

Record initial state, tools available, permissions, required effects, prohibited effects, and completion condition. Use sandboxed or recorded tools for evaluation. Pin tool schemas and data fixtures with the case.

Choose trajectory comparison based on actual constraints: exact order for a required protocol, partial order for dependencies, or a set of invariants when several valid routes exist. Avoid failing an efficient alternative just because it differs from a reference transcript. Compare meaningful arguments and actual effects; normalize incidental call IDs without discarding entity IDs or amounts.

Check missing prerequisites, wrong routing, repeated side effects, loops, stale state, handled and unhandled errors, unnecessary calls, cancellation, and escalation. Link each failure to a call/transition and the violated requirement. A claim that a tool succeeded is not proof of a recorded effect.

## Run and diagnose

Use component tests to locate a failure, then evaluate the complete workflow with its state and tool boundaries intact. Keep model variability and external dependency variability visible. Compare cost and step budgets only against agreed limits; fewer calls alone is not better quality.

Deliver a case-by-case result with outcome, path validity, efficiency, and evidence availability separated. LangGraph/LangSmith can provide node or tool trajectories; custom runtimes can supply equivalent event records. No hidden chain-of-thought is needed to evaluate observable tool behavior.

## Sources and adaptation

- [Agent](https://docs.langchain.com/langsmith/evaluate-complex-agent)
- [Orchestration](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
