# Django survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Django.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Django, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Django and Python versions, WSGI or ASGI, server
  and worker model, databases, caches, queues, storage, authentication, settings
  environments, and migration process.
- Review doctrine for: Settings and app loading, middleware order, ORM and
  transactions, migrations, signals, authentication, forms, async boundaries,
  caching, static media, jobs, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Python, WSGI or ASGI server, worker type and
  count, proxy, static and media storage, cache, sessions, queues, settings
  authority, migration process, drain, and rollback.

## Ask only when materially unresolved

- Which Django, Python, database, application server, and deployment versions
  apply?
- How do middleware, transactions, migrations, authentication, async boundaries,
  caching, and background work interact?
- Align existing domain questions with this deployment guidance when it is
  material: Python, WSGI or ASGI server, worker type and count, proxy, static
  and media storage, cache, sessions, queues, settings authority, migration
  process, drain, and rollback. Do not repeat the core profile confirmation.

## Record in .grump

Record Django answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Django survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Django doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Django when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
