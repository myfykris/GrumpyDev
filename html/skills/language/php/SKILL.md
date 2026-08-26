---
name: php
description: Review PHP engineering plans for runtime and extension compatibility, request lifecycle, typing, dependency resolution, serialization, process state, security, and deployment risks. Use when a plan changes PHP applications, libraries, workers, command-line tools, or hosting configuration.
---

# PHP plan review

Apply this guidance alongside the core GrumpyDev review. Add the applicable web
server, framework, storage, queue, and operating-system specialists when those
boundaries materially affect the plan.

## Inspect evidence

- Read `composer.json`, `composer.lock`, repository configuration, Composer
  platform constraints, required extensions, autoload rules, scripts, plugin
  permissions, and the deployment artifact. Do not infer the production runtime
  from a developer's command-line interpreter.
- Compare PHP version, SAPI, loaded configuration files, extensions, INI values,
  error settings, timezone, locale, and encoding across web, CLI, worker, test,
  and CI environments. Treat configuration supplied by a web server, process
  manager, container, or hosting platform as part of the runtime contract.
- Read web-server and PHP integration configuration when a request plan depends
  on paths, headers, authentication, client addresses, HTTPS detection, or
  `$_SERVER`. Establish whether the application runs through Apache mod_php, CGI
  or FastCGI, PHP-FPM, an embedded server, a long-running application server, or
  another SAPI.
- Inspect front controllers, bootstrap and shutdown code, error and exception
  handlers, session configuration, stream wrappers, filesystem access,
  serialization, upload handling, queue workers, scheduled commands, and
  representative tests.
- Trace one request, command, and long-running job when those execution modes
  exist. Follow validation, authorization, transactions, output encoding,
  cleanup, error reporting, logging, and response construction.

## Establish the operating model

- State the supported PHP versions and the language or library features the plan
  depends on. Separate the Composer dependency solver's platform view from the
  runtime that actually executes the code.
- State the SAPI and process lifecycle for every affected environment.
  Conventional PHP-FPM resets request-scoped userland state even when its
  operating-system worker serves later requests, while persistent connections,
  extension state, OPcache, and preloaded code can remain process-wide. Queue
  workers and event-loop applications can retain userland state between units
  of work.
- Identify who constructs request metadata. `$_SERVER` contents vary with SAPI,
  web server, FastCGI parameters, proxy configuration, and INI settings. Values
  derived from request headers are untrusted unless a verified proxy boundary
  replaces or validates them.
- Identify which INI settings are changeable at system, directory, pool, or
  runtime scope. Configuration loaded by CLI can differ from web and worker
  SAPIs even on the same host.
- State extension, database-driver, ICU, OpenSSL, image, XML, and native-library
  dependencies when behavior or supported data depends on them. A loaded
  extension name alone does not establish compatible behavior across versions.
- Define session storage, cache, file, temporary-directory, upload, timezone,
  locale, and character-encoding assumptions. Name shared and per-process state.

## Challenge the plan

### Recurring traps

Watch especially for loose comparison and coercion, request globals trusted as
canonical input, persistent process resources surviving PHP-FPM request cleanup,
long-running worker state assumed to reset between jobs, session locks
serializing requests, encoding and normalization mismatches, include-path or
configuration drift, and stale OPcache behavior during deployment.

### Types and boundary data

- Trace weak coercion, strict typing boundaries, union and nullable types,
  array-shape assumptions, numeric strings, truthiness, comparison, and JSON
  conversion across public inputs and stored data. `strict_types` affects
  caller-side scalar argument coercion and is not a whole-application runtime
  mode.
- Require explicit validation before converting request, environment, database,
  queue, or deserialized data into domain values. Static analysis annotations do
  not validate runtime payloads.
- Check dynamic properties, magic accessors, reflection, attributes, named
  arguments, and method-signature compatibility against every supported PHP
  version and framework proxy behavior.
- Specify UTF-8 and error behavior at HTML, JSON, database, filesystem, mail,
  subprocess, and logging boundaries. Do not rely on a default locale or
  internal encoding to align independent systems.

### Request and process lifecycle

- Reject request-scoped assumptions in long-running workers. Static properties,
  singletons, global variables, locale, timezone, error handlers, open streams,
  database sessions, dependency-container instances, and library caches can
  survive into the next job or request.
- Require deterministic reset or process-recycle behavior for tenant, identity,
  transaction, tracing, and request-specific state. Garbage collection does not
  restore application invariants or close every external resource promptly.
- Check signal handling, graceful shutdown, job cancellation, time limits,
  memory limits, worker restarts, and partial cleanup. A killed worker can leave
  a remote operation committed even when PHP did not finish local handling.
