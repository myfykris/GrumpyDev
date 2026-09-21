# MongoDB survey contribution

## Applies when

Apply this contribution when the project stores or queries application data in MongoDB.

## Inspect

- Read document models, validators, indexes, query and aggregation plans, read
  and write concerns, sessions, shard keys, replicas, and backups.

## Ask when unresolved

- Which MongoDB version, topology, storage mode, read concern, write concern,
  and transaction use apply?

- How are schema variation, indexes, retries, migrations, replication lag, and
  restore handled?

- Which runtime or deployment differences are material for future reviews:
  Product and version, managed or self-hosted mode, replica set or sharding,
  regions, read and write concerns, storage, backup, restore, failover, and
  driver behavior?

## Record

Map MongoDB data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
