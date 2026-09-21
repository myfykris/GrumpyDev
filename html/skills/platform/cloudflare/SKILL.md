---
name: gd-cloudflare
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Cloudflare engineering work for Workers runtime limits, isolate lifecycle, bindings, KV consistency, Durable Objects, D1, queues, caching, networking, and deployment."
---

# Cloudflare developer platform GrumpyDev review

## Quick checks

- Read compatibility date and flags, Workers runtime, bindings, routes, regions, limits,
  deployment configuration, and account settings.

- Classify state across request memory, Cache API, KV, Durable Objects, D1, R2, queues,
  external stores, and browser caches.

Watch especially for mutable global state treated as durable, KV used for
coordination despite eventual consistency, Durable Object in-memory values lost
after hibernation, queue or alarm delivery assumed exactly once, and local
emulation treated as proof of production limits.

- Assess cross-tenant cache leakage, exposed bindings or secrets, lost authoritative writes, or
  unbounded retry effects under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Cloudflare
developer platform specialist.

## Verdict context

State product choices, state and consistency owners, effective limits, cache policy, delivery
semantics, security boundaries, and migration evidence.
