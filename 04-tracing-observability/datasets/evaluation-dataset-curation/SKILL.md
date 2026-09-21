---
name: evaluation-dataset-curation
description: "Build versioned, representative AI evaluation cases from reviewed traces, domain examples, and synthetic gaps. Use when dataset scope, provenance, splits, or labels are unreliable."
---

# Evaluation Dataset Curation

Name the decision the dataset supports and the execution boundary it exercises. End-to-end cases use the application's real input shape; a node-level suite uses the state that node actually receives.

## Curate and version

Inspect available production evidence, existing domain assets, and synthetic cases. Mark provenance and generation method. Review synthetic expectations before using them as reference answers; generated cases are not evidence of real-world frequency.

Record stable case ID, version, permitted input/context, expected behavior or rubric, forbidden actions, slice labels, and source/effective date. Keep evaluation labels separate from application inputs. A judge may legitimately receive an answer reference, but must not see the human verdict it is being calibrated against.

Split related cases by conversation, document family, customer grouping, or time as appropriate before prompt tuning. Deduplicate exact and near-duplicate cases across splits. Maintain a development set, reviewed regression cases, and a protected final comparison set when making generalization claims. Small exploratory sets should be labeled exploratory.

Separate representative usage from challenge suites. Track coverage of common tasks, rare consequential outcomes, languages, missing context, tool failure, stale policies, and permission boundaries relevant to the product. Preserve original rows when revising expectations and record why policy changed.

## Verify and deliver

Run the real input loader in an isolated environment, check missing context and label ambiguity, and reconcile row IDs between dataset and results. Deliver a manifest, slice counts, split rules, provenance/retention policy, and unresolved labels. Use the portable [case template](assets/case-template.json) as an optional starting shape, not a vendor API payload. Null fields require project decisions before use.

## Sources and adaptation

- [Datasets](https://langfuse.com/academy/datasets/designing-great-datasets)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
