---
name: sql
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review SQL plans and other engineering artifacts across relational databases for query semantics, null handling, cardinality, transactions, locking, portability, and data-correctness risks. Project applicability: the project contains or executes SQL queries, reports, stored routines, views, or database access logic independent of one storage engine."
---

# SQL GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read schemas, constraints, indexes, representative data distributions,
  transaction boundaries, query plans, and the exact database dialect and
  version.

- Trace joins, filters, grouping, nulls, duplicates, ordering, pagination,
  isolation, parameter binding, and expected row counts.

Watch especially for NULL and three-valued logic, result order assumed without
ORDER BY, joins that multiply rows, window frames left implicit, type or
collation coercion changing comparisons, and transaction or DDL behavior assumed
portable across engines.

Lean mode is insufficient when this material severity condition may apply:

- Treat injection, broken concurrent invariants, destructive data loss, or
  unbounded critical query cost as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete SQL evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the dialect and version, result-grain contract, transaction and isolation
assumptions, portability limits, and plan or data evidence.
