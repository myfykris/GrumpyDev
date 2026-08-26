---
name: application-security
description: Review application-security plans for trust boundaries, authentication, authorization, input handling, session safety, cryptography, abuse, and incident response. Use when a plan changes security-sensitive application behavior or exposed attack surface.
---

# Application security plan review

Apply this guidance alongside the core GrumpyDev review and the relevant
framework, protocol, and storage skills.

## Inspect evidence

- Read the threat model, trust boundaries, identity flow, authorization checks,
  input and output handling, sessions, secrets, audit logs, and security tests.
- Trace anonymous, low-privilege, cross-tenant, replayed, malformed, automated,
  and compromised-account requests through every boundary.

## Establish the operating model

Establish the project target: Security requirements, data sensitivity, threat
actors, identity providers, trust zones, compliance constraints, secret
handling, scanning, and incident ownership. The changed boundary must define:
Trust boundaries, threat modeling, input handling, authentication,
authorization, sessions, injection, SSRF, file handling, crypto use, abuse,
dependencies, and incident response.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Trust boundaries, threat modeling, input handling,
authentication, authorization, sessions, injection. Prove SSRF, file handling,
crypto use, abuse, dependencies, incident response through rotation, overload,
partial rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for authentication mistaken for authorization, missing
object, property, or function checks, validation before the final decode or
canonicalization step, one sanitizer reused across incompatible output
contexts, fail-open exceptional behavior, server-side request forgery through
indirect fetches, secrets in logs, and check-then-use races at security
boundaries.

- Require authorization at every object, property, function, and state-change
  boundary. Test anonymous, lower-privilege, cross-tenant, stale-role, and
  guessed-identifier requests; a hidden button or authenticated route is not
  access control.
- Define the complete transformation chain before validating input. Decode and
  normalize once, reject ambiguous or duplicate representations, and validate
  the value the dangerous sink will actually consume.
- Prevent cross-site scripting with output encoding for the exact HTML,
  attribute, URL, CSS, or JavaScript context. Avoid unsafe DOM and template
  sinks, sanitize intentionally supported markup, and use Content Security
  Policy as defense in depth rather than the primary control.
- Prevent SQL, NoSQL, operating-system command, code, and template injection
  with parameterized APIs or fixed command arguments. Allowlist dynamic
  identifiers and operations; escaping and deny lists are not general
  substitutes for separating data from instructions.
- Constrain file reads, writes, and archive extraction to an intended root or
  object authority. Cover absolute and alternate paths, traversal, symlinks,
  archive entries, replacement races, filename collisions, and cleanup.
- Treat uploads as untrusted content. Bound bytes, item count, nesting, and
  decompression; establish type from content where relevant; store outside an
  executable web path; randomize server names; scan or transform when the risk
  requires it; and serve with safe type and disposition headers.
- For every server-side URL fetch, allow only required schemes, destinations,
  ports, redirects, and response sizes. Recheck resolved addresses, block local,
  link-local, metadata, and private ranges when not explicitly required, and
  enforce network egress boundaries plus timeouts.
- Reject unsafe deserialization of attacker-controlled types or executable
  object graphs. Apply schema and size limits to messages before allocation or
  side effects, including signed or otherwise integrity-protected data.
- Use established cryptographic libraries and protocols; reject custom
  encryption, token formats, password hashing, or signature rules.
- Define session rotation, revocation, CSRF, CORS, cookie flags, rate limits,
  abuse detection, and account recovery explicitly.
- Make exceptional and dependency failures fail closed at security boundaries.
  Roll back partial effects, avoid success from incomplete authorization or
  validation, return non-sensitive client errors, and correlate them to useful
  internal diagnostics.
- Demand a hardened production baseline, safe logs and alerts, vulnerability
  response, key rotation, dependency patch ownership, and tests for the
  highest-impact abuse paths.

## Verify the claims

- Verify these behaviors through the effective Application security
  configuration and runtime topology: Trust boundaries, threat modeling, input
  handling, authentication, authorization, sessions, injection. Use effective
  rendered configuration and deployable artifacts in a representative identity,
  topology, capacity, and policy boundary.
- Exercise failure and edge behavior for: SSRF, file handling, crypto use,
  abuse, dependencies, incident response. Exercise startup, readiness, normal
  load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Build an authorization matrix covering actor, tenant, object, property,
  function, and state. Run its denied cases through the real entry point and
  data boundary, not only a mocked policy function.
- Exercise encoded and duplicate parameters, output contexts, parser and
  archive bombs, path and symlink changes, redirect and DNS changes, oversized
  third-party responses, upload handling, and unsafe deserialization where
  those boundaries exist.
- Force timeouts, exceptions, malformed dependency responses, partial commits,
  log and alert delivery failures, and resource exhaustion to prove the system
  denies unsafe work, preserves invariants, and remains diagnosable.

## Ask when evidence is missing

- Which actors cross each changed trust boundary, and where are object,
  property, function, tenant, and state-change permissions enforced?
- Which hostile input or output context, abuse case, exceptional failure,
  credential failure, or incident response path can change the design?

## Calibrate findings

- Treat an unbounded path to unauthorized access, privilege escalation, secret
  exposure, or irreversible data change as critical.
- Downgrade or omit the finding when the boundary is unreachable by untrusted
  actors or tested centralized controls enforce it.

## Add to the verdict

State trust boundaries, authorization enforcement, hostile input and output
paths, fail-closed behavior, session and cryptography choices, abuse controls,
and security evidence.
