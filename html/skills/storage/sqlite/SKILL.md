---
name: sqlite
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review SQLite plans and other engineering artifacts for file ownership, locking, transaction mode, durability, migrations, type affinity, concurrency, and backup. Project applicability: an application embeds SQLite or shares a SQLite database file."
---

# SQLite GrumpyDev review

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

- Establish the exact SQLite library version, build options, wrapper or driver
  version, filesystem, and process model.

- Read connection setup, pragmas, schema and migrations, transaction boundaries,
  deployment filesystem, backup method, and concurrency tests.

Watch especially for the single-writer boundary, busy handling omitted from
transactions, WAL side files excluded from backup or packaging, foreign keys not
enabled on every connection, type affinity mistaken for strict typing,
table-rebuild migrations losing metadata, and databases placed on unsafe network
filesystems.

Lean mode is insufficient when this material severity condition may apply:

- Treat shared-file corruption, unhandled write contention on a critical path,
  or unrecoverable migration loss as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete SQLite evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State file ownership, pragma choices, write-concurrency limit, migration and
backup behavior, and crash-recovery evidence.
