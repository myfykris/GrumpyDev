# Neo4j full-review guidance

## Operating conditions

Establish the project target: Neo4j version and edition, topology, graph size
and density, schema and constraints, query patterns, drivers, security, and
backup process. The changed boundary must define: Graph model, labels and
relationship types, constraints, indexes, Cypher plans, traversal growth,
transactions, clustering, imports, and backup.

## Failure patterns

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

## Verification to run or specify in the plan

- Profile Cypher queries on representative degree distributions, including
  dense nodes and long paths. Check result cardinality, traversal bounds,
  uniqueness constraints, and transaction size.
- Interrupt imports and retry conflicting writes. If clustered, exercise
  routing and failover with the intended consistency mechanism; restore a
  backup and verify graph constraints and application queries.
