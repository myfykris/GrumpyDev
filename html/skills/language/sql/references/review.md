# SQL full-review guidance

## Operating conditions

Establish the project target: Database engines and versions, SQL modes,
isolation defaults, collation and encoding, migration tooling, connection layer,
read replicas, and compatibility requirements. The changed boundary must define:
Dialect differences, NULL and three-valued logic, types, collation, joins,
aggregates, transactions, isolation, constraints, locking, query plans,
pagination, injection, and schema evolution.

## Failure patterns

- Require deterministic semantics for ordering, ties, duplicate rows, nulls,
  time zones, collations, and numeric precision.
- Check join cardinality and aggregation grain against representative data
  rather than table names or sample rows.
- Reject string-built SQL and require parameter binding with a defined policy
  for dynamic identifiers.
- Analyze locking, isolation, retries, partial failure, and read-modify-write
  races for mutating statements.
- Use real execution plans and production-like distributions for performance
  claims; syntax validity is not capacity evidence.

## Verification to run or specify in the plan

- Execute queries on the target database versions with the declared SQL modes,
  collations, and isolation. Use NULLs, duplicate join keys, ordering ties,
  and boundary numeric or timestamp values to check exact results.
- Run competing transactions against the same invariant. Check lock waits,
  deadlocks, rollback, and retry behavior, including whether constraints
  prevent conflicting writes.
- Inspect execution plans with representative data and parameter
  distributions. Rehearse affected migrations with overlapping application
  versions and verify the data recovery path.
