# React survey contribution

## Applicability

Apply this contribution when a plan creates or changes React components, hooks,
routes, data flows, or frontend architecture. Skip it when React does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For React, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: React version, renderer and framework, server or
  client rendering, browser targets, state and data libraries, bundler, test
  renderer, and deployment form.
- Review doctrine for: Render purity, state ownership, effects, concurrency,
  transitions, suspense, server rendering, hydration, context, forms,
  accessibility, performance, untrusted rendering, browser storage, and library
  boundaries.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Client-only, SSR, streaming, server-component,
  native, or embedded target; browser and server runtimes; build output; cache;
  content security policy; and hosting base path.

## Ask only when materially unresolved

- Which React version, JavaScript or TypeScript version, framework, rendering
  mode, and supported browsers apply?
- Who owns server data, URL state, form state, effects, hydration, errors, and
  accessibility behavior?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Client-only, SSR, streaming,
  server-component, native, or embedded target; browser and server runtimes;
  build output; cache; content security policy; and hosting base path? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record React answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed React deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable React doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey React when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
