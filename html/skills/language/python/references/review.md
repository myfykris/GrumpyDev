# Python standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

- Distinguish static type promises from runtime validation at untrusted
  boundaries. Flag broad `Any`, unchecked casts, and catch-all exceptions that
  erase invariants.
## Verify the claims

- Verify these behaviors through the declared Python compiler and runtime
  targets: Interpreter behavior, typing limits, packaging, import and
  environment rules, async, threads and processes. Use the real compiler or
  interpreter and supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: GIL implications, object lifetime,
  serialization, native extensions, signals, deployment. Exercise boundary
  values, encoding, cancellation, resource exhaustion, concurrency, dependency
  failure, and termination where they can change behavior.
- Exercise malicious serialized objects, YAML tags, archive entries, symlink
  swaps, command options, expensive regular expressions, deep input, and parser
  limits where those boundaries exist.

## Ask when evidence is missing

- How do async and sync work, cancellation, typing boundaries, serialization,
  resources, and process concurrency interact?

## Calibrate findings

- Downgrade when runtime and inputs are bounded and type, async, packaging,
  resource, and version tests cover the path.
