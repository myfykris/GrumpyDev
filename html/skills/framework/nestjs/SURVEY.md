# NestJS survey contribution

## Applicability

Apply this contribution when a TypeScript plan changes NestJS applications,
modules, controllers, providers, or transports. Skip it when NestJS does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For NestJS, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: NestJS, Node and TypeScript versions, HTTP
  adapter, transport types, provider scope policy, validation stack, process
  topology, and deployment platform.
- Review doctrine for: Module graph, provider scopes, adapters, pipes, guards,
  interceptors, filters, validation, serialization, async context, queues,
  microservices, and shutdown.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Node.js and adapter, Express or Fastify behavior,
  process and worker model, proxy, transports, queues, state, shutdown hooks,
  and deployment artifact.

## Ask only when materially unresolved

- Which Node.js, NestJS, TypeScript, HTTP adapter, transport, and package
  versions apply?
- How do module boundaries, provider scopes, guards, pipes, interceptors,
  validation, and shutdown interact?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Node.js and adapter, Express or Fastify
  behavior, process and worker model, proxy, transports, queues, state,
  shutdown hooks, and deployment artifact? Ask only when evidence and the core
  profile confirmation do not resolve them.

## Record in .grump

Record NestJS answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed NestJS deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable NestJS doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey NestJS when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
