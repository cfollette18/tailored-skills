---
name: human-in-the-loop-workflows
description: "Implement durable pause, review, and resume flows for agent actions. Use when a graph waits for user input or action-specific approval across retries and restarts."
---

# Human-in-the-Loop Workflows

Determine whether the pause requests missing information, quality review, or authorization for a concrete action. These have different decision contracts; a quality label is not approval to execute a tool.

## Persist a reviewable proposal

Store workflow/attempt identity, proposed action and exact inputs, state/proposal version, authorized reviewer scope, evidence, expiry policy, and pending status. Give the reviewer the information needed to decide without exposing unrelated private state.

Persist the pause so it survives worker or browser restart. Resume against the same logical workflow and pending proposal. Validate the actor, decision, proposal version, and current permissions at the execution boundary. Reject stale or duplicate responses; changed material inputs may require a new decision.

Define reject, edit, approve, cancel, timeout, and unavailable-reviewer outcomes according to the product's needs. Silence never becomes approval. Preserve the decision and its application to the action in the operational record.

## Avoid duplicate effects

Inspect whether the runtime resumes from the instruction or restarts the containing node. In LangGraph, code before an interrupt can run again when its node resumes. Move non-repeatable effects behind the approved boundary or protect them with explicit idempotency and receipts. Keep interrupt ordering stable for existing persisted executions or provide a migration strategy.

Test restart while awaiting input, duplicate approvals, stale edits, unauthorized actors, rejected decisions, and cancellation racing with resume. Deliver the state machine, proposal/decision contracts, and recovery tests. Use the existing application's authorization and queue infrastructure; this guide does not prescribe a vendor service.

## Sources and adaptation

- [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [Orchestration](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
