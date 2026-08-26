---
name: tanstack
description: Review TanStack Start, Router, and Query plans for server functions, routing, loaders, caching, invalidation, hydration, authorization, and deployment. Use when a plan depends on TanStack Start, Router, or Query.
---

# TanStack plan review

Apply this guidance alongside the core GrumpyDev review and the `react`, `typescript` and `vite`
skills.

## Inspect evidence

- Identify which TanStack products and versions apply: Start, Router, Query, Form, Table, or
  related packages.
- Read route trees, loaders, server functions, middleware, query clients, keys, defaults,
  persistence, and dehydration code.
- Trace server, client, edge, build, and serialized boundaries plus authentication and
  per-operation authorization.
- Inspect navigation, preloading, cache ownership, invalidation, optimistic updates, retries,
  errors, and deployment output.

## Establish the operating model

Establish the project target: TanStack product versions, React and runtime versions, router
generation, Start server runtime, hosting adapter, query-key conventions, cache defaults,
persistence, hydration, server-function middleware, and authorization boundary.

Route visibility and client middleware are user experience controls, not data authorization.
Every server function and protected data source must enforce its own trusted authorization.

## Challenge the plan

### Recurring traps

Watch especially for query keys missing tenant or filter inputs, stale caches crossing users,
optimistic updates without reconciliation, server functions trusted because callers are
generated, loaders duplicating query ownership, and runtime adapters assumed equivalent.

- Require canonical query keys that include every identity, tenant, locale, filter, and version
  dimension affecting data.
- Define freshness, garbage collection, retries, cancellation, invalidation, optimistic
  rollback, persistence, and offline behavior per query class.
- Authorize and validate inside every server function or trusted service boundary regardless of
  route guards or generated clients.
- Ensure loaders, router context, query cache, and server rendering have one coherent data
  owner and hydration contract.
- Verify Start build output, server runtime APIs, streaming, cookies, environment values, and
  deployment adapter behavior.

## Verify the claims

- Exercise navigation, preloading, parallel requests, cancellation, stale data, failed
  mutations, optimistic rollback, and tenant changes.
- Inspect dehydrated state and persisted caches for private data, incompatible versions, and
  missing query-key dimensions.
- Run production Start output or the actual Router and Query integration under the selected
  runtime and cache topology.

## Ask when evidence is missing

- Which TanStack products and versions, React runtime, host, route generation, and rendering
  mode apply?
- How are query keys, freshness, invalidation, hydration, optimistic updates, server functions,
  and authorization owned?

## Calibrate findings

- Treat cross-user cache leakage, missing server-function authorization, or unreconciled
  irreversible optimistic effects as critical.
- Downgrade when keys, cache policy, invalidation, authorization, hydration, and production
  runtime behavior are tested.

## Add to the verdict

State the products in use, route and data owners, key schema, cache and invalidation policy,
authorization boundary, and runtime evidence.
