# C++ survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with C++ code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For C++, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: C++ standard, compiler and standard-library
  versions, ABI targets, exception and RTTI policy, architectures, build system,
  dependency manager, sanitizers, and deployment platforms.
- Review doctrine for: C++ standard, value and object lifetime, ownership,
  exceptions, RTTI, templates, ODR, ABI, allocators, concurrency, atomics,
  modules, native dependencies, and toolchain compatibility.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Compiler and standard library, ABI, architecture,
  runtime linkage, allocator, plugin boundary, packaging, and supported
  operating targets.

## Ask only when materially unresolved

- Which C++ standard, compiler, standard library, target ABI, and exception or
  RTTI settings apply?
- Who owns each object and resource across move, exception, concurrency, and
  binary boundaries?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Compiler and standard library, ABI,
  architecture, runtime linkage, allocator, plugin boundary, packaging, and
  supported operating targets? Ask only when evidence and the core profile
  confirmation do not resolve them.

## Record in .grump

Record C++ answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed C++ deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable C++ doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey C++ when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
