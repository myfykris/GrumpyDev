---
name: authjs
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Auth.js engineering work for providers, session strategy, adapters, callbacks, cookies, account linking, authorization, and deployment behavior."
---

# Auth.js GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `oauth`, `application-security`
and `secrets-configuration` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read the Auth.js package and framework adapter versions, provider setup, callbacks, events,
  and route wiring.

- Identify database or JWT session strategy, adapter schema, cookie settings, trust-host
  behavior, and proxy topology.

Watch especially for callbacks treated as the only authorization layer, unsafe
automatic account linking, provider tokens exposed in sessions, stale JWT
claims, database session cleanup omitted, and host or cookie settings that
change behind a proxy.

Lean mode is insufficient when this material severity condition may apply:

- Treat account takeover, provider-token disclosure, cross-tenant access, or missing server
  authorization as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Auth.js evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State provider and session choices, linking policy, exposed session fields, authorization
boundary, cookie behavior, revocation path, and identity tests.
