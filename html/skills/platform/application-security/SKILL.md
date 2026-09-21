---
name: gd-application-security
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review application-security engineering work for trust boundaries, authentication, authorization, input handling, session safety, cryptography, abuse, and incident response."
---

# Application security GrumpyDev review

## Quick checks

- Trace anonymous, low-privilege, cross-tenant, stale-role, replayed, malformed,
  automated, and compromised-account requests through every changed boundary.
- Require authorization for the exact object, property, function, and state
  transition. Authentication, hidden UI, and tenant query scopes are not enough.
- Validate after final decoding and normalization, encode for the exact sink,
  bound abusive work, and prove exceptional paths fail closed.
- Challenge injection, traversal, unsafe uploads, server-side request forgery,
  unsafe deserialization, custom cryptography, leaked secrets, check-then-use
  races, weak session revocation, and incident paths with no owner.

## References

- For a material security effect or uncertainty in a full review, read
  [review.md](references/review.md).
- For identity, sessions, authorization, tenant isolation, CSRF, or CORS, read
  [identity-sessions-and-authorization.md](references/identity-sessions-and-authorization.md).
- For untrusted input reaching instruction-bearing or output sinks, read
  [injection-output-and-untrusted-input.md](references/injection-output-and-untrusted-input.md).
- For files, uploads, archives, server-side fetches, or deserialization, read
  [files-uploads-ssrf-and-deserialization.md](references/files-uploads-ssrf-and-deserialization.md).
- For cryptography, tokens, keys, abuse controls, or incident response, read
  [cryptography-abuse-and-incident-response.md](references/cryptography-abuse-and-incident-response.md).

## Verdict context

Name the attacker capability, trust boundary, protected action, failure mode,
impact, and evidence needed to accept the control.
