---
name: gd-sqlite
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review SQLite engineering work for file ownership, locking, transaction mode, durability, migrations, type affinity, concurrency, and backup."
---

# SQLite GrumpyDev review

## Quick checks

- Establish the exact SQLite library version, build options, wrapper or driver
  version, filesystem, and process model.

- Read connection setup, pragmas, schema and migrations, transaction boundaries,
  deployment filesystem, backup method, and concurrency tests.

Watch especially for the single-writer boundary, busy handling omitted from
transactions, WAL side files excluded from backup or packaging, foreign keys not
enabled on every connection, type affinity mistaken for strict typing,
table-rebuild migrations losing metadata, and databases placed on unsafe network
filesystems.

- Assess shared-file corruption, unhandled write contention on a critical path,
  or unrecoverable migration loss under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the SQLite specialist.

## Verdict context

State file ownership, pragma choices, write-concurrency limit, migration and
backup behavior, and crash-recovery evidence.
