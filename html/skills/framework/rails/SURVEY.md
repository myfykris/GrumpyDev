# Ruby on Rails survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Ruby on Rails.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Ruby on Rails, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Rails and Ruby versions, web and job servers,
  database, cache and queue adapters, autoload mode, asset stack, session store,
  and deployment process.
- Review doctrine for: Autoloading, Active Record and transactions, callbacks,
  migrations, jobs, mailers, caching, sessions, authorization, Hotwire, asset
  pipeline, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Ruby and Rails versions, application server,
  process and thread counts, proxy, cache, sessions, Active Job adapter, file
  storage, migrations, assets, restart, and rollback.

## Ask only when materially unresolved

- Which Ruby, Rails, database, job adapter, cache, and application-server
  versions apply?
- How do callbacks, validations, transactions, authorization, autoloading, jobs,
  and migrations interact?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Ruby and Rails versions, application
  server, process and thread counts, proxy, cache, sessions, Active Job
  adapter, file storage, migrations, assets, restart, and rollback? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Ruby on Rails answers in project technology, architecture, runtime,
security, deployment, and verification doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed Ruby on Rails deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Ruby on Rails
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Ruby on Rails when framework or runtime versions, lifecycle or
rendering model, dependency scopes, persistence, authentication, workers,
supported clients, or deployment process materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
