# Functional programming full-review guidance

## Operating conditions

Establish the project target: Language and effect libraries, purity boundaries,
runtime evaluation model, error conventions, state and I/O adapters, and team
constraints that affect the design. The changed boundary must define: Effects,
purity boundaries, immutability, algebraic data, error modeling, recursion,
laziness, resource safety, concurrency, and interoperability.

## Failure patterns

- Require effect types and abstractions to make behavior clearer; reject
  category-theory decoration that hides ordinary control flow.
- Check whether claimed immutability survives shared references, foreign
  libraries, caches, and runtime escape hatches.
- Model expected failure in types without swallowing diagnostics or forcing
  every layer into one oversized error union.
- Verify recursion, lazy evaluation, persistent structures, and allocation
  patterns under production-sized workloads.
- Keep interop and resource lifetime explicit at boundaries where the type
  system cannot enforce the promise.

## Verification to run or specify in the plan

- Exercise claimed pure functions with aliased mutable inputs and
  foreign-library values. Check whether evaluation changes shared state or
  triggers I/O unexpectedly, including repeated evaluation of lazy values.
- Cancel or fail effectful work inside resource scopes and verify release. Use
  large or deeply nested inputs to measure recursion depth, retained lazy
  data, allocation, and bounded parallel execution.
