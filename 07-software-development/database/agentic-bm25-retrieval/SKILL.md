---
name: agentic-bm25-retrieval
description: "Establish and evaluate a lexical retrieval baseline inside an agent loop. Use for exact-identifier search, BM25 configuration, query-trajectory diagnostics, and comparisons with semantic or hybrid retrieval."
---

# Agentic BM25 Retrieval

Inspect the actual corpus and agent query workload. Retrieval quality belongs inside the task loop: query formulation, candidate retrieval, opening evidence, and final answer. Ranking metrics remain useful diagnostics; they are not the whole release outcome.

Build or inspect a lexical baseline before assuming embeddings are required. Record engine, tokenizer/analyzer, fields, filters, corpus/index version, and BM25 configuration. k1 controls term-frequency saturation; b controls document-length normalization. Defaults vary by engine and do not establish an adequate baseline for long or heterogeneous documents. Tune with representative queries and keep a held-out task set.

Exercise exact names, identifiers, phrases, rare terms, long documents, and real reformulation trajectories. Compare lexical, semantic, or hybrid variants with the rest of the loop fixed. Measure final task success and citation support together with retrieval diagnostics, latency, calls, and cost. Separate model query failures from retrieval failures using traced queries/results/opened documents.

Progressive disclosure can return titles/snippets first, then let the agent open permitted sources or a controlled document workspace. Filesystem-shaped retrieval is an interface option, not authorization to run arbitrary source instructions. Filter permissions before materializing results and before evidence expansion.

Deliver the documented baseline, query/case set, configuration comparison, failure categories, and index freshness/rollback ownership. Treat the source talk's benchmark and vendor performance claims as hypotheses to test, not guaranteed superiority or throughput. Consult current engine documentation before implementation-specific parameter/API work.

## Framework sources

[docs/lexical-retrieval-bm25.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/lexical-retrieval-bm25.md), [docs/source-notes-bm25.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/source-notes-bm25.md), [docs/retrieval-and-reproducibility.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/retrieval-and-reproducibility.md).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
