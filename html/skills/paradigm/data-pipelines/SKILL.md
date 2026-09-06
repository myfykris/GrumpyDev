---
name: data-pipelines
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review data-pipeline engineering work for source contracts, replay, idempotency, late data, schema drift, data quality, lineage, and recovery."
---

# Data pipelines GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
