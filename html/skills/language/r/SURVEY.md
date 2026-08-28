# R survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with R code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For R, inspect language and runtime declarations, dependency locks, build files,
compiler or interpreter flags, generated-code settings, CI matrices, native
dependencies, packaging, and deployment documentation. Read existing `.grump`
doctrine and project documentation before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: R version and distribution, package snapshot or
  lock approach, operating systems, BLAS and native libraries, locale and
  encoding, execution environment, and data-volume expectations.
- Review doctrine for: Vectorization and recycling, missing values, type
  coercion, environments, lazy evaluation, package resolution, reproducibility,
  native libraries, numerical behavior, parallelism, and data size.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: R version, package snapshot, native libraries,
  batch or interactive runtime, scheduler, worker topology, memory limits,
  compute platform, and reproducibility environment.

## Ask only when materially unresolved

- Which R version, package snapshot, operating system, locale, and data-size
  assumptions apply?
- How are missing values, factors, copy behavior, randomness, encoding, and
  statistical assumptions validated?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: R version, package snapshot, native
  libraries, batch or interactive runtime, scheduler, worker topology, memory
  limits, compute platform, and reproducibility environment? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record R answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed R deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable R doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey R when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
