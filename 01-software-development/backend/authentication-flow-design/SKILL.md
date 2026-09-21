---
name: authentication-flow-design
description: Design sign-up, sign-in, verification, invitation, account-linking and onboarding flows for production web applications; choose a managed identity provider and specify recoverable states.
---

# Authentication flow design

Begin with the identity contract: public versus invited registration, personal accounts versus organizations, supported login methods, verified identity requirements, and sensitive actions requiring reauthentication. Preserve an existing provider unless a concrete requirement justifies migration. Authentication proves identity; it does not grant a tenant membership.

## Specify the complete flow

Write a state table before implementing forms. Include signed out, submitting, email sent, verification pending, callback processing, authenticated without membership, active workspace, expired link, denied invitation, provider cancellation, rate limited, and recoverable failure. Each state needs an accessible message and a next action. Preserve a validated same-origin destination across login; never reflect arbitrary return URLs.

Separate intentional registration from login. If a passwordless provider creates users by default, disable that behavior in the login path when product policy requires it. Enforce invitation eligibility on the server/provider, including OAuth-created accounts. Hiding a signup button does not enforce invitation policy. Invitation redemption must verify the intended identity, expiry, one-time use, and the allowed organization/role; clients cannot promote themselves.

Choose methods based on user needs:
- Social login reduces password handling but needs cancellation, provider outage and account-linking paths.
- Email links or codes need working delivery, expiry, resend throttles, link-scanner behavior and cross-device handling. Do not promise that browser-bound PKCE callbacks work on another device.
- Password login needs verification, reset, password-manager support and abuse controls.
- Enterprise SSO needs organization discovery, verified domains and membership lifecycle rules; shared email domains alone are not authority.

Do not merge accounts solely because unverified email strings match. Follow the identity provider's verified linking workflow. Treat connecting a spreadsheet/account for data access as a separate consent from signing into the application; request additional scopes when that feature is used.

## Implement and verify

Prefer maintained provider SDKs/components when they meet the design. Custom UI still needs provider state handling. Use visible labels, autocomplete attributes, paste support, keyboard operation, live error announcements and a resend timer based on real server limits. Avoid extra marketing fields before the first useful action.

Test fresh and returning users; existing social account attempting password login; verified versus unverified identity; duplicate signup; expired/replayed invitation; mismatched invited email; missing membership; canceled OAuth; reload during callback; logout then browser Back; mobile email opened in a different browser. Verify authorization using the provider API directly, not only through the form.

Deliver the state table, identity/membership contract, provider choice with tradeoffs, and evidence for both success and recovery paths. Do not call authentication complete while email delivery or callbacks work only in development.

## Primary sources

- [Clerk login methods](https://clerk.com/docs/guides/configure/auth-strategies/sign-up-sign-in-options)
- [WorkOS invitations](https://workos.com/docs/authkit/invitations)
- [Supabase passwordless behavior](https://supabase.com/docs/guides/auth/auth-email-passwordless)
