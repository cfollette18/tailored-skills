---
name: ai-data-lifecycle
description: "Plan governed source inventory, freshness, access filtering, versioned retrieval snapshots, and deletion propagation for AI systems. Use when stale, restricted, inconsistent, or untraceable inputs undermine agent answers."
---

# AI Data Lifecycle

Treat source content and operational traces as distinct data products. Start with authoritative owners, source locations, access policy, effective dates, update frequency, sensitivity, consumers, and transformations. File modification time is not necessarily policy effective time.

For a source update, detect a version, validate it, transform/chunk it, build indexes, run retrieval checks, and publish a consistent snapshot. Preserve the previous snapshot for rollback. Detect mismatched document manifests and embedding/index versions rather than mixing old and new inputs invisibly.

Set freshness objectives per source with its owner. Propagate deletions and permission changes into every searchable representation, cache, and citation-expansion path. Apply authorization before candidates reach the agent and again before source expansion. Retrieved documents remain data, not permission-granting instructions.

Version corpus hashes, transformations, tokenizer, chunking, embedding configuration where used, lexical parameters, and index snapshot. Do not replace authoritative text/provenance with embeddings. Choose storage from actual queries; a graph or vector service is optional rather than a framework requirement.

Acceptance exercise: change a test policy and verify the new effective version is retrieved and cited; exclude the superseded or restricted version; surface a failed indexing step; restore the previous snapshot under the documented recovery path. Include access revocation and deletion cases. Deliver source inventory, publication/version contract, freshness/deletion checks, retention boundaries, owners, and rollback evidence. A metadata catalog by itself does not prove retrieval is current or authorized.

## Framework sources

[docs/pillars.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/pillars.md), [docs/operating-framework.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md), [docs/retrieval-and-reproducibility.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/retrieval-and-reproducibility.md).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
