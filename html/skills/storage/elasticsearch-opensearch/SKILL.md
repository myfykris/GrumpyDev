---
name: gd-elasticsearch-opensearch
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Elasticsearch and OpenSearch engineering work for mappings, analyzers, shards, queries, ingestion, cluster capacity, security, and recovery."
---

# Elasticsearch and OpenSearch GrumpyDev review

## Quick checks

- Establish the exact Elasticsearch or OpenSearch product, version,
  distribution, plugins, hosting mode, and compatibility boundary.

- Read index templates, mappings, analyzers, queries, ingest pipelines, shard
  topology, lifecycle policies, security, snapshots, and benchmarks.

Watch especially for dynamic mappings causing field explosion, analyzed and
exact fields confused, deep pagination, shard counts chosen by habit, refresh
and merge cost ignored, aliases switched before reindex verification, partial
search results accepted silently, and snapshots mistaken for
application-consistent backups.

- Assess irreversible mapping conflict, cluster instability, or search
  authorization leakage under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Elasticsearch and
OpenSearch specialist.

## Verdict context

State mapping and relevance evidence, shard model, expensive-query controls,
ingestion bounds, and recovery proof.
