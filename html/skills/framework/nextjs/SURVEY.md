# Next.js survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Next.js.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Next.js, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Next.js, React and Node versions, router,
  rendering modes, edge or Node runtime, cache and revalidation policy, hosting
  target, build output, and browser support.
- Review doctrine for: App and pages routers, server and client components,
  rendering and caching modes, actions, middleware, route handlers, hydration,
  runtimes, assets, authorization boundaries, outbound fetch and redirect
  policy, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Node, edge, serverless, static, and client
  runtimes; build-time versus request-time data; cache and revalidation
  ownership; regions; assets; and deployment platform.

## Ask only when materially unresolved

- Which Next.js, React, router, rendering mode, cache mode, and deployment
  runtime apply?
- Where do authentication, server actions, route handlers, revalidation,
  serialization, and client state cross boundaries?
- Align existing domain questions with this deployment guidance when it is
  material: Node, edge, serverless, static, and client runtimes; build-time
  versus request-time data; cache and revalidation ownership; regions; assets;
  and deployment platform. Do not repeat the core profile confirmation.

## Record in .grump

Record Next.js answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Next.js survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Next.js
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Next.js when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
