# Elixir survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Elixir or Erlang code, OTP applications, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Elixir, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Elixir and OTP versions, release tooling, node
  topology, clustering and discovery, deployment model, scheduler and resource
  limits, and persistence dependencies.
- Review doctrine for: BEAM processes, supervision, linking and monitoring,
  mailbox growth, OTP behaviors, fault isolation, clustering, distribution, hot
  upgrades, persistence boundaries, and releases.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Erlang/OTP and Elixir versions, release packaging,
  node topology, schedulers, clustering, distribution, process supervision, and
  rolling upgrade model.

## Ask only when materially unresolved

- Which Elixir, Erlang/OTP, release target, and dependency versions define
  runtime behavior?
- Which process owns state and work, and how do supervision, messages, timeouts,
  overload, and upgrades behave?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Erlang/OTP and Elixir versions, release
  packaging, node topology, schedulers, clustering, distribution, process
  supervision, and rolling upgrade model? Ask only when evidence and the core
  profile confirmation do not resolve them.

## Record in .grump

Record Elixir answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Elixir deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Elixir doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Elixir when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
