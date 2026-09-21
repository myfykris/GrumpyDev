---
name: gd-sql
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review SQL engineering work across relational databases for query semantics, null handling, cardinality, transactions, locking, portability, and data-correctness risks."
---

# SQL GrumpyDev review

## Quick checks

- Read schemas, constraints, indexes, representative data distributions,
  transaction boundaries, query plans, and the exact database dialect and
  version.

- Trace joins, filters, grouping, nulls, duplicates, ordering, pagination,
  isolation, parameter binding, and expected row counts.

Watch especially for NULL and three-valued logic, result order assumed without
ORDER BY, joins that multiply rows, window frames left implicit, type or
collation coercion changing comparisons, and transaction or DDL behavior assumed
portable across engines.

- Assess injection, broken concurrent invariants, destructive data loss, or
  unbounded critical query cost under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the SQL specialist.

## Verdict context

State the dialect and version, result-grain contract, transaction and isolation
assumptions, portability limits, and plan or data evidence.
