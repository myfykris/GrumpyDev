# PHP standard review

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

## Challenge the reviewed work

### Recurring traps

Watch especially for loose comparison and coercion, request globals trusted as
canonical input, persistent process resources surviving PHP-FPM request cleanup,
long-running worker state assumed to reset between jobs, session locks
serializing requests, encoding and normalization mismatches, include-path or
configuration drift, and stale OPcache behavior during deployment.

## Verify the claims

- Run repeated jobs or requests in the same long-lived process to expose state,
  resource, locale, transaction, and memory leakage. Include failure and
  cancellation between external side effects.
- Test malformed encodings, oversized bodies, partial uploads, invalid JSON,
  numeric edge cases, serialization-version overlap, session concurrency, and
  filesystem permission failures.
- Require production-like evidence for memory, latency, process count, pool
  saturation, and timeout claims. A single CLI benchmark does not represent a
  web or worker deployment.

## Ask when evidence is missing

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
