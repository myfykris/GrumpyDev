---
name: elasticsearch-opensearch
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Elasticsearch and OpenSearch engineering work for mappings, analyzers, shards, queries, ingestion, cluster capacity, security, and recovery."
---

# Elasticsearch and OpenSearch GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `data-pipelines`
or `observability` skill.

## Lean review

- Establish the exact Elasticsearch or OpenSearch product, version,
  distribution, plugins, hosting mode, and compatibility boundary.

- Read index templates, mappings, analyzers, queries, ingest pipelines, shard
  topology, lifecycle policies, security, snapshots, and benchmarks.

Watch especially for dynamic mappings causing field explosion, analyzed and
exact fields confused, deep pagination, shard counts chosen by habit, refresh
and merge cost ignored, aliases switched before reindex verification, partial
search results accepted silently, and snapshots mistaken for
application-consistent backups.

Lean mode is insufficient when this material severity condition may apply:

- Treat irreversible mapping conflict, cluster instability, or search
  authorization leakage as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Elasticsearch and OpenSearch evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State mapping and relevance evidence, shard model, expensive-query controls,
ingestion bounds, and recovery proof.
