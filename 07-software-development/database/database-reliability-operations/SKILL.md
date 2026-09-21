---
name: database-reliability-operations
description: Prepare managed PostgreSQL for production with recoverable migrations, connection budgets, backup and restore verification, retention, monitoring and idempotent background work.
---

# Database reliability operations

Define recovery point and recovery time objectives with the application's owner. Choose the provider plan and architecture that meet them, and measure recovery rather than equating “backups enabled” with recoverability.

## Recovery and data lifecycle

Inventory database rows, object bytes, encryption keys, auth configuration and external integration settings. Back up and restore each dependency. A database backup that contains file metadata may not contain the actual uploaded files. Store immutable artifact versions with checksums and verify them after restore. Keep backups isolated from ordinary application credentials.

Restore into a new isolated target first, using synthetic or access-controlled data. Verify row counts/invariants, tenant policies, identities, roles, file references and application reads. Record achieved RPO/RTO, recovery steps, credential rotation and cutover/rollback criteria. Define deletion, retention, legal hold where applicable, and when deleted data ages out of backups; do not promise instant deletion from retained backups.

## Migrations and connections

Use versioned, reviewed migrations and one deployment owner. Favor expand/backfill/contract changes so old and new application versions coexist. Bound lock and statement duration; batch backfills and measure replica lag. Evaluate concurrent index creation and its transaction restrictions. Application rollback is not a safe substitute for destructive database rollback. Test old-version compatibility before promotion.

Budget database connections across all function instances, pools, workers and administration. Use a documented pooler mode suited to the workload; verify prepared-statement support with the exact driver/pooler versions. Use direct/session connections for tools requiring session features. Retries need limits and jitter and must cover an entire failed transaction when required, not just its last statement.

For jobs, persist state and ownership before execution. Claim atomically with a lease/fencing mechanism, renew the lease, and make effects idempotent using stable operation keys. Store an outbox in the same transaction when dispatching external work. A browser disconnect must not lose the job, and a retry must not duplicate a report upload or billable action. A queue does not by itself guarantee exactly-once effects.

## Operating evidence

Monitor connection saturation, slow queries, lock waits, storage growth, error rate, replication lag, failed backups and queue age. Audit privileged access. Recheck policies/grants after migrations, not only table existence. Preview databases must use synthetic/redacted data or deliberately restricted access; a branch may inherit production contents.

Deliver migrations, restore runbook, connection budget, alert owners and a demonstrated restore result. Distinguish tests run locally from provider failover/PITR tests still pending.

## Primary sources

- [Supabase backup scope](https://supabase.com/docs/guides/platform/backups)
- [Supabase connection modes](https://supabase.com/docs/guides/database/connecting-to-postgres)
- [Neon connection pooling](https://neon.com/docs/connect/connection-pooling)
- [Neon branching and restore](https://neon.com/docs/introduction/branching)
