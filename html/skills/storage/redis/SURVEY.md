# Redis survey contribution

## Applies when

Apply this contribution when Redis holds cache, coordination, queue, session, or primary
application state.

## Inspect

- Establish the exact Redis-compatible product, version, deployment mode,
  persistence mode, and failover implementation.

## Ask when unresolved

- Which Redis-compatible product, exact version, deployment mode, persistence,
  eviction, and failover behavior apply?

- Is the data disposable cache, coordination state, queue state, session state,
  or primary data, and how is loss recovered?

- Which runtime or deployment differences are material for future reviews:
  Product and version, cache or authority role, topology, cluster or sentinel,
  memory and eviction, persistence, replicas, failover, TLS and identity,
  backup, and reconstruction?

## Record

Map Redis data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
