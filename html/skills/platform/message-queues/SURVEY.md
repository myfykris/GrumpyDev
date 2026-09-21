# Message queues survey contribution

## Applies when

Apply this contribution when work or data crosses a broker, queue, stream, or pub-sub
system.

## Inspect

- Read topic and queue topology, keys, payload schemas, acknowledgements,
  visibility or leases, retries, retention, dead letters, quotas, and
  dashboards.

## Ask when unresolved

- Which broker and delivery, ordering, acknowledgement, retention, and redrive
  guarantees actually apply?

- What makes duplicate, delayed, reordered, poison, or permanently failed
  messages safe and recoverable?

- Which runtime or deployment differences materially change future reviews:
  Product and version, topology, partitions, ordering, acknowledgement,
  visibility, retention, dead letters, security, producer and consumer regions,
  scaling, and failover?

## Record

Map durable Message queues requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
