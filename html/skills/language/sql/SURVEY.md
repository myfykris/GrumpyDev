# SQL survey contribution

## Applies when

Apply this contribution when the project contains or executes SQL queries, reports,
stored routines, views, or database access logic independent of one storage engine.

## Inspect

- Read schemas, constraints, indexes, representative data distributions,
  transaction boundaries, query plans, and the exact database dialect and
  version.

## Ask when unresolved

- Which SQL dialect, database version, schema, collation, isolation level, and
  migration state apply?

- What cardinality, locking, null, transaction, parameterization, pagination,
  and query-plan behavior applies?

## Record

Map durable SQL version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
