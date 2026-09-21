---
name: gd-php
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review PHP engineering work for runtime and extension compatibility, request lifecycle, typing, dependency resolution, serialization, process state, security, and deployment risks."
---

# PHP GrumpyDev review

## Quick checks

- Establish supported PHP versions, SAPI, process lifecycle, loaded
  configuration, extensions, and Composer platform constraints for each web,
  CLI, worker, test, and CI boundary.
- Do not infer production behavior from a developer CLI. Apache mod_php,
  CGI/FastCGI, PHP-FPM, embedded servers, and long-running application servers
  expose different lifecycle and request metadata.
- Treat `$_SERVER`, proxy-derived identity, uploads, serialization, filesystem
  paths, sessions, locale, timezone, and encoding as explicit boundaries.
- Challenge weak coercion, loose comparison, request-scoped assumptions in
  workers, session locking, persistent resources, stale OPcache, and deployment
  artifacts that do not match the locked dependency and extension contract.
- Require deterministic cleanup for tenant, identity, transaction, tracing, and
  request state in long-running processes.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the PHP specialist.

- [Focused rules](references/types-and-boundary-data.md):
  Read when the work changes weak or strict scalar
  coercion, union or nullable types,
  array shapes, numeric strings, truthiness, JSON conversion, reflection, magic access,
  encoding, locale, or data entering from requests, storage, queues, or environment.
- [Focused rules](references/request-and-process-lifecycle.md):
  Read when the work depends on a SAPI, PHP-FPM,
  mod_php, CGI or FastCGI, request
  metadata, server variables, proxy mapping, long-running workers, resident application
  servers, persistent connections, output buffering, streaming, signals, shutdown,
  cancellation, or process recycling.
- [Focused rules](references/security-and-external-input.md):
  Read when the work handles uploads, paths, stream
  wrappers, sessions, cookies,
  untrusted serialization, HTML or other output contexts, SQL or shell boundaries,
  temporary files, client-visible errors, or security-sensitive logging.
- [Focused rules](references/dependencies-and-deployment.md):
  Read when the work changes PHP or extension versions,
  Composer resolution, plugins or
  scripts, classmaps, OPcache, preloading, generated framework artifacts, rolling
  releases, migrations, cache or queue payload compatibility, worker draining, restart,
  rollback, or recovery.

## Verdict context

State the affected PHP version, SAPI, lifecycle, and configuration scope. Name
any runtime or deployment assumption that repository evidence cannot prove.
