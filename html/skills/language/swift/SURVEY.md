# Swift survey contribution

## Applicability

Apply this contribution when a plan changes Swift applications, packages,
services, or Apple-platform code. Skip it when Swift does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Swift, inspect language and runtime declarations, dependency locks, build
files, compiler or interpreter flags, generated-code settings, CI matrices,
native dependencies, packaging, and deployment documentation. Read existing
`.grump` doctrine and project documentation before treating a durable fact as
unresolved.

## Durable project facts

- Target and operating model: Swift and toolchain versions, Apple or server
  targets, deployment versions, strict concurrency mode, package manager,
  architectures, interop boundaries, and distribution form.
- Review doctrine for: Swift version semantics, ownership and value behavior,
  optionals, errors, structured concurrency, actors and isolation, Sendable,
  ABI, packages, Objective-C and C interop, and platform lifecycle.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Apple OS versions, architectures, runtime
  availability, app or server process, concurrency runtime, sandbox,
  entitlements, signing, packaging, and distribution.

## Ask only when materially unresolved

- Which Swift language, compiler, OS, deployment target, package, and
  concurrency versions apply?
- How do actors, tasks, cancellation, sendability, ownership, errors, and
  Objective-C interop cross the boundary?
- Align existing domain questions with this deployment guidance when it is
  material: Apple OS versions, architectures, runtime availability, app or
  server process, concurrency runtime, sandbox, entitlements, signing,
  packaging, and distribution. Do not repeat the core profile confirmation.

## Record in .grump

Record Swift answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Map existing Swift survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Swift doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Swift when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
