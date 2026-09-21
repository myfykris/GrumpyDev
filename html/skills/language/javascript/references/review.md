# JavaScript full-review guidance

## Operating conditions

Establish the project target: Node, browser, edge, or embedded runtimes and
versions, module system, package manager, bundler, transpilation targets, worker
model, and supported client matrix. The changed boundary must define: ECMAScript
semantics, event loops, promises, cancellation, modules, package resolution,
runtime globals, serialization, prototype and injection hazards, workers,
memory, and build output.

## Failure patterns

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

## Verification to run or specify in the plan

- Load the built packages through the actual ESM or CommonJS entrypoints in
  each supported runtime. Check conditional exports, runtime globals, and
  emitted syntax outside the test runner's module loader.
- Resolve asynchronous requests out of order, reject them, and cancel their
  owners. Verify stale callbacks cannot overwrite newer state and that
  listeners, timers, workers, and rejected promises are handled.

- Exercise prototype-polluting keys, hostile property names, deep and cyclic
  objects, expensive regular expressions, executable strings, oversized input,
  and dangerous output contexts where those paths exist.
