---
name: wordpress
description: Review WordPress plans for lifecycle hooks, plugins, themes, blocks, REST endpoints, capabilities, nonces, validation, escaping, database access, cron, caching, updates, multisite, and rollback. Use when a plan changes WordPress core integration, plugins, themes, blocks, or operations.
---

# WordPress plan review

Apply this guidance alongside the core GrumpyDev review and the `php`,
applicable database and web-server, `application-security`, and deployment
skills. Select only companions that match the plan's real boundaries. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect WordPress and PHP targets, plugin and theme code, hook registrations,
  block metadata, REST routes, capability checks, nonce use, database queries,
  cron events, caches, filesystem access, update policy, and deployment
  runbooks.
- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.
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

## Challenge the plan

### Recurring traps

Watch especially for nonces mistaken for authorization, sanitization mistaken
for output escaping, hook order and global state, unreliable pseudo-cron timing,
dbDelta assumed to perform arbitrary migrations safely, stale persistent caches,
and automatic updates without a recovery path.

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
- Namespace functions, classes, options, metadata, routes, script handles, cron
  hooks, and database objects. Define activation, deactivation, uninstall,
  upgrade, and failed-upgrade behavior without deleting user data unexpectedly.
- Review `$wpdb` queries, schema changes, option autoloading, post meta,
  taxonomy, cache invalidation, and concurrency. Do not use the options table as
  an unbounded event store or lock service.
- Make WP-Cron timing limitations, duplicate execution, locks, retries,
  timeouts, and external scheduler integration explicit. Jobs must tolerate
  delayed and repeated invocation.
- Account for page, object, opcode, browser, CDN, and plugin caches plus
  multisite scope. Invalidation and cache keys must match tenant, locale,
  capability, and content ownership.
- Define ownership for core, plugin, theme, translation, and dependency updates;
  staging evidence; maintenance mode; filesystem credentials; mixed-version
  requests; database migration; rollback; and security response.

## Verify the claims

- Test anonymous, authenticated, insufficient-capability, expired-nonce, REST,
  AJAX, cron, CLI, admin, and multisite paths.
- Run static analysis and security tests for SQL injection, output contexts,
  uploads, SSRF, path handling, and capability bypass.
- Exercise activation, upgrade from supported versions, failure during
  migration, rollback, deactivation, and uninstall with preserved content.
- Load test hook, query, cache, cron, block, and REST behavior with
  production-shaped content and plugin combinations.

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

- Treat capability bypass, remote code execution, destructive upgrade or
  uninstall, cross-site data exposure, or an update path that cannot recover as
  critical or high according to blast radius and realistic likelihood.
- Treat a lifecycle, authorization, persistence, or deployment defect that
  breaks a core workflow or loses user state as material when the plan depends
  on it and lacks either a safe design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
core lifecycle and hooks, plugins, themes, blocks, REST endpoints, capabilities,
nonces, sanitization and escaping, database access, cron, caching, updates,
multisite, and rollback, verification evidence, deployment and recovery limits,
and any material assumption that remains unresolved.
