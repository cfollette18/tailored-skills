# Tenant isolation verification matrix

Use isolated fixtures with two unrelated tenants and at least owner/member/viewer roles. Run tests as the actual application role and verified identities. Running every test through a service key or database owner bypasses the boundary being tested.

| Case | Required result |
|---|---|
| Unauthenticated direct table read/write | No private rows; writes rejected |
| Tenant A resource list | Only allowed A rows |
| Tenant A requests guessed B identifier | No B data, including errors, counts or signed URLs |
| Insert with B tenant or parent key | Rejected by policy/constraint |
| Update resource ownership or tenant | Rejected unless explicit authorized transfer exists |
| Update own membership role to owner | Rejected |
| Viewer reads versus writes | Reads allowed by contract; writes denied |
| Membership removed with old unexpired JWT | Denied when policy requires current membership |
| View, aggregate, join, RPC | Same boundary as direct table |
| SECURITY DEFINER helper | Callable only as intended; no argument permits identity impersonation |
| Pool reuse from A to B to anonymous | No previous request identity survives |
| Artifact list/download/preview/cloud export | Same ownership check for bytes and metadata |
| Signed URL after removal | Matches documented bounded expiry; no promise of instant revocation |
| Queue claim or retry after membership removal | Contract enforced before privileged side effects |
| Duplicate/retried job | No duplicate externally visible effect |
| Tenant-scoped cache/search/event subscription | No B content or events delivered to A |
| Schema migration | Grants and RLS still enforce the matrix |
| Backup restore | Policies, grants and object ownership restored correctly |

Assert both allowed and denied operations. On policy denial, verify the row remains unchanged and that an UPDATE affecting zero rows is not reported as a successful mutation. Include concurrent attempts and transaction rollback. Preserve a distinction between a local PostgreSQL test, a provider Data API test, and a complete hosted browser test; each proves a different boundary.
