---
name: python
description: Review Python engineering plans for packaging, runtime, typing, concurrency, resource management, dependency, and test risks. Use when a plan changes Python applications, libraries, workers, scripts, APIs, or their deployment environment.
---

# Python plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read `pyproject.toml`, lockfiles, supported Python versions, entry points,
  framework configuration, type-checker settings, and representative tests.
- Trace sync and async boundaries, database or network clients, background work,
  process models, and shutdown behavior.
- Identify packaging shape, import boundaries, optional dependencies, generated
  files, and environment-specific behavior.

## Establish the operating model

Establish the project target: Interpreter implementations and versions,
packaging and lock tooling, OS and architecture, worker model, async framework,
native dependencies, locale and encoding, and deployment form. The changed
boundary must define: Interpreter behavior, typing limits, packaging, import and
environment rules, async, threads and processes, GIL implications, object
lifetime, serialization, native extensions, signals, and deployment.

Define ownership, errors, cancellation, and concurrency for Interpreter
behavior, typing limits, packaging, import and environment rules, async, threads
and processes. Verify version, package, native, serialization, and artifact
compatibility for GIL implications, object lifetime, serialization, native
extensions, signals, deployment across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for mutable default arguments, late-bound closures, blocking
work inside an event loop, imports with environment-dependent side effects,
typing treated as runtime enforcement, process and thread assumptions hidden by
the GIL, unsafe object deserialization, shell interpolation, archive extraction,
and packaging that imports a different project copy.

- Require a defined ownership and shutdown path for sessions, files, processes,
  executors, tasks, and async clients.
- Test whether blocking work enters the event loop and whether async work is
  incorrectly treated as parallel CPU execution.
- Find retry loops without deadlines, idempotency, bounded backoff, or exception
  classification.
- Distinguish static type promises from runtime validation at untrusted
  boundaries. Flag broad `Any`, unchecked casts, and catch-all exceptions that
  erase invariants.
- Check package/version compatibility across local development, CI, build
  images, and production. Reject plans that assume an undeclared dependency is
  present.
- Check mutable defaults, import-time side effects, global client state, and
  fork/thread safety where the execution model makes them material.
- Reject `pickle`, `marshal`, `shelve`, unsafe YAML constructors, and equivalent
  object loading for untrusted data. A signature does not make an executable
  object graph appropriate; use a bounded data schema and explicit types.
- Keep untrusted input out of `eval`, `exec`, dynamic imports, format-driven
  templates, and shell command strings. Pass fixed executables and separated
  arguments, then validate option-like values and the invoked program's own
  argument semantics.
- Constrain filesystem and archive operations to intended roots while covering
  absolute paths, alternate separators, symlinks, temporary-file races, archive
  traversal, special files, and decompression limits.
- Bound request, parser, regular-expression, image, XML, decompression, and
  collection work before allocation or event-loop execution.
- Require tests for error paths, cancellation, cleanup, serialization edges,
  time behavior, and dependency failures - not only happy-path unit tests.

## Verify the claims

- Verify these behaviors through the declared Python compiler and runtime
  targets: Interpreter behavior, typing limits, packaging, import and
  environment rules, async, threads and processes. Use the real compiler or
  interpreter and supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: GIL implications, object lifetime,
  serialization, native extensions, signals, deployment. Exercise boundary
  values, encoding, cancellation, resource exhaustion, concurrency, dependency
  failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.
- Exercise malicious serialized objects, YAML tags, archive entries, symlink
  swaps, command options, expensive regular expressions, deep input, and parser
  limits where those boundaries exist.

## Ask when evidence is missing

- Which Python version and implementation, target platforms, dependency
  resolver, and packaging mode apply?
- How do async and sync work, cancellation, typing boundaries, serialization,
  resources, and process concurrency interact?

## Calibrate findings

- Treat unsafe deserialization, event-loop blocking, process-unsafe state, or
  incompatible package resolution as critical.
- Downgrade when runtime and inputs are bounded and type, async, packaging,
  resource, and version tests cover the path.

## Add to the verdict

State the supported Python/runtime assumptions, the concurrency model, the
resource lifecycle, and the exact checks that prove the package and deployment
remain compatible.
