# Cloudflare developer platform full-review guidance

## Operating conditions

Establish the project target: Cloudflare products, compatibility date and flags, plans and
limits, routes and domains, bindings, storage consistency requirements, Durable Object
migrations and placement, D1 topology, queue delivery, cache policy, secrets, and deployment
environments.

## Failure patterns

- Match each state transition to KV, Durable Objects, D1, R2, cache, or an external store based
  on consistency and ownership.
- Bound CPU, memory, subrequests, open connections, body size, startup, duration, and
  downstream concurrency under the actual plan.
- Design queue consumers, alarms, and external effects for duplicate delivery, retry, partial
  completion, and poison work.
- Define cache keys, variation, private-data exclusion, purge, stale behavior, origin fallback,
  and version coexistence.
- Require migration and rollback plans for bindings, Durable Object classes, D1 schema,
  compatibility dates, and routed traffic.
- Verify Origin validation, authentication, service binding trust, secret scope, and localhost
  binding for local services.

## Verification to run or specify in the plan

- Run production-like Workers tests against the real product boundaries or documented limits,
  not only local simulation.
- Exercise isolate reuse and eviction, KV lag, D1 replica reads, Durable Object hibernation,
  duplicate queues, and alarm retries.
- Inspect effective bindings, routes, compatibility settings, cache behavior, observability,
  and deployed bundle size locally.
