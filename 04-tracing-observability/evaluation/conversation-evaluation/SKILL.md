---
name: conversation-evaluation
description: "Evaluate multi-turn continuity, corrections, memory boundaries, and final task completion. Use when isolated answer scoring misses conversation-level failures."
---

# Conversation Evaluation

Define the conversation boundary and completion condition before scoring. Preserve turn ordering, user corrections, tool outcomes, and the state available at each turn. Never let an earlier-turn evaluator see future evidence that the assistant did not yet have.

## Design scenarios

Cover follow-up references, changed intent, corrected facts, unresolved questions, handoffs, interruptions, cancellation, and resumption relevant to the product. Check whether the system preserves valid constraints, updates superseded ones, and isolates memory between users or conversations.

Measure per-turn quality and whole-conversation outcome separately. A friendly last message cannot erase an earlier unauthorized action. A long conversation is not automatically unsuccessful; distinguish necessary clarification from repetition, looping, and lost context.

For simulated users, pin simulator prompt/model and scenario, keep the hidden objective outside the agent's input, and cap turns and spend. Review simulator behavior: a simulator that volunteers every answer or cooperates unnaturally can inflate success. Compare selected cases with real reviewed interactions when available.

## Score and report

Use recorded task outcomes where possible; use a calibrated rubric for coherence and unresolved intent. Distinguish completed, failed, interrupted, abandoned, and unknown outcomes. Define a time/window policy for online conversation scoring and revise scores when late turns change the observed boundary.

Deliver conversation IDs/revisions, scenario coverage, turn-level failure locations, task outcome, and evaluator version. Treat related turns as one statistical unit when estimating uncertainty; counting every message as an independent sample exaggerates confidence.

## Sources and adaptation

- [Evals](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Agent](https://docs.langchain.com/langsmith/evaluate-complex-agent)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
