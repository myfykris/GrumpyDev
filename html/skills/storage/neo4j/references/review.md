# Neo4j standard review

## Inspect additional evidence

- Trace dense nodes, variable-length traversal, concurrent updates, retry,
  failover, bulk load, and model evolution.

## Establish the operating model

Establish the project target: Neo4j version and edition, topology, graph size
and density, schema and constraints, query patterns, drivers, security, and
backup process. The changed boundary must define: Graph model, labels and
relationship types, constraints, indexes, Cypher plans, traversal growth,
transactions, clustering, imports, and backup.

Name the schema and data authority, writers, scale, consistency, durability, and
migration owner for Graph model, labels and relationship types, constraints,
indexes, Cypher plans. Prove traversal growth, transactions, clustering,
imports, backup under concurrent access, mixed versions, failover, interrupted
migration, rollback, and restore.

## Challenge the reviewed work

### Recurring traps

- Require a graph-shaped access problem; a relational model with arrows is not
  enough to justify a graph database.
- Enforce uniqueness and required identity with constraints rather than
  application-side hope.
- Bound variable-length paths, fan-out, Cartesian products, eager operators, and
  dense-node contention using plan evidence.
- Define transaction retry, lock behavior, write ordering, and idempotency
  during transient cluster errors.
- Prove import, migration, cluster failover, backup compatibility, and restore
  procedures on representative graph size.

## Verify the claims

- Verify these behaviors through the declared Neo4j topology and workload: Graph
  model, labels and relationship types, constraints, indexes, Cypher plans. Use
  production-shaped scale and workload while observing latency, resource use,
  locks or conflicts, replication, and application errors.
- Exercise failure and edge behavior for: traversal growth, transactions,
  clustering, imports, backup. Exercise concurrent writers, retries, duplicate
  operations, failover, interrupted migration, and mixed application versions
  where applicable.
- Restore or reconstruct state in isolation and verify data, metadata, security,
  application startup, and recovery objectives.

## Ask when evidence is missing

- Which Neo4j version, edition, deployment topology, transaction model, and
  driver behavior apply?
- What graph size, degree distribution, index, constraint, query-plan, and
  cluster recovery evidence supports the design?

## Calibrate findings

- Downgrade when representative graph data and product-specific constraints,
  query plans, and recovery tests support the plan.
