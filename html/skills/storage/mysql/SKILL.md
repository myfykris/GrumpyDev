---
name: gd-mysql
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review MySQL engineering work for schema design, migrations, indexes, transactions, isolation, replication, locking, and recovery."
---

# MySQL GrumpyDev review

## Quick checks

- Read engine and version settings, DDL, migrations, constraints, indexes, query
  plans, transactions, replicas, backups, and restore tests.

- Trace critical writes and reads through isolation, locks, failover, lag,
  retry, and mixed-version deployment.

Watch especially for implicit numeric and string coercion, collation changing
equality, gap locks and isolation surprises, online DDL that still copies or
blocks, replica lag used for fresh reads, permissive SQL modes hiding bad data,
and auto-increment behavior assumed contiguous.

- Assess data loss, prolonged production locking, broken invariants, or
  unverified product compatibility under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the MySQL specialist.

## Verdict context

State engine and encoding choices, migration risk, query-plan evidence,
transaction behavior, replication assumptions, and restore proof.
