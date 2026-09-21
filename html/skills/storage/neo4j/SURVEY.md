# Neo4j survey contribution

## Applies when

Apply this contribution when the project stores or queries connected data in Neo4j.

## Inspect

- Establish the exact Neo4j version, edition, topology, hosting mode, and driver
  versions.

## Ask when unresolved

- Which Neo4j version, edition, deployment topology, transaction model, and
  driver behavior apply?

- What graph size, degree distribution, index, constraint, query-plan, and
  cluster recovery evidence supports the design?

- Which runtime or deployment differences are material for future reviews:
  Product and version, single or clustered topology, roles, regions, routing,
  consistency, memory and storage, backup, restore, failover, and driver
  behavior?

## Record

Map Neo4j data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
