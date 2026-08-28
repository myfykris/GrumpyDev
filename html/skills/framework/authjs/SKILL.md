---
name: authjs
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Auth.js plans and other engineering artifacts for providers, session strategy, adapters, callbacks, cookies, account linking, authorization, and deployment behavior. Project applicability: the project uses or materially depends on Auth.js."
---

# Auth.js GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `oauth`, `application-security`
and `secrets-configuration` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
