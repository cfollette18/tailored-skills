# Tracing, observability, and evaluation coverage

Reviewed 2026-09-21. This category has 22 vendor-neutral skills: four existing Production AI Framework skills relocated here and 18 focused additions. Two further additions implement durable execution and human review under software development. The library now has 96 skills.

## Select a workflow

| Need | Skills |
|---|---|
| Plan instrumentation or quality work | [AI Observability](tracing/ai-observability/SKILL.md), [AI Evaluation and Release](evaluation/ai-evaluation-release/SKILL.md) |
| Trace service boundaries and protect data | [Distributed Agent Tracing](tracing/distributed-agent-tracing/SKILL.md), [Telemetry Privacy and Sampling](tracing/telemetry-privacy-sampling/SKILL.md) |
| Diagnose stateful or streaming runs | [Graph Execution Tracing](tracing/graph-execution-tracing/SKILL.md), [Streaming Trace Diagnostics](tracing/streaming-trace-diagnostics/SKILL.md) |
| Build trustworthy cases and labels | [Dataset Curation](datasets/evaluation-dataset-curation/SKILL.md), [Human Feedback and Review](datasets/human-feedback-review/SKILL.md) |
| Evaluate concrete behavior | [Deterministic Checks](evaluation/deterministic-ai-evaluators/SKILL.md), [Agent Trajectories](evaluation/agent-trajectory-evaluation/SKILL.md), [RAG](evaluation/rag-evaluation/SKILL.md), [Conversations](evaluation/conversation-evaluation/SKILL.md) |
| Design and validate model judges | [Judge Design](judges/llm-judge-design/SKILL.md), [Calibration](judges/judge-calibration/SKILL.md), [Pairwise Comparison](judges/pairwise-judge-evaluation/SKILL.md) |
| Compare changes | [Offline Experiments](experiments/offline-ai-experiments/SKILL.md), [Prompt Version Evaluation](experiments/prompt-version-evaluation/SKILL.md) |
| Observe live quality | [Online Evaluation](monitoring/online-ai-evaluation/SKILL.md), [Quality Monitoring](monitoring/ai-quality-monitoring/SKILL.md) |
| Investigate or govern change | [Error Analysis](operations/ai-error-analysis/SKILL.md), [Incident Response](operations/ai-incident-response/SKILL.md), [Release Governance](operations/ai-release-governance/SKILL.md) |
| Implement resumable workflows | [Durable Execution](../01-software-development/backend/durable-agent-execution/SKILL.md), [Human-in-the-Loop Workflows](../01-software-development/backend/human-in-the-loop-workflows/SKILL.md) |

## Framework coverage and boundaries

All 13 existing [Production AI Framework skill areas](../01-software-development/production-ai-framework-map.md) remain available. Evaluation, observability, incident response, and release governance now live here. Project contracts, data lifecycle, workflow coordination, versioned handoffs, recovery, BM25, multiscale retrieval, portable knowledge, and source ingestion remain in software development. No duplicate copies are needed.

The additions extract reusable engineering patterns from primary documentation. They do not import whole vendor manuals or claim to cover every API in those products. The skills work with local records and project artifacts; a remote platform is optional. Unknown business targets, owners, and release decisions remain unresolved.

## Optional adapter mapping

