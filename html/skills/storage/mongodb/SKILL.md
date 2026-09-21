---
name: gd-mongodb
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review MongoDB engineering work for document boundaries, schema validation, indexes, consistency, transactions, sharding, replication, and recovery."
---

# MongoDB GrumpyDev review

## Quick checks

- Read document models, validators, indexes, query and aggregation plans, read
  and write concerns, sessions, shard keys, replicas, and backups.

- Trace document growth, concurrent updates, failover, retries, migrations, and
  mixed-schema reads across application versions.

Watch especially for schema-less treated as schema-free, unbounded document or
array growth, multi-document transactions used to recreate relational behavior,
multikey index surprises, read and write concerns weaker than business needs,
poor shard keys, and retryable writes repeating external effects.

- Assess acknowledged data loss, unsafe concurrent updates, or an unrecoverable
  schema migration under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the MongoDB specialist.

## Verdict context

State document and schema boundaries, index evidence, consistency choices,
distribution risks, and restore proof.
