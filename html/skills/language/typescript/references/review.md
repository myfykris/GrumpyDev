# TypeScript standard review

## Inspect additional evidence

- Trace external data from network, storage, environment, and JavaScript callers
  to its runtime validation boundary.

## Establish the operating model

Establish the project target: TypeScript version, runtime targets, module system
and resolution, strictness flags, emit owner, bundler, package manager,
declaration consumers, and generated-code sources. The changed boundary must
define: Erased types, compiler options, narrowing, structural typing,
declaration accuracy, module resolution, emit modes, runtime validation,
decorators, generated types, build graph, and JS interoperability.

Define ownership, errors, cancellation, and concurrency for Erased types,
compiler options, narrowing, structural typing, declaration accuracy, module
resolution. Verify version, package, native, serialization, and artifact
compatibility for emit modes, runtime validation, decorators, generated types,
build graph, JS interoperability across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

- Reject any assumption that a TypeScript type validates runtime data. Require
  parsing or guards at trust boundaries and defined failure behavior.
- Find `any`, unchecked `as`, non-null assertions, declaration merging, and
  suppressed compiler errors that cross the proposed change.
- Check whether module resolution, conditional exports, path aliases, and
  generated declarations work in every declared consumer environment.
- Distinguish source compatibility from emitted JavaScript compatibility and
  build-time success from runtime availability.
- Inspect promise ownership, cancellation, timeouts, unhandled rejection paths,
  concurrent mutation, and retry/idempotency behavior.
- Require an explicit compatibility plan for API or shared-type evolution;
  independently deployed consumers may not upgrade atomically.
- Demand tests that execute emitted/runtime behavior, not only compile-time type
  assertions.

## Verify the claims

- Verify these behaviors through the declared TypeScript compiler and runtime
  targets: Erased types, compiler options, narrowing, structural typing,
  declaration accuracy, module resolution. Use the real compiler or interpreter
  and supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: emit modes, runtime validation,
  decorators, generated types, build graph, JS interoperability. Exercise
  boundary values, encoding, cancellation, resource exhaustion, concurrency,
  dependency failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which TypeScript version, tsconfig strictness, module mode, runtime, and
  generated-type sources apply?
- Where do untyped inputs, assertions, narrowing, serialization, async work, and
  JavaScript consumers cross the boundary?

## Calibrate findings

- Downgrade when inputs are internal and proven or runtime validation, strict
  settings, and compatibility tests cover the boundary.
