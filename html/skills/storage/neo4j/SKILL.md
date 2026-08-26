---
name: neo4j
description: Review Neo4j plans for graph modeling, constraints, indexes, traversal bounds, transactions, clustering, security, and recovery. Use when a plan stores or queries connected data in Neo4j.
---

# Neo4j plan review

Apply this guidance alongside the core GrumpyDev review and the applicable
installed application specialist for the graph-access boundary.

## Inspect evidence

- Establish the exact Neo4j version, edition, topology, hosting mode, and driver
  versions.
- Read node and relationship models, constraints, indexes, Cypher queries and
  plans, transactions, import jobs, topology, and backups.
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

## Challenge the plan

### Recurring traps

Watch especially for supernodes and dense relationships, unbounded
variable-length traversals, accidental Cartesian products, relationship
direction ignored, missing uniqueness constraints, large transactions, and
causal-cluster reads assumed current without bookmarks or an equivalent
consistency mechanism.

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

- Treat unbounded traversal, missing uniqueness enforcement, or unrecoverable
  cluster or migration behavior as critical.
- Downgrade when representative graph data and product-specific constraints,
  query plans, and recovery tests support the plan.

## Add to the verdict

State why a graph is justified, model invariants, traversal bounds, transaction
behavior, topology, and recovery evidence.
