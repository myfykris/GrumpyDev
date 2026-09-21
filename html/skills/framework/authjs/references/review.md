# Auth.js full-review guidance

## Operating conditions

Establish the project target: Auth.js version and framework integration, providers, deployment
origins, session strategy, adapter and schema, cookie policy, account-linking policy, callback
ownership, and authorization boundary.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise first sign-in, repeat sign-in, denied consent, duplicate identity, expired tokens,
  sign-out, and revoked access.
- Test the actual adapter schema, migrations, callback failures, cookie behavior, and parallel
  requests under production routing.
- Inspect browser-visible session data, logs, redirects, and error pages for credentials or
  identity leakage.
