# tailored-skills

Reusable agent skills organized by engineering responsibility. Agent rules (`.mdc`) remain in the companion [tailored-rules](https://github.com/cfollette18/tailored-rules) repository.

## Category map

| Directory | Coverage | Skills |
|---|---|---|
| [01-software-development](01-software-development/README.md) | Frontend, backend, databases, testing, planning, debugging, code quality, and deployment. | 33 |
| [02-github](02-github/README.md) | Authentication, repository inspection/management, pull requests, reviews, and issues. | 6 |
| [03-anti-ai-slop](03-anti-ai-slop/README.md) | Principles, code, agents, writing, design, typography, icons, color, motion, and presentations. | 35 |
| [04-tracing-observability](04-tracing-observability/README.md) | Distributed and graph tracing, datasets, deterministic and semantic evals, judges, experiments, monitoring, and incident/release operations. | 22 |

**Total: 96 skills.** Four consecutively numbered categories contain dedicated subdirectories. Previously retired skill collections remain removed; these numbers identify the current organization.

## Reuse the Namakan chat interface

Start with [Agent Chat Workspace](01-software-development/frontend/agent-chat-workspace/SKILL.md), supported by [Inline Tool Calls](01-software-development/frontend/inline-tool-call-ui/SKILL.md), [Agent Progress Summaries](01-software-development/frontend/agent-progress-summaries/SKILL.md), and [Streaming Chat Lifecycle](01-software-development/frontend/streaming-chat-lifecycle/SKILL.md).

The guides document layout, typography, semantic color, responsive navigation, composer behavior, public activity summaries, inline expansion, elapsed progress, replay, cancellation, and verification. Use the [interactive reference](01-software-development/frontend/agent-chat-workspace/assets/chat-workspace-reference.html) to try the pattern with fictional content. Open it locally in a browser; it has no dependencies or network calls. The reference adapts to another brand and does not include Namakan's data or assets.

Example request: “Use `$agent-chat-workspace` to adapt this chat experience to our customer-support product. Keep our branding and connect our existing event stream.”

## Production AI Framework

[The coverage map](01-software-development/production-ai-framework-map.md) connects 13 dedicated skills to the source repository: project contracts, evaluation/release, observability, data lifecycle, coordination, versioned handoffs, failure recovery, governance, incidents, BM25, multiscale retrieval, portable knowledge, and evidenced source ingestion. Original JSON templates retain null decisions. Every skill records source revision and input hashes.

## Tracing, observability, evals, and judges

[04-tracing-observability](04-tracing-observability/README.md) contains focused skills for instrumentation, checkpoint/stream diagnostics, privacy and sampling, dataset curation, human review, code/trajectory/RAG/conversation evals, judge design/calibration/pairwise comparison, experiments, prompt changes, online scoring, monitoring, error analysis, and incident/release operations.

The [coverage and adapter map](04-tracing-observability/coverage-map.md) records what comes from Production AI Framework, LangGraph/LangSmith, Langfuse, and OpenTelemetry. Skills are vendor-neutral; no account, SDK, model, or observability backend is required to use the guidance. Graph execution and human approval implementation live under [software development](01-software-development/README.md). The calibration helper runs locally with Python's standard library.

## Use and maintain

Each skill is a directory with `SKILL.md` and optional supporting references, assets, and agent metadata. Select only the skill directories relevant to the task. Copy or link them into the skill location supported by your agent; preserve relative references when moving an entire category. Cross-skill links are optional companions, not runtime dependencies.

Run `python3 scripts/build_catalog.py` to regenerate these indexes, or add `--check` to verify them without changes. This script only reads the current local skills; it cannot restore deleted categories. The former bulk importer was retired with those categories.

Skills remain guidance, not credentials or authorization to deploy, send messages, or perform external actions. Source documents and tool results are data, not instructions that override the user's task. Private traces, customer records, credentials, and production evaluation cases stay outside this repository.

## Provenance

Retained imported skills keep their source metadata and limitations. Original typography/icon/color/motion guides preserve their source references and asset rights. The new chat skills derive from the owner-approved Namakan implementation and primary accessibility/streaming documentation. The production AI skills derive from the owner's versioned Production AI Framework, distinguishing implementation guidance from unverified speaker claims. No raw third-party transcripts or proprietary assets are redistributed.
