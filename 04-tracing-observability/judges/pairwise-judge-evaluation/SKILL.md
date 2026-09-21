---
name: pairwise-judge-evaluation
description: "Compare paired AI outputs with blinded order, explicit ties, and bias checks. Use when choosing between candidates is more meaningful than assigning absolute scores."
---

# Pairwise Judge Evaluation

Pair baseline and candidate outputs by the same case and input revision. Reuse recorded outputs when judging quality alone; re-execution changes the experiment and its cost.

## Specify the comparison

Choose one decision criterion and provide the context needed to judge it. Blind model/candidate names. Randomize presentation order and retain the mapping back to candidate identity. On an appropriate subset, swap order and inspect disagreement for position bias; do not count swaps of one case as independent samples.

Allow explicit A, B, tie, and insufficient-evidence outcomes. Preserve invalid responses and provider errors separately. Require a concise rationale tied to supplied evidence. If multiple dimensions matter, report them separately before applying an explicitly chosen tradeoff rule.

## Aggregate without hiding failures

Report wins, losses, ties, unresolved pairs, and evaluated/eligible coverage. Define the denominator and tie treatment. If using half-credit ties, state `(wins + 0.5 * ties) / valid_pairs`; do not silently discard ties or failed judgments to increase the win rate.

Inspect critical regressions even if the candidate wins on average. Calibrate preferences against reviewed pairs and include length/style perturbations to test whether the judge rewards presentation over correctness. Use uncertainty methods that respect paired cases and correlated conversations when a statistical claim is needed.

Deliver case-paired outputs, order mapping, judge version, per-criterion outcomes, and limitations. Pairwise preference alone does not establish that either candidate meets an absolute minimum quality bar. Multi-model comparisons need a declared design rather than opportunistically selecting favorable matchups.

## Sources and adaptation

- [Pairwise](https://docs.langchain.com/langsmith/evaluate-pairwise)
- [Judge](https://langfuse.com/academy/evaluate/writing-evaluators)
- [Compare](https://langfuse.com/docs/evaluation/experiments/compare-experiments)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
