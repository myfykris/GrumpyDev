# TanStack survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on one or
more TanStack products, including Start, Router, Query, DB, Store, Table, Form,
Virtual, Pacer, AI, Charts, Hotkeys, Markdown, Highlight, Devtools, Config, CLI,
Intent, or related packages.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output,
route trees, server functions, query clients, collections, stores, component
state, renderers, build and deployment workflows, project documentation,
representative tests, and existing `.grump` doctrine. Resolve facts from current
evidence before asking.

## Durable project facts

- Product roster, versions, supported UI framework and runtime, and which
  product owns each route, remote-data, local-state, tabular, form,
  virtualization, scheduling, AI, content-rendering, or tooling concern.
- For Start and Router: route generation, loaders, server runtime and adapter,
  rendering and streaming, server functions, middleware, cookies, error
  boundaries, and authorization.
- For Query, DB, and Store: key or collection identity, cache and freshness,
  invalidation, optimistic updates, persistence, hydration, synchronization,
  conflict handling, selectors, and subscription ownership.
- For Table, Form, Virtual, and Pacer: controlled-state ownership, row or item
  identity, server-side operations, validation, cancellation, flush behavior,
  measurement, accessibility, and performance limits.
- For AI, Charts, Markdown, Highlight, and Hotkeys: trust and escaping, stream or
  tool-call behavior, model and data contracts, keyboard conflicts,
  accessibility, and rendering cost.
- For Devtools, Config, CLI, Intent, and generated artifacts: source of truth,
  environment and secret handling, production exclusion, regeneration, and
  dependency ownership.
- Review doctrine: Route visibility and client middleware are user experience controls, not
  data authorization. Every server function and protected data source must enforce its own
  trusted authorization.
- Conditional deployment boundary: selected TanStack products and UI framework,
  generated routes or artifacts, server runtime and adapter, regions, cookie and
  proxy settings, persisted or synchronized state, environment sources, build
  output, and production command.

## Ask only when materially unresolved

- Which TanStack products and versions apply, which framework and runtime host
  them, and what project concern does each product own?
- For the selected products, which identity, state, persistence, authorization,
  trust, accessibility, performance, build, and deployment rules materially
  affect later reviews?

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

Re-survey TanStack when the product roster or a product version, UI framework,
runtime adapter, route or server-function contract, data or state owner,
persistence or sync model, rendering trust boundary, generated-artifact source,
accessibility baseline, or deployment behavior materially changes. Also
re-survey when evidence conflicts with saved doctrine or the user requests a
context refresh.
