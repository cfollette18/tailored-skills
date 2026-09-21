---
name: production-database-selection
description: Compare managed production databases and auth integration using workload, tenant isolation, availability, recovery, operations and cost requirements rather than generic enterprise labels.
---

# Production database selection

Translate “production grade” into measurable requirements: data model, transactional invariants, tenant boundaries, expected concurrency, latency region, recovery point/time objectives, availability needs, operator capacity, retention and spend ceiling. Avoid choosing a distributed database merely because the product might grow.

## Compare architecture, not logos

| Option | Strong fit | Questions that can disqualify it |
|---|---|---|
| Managed Postgres with integrated auth/storage (for example Supabase) | Relational application data with JWT-aware RLS and private artifacts | Required plan controls, restore scope, compute headroom, regions, operational responsibility |
| Serverless Postgres (for example Neon) with managed auth | Bursty/serverless workloads and isolated preview databases | Cold-start tolerance, pool behavior, auth-to-database identity mapping, backup history, storage service |
| Aurora/RDS Postgres | Existing AWS network/IAM operations and specified HA/recovery controls | Operational complexity, cost floor, network access from frontend hosting, failover testing |
| Distributed SQL (for example CockroachDB) | Demonstrated regional survival or distributed transaction requirements | SQL/extension compatibility, transaction retries, RLS/CDC limitations and higher topology complexity |

Evaluate integrated auth, Clerk, WorkOS or another existing identity provider separately from the database. Native JWT integration can reduce glue, but authorization still needs policy and tests. Auth billing and SSO/SCIM entitlements are distinct from database/storage costs.

Compare the chosen service's current region/plan for pooling, backups/PITR, restore time, object-store backup, observability, maintenance, network restrictions, encryption/key ownership and support/SLA. Distinguish storage replication from a compute failover configuration. Vendor certification does not certify the application. A free tier can support evaluation without satisfying production retention or availability requirements.

## Proof before commitment

Prototype the hardest invariant with real database roles: two tenants, a removed member, a queued job, and a file download. Measure the hot query with RLS, indexes and realistic row counts. Test connection bursts and a restore into an isolated target. Model cost using reads/writes, compute uptime, egress, auth users, backup retention and worker concurrency; date any prices instead of hardcoding them into this skill.

Deliver a short decision record with a preferred option, a credible alternative, rejected options with concrete reasons, unresolved requirements and migration/exit costs. Keep recommendations conditional where workload or SLA is unknown. Avoid provisioning paid tiers or migrating existing records merely to complete a comparison.

## Primary sources

- [Supabase shared responsibility](https://supabase.com/docs/guides/deployment/shared-responsibility-model)
- [Neon pooling](https://neon.com/docs/connect/connection-pooling)
- [Neon branching](https://neon.com/docs/introduction/branching)
- [Aurora availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html)
- [CockroachDB RLS and limitations](https://www.cockroachlabs.com/docs/stable/row-level-security)
