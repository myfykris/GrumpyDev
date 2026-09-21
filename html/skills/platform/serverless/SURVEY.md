# Serverless survey contribution

## Applies when

Apply this contribution when the project runs application work on functions or managed
event-driven compute.

## Inspect

- Establish the exact provider, service, runtime version, deployment mode,
  region, and provider limits.

## Ask when unresolved

- Which provider, service, runtime version, deployment mode, trigger, and
  regional limits apply?

- What delivery, concurrency, timeout, retry, state, networking, permission,
  and cost behavior follows from that platform?

- Which runtime or deployment differences are material for future reviews:
  provider, region, runtime, trigger, concurrency, timeout, ephemeral storage,
  identity, networking, cold start, retries, destinations, limits, and
  deployment coverage?

## Record

Map durable Serverless requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
