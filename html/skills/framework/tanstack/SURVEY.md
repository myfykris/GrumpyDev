# TanStack survey contribution

## Applicability

Apply this contribution when a plan depends on tanstack start, router, or query. Skip it when
TanStack does not constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
TanStack. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: TanStack product versions, React and runtime versions, router
  generation, Start server runtime, hosting adapter, query-key conventions, cache defaults,
  persistence, hydration, server-function middleware, and authorization boundary.
- Review doctrine: Route visibility and client middleware are user experience controls, not
  data authorization. Every server function and protected data source must enforce its own
  trusted authorization.
- Conditional deployment boundary: TanStack product and React versions, generated
  routes, server runtime and adapter, regions, cookie and proxy settings, query persistence,
  environment sources, build output, and production command.

## Ask only when materially unresolved

- Which TanStack products and versions, React runtime, host, route generation, and rendering
  mode apply?
- How are query keys, freshness, invalidation, hydration, optimistic updates, server functions,
  and authorization owned?

## Record in .grump

Record confirmed TanStack answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable TanStack doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey TanStack when its version, target platform, rendering or execution model, trust
boundary, deployment adapter, persistent state, update process, or recovery policy materially
changes, when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
