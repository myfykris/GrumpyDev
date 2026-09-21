# WordPress full-review guidance

## Operating conditions

Establish the project target: WordPress, PHP, database and web-server versions,
hosting topology, multisite, plugin and theme ownership, cache and object store,
update policy, filesystem access, and deployment process. The changed boundary
must define: Core lifecycle and hooks, plugins, themes, blocks, REST endpoints,
capabilities, nonces, sanitization and escaping, database access, cron, caching,
updates, multisite, and rollback.

## Failure patterns

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

## Verification to run or specify in the plan

- Test anonymous, authenticated, insufficient-capability, expired-nonce, REST,
  AJAX, cron, CLI, admin, and multisite paths.
- Run static analysis and security tests for SQL injection, output contexts,
  uploads, SSRF, path handling, and capability bypass.
