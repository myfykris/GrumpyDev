# PostgreSQL queries and indexes

Read this reference when the reviewed work directly or indirectly changes SQL queries,
predicates, joins, ordering,
pagination, indexes, selectivity, statistics, parameter-sensitive plans, collation, N+1
behavior, write amplification, or performance and capacity claims.

## Queries and indexes

- Match indexes to actual predicates, join keys, ordering, selectivity,
  cardinality, null behavior, and access patterns. Include write amplification,
  storage, vacuum, and cache cost in the decision.
- Challenge redundant, speculative, or low-selectivity indexes and indexes whose
  column order cannot serve the query. Check partial-index predicates and
  expression-index equivalence exactly.
- Examine N+1 access, unbounded result sets, offset pagination at depth,
  unstable ordering, parameter-sensitive plans, stale statistics, and queries
  that depend on implicit casts or collation behavior.
- State the performance envelope and the fallback if a chosen plan changes as
  data grows. A single favorable plan is evidence, not a permanent guarantee.
