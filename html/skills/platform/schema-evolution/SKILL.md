---
name: gd-schema-evolution
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review schema-evolution engineering work for compatibility, sequencing, backfills, mixed versions, defaults, validation, rollback, and data repair."
---

# Schema evolution GrumpyDev review

## Quick checks

- Read old and new schemas, serializers, validators, migrations, consumers,
  deployment order, backfills, compatibility tests, and repair tooling.

- Trace old data through new code and new data through old code during deploy,
  rollback, replay, replication, and delayed processing.

Watch especially for destructive changes combined into one deployment, backfills
holding locks or exhausting capacity, old and new code unable to coexist,
defaults rewriting large tables, renames implemented as delete-and-add, rollback
requiring discarded data, and schema validation that ignores stored history.

- Assess unreadable retained data, incompatible mixed versions, or irreversible
  transformation without recovery under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Schema evolution
specialist.

## Verdict context

State compatibility mode, deployment sequence, mixed-version behavior, backfill
controls, encoding contract, and repair evidence.
