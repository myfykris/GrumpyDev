---
name: authjs
description: Review Auth.js plans for providers, session strategy, adapters, callbacks, cookies, account linking, authorization, and deployment behavior. Use when a plan authenticates users with Auth.js or NextAuth.js.
---

# Auth.js plan review

Apply this guidance alongside the core GrumpyDev review and the `oauth`, `application-security`
and `secrets-configuration` skills.

## Inspect evidence

- Read the Auth.js package and framework adapter versions, provider setup, callbacks, events,
  and route wiring.
- Identify database or JWT session strategy, adapter schema, cookie settings, trust-host
  behavior, and proxy topology.
- Trace sign-in, callback, account linking, session lookup, refresh, sign-out, revocation, and
  authorization checks.
- Inspect secret sources, provider credentials, redirect origins, custom pages, middleware, and
  server-side consumers.

## Establish the operating model

Establish the project target: Auth.js version and framework integration, providers, deployment
origins, session strategy, adapter and schema, cookie policy, account-linking policy, callback
ownership, and authorization boundary.

Authentication proves identity and creates a session; it does not replace resource
authorization. The plan must separate provider tokens, Auth.js sessions, application
permissions, and tenant membership.

## Challenge the plan

### Recurring traps

Watch especially for callbacks treated as the only authorization layer, unsafe automatic account
linking, provider tokens exposed in sessions, stale JWT claims, database session cleanup
omitted, and host or cookie settings that change behind a proxy.

- Require stable account-linking keys and explicit policy for duplicate email addresses,
  provider changes, and unverified claims.
- Minimize data returned by session callbacks and keep provider refresh tokens and secrets out
  of browser-visible state.
- Define revocation and permission-change behavior for both JWT and database sessions,
  including stale authorization claims.
- Verify secure cookie names, domain, SameSite, proxy, base URL, callback, and trusted-host
  behavior in every environment.
- Require server-side authorization at each protected action, route, and data query rather than
  relying on session presence.

## Verify the claims

- Exercise first sign-in, repeat sign-in, denied consent, duplicate identity, expired tokens,
  sign-out, and revoked access.
- Test the actual adapter schema, migrations, callback failures, cookie behavior, and parallel
  requests under production routing.
- Inspect browser-visible session data, logs, redirects, and error pages for credentials or
  identity leakage.

## Ask when evidence is missing

- Which Auth.js version, framework adapter, providers, session strategy, database adapter, and
  deployment origins apply?
- How are accounts linked, provider credentials refreshed, sessions revoked, cookies scoped,
  and resources authorized?

## Calibrate findings

- Treat account takeover, provider-token disclosure, cross-tenant access, or missing server
  authorization as critical.
- Downgrade when identity linking, session lifetime, cookies, revocation, and per-resource
  authorization are explicit and tested.

## Add to the verdict

State provider and session choices, linking policy, exposed session fields, authorization
boundary, cookie behavior, revocation path, and identity tests.
