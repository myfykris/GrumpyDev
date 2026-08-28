# Functional programming standard review

## Establish the operating model

Establish the project target: Language and effect libraries, purity boundaries,
runtime evaluation model, error conventions, state and I/O adapters, and team
constraints that affect the design. The changed boundary must define: Effects,
purity boundaries, immutability, algebraic data, error modeling, recursion,
laziness, resource safety, concurrency, and interoperability.

Name the invariants, authorities, owners, and enforcement for Effects, purity
boundaries, immutability, algebraic data, error modeling. Prove recursion,
laziness, resource safety, concurrency, interoperability under concurrency,
partial failure, incompatible versions, operational response, rollback, and
repair, and justify the added complexity.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Effects, purity boundaries, immutability, algebraic data, error
  modeling. Use dependency, architecture, contract, schema, or ownership tests
  that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: recursion, laziness, resource safety,
  concurrency, interoperability. Exercise the material invariant under
  concurrency, delay, duplication, partial failure, incompatible versions,
  rollback, and repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Where do effects, mutable state, failure, cancellation, and resource lifetime
  enter the proposed functional boundary?
- Which evaluation, recursion, allocation, or parallelism assumptions affect
  correctness or scale?

## Calibrate findings

- Downgrade when effects are isolated and types, laws, property tests, and
  measured resource behavior support the design.
