---
name: modular-monoliths
description: Review modular-monolith plans for enforceable boundaries, dependency direction, data ownership, transaction scope, deployment coupling, and extraction seams. Use when one deployable system contains intentionally isolated business modules.
---

# Modular monolith plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed language, framework, and storage specialists for the module
boundaries.

## Inspect evidence

- Read module APIs, dependency rules, build layout, database ownership,
  transaction boundaries, background work, and architecture tests.
- Trace calls and data access that cross modules, including shortcuts through
  shared helpers, tables, and internal types.

## Establish the operating model

Establish the project target: Module map and owners, allowed dependencies, data
ownership, transaction model, enforcement tooling, deployment unit, and
extraction intentions. The changed boundary must define: Module boundaries,
dependency direction, encapsulation, transactions, shared database rules,
internal contracts, extraction seams, build enforcement, and deployment.

Name the invariants, authorities, owners, and enforcement for Module boundaries,
dependency direction, encapsulation, transactions, shared database rules. Prove
internal contracts, extraction seams, build enforcement, deployment under
concurrency, partial failure, incompatible versions, operational response,
rollback, and repair, and justify the added complexity.

## Challenge the plan

### Recurring traps

Watch especially for package names without enforceable boundaries, cyclic
dependencies, shared mutable tables with no owning module, framework-wide
dependency injection bypassing module APIs, global events with unclear delivery
rules, and speculative extraction driving needless indirection.

- Require boundaries that tools or tests can enforce; folder names and developer
  discipline are not architecture.
- Keep shared code small and technical; reject a common module that becomes an
  unowned dependency dump.
- Define table and schema ownership even when modules share one database and one
  transaction manager.
- Allow direct in-process calls when contracts remain explicit; do not recreate
  network protocols inside one process.
- Identify extraction seams without paying distributed-system costs before
  extraction is justified.

## Verify the claims

- Verify these behaviors through the claimed architecture and its enforcement
  boundaries: Module boundaries, dependency direction, encapsulation,
  transactions, shared database rules. Use dependency, architecture, contract,
  schema, or ownership tests that fail when a claimed boundary is violated.
- Exercise failure and edge behavior for: internal contracts, extraction seams,
  build enforcement, deployment. Exercise the material invariant under
  concurrency, delay, duplication, partial failure, incompatible versions,
  rollback, and repair.
- Verify that operators can observe, diagnose, and recover the design without
  bypassing its ownership rules.

## Ask when evidence is missing

- Which module owns each invariant and data set, and what mechanism enforces
  dependency direction?
- How do transactions, background work, migrations, tests, and future extraction
  cross module boundaries?

## Calibrate findings

- Treat cyclic ownership or unenforced writes that allow modules to violate core
  invariants as critical.
- Downgrade when boundaries are advisory by choice or dependency checks,
  ownership, and integration evidence enforce them.

## Add to the verdict

State module boundaries, enforcement mechanism, data ownership, allowed
coupling, transaction scope, and realistic extraction seams.
