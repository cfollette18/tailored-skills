---
name: deterministic-ai-evaluators
description: "Write code-based checks for structured outputs, tool contracts, and observable state changes. Use when AI behavior can be checked directly without a model judge."
---

# Deterministic AI Evaluators

Translate each requirement into an observable assertion over an output, event, or controlled state. Prefer a parser, schema, calculation, or recorded side effect when it directly measures the requirement.

## Specify evaluator semantics

Define required inputs, allowed normalization, expected values, units, tolerance when justified, and handling for missing evidence. Preserve distinctions such as number versus numeric string if the public contract requires them. Do not coerce arbitrary invalid output until it happens to pass.

Separate format validity from domain correctness. A syntactically valid tool call can have the wrong entity, amount, permission, or effect. Check the call arguments and verified operation receipt/state where available. Transport success alone does not establish success of the business action.

Return metric identity/version, target identity, status, value, and concise evidence. Distinguish scored failure from evaluator exception, skipped/inapplicable cases, and missing inputs. An exception or absent result must not default to zero or a passing value. Keep status and score separate so zero can be a legitimate measurement.

## Verify the checker

Use known pass/fail cases, malformed structures, absent fields, duplicated actions, and boundary values. Test that an intentionally wrong entity or repeated side effect is caught even when the final answer sounds correct. Evaluate untrusted generated code in an appropriate sandbox with no production credentials.

Keep evaluators read-only against recorded artifacts unless an isolated fixture explicitly needs execution. A checker should not send another refund to verify that the first refund succeeded. Deliver the contract, implementation, meaningful fixtures, and limitations; route semantic judgments that cannot be observed directly to a calibrated rubric.

## Sources and adaptation

- [Judge](https://langfuse.com/academy/evaluate/writing-evaluators)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
