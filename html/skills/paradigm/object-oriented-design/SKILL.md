---
name: object-oriented-design
description: Review object-oriented design plans for ownership, invariants, mutability, inheritance, polymorphism, dependency direction, and test seams. Use when objects and collaborating types are the primary structure of a design.
---

# Object-oriented design plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language or framework specialist for the object model in use.

## Inspect evidence

- Read object responsibilities, constructors, state transitions, public methods,
  inheritance trees, interfaces, dependencies, and tests.
- Trace who owns mutable state, who may change it, and how invariants survive
  callbacks, exceptions, persistence, and concurrency.

## Establish the operating model

Establish the project target: Domain object conventions, framework lifecycle
constraints, mutability policy, dependency injection approach, persistence
mapping, and accepted inheritance or composition rules. The changed boundary
must define: Identity, state and invariants, composition, inheritance,
substitutability, encapsulation, mutation, lifecycle, dependency direction, and
test seams.

Name the invariants, authorities, owners, and enforcement for Identity, state
and invariants, composition, inheritance, substitutability. Prove encapsulation,
mutation, lifecycle, dependency direction, test seams under concurrency, partial
failure, incompatible versions, operational response, rollback, and repair, and
justify the added complexity.

## Challenge the plan

### Recurring traps

Watch especially for inheritance used only for reuse, god objects, mutable
aliases crossing ownership boundaries, subtype behavior that violates caller
expectations, temporal coupling hidden behind setters, domain behavior displaced
into services, and accessors that trigger surprising I/O.

- Reject classes that only rename records, functions, or database tables without
  owning behavior or invariants.
- Prefer composition unless substitution is real, tested, and stable across
  every subtype.
- Keep invalid state unrepresentable where practical and prevent partially
  initialized objects from escaping.
- Check whether dependency injection clarifies replaceable boundaries or merely
  adds interfaces and factories everywhere.
- Expose temporal coupling, feature envy, god objects, hidden mutation, and
  mocks that test implementation instead of behavior.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Identity, state and invariants, composition, inheritance,
  substitutability. Use dependency, architecture, contract, schema, or ownership
  tests that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: encapsulation, mutation, lifecycle,
  dependency direction, test seams. Exercise the material invariant under
  concurrency, delay, duplication, partial failure, incompatible versions,
  rollback, and repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Which object owns each invariant, mutable resource, and lifecycle transition?
- Which substitution, identity, concurrency, persistence, or failure assumptions
  must callers respect?

## Calibrate findings

- Treat split ownership or polymorphism that can violate a core invariant or
  resource lifecycle as critical.
- Downgrade when the abstraction is local and stable or contracts, ownership,
  and behavior tests prove substitutability.

## Add to the verdict

State object ownership, protected invariants, mutation boundaries, polymorphism
justification, dependency direction, and test evidence.
