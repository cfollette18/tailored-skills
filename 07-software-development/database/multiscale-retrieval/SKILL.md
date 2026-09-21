---
name: multiscale-retrieval
description: "Evaluate query-dependent chunk sizes and multiscale document retrieval with rank fusion. Use when one fixed chunk size loses either precise facts or broader context, or when comparing indexing-scale trade-offs."
---

# Multiscale Retrieval

Test whether chunk-size sensitivity matters on the product's own queries before adding index fleets. Small chunks can lose context; large chunks can dilute localized evidence. The source's experiment motivates measurement, not a universal size ladder.

Build representative queries spanning precise fact lookup and context-dependent questions. Compare fixed-size indexes under the same corpus, permissions, embedding configuration, and answer pipeline. Measure recall per query and at several k values, then end-to-end task/citation quality. A per-query oracle uses known answers to estimate an upper bound; it is not a deployable selector or a valid test-time feature.

If justified, version multiple scale indexes and query them with bounded parallelism. Resolve chunk hits to stable parent document identities before fusing rankings across scales; deduplicate so rankings refer to comparable items. Record the document-mapping policy, per-scale candidate count, fusion method/configuration, and context expansion policy. Reciprocal Rank Fusion is a candidate, not proof that every RRF configuration wins.

Measure storage, indexing effort, per-query compute, tail latency, cost, and partial-scale failure. Parallel requests may reduce wall-clock time while multiplying compute and stressing dependencies. Define degraded fusion if a scale times out; retain authorization and version coherence across every index.

Deliver fixed-scale baselines, oracle analysis labelled correctly, multiscale comparison, resource budget, failure policy, and the owner/rationale for the size ladder. The source's reported recall/storage/latency numbers are not independently reproduced guarantees; do not copy them as project acceptance thresholds. Requalify when corpus or query mix changes.

## Framework sources

[docs/multiscale-indexing.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/multiscale-indexing.md), [docs/source-notes-multiscale.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/source-notes-multiscale.md), [docs/retrieval-and-reproducibility.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/retrieval-and-reproducibility.md).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
