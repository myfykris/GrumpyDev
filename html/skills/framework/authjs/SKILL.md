---
name: gd-authjs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Auth.js engineering work for providers, session strategy, adapters, callbacks, cookies, account linking, authorization, and deployment behavior."
---

# Auth.js GrumpyDev review

## Quick checks

- Read the Auth.js package and framework adapter versions, provider setup, callbacks, events,
  and route wiring.

- Identify database or JWT session strategy, adapter schema, cookie settings, trust-host
  behavior, and proxy topology.

Watch especially for callbacks treated as the only authorization layer, unsafe
automatic account linking, provider tokens exposed in sessions, stale JWT
claims, database session cleanup omitted, and host or cookie settings that
change behind a proxy.

- Assess account takeover, provider-token disclosure, cross-tenant access, or missing server
  authorization under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Auth.js specialist.

## Verdict context

State provider and session choices, linking policy, exposed session fields, authorization
boundary, cookie behavior, revocation path, and identity tests.
