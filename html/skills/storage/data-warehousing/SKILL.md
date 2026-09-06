---
name: data-warehousing
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review data-warehouse engineering work for dimensional models, grain, slowly changing dimensions, ingestion, freshness, cost, governance, and reconciliation."
---

# Data warehousing GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
