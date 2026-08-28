---
name: postgresql
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review PostgreSQL plans and other engineering artifacts for schema migration, locking, transaction, indexing, query, concurrency, backup, replication, and data-integrity risks. Project applicability: the project stores or queries data in PostgreSQL or depends on PostgreSQL topology or operations."
---

# PostgreSQL GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Coordinate findings with the active SQL specialist. Treat material PostgreSQL
behavior as server-version and topology specific.

## Lean review

- Inspect the actual schema, constraints, indexes, policies, extensions,
  migrations, transaction boundaries, and representative scale. An ORM model is
  not evidence of current database state.
- Establish server versions, topology, pool mode, connection limits,
  replication, failover authority, backup, restore, write load, and old/new
  application overlap.
- Challenge long transactions, misunderstood lock levels, unbounded backfills,
  invalid failed concurrent indexes, replica lag, NULL and collation behavior,
  serializable transactions without retries, and rollback that cannot restore
  transformed data.
- Require explicit lock and statement timeout decisions, bounded restartable
  migration work, mixed-version compatibility, post-migration invariant
  validation, and a recovery path for data as well as code.
- Treat query performance claims without representative plans, statistics, and
  data shape as unproven.

Lean mode is insufficient for DDL on material tables, data transformation,
replication or failover changes, isolation or locking changes, row-level
security, extension changes, or recovery design.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/schema-migrations-and-locking.md):
  Read when the reviewed work directly or indirectly changes DDL, constraints, indexes,
  defaults, generated values,
  types, partitions, extensions, table or index rewrites, lock acquisition, validation
  scans, timeouts, WAL volume, schema migration, backfills, coexistence, expand and
  contract sequencing, or irreversible data conversion.
- [Focused rules](references/transactions-and-concurrency.md):
  Read when the reviewed work directly or indirectly changes transaction boundaries,
  isolation, read-modify-write
  invariants, constraints, row or advisory locks, leases, leader election, deadlock or
  serialization retries, multiple writers, outboxes, or non-transactional side effects.
- [Focused rules](references/queries-and-indexes.md):
  Read when the reviewed work directly or indirectly changes SQL queries, predicates,
  joins, ordering, pagination,
  indexes, selectivity, statistics, parameter-sensitive plans, collation, N+1 behavior,
  write amplification, or performance and capacity claims.
- [Focused rules](references/operations-replication-and-recovery.md):
  Read when the reviewed work directly or indirectly changes connection pools, pool
  modes, maintenance, vacuum, bloat,
  WAL, roles, row-level security, replicas, lag, read routing, failover, backup,
  retention, point-in-time recovery, restore, recovery objectives, or operator
  ownership.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the affected version, topology, scale, lock or transaction boundary,
mixed-version window, and data recovery limit behind material conclusions.
