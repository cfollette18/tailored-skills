---
name: offline-ai-experiments
description: "Run reproducible baseline/candidate comparisons with versioned cases, evaluators, and bounded execution. Use for prompt, model, retrieval, or orchestration changes."
---

# Offline AI Experiments

Write the hypothesis, primary metric, required slices, comparison unit, and decision policy before inspecting candidate results. Separate exploratory tuning from a final comparison.

## Freeze the experiment

Record application commit, prompt/template versions, exact model identifier and decoding settings where available, tool contracts, data snapshot, dataset manifest, evaluator versions, and environment. Version identity does not make stochastic model output deterministic.

Match cases by stable ID and input revision. Keep external effects in isolated fixtures or recorded tools. Define concurrency, timeout, retry policy, spend budget, and stopping condition. Retrying one candidate more often or using a different cache state changes the comparison; record those differences.

Keep application output, evaluator verdict, infrastructure error, and missing result distinct. Check full case coverage before aggregating. Use repetitions when variability matters, but preserve per-case grouping so repeated runs do not inflate the independent sample size.

## Compare and hand off

Show paired gains/regressions, slice results, cost, and latency alongside aggregate quality. Inspect evaluator mistakes before attributing every score change to the application. If an evaluator changes, re-score both candidates and preserve original results.

Deliver a manifest, per-case artifacts, summary with denominators and uncertainty appropriate to the claim, and unresolved decisions. The optional [experiment manifest](assets/experiment-manifest.json) is vendor-neutral. Baseline approval is a separate decision; the newest or highest-scoring run does not silently become the release baseline.

## Sources and adaptation

- [Compare](https://langfuse.com/docs/evaluation/experiments/compare-experiments)
- [Evals](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
