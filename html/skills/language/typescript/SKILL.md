---
name: typescript
description: Review TypeScript engineering plans for runtime validation, type-safety gaps, module boundaries, build configuration, dependency, and asynchronous failure risks. Use when a plan changes TypeScript services, libraries, tools, or browser applications.
---

# TypeScript plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read `package.json`, the lockfile, `tsconfig` variants, bundler/runtime
  config, package exports, lint rules, and representative tests.
- Identify actual execution targets: browser, Node, edge runtime, worker, test
  runner, CommonJS, ESM, or multiple outputs.
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

## Challenge the plan

### Recurring traps

Watch especially for erased types treated as runtime validation, any or
assertions silencing uncertainty, structural compatibility accepting
semantically wrong objects, excess-property checks applied inconsistently,
module-resolution differences, and promises whose rejection path is missing.

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

- Treat trusted static types at an unvalidated runtime boundary or unsafe
  assertion on security-critical input as critical.
- Downgrade when inputs are internal and proven or runtime validation, strict
  settings, and compatibility tests cover the boundary.

## Add to the verdict

State the runtime targets, validation boundaries, compiler guarantees actually
enabled, compatibility assumptions, and evidence that built artifacts work for
their real consumers.
