---
name: judge-calibration
description: "Measure model-judge agreement with reviewed human labels and inspect error direction. Use before trusting judge scores for comparisons, monitoring, or automated gates."
---

# Judge Calibration

Name the label vocabulary and positive class before computing results. Keep the human verdict outside judge inputs. Preserve the rubric, judge prompt/model/config, dataset version, and row identities.

## Choose the strength of the claim

For an exploratory check, report valid rows, invalid/missing predictions, and agreement with the supplied labels. Do not present a small convenience sample as production validation. For a judge used in a release or automation decision, tune on development examples and reserve an independent held-out set grouped to prevent related-example leakage.

Inspect both failure directions. If positive means a defect, false negatives are missed defects and false positives are false alarms. Choose acceptance criteria from their operational costs; do not invent a universal accuracy cutoff. Report per-slice coverage, class balance, abstentions, and label ambiguity alongside aggregates.

Use the dependency-free [calibration report](scripts/calibration_report.py) on JSONL rows containing `expected` and `actual`. Each row also requires a unique string `case_id`. Pass exact `--positive` and `--negative` labels; labels are not normalized automatically. It calculates a binary confusion matrix, coverage, agreement, precision, recall, specificity, and F1; unknown labels remain invalid and undefined ratios remain null. It does not call a model, tune a judge, calculate uncertainty, or decide release readiness.

Example with project-owned labels (run from this skill directory):

```bash
python3 scripts/calibration_report.py /path/to/reviewed-predictions.jsonl --positive DEFECT --negative PASS
```

## Diagnose and maintain

Review disagreements against original evidence; the human label can also be wrong. Preserve both the initial and adjudicated labels. Change the rubric or examples on development data, then freeze the candidate before final validation. Recalibrate after a judge model, prompt, domain, or input-distribution change.

Deliver row-level evidence, counts/denominators, limitations, and supported disposition. Agreement estimates reliability against the reviewed labels, not objective truth or probability calibration. For uncertainty, choose a method suited to the sampling and clustering instead of treating repeated judgments as independent users.

## Sources and adaptation

- [Judge](https://langfuse.com/academy/evaluate/writing-evaluators)
- [Evals](https://docs.langchain.com/langsmith/evaluation-concepts)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
