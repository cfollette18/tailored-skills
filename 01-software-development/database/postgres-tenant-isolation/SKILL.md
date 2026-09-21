---
name: postgres-tenant-isolation
description: Design and verify PostgreSQL tenant isolation with row-level security, least-privilege roles, membership checks, tenant-safe foreign keys and adversarial cross-tenant tests.
---

# Postgres tenant isolation

Define the tenant and authorization matrix first: who can read, create, change, delete, export and administer each resource. Authentication is necessary but insufficient. Derive identity from a verified token/session, and resolve current membership from server-owned data. Never authorize using a requested tenant ID or user-editable profile metadata alone.

## Database boundary

Use explicit least-privilege grants plus RLS. Separate migration/owner, application, worker and backup roles. Owners normally bypass policies; FORCE ROW LEVEL SECURITY subjects owners to them, but does not constrain superusers or BYPASSRLS roles. Exercise policies through the actual unprivileged role, not just the SQL console owner.

Specify both read/target visibility (USING) and allowed new row state (WITH CHECK), including ownership/tenant changes. Permissive policies combine with OR, so a broad additional policy can undo a careful restriction. Restrictive policies need an applicable permissive policy. Missing policies deny ordinary access when RLS is enabled.

Carry a non-null tenant key on tenant data. Use compound unique keys and foreign keys such as `(tenant_id, parent_id)` so a child cannot attach to a parent from another tenant. Restrict sensitive columns separately: RLS is not column authorization. Membership and role changes need controlled server operations, not an unrestricted self-update policy.

For membership-based policies, avoid self-recursive membership queries. Use a narrowly scoped helper only if needed, with fixed search_path, fully qualified objects, controlled EXECUTE grants and a reviewed SECURITY DEFINER owner. Views and privileged functions can bypass intended policy; use invoker semantics where appropriate and test every exposed RPC/view. Referential-integrity checks can reveal existence through constraint errors; return safe application errors.

If a trusted backend supplies identity via a custom setting, parameterize `set_config(..., true)` inside the same explicit transaction as every protected query. Never let an untrusted SQL client choose that setting. Transaction pooling must not carry identity between requests; session-level SET and checkout/release assumptions are insufficient.

## Non-database boundaries

Apply the same tenant ownership to object paths, cache keys, search indexes, events, telemetry and background jobs. A service-role worker may bypass RLS; it must claim jobs from server-owned records, validate resource relationships and recheck revoked membership before external actions. Do not describe privileged-worker queries as protected by end-user RLS.

## Verification

Use the [isolation test matrix](references/isolation-tests.md). Prove negative cases directly through the database/API as two unrelated users, then through application routes. Include removed membership without refreshing an old JWT, cross-tenant reassignment, views/functions, pooled request reuse and file URLs. Use EXPLAIN ANALYZE with realistic data and the application role; index tenant/membership predicates.

## Primary sources

- [Postgres row security semantics](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- [Supabase policies and invoker views](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Column privileges](https://supabase.com/docs/guides/database/postgres/column-level-security)
- [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
