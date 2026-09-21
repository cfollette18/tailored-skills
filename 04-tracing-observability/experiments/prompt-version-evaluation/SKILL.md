---
name: prompt-version-evaluation
description: "Evaluate and trace prompt changes as versioned behavioral changes. Use when changing instructions, templates, variables, or model configuration and comparing their effects."
---

# Prompt Version Evaluation

Locate the prompt actually used at runtime, including composition, defaults, variable interpolation, tool descriptions, and environment overrides. A repository template can differ from the rendered request.

## Preserve identity and intent

Record template/version, variable schema, composition dependencies, model/config, tool contract, and a hash or controlled reference for the rendered prompt. Keep private interpolated content out of general logs. If a remote prompt service or cache is used, record the version that was served rather than only the requested label.

Translate the desired behavior into cases before editing. Preserve user requirements and authorization boundaries. Separate a focused prompt change from unrelated model or tool changes when attribution matters. If several components must change, record the bundle and its limitations as an experiment.

Test missing variables, escaping, instruction/data boundaries, long inputs, conflicting retrieved text, refusal/escalation behavior, and tool argument shape relevant to the product. Use actual prior failures as reviewed regression cases.

## Compare and preserve rollback

Run baseline and candidate on the same versioned cases with the same evaluators. Review per-case regressions and cost/latency changes; a better style score cannot waive a required action constraint. Judge prompt changes require calibration independently from the application prompt change.

Deliver the prompt diff, version manifest, motivating behavior, evaluation evidence, and rollback target. Preserve approved versions and cache behavior in the release plan. Creating a prompt draft or passing an experiment does not itself publish the prompt to production.

## Sources and adaptation

- [Compare](https://langfuse.com/docs/evaluation/experiments/compare-experiments)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
