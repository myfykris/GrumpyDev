---
name: gd-redis
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Redis engineering work for data structures, eviction, persistence, atomicity, clustering, hot keys, cache consistency, and recovery."
---

# Redis GrumpyDev review

## Quick checks

- Establish the exact Redis-compatible product, version, deployment mode,
  persistence mode, and failover implementation.

- Read key design, value sizes, TTLs, commands, scripts, transactions, memory
  policy, persistence, topology, failover, and load tests.

Watch especially for a cache silently becoming authoritative, hot or oversized
keys, eviction removing required state, multi-key operations crossing cluster
slots, distributed locks without fencing, failover losing acknowledged writes,
scripts blocking the server, and cache fills stampeding dependencies.

- Assess loss of non-reconstructible state, unsafe distributed coordination, or
  unbounded hot-key impact under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Redis specialist.

## Verdict context

State Redis's authority, memory bounds, atomicity scope, cache-consistency
behavior, topology, and recovery evidence.