| Source | Reusable concepts | Mapping to verify when implementing |
|---|---|---|
| [Production AI Framework](https://github.com/cfollette18/production-ai-framework/tree/feb7e5ca4df01bb722f8b83f6ff1962c276f2bd8) | Evaluation, Observability, Data foundations, Orchestration, Governance | Project-specific ownership, criteria, evidence, versioned state, and recovery contracts. The repository's implementation guidance is distinct from unverified source-talk assertions. |
| [LangGraph checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers), [interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), [streaming](https://docs.langchain.com/oss/python/langgraph/streaming) | Durable graph state, execution lineage, pause/resume, replay, public event streams | Installed runtime/checkpointer and durability mode; thread/checkpoint/namespace IDs; reducer behavior; stream event shape. Checkpoint replay can repeat model and tool execution. LangGraph runtime persistence is distinct from a trace backend. |
| [LangSmith evaluation](https://docs.langchain.com/langsmith/evaluation-concepts), [agent evaluation](https://docs.langchain.com/langsmith/evaluate-complex-agent), [pairwise evaluation](https://docs.langchain.com/langsmith/evaluate-pairwise) | Dataset examples, experiments, observable trajectories, conversation scope, human/code/model judgments | Run/thread/case IDs, evaluator input/output contract, target selection, and score attachment. The underlying evaluation design does not require LangChain or LangGraph. |
| [Langfuse trace guidance](https://langfuse.com/docs/observability/best-practices), [evaluator design](https://langfuse.com/academy/evaluate/writing-evaluators), [experiment comparisons](https://langfuse.com/docs/evaluation/experiments/compare-experiments) | Operation scope, labeled examples, reliable checks, sample-aware online scores, paired regressions | SDK/version, observation types, score schema, ingestion/export routes, datasets, and selectors. Backend-specific field names stay in the consuming project's adapter. |
| [OpenTelemetry context](https://opentelemetry.io/docs/concepts/context-propagation/), [sampling](https://opentelemetry.io/docs/concepts/sampling/), [GenAI conventions entry point](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | Cross-service causal context, spans/links, sampling, telemetry export | Propagation and export configuration, applicable convention revision and stability, payload controls across every destination. Convention names and provider compatibility require verification against the installed instrumentation. |

No skills require a particular judge model, API key, paid account, storage engine, or agent framework. They describe observed operations and evidence-based score explanations, not private model reasoning. SDK adapters were not implemented or executed as part of this documentation update.

## New skill provenance

Each package has its own `SOURCE.json` with reviewed primary links and, where used, the Production AI Framework revision and input hashes. The descriptions below are original implementation guidance rather than verbatim vendor documentation.

| Skill | Primary source families |
|---|---|
| [Distributed Agent Tracing](tracing/distributed-agent-tracing/SKILL.md) | OpenTelemetry, Langfuse, Production AI Framework |
| [Telemetry Privacy and Sampling](tracing/telemetry-privacy-sampling/SKILL.md) | Langfuse, OpenTelemetry, Production AI Framework |
| [Graph Execution Tracing](tracing/graph-execution-tracing/SKILL.md) | LangGraph, Production AI Framework |
| [Streaming Trace Diagnostics](tracing/streaming-trace-diagnostics/SKILL.md) | LangGraph, Langfuse |
| [Evaluation Dataset Curation](datasets/evaluation-dataset-curation/SKILL.md) | Langfuse, Production AI Framework |
| [Human Feedback and Review](datasets/human-feedback-review/SKILL.md) | LangSmith, Langfuse, Production AI Framework |
| [Deterministic AI Evaluators](evaluation/deterministic-ai-evaluators/SKILL.md) | Langfuse, Production AI Framework |
| [Agent Trajectory Evaluation](evaluation/agent-trajectory-evaluation/SKILL.md) | LangSmith, Production AI Framework |
| [Retrieval and RAG Evaluation](evaluation/rag-evaluation/SKILL.md) | LangSmith, Production AI Framework |
| [Conversation Evaluation](evaluation/conversation-evaluation/SKILL.md) | LangSmith, Production AI Framework |
| [LLM Judge Design](judges/llm-judge-design/SKILL.md) | Langfuse, Production AI Framework |
| [Judge Calibration](judges/judge-calibration/SKILL.md) | Langfuse, LangSmith, Production AI Framework |
| [Pairwise Judge Evaluation](judges/pairwise-judge-evaluation/SKILL.md) | LangSmith, Langfuse |
| [Offline AI Experiments](experiments/offline-ai-experiments/SKILL.md) | Langfuse, LangSmith, Production AI Framework |
| [Prompt Version Evaluation](experiments/prompt-version-evaluation/SKILL.md) | Langfuse, Production AI Framework |
| [Online AI Evaluation](monitoring/online-ai-evaluation/SKILL.md) | Langfuse, LangSmith, Production AI Framework |
| [AI Quality Monitoring](monitoring/ai-quality-monitoring/SKILL.md) | Production AI Framework, OpenTelemetry, Langfuse |
| [AI Error Analysis](operations/ai-error-analysis/SKILL.md) | Langfuse, Production AI Framework |
| [Durable Agent Execution](../01-software-development/backend/durable-agent-execution/SKILL.md) | LangGraph, Production AI Framework |
| [Human-in-the-Loop Workflows](../01-software-development/backend/human-in-the-loop-workflows/SKILL.md) | LangGraph, Production AI Framework |

## Portable assets

- [Case template](datasets/evaluation-dataset-curation/assets/case-template.json): input, context, reference, behavior, provenance, split, and review state.
- [Rubric template](judges/llm-judge-design/assets/rubric-template.json): evidence, labels, abstention, judge identity, and unresolved calibration decisions.
- [Experiment manifest](experiments/offline-ai-experiments/assets/experiment-manifest.json): baseline/candidate, dataset/evaluators, execution controls, and decision policy.
- [Calibration report](judges/judge-calibration/scripts/calibration_report.py): local binary confusion metrics with explicit invalid-label counts and null undefined ratios. It does not query a model or establish a release threshold.

Templates are draft starting shapes, not schemas that guarantee validity or vendor API requests. Populate and validate them within the consuming project. Keep customer examples and production traces in controlled project storage.
