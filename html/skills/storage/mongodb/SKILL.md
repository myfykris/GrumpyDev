---
name: mongodb
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review MongoDB plans and other engineering artifacts for document boundaries, schema validation, indexes, consistency, transactions, sharding, replication, and recovery. Project applicability: the project stores or queries application data in MongoDB."
---

# MongoDB GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
