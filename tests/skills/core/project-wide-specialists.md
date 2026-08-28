# Project-wide specialist participation

A project has installed specialist packages for its language, framework,
storage, architecture, and operating boundaries. Some proposed work does not
name or modify artifacts owned by every installed specialist.

Expected behavior:

- Ordinary planning, revision, implementation, or generic review does not
  invoke GrumpyDev or any specialist review behavior.
- An explicit Grump review establishes its roster from installed project-local
  specialists and excludes only a package explicitly marked `inapplicable` in
  `.grump` from project evidence or a user answer.
- `current`, `incomplete`, `not surveyed`, and unrecorded installed specialists
  participate. Missing survey context limits only conclusions that depend on
  that context.
- Every active specialist entrypoint evaluates direct and indirect effects.
  It produces no finding when no material effect exists.
- Lean review loads every active specialist entrypoint. Standard and deep
  review load supporting specialist references only after an entrypoint finds
  a plausible direct or indirect material effect.
- No review downloads a missing package or loads a specialist `SURVEY.md`.

## Java and PostgreSQL

The project runs a Java service backed by PostgreSQL. The plan changes only the
database schema and migration sequence.

- Both specialist entrypoints participate.
- PostgreSQL evaluates locking, migration, coexistence, and recovery.
- Java evaluates ORM mappings, serialized values, transaction assumptions,
  mixed application versions, and runtime compatibility even though no Java
  source file changes.

## Nginx and PHP

The project runs PHP behind Nginx and PHP-FPM. The plan changes only Nginx
routing, FastCGI parameters, buffering, or proxy headers.

- Both specialist entrypoints participate.
- PHP evaluates request metadata, server variables, upload behavior, streaming,
  lifecycle, and identity assumptions affected by the Nginx change.

## API contract, frontend, and backend

The plan changes an HTTP or schema contract without naming frontend or backend
implementation files.

- Installed API, schema, frontend framework, backend framework, and language
  specialists participate.
- They evaluate generated clients, runtime validation, nullability, error
  handling, compatibility, rollout order, caching, and user-visible failure.

## Security and privacy

An apparently ordinary feature changes what data is accepted, displayed,
stored, shared, retained, or deleted.

- Installed application-security and data-privacy entrypoints participate even
  when the plan has no security or privacy section.
- Supporting references load only for the trust, authorization, input, data,
  retention, vendor, or incident boundaries actually affected.

## Architecture and operations

An infrastructure or deployment change affects timing, ownership, retries,
ordering, failure isolation, or state recovery.

- Installed concurrency, distributed-system, event-driven, microservice, data
  pipeline, or other applicable paradigm entrypoints participate.
- A paradigm produces no finding when the operational change has no plausible
  material effect on its invariants.

## Missing specialist coverage

A plan introduces Kubernetes, but no Kubernetes specialist is installed.

- Report incomplete specialist coverage and identify the missing project
  boundary.
- Recommend an explicit GrumpyDev installation update.
- Do not fetch the Kubernetes package, inspect the remote catalog, or imply
  that the current review installed anything.
