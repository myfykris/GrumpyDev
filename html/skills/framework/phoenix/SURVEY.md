# Phoenix survey contribution

## Applicability

Apply this contribution when an Elixir plan changes Phoenix endpoints,
controllers, LiveViews, channels, contexts, or releases. Skip it when Phoenix
does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

For Phoenix, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Phoenix, Elixir and OTP versions, LiveView use,
  database, PubSub and cluster topology, session and proxy setup, release
  tooling, and deployment environment.
- Review doctrine for: Endpoint and plug order, LiveView lifecycle, channels,
  PubSub, Ecto transactions, supervision, sessions, presence, clustering,
  releases, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Elixir and OTP release, node topology, endpoint and
  proxy, PubSub adapter, clustering, sessions, Ecto pool, workers, rollout, and
  distributed shutdown.

## Ask only when materially unresolved

- Which Elixir, Erlang/OTP, Phoenix, LiveView, and deployment versions apply?
- How do process ownership, supervision, socket state, PubSub, transactions,
  reconnect, and release rollout interact?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Elixir and OTP release, node topology,
  endpoint and proxy, PubSub adapter, clustering, sessions, Ecto pool, workers,
  rollout, and distributed shutdown? Ask only when evidence and the core
  profile confirmation do not resolve them.

## Record in .grump

Record Phoenix answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed Phoenix deployment facts on the affected `DEP-###` profile.
Use a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Phoenix
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Phoenix when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
