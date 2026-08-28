---
name: data-pipelines
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review data-pipeline plans and other engineering artifacts for source contracts, replay, idempotency, late data, schema drift, data quality, lineage, and recovery. Project applicability: the project ingests, transforms, moves, or aggregates data in batches or streams."
---

# Data pipelines GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed storage and platform specialists for the pipeline boundaries in use.

## Lean review

- Read source and sink contracts, checkpoints, watermark rules, schemas,
  transformation code, orchestration, and quality checks.

- Trace one record from ingestion through validation, enrichment, deduplication,
  publication, replay, and deletion.

Watch especially for duplicate effects under at-least-once delivery, late data
outside watermark assumptions, schema drift, poison records blocking progress,
partial reruns that double count, backfills competing with live work, and local
event time confused with processing time.

Lean mode is insufficient when this material severity condition may apply:

- Treat silent data loss, unreconcilable output, or a replay that changes
  committed meaning as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Data pipelines evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State delivery semantics, replay boundary, data-quality gates, schema policy,
lineage, and recovery evidence.
