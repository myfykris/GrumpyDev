---
name: mongodb
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review MongoDB engineering work for document boundaries, schema validation, indexes, consistency, transactions, sharding, replication, and recovery."
---

# MongoDB GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed application specialist for the data-access boundary.

## Lean review

- Read document models, validators, indexes, query and aggregation plans, read
  and write concerns, sessions, shard keys, replicas, and backups.

- Trace document growth, concurrent updates, failover, retries, migrations, and
  mixed-schema reads across application versions.

Watch especially for schema-less treated as schema-free, unbounded document or
array growth, multi-document transactions used to recreate relational behavior,
multikey index surprises, read and write concerns weaker than business needs,
poor shard keys, and retryable writes repeating external effects.

Lean mode is insufficient when this material severity condition may apply:

- Treat acknowledged data loss, unsafe concurrent updates, or an unrecoverable
  schema migration as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete MongoDB evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State document and schema boundaries, index evidence, consistency choices,
distribution risks, and restore proof.
