---
name: neo4j
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Neo4j plans and other engineering artifacts for graph modeling, constraints, indexes, traversal bounds, transactions, clustering, security, and recovery. Project applicability: the project stores or queries connected data in Neo4j."
---

# Neo4j GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
