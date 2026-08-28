---
name: mysql
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review MySQL plans and other engineering artifacts for schema design, migrations, indexes, transactions, isolation, replication, locking, and recovery. Project applicability: the project stores or queries data in MySQL or a compatible relational database."
---

# MySQL GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `sql` skill.

## Lean review

- Read engine and version settings, DDL, migrations, constraints, indexes, query
  plans, transactions, replicas, backups, and restore tests.

- Trace critical writes and reads through isolation, locks, failover, lag,
  retry, and mixed-version deployment.

Watch especially for implicit numeric and string coercion, collation changing
equality, gap locks and isolation surprises, online DDL that still copies or
blocks, replica lag used for fresh reads, permissive SQL modes hiding bad data,
and auto-increment behavior assumed contiguous.

Lean mode is insufficient when this material severity condition may apply:

- Treat data loss, prolonged production locking, broken invariants, or
  unverified product compatibility as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete MySQL evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State engine and encoding choices, migration risk, query-plan evidence,
transaction behavior, replication assumptions, and restore proof.
