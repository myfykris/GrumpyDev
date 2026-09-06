---
name: php
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review PHP engineering work for runtime and extension compatibility, request lifecycle, typing, dependency resolution, serialization, process state, security, and deployment risks."
---

# PHP GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Check every reviewed change for direct or indirect effects on PHP execution,
runtime, or hosting, including changes made outside PHP files. Use the installed
framework, web server, storage, queue, and operating-system specialists rather
than assuming a conventional PHP stack.

## Lean review

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

Lean mode is insufficient when the reviewed work directly or indirectly changes SAPI,
PHP version, extensions,
serialization trust, session topology, process lifetime, deployment caching, or
an irreversible data boundary.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/types-and-boundary-data.md):
  Read when the reviewed work directly or indirectly changes weak or strict scalar
  coercion, union or nullable types,
  array shapes, numeric strings, truthiness, JSON conversion, reflection, magic access,
  encoding, locale, or data entering from requests, storage, queues, or environment.
- [Focused rules](references/request-and-process-lifecycle.md):
  Read when the reviewed work directly or indirectly depends on a SAPI, PHP-FPM,
  mod_php, CGI or FastCGI, request
  metadata, server variables, proxy mapping, long-running workers, resident application
  servers, persistent connections, output buffering, streaming, signals, shutdown,
  cancellation, or process recycling.
- [Focused rules](references/security-and-external-input.md):
  Read when the reviewed work directly or indirectly handles uploads, paths, stream
  wrappers, sessions, cookies,
  untrusted serialization, HTML or other output contexts, SQL or shell boundaries,
  temporary files, client-visible errors, or security-sensitive logging.
- [Focused rules](references/dependencies-and-deployment.md):
  Read when the reviewed work directly or indirectly changes PHP or extension versions,
  Composer resolution, plugins or
  scripts, classmaps, OPcache, preloading, generated framework artifacts, rolling
  releases, migrations, cache or queue payload compatibility, worker draining, restart,
  rollback, or recovery.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the affected PHP version, SAPI, lifecycle, and configuration scope. Name
any runtime or deployment assumption that repository evidence cannot prove.
