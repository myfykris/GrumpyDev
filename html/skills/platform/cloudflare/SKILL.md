---
name: cloudflare
description: Review Cloudflare plans for Workers runtime limits, isolate lifecycle, bindings, KV consistency, Durable Objects, D1, queues, caching, networking, and deployment. Use when applications run on Cloudflare Workers or related developer-platform services.
---

# Cloudflare developer platform plan review

Apply this guidance alongside the core GrumpyDev review and the `serverless`,
`distributed-systems` and `observability` skills.

## Inspect evidence

- Read compatibility date and flags, Workers runtime, bindings, routes, regions, limits,
  deployment configuration, and account settings.
- Classify state across request memory, Cache API, KV, Durable Objects, D1, R2, queues,
  external stores, and browser caches.
- Trace subrequests, concurrency, CPU, wall time, memory, connection limits, retries, alarms,
  queue delivery, and failure handling.
- Inspect secrets, service bindings, origins, custom domains, cache keys, migrations,
  observability, and local versus remote development.

## Establish the operating model

Establish the project target: Cloudflare products, compatibility date and flags, plans and
limits, routes and domains, bindings, storage consistency requirements, Durable Object
migrations and placement, D1 topology, queue delivery, cache policy, secrets, and deployment
environments.

A Worker isolate and its global memory are reusable but not durable or guaranteed to handle the
next request. State consistency must follow the selected storage product, not a generic edge
assumption.

## Challenge the plan

### Recurring traps

Watch especially for mutable global state treated as durable, KV used for coordination despite
eventual consistency, Durable Object in-memory values lost after hibernation, queue or alarm
delivery assumed exactly once, and local emulation treated as proof of production limits.

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

## Verify the claims

- Run production-like Workers tests against the real product boundaries or documented limits,
  not only local simulation.
- Exercise isolate reuse and eviction, KV lag, D1 replica reads, Durable Object hibernation,
  duplicate queues, and alarm retries.
- Inspect effective bindings, routes, compatibility settings, cache behavior, observability,
  and deployed bundle size locally.

## Ask when evidence is missing

- Which Cloudflare products, compatibility settings, account limits, routes, bindings, regions,
  and stores apply?
- What consistency, isolate lifecycle, retry, cache, migration, security, observability, and
  rollback behavior is required?

## Calibrate findings

- Treat cross-tenant cache leakage, exposed bindings or secrets, lost authoritative writes, or
  unbounded retry effects as critical.
- Downgrade when product semantics, limits, consistency, duplicate delivery, migrations, and
  recovery are proven.

## Add to the verdict

State product choices, state and consistency owners, effective limits, cache policy, delivery
semantics, security boundaries, and migration evidence.
