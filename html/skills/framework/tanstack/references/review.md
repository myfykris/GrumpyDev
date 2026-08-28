# TanStack standard review

## Inspect additional evidence

- Trace server, client, edge, build, generated, persisted, synchronized, and
  serialized boundaries. Include authentication and per-operation
  authorization wherever a selected product can cross a trust boundary.
- Inspect the exact products in use and their state identity, lifecycle,
  cancellation, errors, rendering, accessibility, performance, and production
  artifact behavior.

## Establish the operating model

Establish the exact TanStack product roster and versions, supported UI framework
and runtime, source of truth for each product's state or generated output, and
the boundaries where its data becomes persisted, serialized, rendered,
executed, or trusted.

Route visibility and client middleware are user experience controls, not data authorization.
Every server function and protected data source must enforce its own trusted authorization.

## Challenge the reviewed work

### Recurring traps

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
- For DB, define collection identity, schema, sync authority, live-query
  consistency, transaction and optimistic behavior, persistence, conflicts,
  reconciliation, and offline recovery.
- For Store, require stable selectors, explicit derived-state ownership,
  bounded subscriptions, and teardown that does not leak listeners or retain
  stale closures.
- For Table, separate client and server sorting, filtering and pagination;
  require stable row identity, controlled-state ownership, accessible semantics,
  and a deliberate relationship with virtualization.
- For Form, define client and server validation authority, asynchronous
  validation cancellation, submission idempotency, sensitive-value lifetime,
  field identity, reset behavior, and SSR or hydration behavior.
- For Virtual, require stable item identity, correct dynamic measurement,
  scroll restoration, focus retention, keyboard and assistive-technology
  access, and production-shaped performance evidence.
- For Pacer, specify debounce, throttle, rate-limit, queue, concurrency,
  cancellation, flush, teardown and backpressure semantics. Ensure required work
  is not silently discarded at navigation or unmount.
- For AI, treat model output and tool arguments as untrusted. Define streaming,
  cancellation, session and context boundaries, authorization, cost, retries,
  tool confirmation, and output validation before effects or rendering.
- For Charts, Markdown, Highlight, and Hotkeys, verify content escaping, HTML and
  URL policy, keyboard conflicts, accessibility, reduced motion, large-input
  performance, and server/client rendering parity where applicable.
- For Devtools, Config, CLI, Intent and other tooling, keep secrets out of
  generated output, identify the authoritative input, make regeneration
  reproducible, and prove development-only behavior cannot leak into production.

## Verify the claims

- Exercise navigation, preloading, parallel requests, cancellation, stale data, failed
  mutations, optimistic rollback, and tenant changes.
- Inspect dehydrated state and persisted caches for private data, incompatible versions, and
  missing query-key dimensions.
- Run production Start output or the actual Router and Query integration under the selected
  runtime and cache topology.
- Exercise every selected product at its risky lifecycle boundaries: concurrent
  updates, cancellation, navigation or teardown, persistence and reload,
  synchronization conflict, SSR and hydration, authorization failure, untrusted
  content, keyboard and assistive use, and production build output as applicable.

## Ask when evidence is missing

- Which TanStack products and versions apply, which framework and runtime host
  them, and what project concern does each product own?
- For the selected products, which identity, state, persistence, authorization,
  trust, accessibility, performance, build, and deployment rules materially
  affect this review?

## Calibrate findings

- Downgrade when the applicable product-specific identity, state, trust,
  lifecycle, accessibility, performance, build, and production-runtime claims
  are demonstrated rather than inferred from the TanStack name.