- Verify output buffering, header construction, streaming, flush behavior, and
  client disconnect handling under the actual SAPI and reverse proxy.

### Security and external input

- Treat superglobals, uploaded-file metadata, environment variables, forwarded
  headers, cookies, sessions, and deserialized values as boundary input. Require
  context-specific HTML, attribute, URL, JavaScript, SQL, shell, and header
  handling rather than one generic escaping function.
- Reject unsafe native serialization of untrusted data. Account for object
  instantiation, magic methods, autoloading, gadget chains, and compatibility of
  stored serialized values during deployments.
- Check path normalization, stream wrappers, symbolic links, archive handling,
  upload moves, temporary-file permissions, and race conditions before file
  operations. An extension check on the original filename is not a filesystem
  security boundary.
- Verify session cookie attributes, fixation prevention, regeneration timing,
  concurrent request behavior, storage locking, logout invalidation, and secret
  rotation. Authorization must be re-established at the protected operation.
- Ensure production errors are not rendered to clients and that logs redact
  credentials, session identifiers, tokens, personal data, and raw payloads.

### Dependencies and deployment

- Verify that the lockfile was resolved for the intended PHP and extension
  platform. Review Composer plugins, scripts, abandoned packages, replacement
  packages, autoload changes, and optimized or authoritative classmaps.
- Analyze OPcache and preloading behavior, generated containers, framework
  caches, route and template caches, and immutable artifacts. Old workers can
  retain old code or configuration after files change.
- Require a mixed-version compatibility window for rolling web and worker
  deployments. Coordinate database migrations, session formats, cache values,
  queued payloads, serialized objects, and API contracts across old and new
  processes.
- Define restart, drain, health, rollback, and recovery behavior for PHP-FPM,
  application servers, queue workers, schedulers, and web-server reloads. A code
  rollback does not reverse destructive data or incompatible queued messages.

## Verify the claims

- Test the exact supported PHP versions, SAPIs, extension sets, INI profiles,
  and dependency lockfile in CI or equivalent reproducible environments.
- Exercise request metadata behind the real proxy and web-server arrangement,
  including HTTPS, host, port, path information, client address, forwarded
  headers, missing variables, and hostile values.
- Run repeated jobs or requests in the same long-lived process to expose state,
  resource, locale, transaction, and memory leakage. Include failure and
  cancellation between external side effects.
- Test malformed encodings, oversized bodies, partial uploads, invalid JSON,
  numeric edge cases, serialization-version overlap, session concurrency, and
  filesystem permission failures.
- Rehearse deployment with old and new web workers and queue workers active at
  the same time. Verify cache invalidation, OPcache refresh or restart,
  migration ordering, drain behavior, rollback limits, and observable health.
- Require production-like evidence for memory, latency, process count, pool
  saturation, and timeout claims. A single CLI benchmark does not represent a
  web or worker deployment.

## Ask when evidence is missing

- If the plan uses version-specific syntax, runtime behavior, or dependencies,
  ask which PHP versions and extension versions execute the affected web, CLI,
  worker, CI, and test paths.
- If request metadata or routing affects correctness or security, ask which
  SAPI, web server, FastCGI or proxy mapping, trusted proxy rules, and exact
  `$_SERVER` values form the contract.
- If the plan adds a daemon, worker, scheduler, or application server, ask what
  state survives between units of work and how shutdown, cleanup, memory growth,
  and deployment restarts are controlled.
- If configuration can differ by environment, ask which INI files, pool values,
  environment sources, and runtime overrides are authoritative.
- If serialized, cached, session, or queued values cross a deployment, ask how
  old and new code coexist and how incompatible values are detected or removed.

## Calibrate findings

- Treat request-to-request identity or tenant leakage, authorization bypass,
  injection, unsafe untrusted deserialization, arbitrary file access, exposed
  secrets, or unrecoverable data corruption as critical.
- Treat a version, SAPI, extension, worker-lifecycle, or migration mismatch as a
  required revision when it can break a supported path or deployment.
- Treat undocumented configuration variance as an evidence gap until the
  affected runtime is identified. Do not claim a defect solely because another
  deployment model could behave differently.
- Downgrade or omit findings when the actual runtime matrix is bounded and
  representative tests prove types, validation, request metadata, persistent
  state reset, error handling, resource cleanup, mixed-version operation, and
  rollback behavior.

## Add to the verdict

State the supported PHP and extension targets, SAPI and process lifecycle,
configuration authority, request-metadata trust boundary, persistent-state
hazards, serialization and encoding contracts, deployment overlap, restart and
rollback behavior, and the evidence that supports those conclusions.
