---
name: cassandra
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Cassandra engineering work for query-driven modeling, partition sizing, consistency, tombstones, compaction, repair, topology, and recovery."
---

# Cassandra GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems` skill.

## Lean review

- Establish the exact product, version, edition, topology, hosting mode, and
  compatibility boundary.

- Read query inventory, primary keys, partition estimates, consistency levels,
  TTLs, compaction, replication, repair, backup, and load tests.

Watch especially for hot or unbounded partitions, tombstone accumulation, ALLOW
FILTERING accepted as a design, consistency levels treated as freshness
guarantees, lightweight transactions used as general locking, repair falling
behind gc_grace, and topology changes ignored in capacity plans.

Lean mode is insufficient when this material severity condition may apply:

- Treat an unbounded partition, unrecoverable consistency gap, or topology
  change that risks data loss as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Cassandra evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State query coverage, partition bounds, consistency choices, maintenance burden,
topology assumptions, and recovery evidence.
