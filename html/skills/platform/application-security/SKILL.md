---
name: application-security
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review application-security plans and other engineering artifacts for trust boundaries, authentication, authorization, input handling, session safety, cryptography, abuse, and incident response. Project applicability: the project exposes security-sensitive application behavior, trust boundaries, untrusted input, or attack surface."
---

# Application security GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

During every review, check whether the work directly or indirectly affects
identity, authentication, authorization, tenant or trust boundaries, exposed
endpoints, untrusted input or output, uploads, server-side fetches, filesystem
access, parsing, deserialization, code or command execution, secrets, payments,
or sensitive data.

## Lean review

- Trace anonymous, low-privilege, cross-tenant, stale-role, replayed, malformed,
  automated, and compromised-account requests through each changed boundary.
- Require authorization for the exact object, property, function, and state
  transition. Authentication, hidden UI, and tenant query scopes are not enough.
- Validate after the final decode and normalization step, and encode output for
  its exact sink. Reject ambiguous representations and fail-open errors.
- Challenge injection, traversal, unsafe uploads, server-side request forgery,
  unsafe deserialization, custom cryptography, secrets in logs, check-then-use
  races, and exceptional paths that bypass security decisions.
- Require bounded abuse controls, session rotation and revocation, safe audit
  evidence, key rotation, patch ownership, and incident recovery.

Lean mode is insufficient for a new identity provider, authorization model,
tenant boundary, executable input path, cryptographic protocol, payment flow,
or sensitive-data trust transition.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/identity-sessions-and-authorization.md):
  Read when the reviewed work directly or indirectly changes authentication, object or
  property authorization, tenant
  isolation, session creation or rotation, cookies, CSRF, CORS, account recovery,
  revocation, role changes, or security-sensitive state transitions.
- [Focused rules](references/injection-output-and-untrusted-input.md):
  Read when the reviewed work directly or indirectly lets untrusted data reach
  HTML, attributes, URLs, CSS, JavaScript, SQL, NoSQL, operating-system commands,
  code, templates, dynamic identifiers, parsers, canonicalization, or other
  instruction-bearing sinks.
- [Focused rules](references/files-uploads-ssrf-and-deserialization.md):
  Read when the reviewed work directly or indirectly changes file or archive handling,
  uploads, path resolution,
  symlinks, temporary files, decompression, server-side URL fetching, redirects, DNS
  resolution, private network access, object deserialization, or schema and allocation
  limits.
- [Focused rules](references/cryptography-abuse-and-incident-response.md):
  Read when the reviewed work directly or indirectly changes encryption, hashing,
  signatures, tokens, key management,
  secret rotation, rate limits, automation abuse, fail-closed behavior, security logs,
  vulnerability response, patch ownership, alerts, or incident handling.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

Name the attacker capability, trust boundary, protected object or action,
failure mode, impact, and evidence required to accept the control.
