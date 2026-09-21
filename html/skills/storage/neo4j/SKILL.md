---
name: gd-neo4j
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Neo4j engineering work for graph modeling, constraints, indexes, traversal bounds, transactions, clustering, security, and recovery."
---

# Neo4j GrumpyDev review

## Quick checks

- Establish the exact Neo4j version, edition, topology, hosting mode, and driver
  versions.

- Read node and relationship models, constraints, indexes, Cypher queries and
  plans, transactions, import jobs, topology, and backups.

Watch especially for supernodes and dense relationships, unbounded
variable-length traversals, accidental Cartesian products, relationship
direction ignored, missing uniqueness constraints, large transactions, and
causal-cluster reads assumed current without bookmarks or an equivalent
consistency mechanism.

- Assess unbounded traversal, missing uniqueness enforcement, or unrecoverable
  cluster or migration behavior under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Neo4j specialist.

## Verdict context

State why a graph is justified, model invariants, traversal bounds, transaction
behavior, topology, and recovery evidence.
