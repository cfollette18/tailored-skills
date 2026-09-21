---
name: authentication-abuse-and-recovery
description: Build and test account recovery, email verification, password policy, MFA recovery and login abuse controls without leaking account existence or creating takeover paths.
---

# Authentication abuse and recovery

Treat recovery as an authentication mechanism with its own threat model. Prefer the identity provider's maintained implementation and configure it; a custom form must not weaken the provider's controls.

## Controls that change implementation

Use generic recovery responses and comparable processing paths for existing and nonexistent accounts. Do not reveal account existence through status codes, response timing, resend controls or logs returned to the caller. Apply layered limits by account and network/device signals; an IP-only lockout can punish shared networks, while permanent account lockout can enable denial of service. Use server-verified bot challenges when justified, with an accessible fallback.

Recovery tokens must be unpredictable, purpose-bound, short-lived and consumed once. Bind resets to the intended account and safe callback host. Rate-limit requesting and verifying codes separately. Never auto-login after a reset unless the provider's secure flow intentionally establishes a session; define whether existing sessions are revoked and test the actual provider behavior. Notify the account holder of sensitive changes without including secrets.

For password-based flows use the current NIST guidance as a baseline, not a claim of certification: at least 15 characters for single-factor passwords, at least 8 where passwords are always part of MFA, support at least 64, allow paste/password managers, block compromised/common choices, and avoid arbitrary composition rules or periodic forced changes without evidence of compromise. Check the provider's real limits and hashing behavior rather than implementing password storage locally.

MFA recovery must not reduce to an easier security question. Provide provider-supported backup/recovery methods with auditable, delayed/manual procedures where appropriate. Require recent authentication for factor removal and email changes. Do not claim email OTP or ordinary TOTP is phishing-resistant; evaluate passkeys/security keys for that requirement.

## Delivery and failure behavior

Use a production mail provider with an authenticated sending domain and verified delivery. Turn off link rewriting where it breaks auth links; test scanners consuming single-use links, resend invalidating earlier messages, bounces, delayed mail and different-device opening. A development SMTP default is not a launch-ready mail system.

Test rate-limit recovery, distributed guessing, reset replay, changing email during recovery, social-only accounts, unverified accounts, and concurrent requests. Ensure auth telemetry excludes passwords, tokens, full reset URLs and MFA seeds.

## Primary sources

- [OWASP authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP forgotten passwords](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [Supabase SMTP](https://supabase.com/docs/guides/auth/auth-smtp)
- [Supabase MFA assurance](https://supabase.com/docs/guides/auth/auth-mfa/totp)
