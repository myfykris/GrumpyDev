# Auth.js standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when identity linking, session lifetime, cookies, revocation, and per-resource
  authorization are explicit and tested.
