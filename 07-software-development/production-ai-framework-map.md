# Production AI Framework skill map

These 13 dedicated skills were derived from the owner’s [Production AI Framework](https://github.com/cfollette18/production-ai-framework) at revision `feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8`, reviewed 2026-09-21. They fit the reorganized software-development areas rather than restoring the removed numbered AI/research categories.

The canonical pillars are **Evaluation, Observability, Data foundations, Orchestration, Governance**. They organize responsibilities, not a mandatory stack or implementation order. Unknown owners/thresholds remain unresolved. Source-talk assertions, benchmark numbers, and illustrative thresholds are not independently verified guarantees. No raw transcripts, private traces, or production cases are bundled.

| Skill | Source coverage |
|---|---|
| [Production AI Project Contract](planning/production-ai-project-contract/SKILL.md) | `START_HERE.md`, `docs/pillars.md`, `docs/operating-framework.md`, `templates/project.json` |
| [AI Evaluation and Release](testing/ai-evaluation-release/SKILL.md) | `docs/operating-framework.md`, `docs/pillars.md`, `templates/evaluation-case.json` |
| [AI Observability](backend/ai-observability/SKILL.md) | `docs/pillars.md`, `docs/operating-framework.md`, `templates/trace.json` |
| [AI Data Lifecycle](database/ai-data-lifecycle/SKILL.md) | `docs/pillars.md`, `docs/operating-framework.md`, `docs/retrieval-and-reproducibility.md` |
| [Agent Workflow Coordination](backend/agent-workflow-coordination/SKILL.md) | `docs/multi-agent-orchestration.md`, `docs/operating-framework.md` |
| [Versioned Agent Handoffs](backend/versioned-agent-handoffs/SKILL.md) | `docs/multi-agent-orchestration.md`, `templates/handoff-contract.json` |
| [Agent Failure Recovery](backend/agent-failure-recovery/SKILL.md) | `docs/multi-agent-orchestration.md`, `docs/operating-framework.md`, `templates/circuit-breaker-policy.json` |
| [AI Release Governance](deployment/ai-release-governance/SKILL.md) | `docs/operating-framework.md`, `docs/pillars.md`, `templates/change.json` |
| [AI Incident Response](debugging/ai-incident-response/SKILL.md) | `docs/operating-framework.md`, `docs/multi-agent-orchestration.md`, `templates/incident.json` |
| [Agentic BM25 Retrieval](database/agentic-bm25-retrieval/SKILL.md) | `docs/lexical-retrieval-bm25.md`, `docs/source-notes-bm25.md`, `docs/retrieval-and-reproducibility.md` |
| [Multiscale Retrieval](database/multiscale-retrieval/SKILL.md) | `docs/multiscale-indexing.md`, `docs/source-notes-multiscale.md`, `docs/retrieval-and-reproducibility.md` |
| [Portable AI Knowledge](backend/portable-ai-knowledge/SKILL.md) | `docs/agent-integration.md`, `docs/retrieval-and-reproducibility.md`, `START_HERE.md` |
| [Evidence Source Ingestion](backend/evidence-source-ingestion/SKILL.md) | `ingestion/WORKFLOW.md`, `ingestion/ROUTING.md`, `ingestion/packet.schema.json`, `ingestion/packet.template.json` |

Each `SOURCE.json` records exact input hashes. Copied JSON templates retain null values intentionally; validation and owner decisions are still required in the destination project. The source repository was read, not modified. Vendor-specific APIs, compliance conclusions, external execution, and live deployments require their own evidence and authorization.
