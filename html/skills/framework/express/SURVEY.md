# Express survey contribution

## Applicability

Apply this contribution when a JavaScript or TypeScript plan changes Express
applications, routers, middleware, or HTTP handlers. Skip it when Express does
not constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Express, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Express and Node versions, module system, proxy
  topology, session store, body limits, worker or cluster model, process
  manager, and deployment platform.
- Review doctrine for: Middleware and error order, request lifecycle, async
  failures, body parsing, proxy trust, sessions, streaming, shutdown, Node event
  loop, and security boundaries.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Node.js and Express versions, proxy topology,
  trust proxy, worker or cluster model, process manager, sessions, body limits,
  timeouts, signals, and graceful shutdown.

## Ask only when materially unresolved

- Which Node.js and Express versions, module mode, proxy topology, and server
  runtime apply?
- How do middleware order, trust proxy, body limits, async errors,
  authentication, and shutdown behave?
- Align existing domain questions with this deployment guidance when it is
  material: Node.js and Express versions, proxy topology, trust proxy, worker
  or cluster model, process manager, sessions, body limits, timeouts, signals,
  and graceful shutdown. Do not repeat the core profile confirmation.

## Record in .grump

Record Express answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Express survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Express
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Express when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
