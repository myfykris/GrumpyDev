---
name: elasticsearch-opensearch
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Elasticsearch and OpenSearch plans and other engineering artifacts for mappings, analyzers, shards, queries, ingestion, cluster capacity, security, and recovery. Project applicability: the project implements search, analytics, or log storage with Elasticsearch or OpenSearch."
---

# Elasticsearch and OpenSearch GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
