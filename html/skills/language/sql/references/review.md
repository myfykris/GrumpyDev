# SQL standard review

## Establish the operating model

Establish the project target: Database engines and versions, SQL modes,
isolation defaults, collation and encoding, migration tooling, connection layer,
read replicas, and compatibility requirements. The changed boundary must define:
Dialect differences, NULL and three-valued logic, types, collation, joins,
aggregates, transactions, isolation, constraints, locking, query plans,
pagination, injection, and schema evolution.

Define ownership, errors, cancellation, and concurrency for Dialect differences,
NULL and three-valued logic, types, collation, joins, aggregates, transactions.
Verify version, package, native, serialization, and artifact compatibility for
isolation, constraints, locking, query plans, pagination, injection, schema
evolution across every declared target and rollback path.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared SQL compiler and runtime targets:
  Dialect differences, NULL and three-valued logic, types, collation, joins,
  aggregates, transactions. Use the real compiler or interpreter and supported
  release modes rather than a development substitute.
- Exercise failure and edge behavior for: isolation, constraints, locking, query
  plans, pagination, injection, schema evolution. Exercise boundary values,
  encoding, cancellation, resource exhaustion, concurrency, dependency failure,
  and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which SQL dialect, database version, schema, collation, isolation level, and
  migration state apply?
- What cardinality, locking, null, transaction, parameterization, pagination,
  and query-plan behavior applies?

## Calibrate findings

- Downgrade when the query is bounded and parameterization, constraints, plans,
  transactions, and representative data prove it.
