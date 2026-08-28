# Shell survey contribution

## Applicability

Apply this contribution when the project contains or executes POSIX shell or Bash
scripts, build steps, deployment scripts, or operational automation.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Shell, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Shells and versions, operating systems, required
  utilities, POSIX requirement, locale and encoding, privilege context,
  scheduler or CI host, and supported execution environments.
- Review doctrine for: Shell dialects, expansion, quoting, globbing, pipelines,
  exit status, traps, signals, subprocesses, portability, temporary files,
  concurrency, encoding, and destructive boundaries.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Exact shell and utilities, OS or container image,
  locale and encoding, user and privileges, non-interactive environment,
  filesystem, service manager, and scheduler.

## Ask only when materially unresolved

- Which shell implementations, operating systems, utilities, locales, and
  privilege contexts must the script support?
- How do quoting, word splitting, globbing, pipelines, temporary files, signals,
  errors, and encoding cross boundaries?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Exact shell and utilities, OS or
  container image, locale and encoding, user and privileges, non-interactive
  environment, filesystem, service manager, and scheduler? Ask only when
  evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record Shell answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Shell deployment facts on the affected `DEP-###` profile. Use
a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Shell doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Shell when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
