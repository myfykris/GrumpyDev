---
name: data-warehousing
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review data-warehouse plans and other engineering artifacts for dimensional models, grain, slowly changing dimensions, ingestion, freshness, cost, governance, and reconciliation. Project applicability: the project builds analytical models or operates a columnar cloud data warehouse."
---

# Data warehousing GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `data-pipelines`
skill.

## Lean review

- Read source contracts, model grain, keys, dimensions and facts, incremental
  logic, partitions, quality tests, lineage, access controls, and cost reports.

- Trace a business metric from source records through late updates, backfills,
  model rebuilds, dashboards, and reconciliation.

Watch especially for fact-table grain left ambiguous, slowly changing dimensions
applied inconsistently, late-arriving facts assigned to the wrong version, joins
that double count, local time mixed across sources, backfills overwhelming
shared compute, and dashboards bypassing governed semantic definitions.

Lean mode is insufficient when this material severity condition may apply:

- Treat silently incorrect business metrics, unreconcilable history, or a
  destructive backfill without recovery as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Data warehousing evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State model grain, metric reconciliation, history and backfill behavior,
governance boundaries, freshness, and cost evidence.
