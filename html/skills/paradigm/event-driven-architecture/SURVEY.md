# Event-driven architecture survey contribution

## Applies when

Apply this contribution when services communicate or trigger work through events or
messages.

## Inspect

- Read event schemas, producers, consumers, brokers, delivery settings, retry
  and dead-letter policy, replay tooling, and ownership.

## Ask when unresolved

- Is each message an event, command, or data stream, and who owns its meaning
  and handling?

- What delivery, ordering, acknowledgement, duplication, evolution, replay, and
  recovery semantics apply?

- Which runtime or deployment differences materially change future reviews:
  Broker or transport, delivery and acknowledgement, partitions, ordering,
  retention, dead letters, consumer topology, replay, regions, and operational
  owner?

## Record

Map accepted Event-driven architecture choices to `Accepted decisions`, binding
boundaries to `Requirements` or `Constraints`, and material gaps to `Unknowns`.
