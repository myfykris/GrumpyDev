# Background jobs survey contribution

## Applies when

Apply this contribution when work continues outside the request or initiating process.

## Inspect

- Read enqueue boundaries, payloads, worker configuration, leases, retries,
  schedules, idempotency records, dead-letter handling, and dashboards.

## Ask when unresolved

- What durable record owns each job, and what makes retry or duplicate
  execution safe?

- How are cancellation, lease expiry, poison work, and operator recovery
  handled?

- Which runtime or deployment differences materially change future reviews:
  Queue backend, worker topology, concurrency, acknowledgement and visibility,
  retry, dead letters, scheduler, shutdown, scaling, and deployment ordering?

## Record

Map durable Background jobs requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
