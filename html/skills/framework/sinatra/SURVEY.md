# Sinatra survey contribution

## Applicability

Apply this contribution when a Ruby plan changes Sinatra applications, routes,
extensions, or Rack middleware. Skip it when Sinatra does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Sinatra, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Sinatra and Ruby versions, Rack and server
  versions, thread and worker model, middleware, sessions, proxy setup, and
  deployment platform.
- Review doctrine for: Request lifecycle, settings and environments, middleware,
  thread safety, sessions, errors, streaming, reloading, server behavior, and
  deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Ruby implementation, Rack and server, process and
  thread model, middleware, proxy, sessions, static files, timeouts, signals,
  and production deployment.

## Ask only when materially unresolved

- Which Ruby, Sinatra, Rack, server, concurrency, and deployment versions or
  modes apply?
- How do middleware, shared state, sessions, authentication, errors, blocking
  work, and shutdown behave?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Ruby implementation, Rack and server,
  process and thread model, middleware, proxy, sessions, static files,
  timeouts, signals, and production deployment? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Sinatra answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Sinatra deployment facts on the affected `DEP-###` profile.
Use a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Sinatra
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Sinatra when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
