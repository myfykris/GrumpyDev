# Application security full-review guidance

## Operating conditions

Establish the project target: Security requirements, data sensitivity, threat
actors, identity providers, trust zones, compliance constraints, secret
handling, scanning, and incident ownership. The changed boundary must define:
Trust boundaries, threat modeling, input handling, authentication,
authorization, sessions, injection, SSRF, file handling, crypto use, abuse,
dependencies, and incident response.

## Failure patterns

Watch especially for authentication mistaken for authorization, missing
object, property, or function checks, validation before the final decode or
canonicalization step, one sanitizer reused across incompatible output
contexts, fail-open exceptional behavior, server-side request forgery through
indirect fetches, secrets in logs, and check-then-use races at security
boundaries.

## Verification to run or specify in the plan

- Exercise old and new identity, session, policy, parser, and data versions
  together during rollout and rollback. Verify neither version interprets the
  other's state more permissively.
- Force timeouts, exceptions, malformed dependency responses, partial commits,
  log and alert delivery failures, and resource exhaustion to prove the system
  denies unsafe work, preserves invariants, and remains diagnosable.
