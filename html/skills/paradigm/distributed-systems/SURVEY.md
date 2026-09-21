# Distributed systems survey contribution

## Applies when

Apply this contribution when correctness or availability crosses independently failing
processes, services, machines, regions, or external authorities. A small application
with a database, queue, cache, or remote API can qualify.

## Inspect

- Identify the authority and commit point for each user-visible decision and
  what a caller observes after success, rejection, delay, timeout, or partition.

## Ask when unresolved

- Which durable ownership, staleness, partition, retry, idempotency, delivery,
  reconciliation, fencing, or recovery rules govern distributed work?

- Which runtime or deployment differences are material for future reviews:
  Nodes, regions, failure domains, network assumptions, clocks, membership,
  quorum, consistency, partitions, reconciliation, rollout, and disaster
  recovery?

## Record

Map accepted Distributed systems choices to `Accepted decisions`,
binding boundaries to `Requirements` or `Constraints`, and material gaps to
`Unknowns`.
