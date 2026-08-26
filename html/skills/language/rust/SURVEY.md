# Rust survey contribution

## Applicability

Apply this contribution when a plan changes Rust services, libraries,
command-line tools, embedded code, or native interfaces. Skip it when Rust does
not constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Rust, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Rust edition, MSRV and toolchain channel, targets,
  async runtime, feature sets, panic strategy, unsafe policy, FFI and native
  dependencies, allocator, and no_std use.
- Review doctrine for: Ownership and lifetime boundaries, unsafe code, pinning,
  async runtimes, Send and Sync, atomics, panic behavior, feature flags, MSRV,
  FFI, allocators, no_std, and cross-compilation.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Rust target triple, libc or static linkage,
  architecture, feature set, native libraries, service or embedded process,
  packaging, and FFI runtime boundary.

## Ask only when materially unresolved

- Which Rust edition, minimum supported Rust version, Cargo version, target
  toolchain, and feature set apply?
- Where do unsafe code, FFI, pinning, async cancellation, shared state, and
  resource lifetime cross the boundary?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Rust target triple, libc or static
  linkage, architecture, feature set, native libraries, service or embedded
  process, packaging, and FFI runtime boundary? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record Rust answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed Rust deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Rust doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Rust when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
