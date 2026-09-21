---
name: gd-sql-server
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review SQL Server engineering work for schema changes, indexes, statistics, transactions, locking, availability, security, and restore."
---

# SQL Server GrumpyDev review

## Quick checks

- Establish the exact SQL Server or Azure SQL product, version, edition,
  compatibility level, hosting mode, and feature set.

- Read compatibility level, DDL, migrations, indexes, query plans, statistics,
  isolation settings, jobs, availability topology, and restore tests.

Watch especially for plan-cache and parameter-sensitivity regressions, implicit
conversions disabling useful indexes, lock escalation, snapshot isolation
pressure on tempdb, identity values assumed contiguous, online operations
unavailable in the deployed edition, and availability replicas serving data
beyond acceptable lag.

- Assess data loss, prolonged blocking, broken invariants, or use of unsupported
  variant behavior under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the SQL Server
specialist.

## Verdict context

State compatibility and encoding choices, plan evidence, locking and isolation
behavior, availability assumptions, and restore proof.
