# Elasticsearch and OpenSearch survey contribution

## Applies when

Apply this contribution when the project implements search, analytics, or log storage
with Elasticsearch or OpenSearch.

## Inspect

- Establish the exact Elasticsearch or OpenSearch product, version,
  distribution, plugins, hosting mode, and compatibility boundary.

## Ask when unresolved

- Which Elasticsearch or OpenSearch product, exact version, deployment mode,
  plugins, and compatibility promises apply?

- How are mappings, aliases, refresh behavior, reindexing, shard size, and
  failed-node recovery handled?

- Which runtime or deployment differences are material for future reviews:
  Product and version, managed or self-hosted mode, nodes, roles, shards,
  replicas, zones, storage, snapshots, reindex capacity, security, and
  failover?

## Record

Map Elasticsearch and OpenSearch data guarantees to `Requirements`, accepted
tradeoffs to `Accepted decisions`, topology and recovery facts to `Runtime and
deployment`, and material gaps to `Unknowns`.
