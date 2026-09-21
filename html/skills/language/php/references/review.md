# PHP full-review guidance

## Operating conditions

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

## Failure patterns

Watch especially for loose comparison and coercion, request globals trusted as
canonical input, persistent process resources surviving PHP-FPM request cleanup,
long-running worker state assumed to reset between jobs, session locks
serializing requests, encoding and normalization mismatches, include-path or
configuration drift, and stale OPcache behavior during deployment.

## Verification to run or specify in the plan

- Run repeated jobs or requests in the same long-lived process to expose state,
  resource, locale, transaction, and memory leakage. Include failure and
  cancellation between external side effects.
- Test malformed encodings, oversized bodies, partial uploads, invalid JSON,
  numeric edge cases, serialization-version overlap, session concurrency, and
  filesystem permission failures.
- Require production-like evidence for memory, latency, process count, pool
  saturation, and timeout claims. A single CLI benchmark does not represent a
  web or worker deployment.
