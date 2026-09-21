---
name: telemetry-privacy-sampling
description: "Design trace payload controls, retention, sampling, and exporter checks. Use when collecting AI telemetry without leaking sensitive payloads or misreading sampled quality metrics."
---

# Telemetry Privacy and Sampling

Inventory every telemetry destination: SDK exporters, console logs, exceptions, attachments, debug streams, queues, and collector routes. A mask in one exporter does not protect another. Classify fields before choosing capture and retention rules.

## Control capture and access

Prefer allowlisted metadata and controlled evidence references. Inspect nested tool arguments, error messages, URLs, headers, media, and resource attributes for sensitive content. Apply filtering before each untrusted storage or network boundary. Test with synthetic canary values; do not use a customer's records as a redaction fixture. If filtering fails, follow an explicit payload-drop policy and emit a content-free diagnostic.

Give payloads and identifiers separate retention and access rules when needed. Deletion must account for derived dataset rows, caches, and exported copies within the agreed scope. Hashing predictable identifiers is pseudonymization, not a claim of anonymity. Neither a trace ID nor a checkpoint ID is an authorization credential.

## Preserve measurement meaning

Choose sampling unit and stage deliberately. Head sampling can decide early; tail sampling can use a completed outcome but needs buffering and coordination. Document selection probabilities, exclusions, and late/missing spans. Keep representative traffic separate from intentionally oversampled failures.

Track eligible operations, selected operations, successfully exported traces, and scored operations independently. A low error percentage in a filtered sample is not the population error rate. Keep high-cardinality user identifiers out of metric labels.

Deliver a field/destination policy and selection policy, with unresolved owners and limits explicit. Verify every exporter, redaction failure, sampling consistency across children, retention expiry, and export queue pressure.

## Sources and adaptation

- [Masking](https://langfuse.com/docs/observability/features/masking)
- [Sampling](https://opentelemetry.io/docs/concepts/sampling/)
- [Paf](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/docs/operating-framework.md)

Original vendor-neutral implementation guidance, reviewed 2026-09-21. The linked products illustrate capabilities; they are optional adapters. Check installed versions and current official API documentation when implementing one. Source identity and limitations are recorded in [SOURCE.json](SOURCE.json).
