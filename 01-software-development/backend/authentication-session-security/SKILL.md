---
name: authentication-session-security
description: Implement and review production web sessions, OAuth callbacks, token verification, CSRF boundaries and logout behavior across browser, server and worker runtimes.
---

# Authentication session security

Map where credentials and sessions live before choosing cookie or bearer-token patterns. A browser-only SPA and a backend-for-frontend have different trust boundaries. Use a supported identity SDK; do not invent JWT signing, refresh rotation, or OAuth state handling.

## Trust boundaries

On the server verify signature, allowed algorithm, issuer, audience, expiry and subject using the provider's documented verification method. Decoding a JWT or reading an SDK session object is not identity verification. Cache JWKS with rotation support and a bounded unknown-key refresh. Use immutable provider subject IDs for ownership, not email addresses or client-supplied user IDs.

Use authorization code with PKCE and the provider's CSRF/state protection. Match allowed callback destinations precisely in production. Validate same-origin return paths and preserve one-time exchange semantics. Never log authorization codes, refresh tokens, cookies or callback URLs containing secrets.

For a server-owned session, use Secure, HttpOnly, appropriate SameSite cookies and explicit CSRF protection for state changes. SameSite alone is not a complete CSRF model. For SDK-managed browser sessions, document that JavaScript can access the session and control XSS accordingly; do not blindly set HttpOnly on cookies that the chosen SDK must read. Never put privileged database keys into public build variables.

Use one refresh owner per request boundary and preserve all refreshed cookies on redirects and responses. Disable shared caching of authenticated responses and Set-Cookie responses. Partition client caches by identity/workspace, and clear them on signout/account switch. Inspect service workers and prefetched pages as well as normal requests.

## Revocation and sensitive actions

Short-lived access tokens may remain valid after refresh-session revocation. Specify the acceptable revocation delay. Use provider-backed session checks or an application revocation/membership check where immediate removal is required. Check current authorization again for exports, credential changes, tenant administration and queued jobs, rather than relying indefinitely on stale claims.

Reauthenticate before high-impact account changes. Treat MFA enrollment, challenge, replacement and recovery as separate tested flows. An enrolled factor does not mean the current session completed MFA; enforce the provider's assurance level where needed.

Test forged/expired/wrong-audience/wrong-issuer tokens, key rotation, concurrent refresh, session fixation, cross-origin mutations, replayed callbacks, open redirects, logout across tabs, and account switching with cached data. Keep tests isolated from production identities.

## Primary sources

- [OAuth security BCP, RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html)
- [OWASP session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [Supabase SSR verification/caching](https://supabase.com/docs/guides/auth/server-side/creating-a-client)
- [Supabase JWTs](https://supabase.com/docs/guides/auth/jwts)
