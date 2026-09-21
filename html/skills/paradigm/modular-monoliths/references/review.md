# Modular monolith full-review guidance

## Operating conditions

Establish the project target: Module map and owners, allowed dependencies, data
ownership, transaction model, enforcement tooling, deployment unit, and
extraction intentions. The changed boundary must define: Module boundaries,
dependency direction, encapsulation, transactions, shared database rules,
internal contracts, extraction seams, build enforcement, and deployment.

## Failure patterns

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

## Verification to run or specify in the plan

- Introduce a forbidden import or table access in an isolated check and
  confirm the project's boundary enforcement detects it. Verify allowed module
  calls use the owning module's contract.
- Fail a cross-module operation partway through and check the declared
  transaction and recovery behavior. Verify shared helpers do not allow
  callers to bypass module-owned invariants.
