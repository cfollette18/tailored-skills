---
name: rag-evaluation
description: "Evaluate retrieval, grounding, answer correctness, and citation evidence separately. Use when comparing RAG configurations or diagnosing stale, irrelevant, or unsupported answers."
---

# Retrieval and RAG Evaluation

Freeze the source snapshot, access policy, query set, index/chunk configuration, retrieval parameters, reranker, and answer/judge versions. Evaluate what the application actually retrieved and used, not a reconstructed best-case context.

## Separate the questions

Measure retrieval relevance against the query, answer relevance against user intent, grounding against supplied context, and correctness against an authoritative reference when available. A response can faithfully repeat an obsolete source and still be wrong. A citation's existence is not evidence that it supports the attached claim.

When relevance labels exist, define the retrieval unit and ranking metric explicitly: document or chunk, cutoff, binary/graded labels, and handling for unjudged candidates. Deduplicate identities when multiscale chunks refer to one document. Report recall or ranking scores only with their label-coverage limits; incomplete judgments are not exhaustive ground truth.

Test missing answers, conflicting sources, changed/deleted documents, restricted content, distractors, and citation expansion. Permission filtering must survive retrieval and evidence rendering. Score appropriate abstention separately from unsupported confident answers.

## Compare and localize

First inspect whether the needed evidence was available, indexed, retrieved, included, and used. Separate data freshness, search, context assembly, generation, and evaluator errors. Compare identical cases and report slice changes, retrieval latency, token use, and cost alongside answer quality.

Deliver per-stage metrics, evidence references, failure cases, and the source/config manifest. BM25, vector search, hybrid retrieval, and multiscale indexing are candidates to compare on the workload; no retrieval method or chunk size is universally best.

## Sources and adaptation

- [Rag](https://docs.langchain.com/langsmith/evaluate-rag-tutorial)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
