# DynamoDB survey contribution

## Applies when

Apply this contribution when the project stores or queries application data in Amazon
DynamoDB.

## Inspect

- Establish the regions, table class and capacity mode, global-table version,
  backup settings, and client behavior.

## Ask when unresolved

- Which access patterns, key distributions, consistency needs, table mode,
  regions, and transaction boundaries apply?

- How are conditional writes, hot keys, retries, streams, indexes, and item
  growth bounded?

- Which runtime or deployment differences are material for future reviews:
  Region and account, table and index design, capacity mode, partitions, global
  tables, consistency, streams, TTL, backup, restore, IAM, endpoints, and
  limits?

## Record

Map DynamoDB data guarantees to `Requirements`, accepted tradeoffs to `Accepted
decisions`, topology and recovery facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
