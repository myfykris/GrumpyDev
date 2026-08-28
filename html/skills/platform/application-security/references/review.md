# Application security standard review

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

Map every untrusted actor and data path to the parser, identity, authorization,
state-change, output, audit, and incident-response controls that own it. Identify
who can change those controls and prove exceptional paths fail closed without
turning dependency failure, overload, or partial persistence into an
authorization or integrity bypass.

## Challenge the reviewed work

### Recurring traps

Watch especially for authentication mistaken for authorization, missing
object, property, or function checks, validation before the final decode or
canonicalization step, one sanitizer reused across incompatible output
contexts, fail-open exceptional behavior, server-side request forgery through
indirect fetches, secrets in logs, and check-then-use races at security
boundaries.

## Verify the claims

- Exercise old and new identity, session, policy, parser, and data versions
  together during rollout and rollback. Verify neither version interprets the
  other's state more permissively.
- Force timeouts, exceptions, malformed dependency responses, partial commits,
  log and alert delivery failures, and resource exhaustion to prove the system
  denies unsafe work, preserves invariants, and remains diagnosable.

## Ask when evidence is missing

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
