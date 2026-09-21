---
name: evidence-source-ingestion
description: "Turn supplied transcripts or documents into source-scoped, evidenced knowledge packets with coverage and unresolved conflicts. Use when adding new material to a production AI knowledge base while preserving attribution and review boundaries."
---

# Evidence Source Ingestion

This is authoring, not deployment or runtime advice. Inventory the actual supplied files/modalities and record unknown metadata as null. A URL does not mean its contents were read; transcript review is not video/slide verification. Compute a source hash only from actual bytes when possible.

Segment the full supplied input before summarizing. Preserve supplied timestamps/pages or use paragraph locators; do not invent timings. Retain reviewed, unread, unavailable, excluded, and unresolved segments in a coverage ledger. Long inputs need a checkpoint with pending IDs rather than a completeness claim over a truncated source.

Extract atomic claims with stable source-scoped IDs, supporting segments, scope, caveats, units/denominators/windows, and one primary pillar plus optional secondary tags. Use Evaluation, Observability, Data foundations, Orchestration, Governance, or an explained unmapped topic. Deduplicate genuinely repeated assertions without erasing different scopes or contradictions.

Source claims remain `source_assertion` and `not_independently_verified` under the framework's intake contract. Keep example thresholds and vendor metrics labelled as such. Derived procedures distinguish source guidance from implementation proposals. Never fabricate reviewer decisions or promote an unreviewed packet to approved knowledge.

Compare only against records actually supplied. With no snapshot, mark comparison not provided; do not claim deduplication or conflict review against an unseen corpus. Preserve conflicting source positions pending adjudication.

Deliver `intake.json`, `guide.md`, and `handoff.md` using the source framework's versioned packet schema and routing contract. Source additions live under their own `sources/<id>/`; do not overwrite the original source manifest or put claims directly into a navigation catalog. Follow the existing authorized review/export/index procedure and record actual validation results. Structural validation does not prove semantic fidelity or grant publication rights.

## Framework sources

[ingestion/WORKFLOW.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/ingestion/WORKFLOW.md), [ingestion/ROUTING.md](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/ingestion/ROUTING.md), [ingestion/packet.schema.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/ingestion/packet.schema.json), [ingestion/packet.template.json](https://github.com/cfollette18/production-ai-framework/blob/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8/ingestion/packet.template.json).

Derived implementation guidance from the pinned Production AI Framework; source assertions and examples are not independently verified guarantees. See [coverage and provenance](../../production-ai-framework-map.md).
