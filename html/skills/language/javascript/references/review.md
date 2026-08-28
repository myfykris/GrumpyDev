# JavaScript standard review

## Establish the operating model

Establish the project target: Node, browser, edge, or embedded runtimes and
versions, module system, package manager, bundler, transpilation targets, worker
model, and supported client matrix. The changed boundary must define: ECMAScript
semantics, event loops, promises, cancellation, modules, package resolution,
runtime globals, serialization, prototype and injection hazards, workers,
memory, and build output.

Define ownership, errors, cancellation, and concurrency for ECMAScript
semantics, event loops, promises, cancellation, modules, package resolution.
Verify version, package, native, serialization, and artifact compatibility for
runtime globals, serialization, prototype and injection hazards, workers,
memory, build output across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

- Require runtime validation for network, storage, environment, and user data;
  JavaScript shape assumptions are not contracts.
- Find floating promises, unhandled rejections, stale closures, event-listener
  leaks, timer ownership, and missing cancellation.
- Verify ESM and CommonJS behavior, package exports, conditional resolution, and
  bundler output for every consumer environment.
- Check coercion, truthiness, number precision, date and time, Unicode,
  prototype, and property-enumeration assumptions where material.
- Reject untrusted keys such as prototype, constructor, and prototype-chain
  properties before recursive merge, clone, assignment, query parsing, or
  configuration overlay. Prefer own-property checks and data structures that do
  not inherit attacker-controlled object state.
- Keep untrusted strings out of `eval`, `Function`, string timers, executable
  templates, selectors, and command construction. Validate structured data at
  runtime and apply output controls for the exact HTML, URL, script, style,
  query, filesystem, or process sink.
- Bound input length, nesting, collection size, parsing, decompression, and
  regular-expression work before allocation or event-loop execution.
- Require tests against built artifacts and supported runtimes, not only source
  code under one test runner.

## Verify the claims

- Verify these behaviors through the declared JavaScript compiler and runtime
  targets: ECMAScript semantics, event loops, promises, cancellation, modules,
  package resolution. Use the real compiler or interpreter and supported release
  modes rather than a development substitute.
- Exercise failure and edge behavior for: runtime globals, serialization,
  prototype and injection hazards, workers, memory, build output. Exercise
  boundary values, encoding, cancellation, resource exhaustion, concurrency,
  dependency failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.
- Exercise prototype-polluting keys, hostile property names, deep and cyclic
  objects, expensive regular expressions, executable strings, oversized input,
  and dangerous output contexts where those paths exist.

## Ask when evidence is missing

- Which ECMAScript, Node.js or browser versions, module mode, package
  resolution, and runtime globals apply?
- How do promises, cancellation, event-loop work, coercion, serialization, and
  untrusted input cross the boundary?

## Calibrate findings

- Downgrade when inputs and runtime are bounded and async, module,
  compatibility, and failure tests cover the path.
