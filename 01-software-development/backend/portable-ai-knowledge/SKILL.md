---
name: portable-ai-knowledge
description: "Package versioned knowledge for different agents with stable records, provenance, deterministic exports, and controlled retrieval. Use when building provider-independent context packs or adapters from a maintained knowledge repository."
---

# Portable AI Knowledge

Keep reviewed human-readable source documents authoritative. A database, embedding index, or graph is an optional derived access layer, not the only copy. Inspect the existing manifest and consumer contract before changing record identities.

Declare inputs with stable IDs, document paths, optional exact headings, origins, text, and content hashes. Preserve record identity when its purpose stays the same; splitting/retiring IDs requires consumer compatibility review. Pin repository revision or content hash in downstream engagements. Hashes establish version identity, not factual truth or bit-for-bit reproducibility of model answers.

Provide a text pack for reading agents and structured JSON for programs. Keep a reviewed entry-point contract distinct from delimited reference data. An agent should cite only records it actually received/read; valid IDs alone do not establish semantic support. Search results are pointers to open, not substitutes for the source.

Use deterministic export/check commands and rebuild disposable indexes from declared inputs. Retain provenance and parent context through chunking or embedding changes. Graph services should answer demonstrated traversal needs; evaluate simpler relations first. A new registered source is not automatically indexed by every adapter.

Deliver the manifest/record schema, reproducible export, access contract, version policy, and checks for resolving IDs, changed input hashes, unsupported questions, instruction injection, and stale indexes. The source framework exposes validate/export/check-export/get/related/bundle/build/search through `scripts/knowledge.py`; inspect that version's command contract before invoking it. Do not automatically alter downstream model profiles, credentials, or tools when refreshing knowledge.

## Framework sources

[docs/agent-integration.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/agent-integration.md), [docs/retrieval-and-reproducibility.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/retrieval-and-reproducibility.md), [START_HERE.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/START_HERE.md).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
