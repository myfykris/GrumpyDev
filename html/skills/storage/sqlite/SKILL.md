---
name: sqlite
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review SQLite engineering work for file ownership, locking, transaction mode, durability, migrations, type affinity, concurrency, and backup."
---

# SQLite GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
