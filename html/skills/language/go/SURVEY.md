# Go survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Go code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Go, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Go and toolchain targets, module mode, OS and
  architecture matrix, CGO policy, build tags, race testing, proxy or
  private-module setup, and deployment form.
- Review doctrine for: Go version semantics, module and toolchain rules,
  interfaces, nil behavior, error contracts, goroutine lifetime, contexts,
  channels, memory model, races, CGO, build tags, and cross-compilation.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Go version, OS and architecture matrix, CGO and
  libc, build tags, static or dynamic linkage, container or host process,
  signals, and executable packaging.

## Ask only when materially unresolved

- Which Go language version in go.mod, toolchain version, target, build tags,
  and module graph apply?
- Who owns each goroutine, channel, context, timer, and shared value, including
  the exact loop form for captures?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Go version, OS and architecture matrix,
  CGO and libc, build tags, static or dynamic linkage, container or host
  process, signals, and executable packaging? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Go answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Go deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Go doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Go when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
