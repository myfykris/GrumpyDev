---
name: gd-dynamodb
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review DynamoDB engineering work for access patterns, keys, indexes, consistency, hot partitions, transactions, capacity, streams, and recovery."
---

# DynamoDB GrumpyDev review

## Quick checks

- Establish the regions, table class and capacity mode, global-table version,
  backup settings, and client behavior.

- Read access-pattern inventory, key design, item shapes, indexes, conditions,
  transactions, capacity mode, TTL, streams, and recovery settings.

Watch especially for hot partition keys, scans hidden behind convenience APIs,
secondary-index consistency assumed to be immediate, conditional writes omitted
from read-modify-write flows, item-size growth, transaction limits, TTL deletion
treated as timely, and retries repeating non-idempotent effects.

- Assess a hot partition on a critical path, lost-update behavior, or
  retry-amplified side effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the DynamoDB
specialist.

## Verdict context

State access-pattern coverage, key distribution, consistency and transaction
guarantees, capacity risk, and recovery proof.
