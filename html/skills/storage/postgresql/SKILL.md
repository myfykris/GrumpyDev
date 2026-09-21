---
name: gd-postgresql
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review PostgreSQL engineering work for schema migration, locking, transaction, indexing, query, concurrency, backup, replication, and data-integrity risks."
---

# PostgreSQL GrumpyDev review

## Review focus

Treat material PostgreSQL behavior as server-version and topology specific.

## Quick checks

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

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the PostgreSQL
specialist.

- [Focused rules](references/schema-migrations-and-locking.md):
  Read when the work changes DDL, constraints, indexes,
  defaults, generated values,
  types, partitions, extensions, table or index rewrites, lock acquisition, validation
  scans, timeouts, WAL volume, schema migration, backfills, coexistence, expand and
  contract sequencing, or irreversible data conversion.
- [Focused rules](references/transactions-and-concurrency.md):
  Read when the work changes transaction boundaries,
  isolation, read-modify-write
  invariants, constraints, row or advisory locks, leases, leader election, deadlock or
  serialization retries, multiple writers, outboxes, or non-transactional side effects.
- [Focused rules](references/queries-and-indexes.md):
  Read when the work changes SQL queries, predicates,
  joins, ordering, pagination,
  indexes, selectivity, statistics, parameter-sensitive plans, collation, N+1 behavior,
  write amplification, or performance and capacity claims.
- [Focused rules](references/operations-replication-and-recovery.md):
  Read when the work changes connection pools, pool
  modes, maintenance, vacuum, bloat,
  WAL, roles, row-level security, replicas, lag, read routing, failover, backup,
  retention, point-in-time recovery, restore, recovery objectives, or operator
  ownership.

## Verdict context

State the affected version, topology, scale, lock or transaction boundary,
mixed-version window, and data recovery limit behind material conclusions.
