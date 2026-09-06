---
name: sql
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review SQL engineering work across relational databases for query semantics, null handling, cardinality, transactions, locking, portability, and data-correctness risks."
---

# SQL GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
