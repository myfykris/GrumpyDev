# FastAPI survey contribution

## Applicability

Apply this contribution when a Python plan changes FastAPI applications, routes,
dependencies, models, or middleware. Skip it when FastAPI does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For FastAPI, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: FastAPI, Pydantic and Python versions, ASGI
  server, worker model, proxy path, schema consumers, dependency lifetimes, and
  deployment topology.
- Review doctrine for: Dependency scopes, async and blocking work, Pydantic
  validation, OpenAPI contracts, lifespan, background tasks, streaming, errors,
  workers, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Python, ASGI server, worker class and count,
  sync-thread pool, proxy, lifespan, sessions, background execution, limits,
  drain, and deployment.

## Ask only when materially unresolved

- Which Python, FastAPI, Starlette, and Pydantic versions and server-worker
  model apply?
- How do validation, dependency lifetimes, sync work, async cancellation,
  errors, and schema compatibility behave?
- Align existing domain questions with this deployment guidance when it is
  material: Python, ASGI server, worker class and count, sync-thread pool,
  proxy, lifespan, sessions, background execution, limits, drain, and
  deployment. Do not repeat the core profile confirmation.

## Record in .grump

Record FastAPI answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing FastAPI survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable FastAPI
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey FastAPI when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
