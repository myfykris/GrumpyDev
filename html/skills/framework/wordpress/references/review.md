# WordPress standard review

## Inspect additional evidence

- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: WordPress, PHP, database and web-server versions,
hosting topology, multisite, plugin and theme ownership, cache and object store,
update policy, filesystem access, and deployment process. The changed boundary
must define: Core lifecycle and hooks, plugins, themes, blocks, REST endpoints,
capabilities, nonces, sanitization and escaping, database access, cron, caching,
updates, multisite, and rollback.

Assign lifecycle, state, dependency, persistence, and security ownership for
Core lifecycle and hooks, plugins, themes, blocks, REST endpoints, capabilities,
nonces. Prove sanitization and escaping, database access, cron, caching,
updates, multisite, rollback through startup, invalid or denied work,
cancellation, background execution, mixed versions, shutdown, rollback, and
recovery.

## Challenge the reviewed work

### Recurring traps

- Place hooks on the correct action or filter with the right priority, accepted
  arguments, request context, and registration lifetime. Prevent repeated
  registration, recursive filters, and work that runs on every request without
  need.
- Enforce capabilities at the side-effect boundary. Nonces help with request
  intent but are not authentication or authorization, and REST, AJAX, cron, CLI,
  and admin paths need their own checks.
- Validate or reject input early, normalize once, use safe database APIs, and
  escape for the exact output context as late as possible. Sanitizing on write
  does not remove the need for contextual output escaping.
## Verify the claims

- Test anonymous, authenticated, insufficient-capability, expired-nonce, REST,
  AJAX, cron, CLI, admin, and multisite paths.
- Run static analysis and security tests for SQL injection, output contexts,
  uploads, SSRF, path handling, and capability bypass.
## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: WordPress, PHP,
database and web-server versions, hosting topology, multisite, plugin and theme
ownership, cache and object store, update policy, filesystem access, and
deployment process. For the changed boundary, ask only about unresolved Core
lifecycle and hooks, plugins, themes, blocks, REST endpoints, capabilities,
nonces, sanitization and escaping, database access, cron, caching, updates,
multisite, and rollback when the answer can change the verdict or
implementation.

## Calibrate findings

- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the reviewed work depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
