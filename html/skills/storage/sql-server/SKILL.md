---
name: sql-server
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review SQL Server engineering work for schema changes, indexes, statistics, transactions, locking, availability, security, and restore."
---

# SQL Server GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `sql` skill.

## Lean review

- Establish the exact SQL Server or Azure SQL product, version, edition,
  compatibility level, hosting mode, and feature set.

- Read compatibility level, DDL, migrations, indexes, query plans, statistics,
  isolation settings, jobs, availability topology, and restore tests.

Watch especially for plan-cache and parameter-sensitivity regressions, implicit
conversions disabling useful indexes, lock escalation, snapshot isolation
pressure on tempdb, identity values assumed contiguous, online operations
unavailable in the deployed edition, and availability replicas serving data
beyond acceptable lag.

Lean mode is insufficient when this material severity condition may apply:

- Treat data loss, prolonged blocking, broken invariants, or use of unsupported
  variant behavior as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete SQL Server evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State compatibility and encoding choices, plan evidence, locking and isolation
behavior, availability assumptions, and restore proof.
