---
name: neo4j
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Neo4j engineering work for graph modeling, constraints, indexes, traversal bounds, transactions, clustering, security, and recovery."
---

# Neo4j GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the applicable
installed application specialist for the graph-access boundary.

## Lean review

- Establish the exact Neo4j version, edition, topology, hosting mode, and driver
  versions.

- Read node and relationship models, constraints, indexes, Cypher queries and
  plans, transactions, import jobs, topology, and backups.

Watch especially for supernodes and dense relationships, unbounded
variable-length traversals, accidental Cartesian products, relationship
direction ignored, missing uniqueness constraints, large transactions, and
causal-cluster reads assumed current without bookmarks or an equivalent
consistency mechanism.

Lean mode is insufficient when this material severity condition may apply:

- Treat unbounded traversal, missing uniqueness enforcement, or unrecoverable
  cluster or migration behavior as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Neo4j evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State why a graph is justified, model invariants, traversal bounds, transaction
behavior, topology, and recovery evidence.
