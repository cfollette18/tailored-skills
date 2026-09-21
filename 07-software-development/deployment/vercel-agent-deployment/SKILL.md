---
name: vercel-agent-deployment
description: Prepare Vercel-hosted applications with authentication, tenant-safe APIs and durable long-running agent workers; verify runtime limits, secrets, preview isolation and deployment readiness.
---

# Vercel agent deployment

Inventory the existing frontend, API, local databases, artifacts, background processes and credential stores. Determine which components actually fit the current Vercel runtime. Preserve working application behavior and data during migration; do not expose a localhost-oriented backend merely by adding a rewrite.

## Choose the boundary

Vercel can serve the frontend and bounded request handlers. Check current plan/runtime duration, filesystem, bundle and streaming limits. In-memory task registries and local SQLite files are not a durable shared job system. A serverless timeout increase does not make a detached subprocess reliable.

For an existing long-running process-based agent, prefer a durable worker service or a deliberately redesigned durable workflow. Persist jobs/events in managed storage, return a job ID promptly, and reconnect clients using a cursor. Bound SSE connections or use polling/realtime with resumable delivery. Define worker heartbeats, leases, cancellation and idempotency before enabling concurrent replicas. Vercel Workflow, queues or Sandbox may be options, but evaluate their present runtime compatibility and lifecycle rather than assuming they host an unchanged local agent.

For a Vite frontend, configure its real monorepo root, install/build commands and output directory. Confirm font/asset generation works in clean CI. Configure SPA fallback without swallowing API routes. A same-origin external API rewrite simplifies browser cookies/CORS but does not authenticate requests; protect the backend independently and validate trusted proxy headers only from known infrastructure.

## Production boundaries

Use exact callback URLs per environment. Preview deployments get separate auth/database settings and synthetic data; never copy production credentials indiscriminately. Public build variables are visible to users. Keep database admin, model, Langfuse and OAuth client secrets in server/worker secret stores. Do not upload a developer's entire home directory, Hermes profile, OAuth cache or ignored research data as a deployment artifact.

Authenticate every API, stream, preview and download, then authorize the current tenant and resource. Workers must receive a server-created job reference, not arbitrary filesystem paths or a caller-chosen identity. Give each tenant an isolated runtime/data/credential context. Migration of existing private data needs an explicit owner assignment; leave it private until that mapping is verified.

Trace web requests and workers with trusted user/workspace/job IDs, redacted inputs and a remote-reachable observability endpoint. `localhost` in a cloud runtime refers to that runtime, not the developer's machine. Separate test traces and preserve existing evaluation gates.

## Deployment evidence

Produce a deployment matrix for frontend, API, worker, database, storage, auth and telemetry; list the exact account/project and config each requires. Run build, auth callback tests, two-tenant API/storage tests, queued-job reconnect/cancel tests and a restore drill. Verify an authenticated preview before production promotion. If account access is unavailable, complete local artifacts and name the remaining account connection; do not describe an uncreated deployment as live.

## Primary sources

- [Vercel function limits](https://vercel.com/docs/functions/limitations)
- [Vercel runtimes](https://vercel.com/docs/functions/runtimes)
- [Vite deployment](https://vercel.com/docs/frameworks/frontend/vite)
- [External rewrites](https://vercel.com/docs/routing/rewrites)
- [Sandbox lifecycle](https://vercel.com/kb/guide/vercel-sandbox-duration-and-persistence)
