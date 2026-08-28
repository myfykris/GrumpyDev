# Laravel survey contribution

## Applicability

Apply this contribution when Laravel owns the application's HTTP, console, queue, event,
scheduling, model, or deployment lifecycle. Combine it with PHP, the selected database,
queue, cache, filesystem, web-server, and deployment survey contributions. Do not repeat
their version or topology questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

- Read Composer constraints and lock data, Laravel bootstrap and configuration,
  service providers, package discovery, environment mapping, and application
  structure.
- Inspect routes, middleware groups, authentication guards and providers,
  policies, models, migrations, queue and cache configuration, filesystems,
  session storage, scheduler definitions, broadcasting, mail, and notifications.
- Inspect deployment scripts for generated caches, static assets, migrations,
  maintenance mode, queue drain and restart, Horizon, Octane reload, scheduler
  ownership, OPcache, health checks, and rollback.
- Determine runtime drivers and versions from actual configuration and
  infrastructure, not from example environment files.
- Read architecture and operational documentation for tenant boundaries,
  transaction rules, queue guarantees, deployment overlap, and recovery.

## Durable project facts

- Supported Laravel and PHP versions and the policy for framework and package
  upgrades.
- Conventional PHP request runtime, Octane or another resident server, queue
  workers, Horizon, scheduled commands, and their process lifecycles.
- Database connections and versions, migration ownership, transaction
  conventions, backfill process, and mixed-version deployment expectation.
- Queue connections and drivers, delivery expectations, retry and timeout
  policy, failed-job handling, uniqueness conventions, worker topology, and
  deployment restart process.
- Cache, session, filesystem, mail, broadcast, and notification drivers and the
  material behavior expected when each dependency is degraded.
- Authentication guards and providers, authorization ownership, tenant model,
  trusted proxy policy, and API contract conventions.
- Container binding and request-scope conventions, especially under resident
  runtimes.
- Configuration, route, event, view, and service cache policy and which
  deployment stage produces them.
- Scheduler ownership, overlap and single-server policy, timezone, missed-run
  expectations, and manual recovery.
- Deployment unit, artifact model, maintenance and health behavior, worker drain
  and restart, rollback limits, and operational owners.
- Deployment-profile guidance: PHP SAPI, server, FPM or
  Octane, queues, scheduler, sessions, cache, files, database, proxy, config
  cache, rollout, and worker restart coverage.

## Ask only when materially unresolved

- Which Laravel and PHP versions and which database, queue, cache, session, and
  filesystem drivers are supported? Ask only where those choices change
  lifecycle, compatibility, or recovery behavior.
- Does any HTTP or job code run in a resident process such as Octane or a
  long-lived worker, and what resets tenant, identity, locale, container,
  database, and third-party client state between units of work?
- Which authentication guards, user providers, tenant boundaries, and policy
  conventions must every protected operation follow?
- What queue delivery, retry, timeout, uniqueness, failed-job, and idempotency
  expectations are project-wide, and how do workers drain during deployment?
- What is the project's expand, backfill, contract, and rollback convention for
  database changes while old and new web and worker code can overlap?
- Which generated caches and artifacts are built before deployment, and which
  processes must reload or restart before new configuration and code apply?
- Who owns the scheduler, what prevents overlap or duplicate schedulers, and how
  are missed or failed scheduled tasks recovered?
- Align existing domain questions with this deployment guidance when it is
  material: PHP SAPI, server, FPM or Octane, queues,
  scheduler, sessions, cache, files, database, proxy, config cache, rollout,
  and worker restart coverage. Do not repeat the core profile confirmation.

## Record in .grump

Record stable framework and driver targets under `Technology and runtime`.
Record HTTP, queue, scheduler, tenant, authentication, and storage ownership
under `System boundaries`. Record transaction, authorization, queue,
idempotency, worker-lifecycle, cache, deployment, and rollback conventions as
constraints, durable decisions, or operational invariants as appropriate.

Name the configuration, deployment, documentation, or explicit statement that
supports each material answer. Use an `UNK-###` item only for a missing Laravel
lifecycle or driver decision that can materially alter later plan reviews.

Map existing Laravel survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

- Do not request `.env` contents, application keys, credentials, tokens,
  production payloads, session identifiers, or queue messages containing user
  data.
- Do not copy entire configuration dumps into `.grump`.
- Do not store route-specific validation, a temporary queue name, a one-time
  migration command, or a current worker count as durable doctrine unless it is
  explicitly a stable project constraint.
- Do not infer authorization policy from controller or route names.
- Do not treat example configuration as evidence of an active production driver.

## Re-survey triggers

Re-survey after a Laravel major-version change, PHP runtime or SAPI change,
Octane or resident-runtime adoption, authentication or tenant-model change,
database or migration-process change, queue or cache driver change, worker and
scheduler topology change, generated-cache change, filesystem or session move,
or material deployment and rollback redesign.
