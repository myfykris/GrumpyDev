# TypeScript full-review guidance

## Operating conditions

Establish the project target: TypeScript version, runtime targets, module system
and resolution, strictness flags, emit owner, bundler, package manager,
declaration consumers, and generated-code sources. The changed boundary must
define: Erased types, compiler options, narrowing, structural typing,
declaration accuracy, module resolution, emit modes, runtime validation,
decorators, generated types, build graph, and JS interoperability.

## Failure patterns

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

## Verification to run or specify in the plan

- Type-check using the actual project configuration, then execute the emitted
  JavaScript. Send malformed runtime data through typed boundaries to verify
  validation does not depend on erased types or assertions.
- Compile and run a consumer of changed package exports and declarations using
  the supported module resolution and runtime targets. Check path aliases,
  generated types, and independently versioned consumers.
