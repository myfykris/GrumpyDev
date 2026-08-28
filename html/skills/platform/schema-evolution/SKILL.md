---
name: schema-evolution
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review schema-evolution plans and other engineering artifacts for compatibility, sequencing, backfills, mixed versions, defaults, validation, rollback, and data repair. Project applicability: the project has persistent, message, API, file, or configuration schemas that can evolve."
---

# Schema evolution GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed storage, API-contract, or `event-driven-architecture` skill.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read old and new schemas, serializers, validators, migrations, consumers,
  deployment order, backfills, compatibility tests, and repair tooling.

- Trace old data through new code and new data through old code during deploy,
  rollback, replay, replication, and delayed processing.

Watch especially for destructive changes combined into one deployment, backfills
holding locks or exhausting capacity, old and new code unable to coexist,
defaults rewriting large tables, renames implemented as delete-and-add, rollback
requiring discarded data, and schema validation that ignores stored history.

Lean mode is insufficient when this material severity condition may apply:

- Treat unreadable retained data, incompatible mixed versions, or irreversible
  transformation without recovery as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Schema evolution evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State compatibility mode, deployment sequence, mixed-version behavior, backfill
controls, encoding contract, and repair evidence.
