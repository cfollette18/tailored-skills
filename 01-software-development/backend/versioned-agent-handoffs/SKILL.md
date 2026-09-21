---
name: versioned-agent-handoffs
description: "Define immutable versioned agent state and enforceable producer-consumer contracts. Use for stale reads, lost updates, incompatible outputs, branch merges, or debugging where an agent workflow first diverged."
---

# Versioned Agent Handoffs

Pass a specific snapshot, not an ambiguous request for the latest mutable value. Retain parent version, producer, schema version, timestamp, and evidence references. Append each accepted result; do not overwrite prior audit inputs. The workflow coordinator owns persistence and version selection.

Immutability is not a complete consistency solution. A frozen object can still contain mutable nested lists/maps. Version selection, cache coherence, branch merging, and access enforcement remain explicit responsibilities. When shared mutable state is unavoidable, deliberately choose transactions/concurrency controls rather than assuming database defaults prevent races.

Use [handoff-contract.json](assets/handoff-contract.json). Define producer/consumer, versioned schema reference, required fields, acceptance rules, and rejection handling. Validate before the consumer acts. A schema registry helps discovery but does not enforce runtime acceptance. Rejections need a bounded corrective retry, human route, or failed-workflow disposition.

Do not adopt the source talk's illustrative confidence threshold as a default. Acceptance thresholds need a named decision-maker and rationale; self-reported model confidence is not automatically calibrated. Leave unresolved thresholds null while producing the rest of the contract.

For parallel branches, record their shared parent and a merge policy. Check duplicate submissions, conflicting changes, wrong-version inputs, stale cache reads, schema upgrades, and nested mutation. Diagnose divergence using retained inputs and outputs; history search is only valid when the check and ordering support it. Deliver the state schema, contract, rejection policy, migration/merge decisions, and observed regression evidence.

## Framework sources

[docs/multi-agent-orchestration.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multi-agent-orchestration.md), [templates/handoff-contract.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/templates/handoff-contract.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
