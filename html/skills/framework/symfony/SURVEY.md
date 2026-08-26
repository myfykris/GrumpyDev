# Symfony survey contribution

## Applicability

Apply this contribution when a PHP plan changes Symfony controllers, services,
entities, messages, listeners, or operations. Skip it when Symfony does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Symfony, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Symfony and PHP versions, runtime and SAPI,
  Doctrine providers, Messenger transports, cache, authentication, worker
  topology, and deployment process.
- Review doctrine for: Container compilation, request and kernel events,
  configuration, Doctrine, validation, security voters, messenger, cache,
  console, workers, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: PHP SAPI and server, FPM pools, Messenger
  workers, scheduler, cache, sessions, files, proxy, compiled container,
  migrations, worker restart, and deployment.

## Ask only when materially unresolved

- Which PHP, Symfony, runtime, container, database, cache, and Messenger
  versions or transports apply?
- How do service scopes, security voters, validation, transactions, messages,
  retries, and migrations interact?
- Align existing domain questions with this deployment guidance when it is
  material: PHP SAPI and server, FPM pools, Messenger workers, scheduler,
  cache, sessions, files, proxy, compiled container, migrations, worker
  restart, and deployment. Do not repeat the core profile confirmation.

## Record in .grump

Record Symfony answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Symfony survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Symfony
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Symfony when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
