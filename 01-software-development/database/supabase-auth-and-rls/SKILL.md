---
name: supabase-auth-and-rls
description: Integrate Supabase Auth, PostgreSQL RLS and private Storage for a production application, including verified sessions, membership policies, SSR caching and deployment configuration.
---

# Supabase auth and RLS

Read the current docs for the selected framework and SDK versions before coding. Keep application policy separate from provider defaults; do not assume that enabling Auth makes tables or files private.

## Identity and clients

Use the publishable key for public clients and keep secret/service-role keys server-only. Privileged keys can bypass RLS; they are not an acceptable replacement for forwarding the user's verified authorization. Create request-scoped server clients so one user's session cannot leak into another request.

For SSR use the supported `@supabase/ssr` pattern for the framework version. Verify claims with the documented method; use `getUser()` or another server-backed session check when the operation requires current server state. Do not authorize from server-side `getSession()` alone. Preserve refreshed cookies and cache-control headers through redirects; never cache authenticated responses for another user. Browser-session storage has an XSS exposure; choose a server-owned session architecture if HttpOnly-only token storage is a requirement.

Configure exact production redirects, separate preview/staging projects, email confirmation, production SMTP, reasonable token expiry, rate limits and CAPTCHA where needed. Restrict registration server-side using configured Auth behavior or a before-user-created hook; a client setting alone is not invitation enforcement. Google application login and Google Drive/Sheets authorization are distinct grants.

## Tenant authorization

Create server-controlled workspaces/memberships and attach resources using compound tenant keys. Use `auth.uid()` only after authenticating; the unauthenticated value is null. Do not place authoritative roles in editable user metadata. For prompt revocation, look up current membership rather than trusting stale JWT membership claims. Restrict role and membership mutations to deliberately authorized operations.

Enable RLS on exposed tables before granting access. Use command-specific policies and safe column privileges. Audit views, RPCs, SECURITY DEFINER functions and service workers separately. Keep credential ciphertext in an unexposed schema with no client grants, and store encryption keys outside the database. Column encryption does not replace authorization.

Use private Storage buckets. Check ownership before producing short-lived signed URLs, and bind object prefixes to the tenant/resource manifest. A signed URL is a transferable capability until it expires; do not claim membership revocation invalidates it instantly. Database backups need a separate artifact-byte backup strategy.

## Verification and handoff

Run migrations in an isolated project and exercise anon, tenant A, tenant B, removed-member and privileged-worker paths. Test direct Data API requests, storage listing/download/upload/delete, RPCs and concurrent refresh. Verify that invitations cannot be bypassed by calling Auth directly. Inspect provider Security Advisor and actual production configuration without claiming that either alone certifies the system.

Record the exact SDK versions, key locations (never values), configured callbacks, SMTP delivery result, RLS tests and backup/restore evidence. State which paid-plan controls or provider configuration remain unverified.

## Primary sources

- [Supabase production checklist](https://supabase.com/docs/guides/deployment/going-into-prod)
- [API key types](https://supabase.com/docs/guides/getting-started/api-keys)
- [SSR clients](https://supabase.com/docs/guides/auth/server-side/creating-a-client)
- [Signup hook](https://supabase.com/docs/guides/auth/auth-hooks/before-user-created-hook)
- [Storage access](https://supabase.com/docs/guides/storage/security/access-control)
