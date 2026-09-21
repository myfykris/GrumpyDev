# Laravel survey contribution

## Applies when

Apply this contribution when Laravel owns the application's HTTP, console, queue, event,
scheduling, model, or deployment lifecycle.

## Inspect

- Establish Laravel and PHP versions, container lifetimes, process model,
  database connection, queue semantics, and generated or cached configuration.

## Ask when unresolved

- Which Laravel and PHP versions and which database, queue, cache, session, and
  filesystem drivers are supported? Ask only where those choices change
  lifecycle, compatibility, or recovery behavior.

- Does any HTTP or job code run in a resident process such as Octane or a long-
  lived worker, and what resets tenant, identity, locale, container, database,
  and third-party client state between units of work?

- Which authentication guards, user providers, tenant boundaries, and policy
  conventions must every protected operation follow?

- What queue delivery, retry, timeout, uniqueness, failed-job, and idempotency
  expectations are project-wide, and how do workers drain during deployment?

- What is the project's expand, backfill, contract, and rollback convention for
  database changes while old and new web and worker code can overlap?

- Which generated caches and artifacts are built before deployment, and which
  processes must reload or restart before new configuration and code apply?

- Who owns the scheduler, what prevents overlap or duplicate schedulers, and
  how are missed or failed scheduled tasks recovered?

- Which runtime or deployment differences are material for future reviews: PHP
  SAPI, server, FPM or Octane, queues, scheduler, sessions, cache, files,
  database, proxy, config cache, rollout, and worker restart coverage?

## Record

Map durable Laravel version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
