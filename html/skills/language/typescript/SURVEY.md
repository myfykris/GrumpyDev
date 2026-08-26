# TypeScript survey contribution

## Applicability

Apply this contribution when a plan changes TypeScript services, libraries,
tools, or browser applications. Skip it when TypeScript does not constrain a
supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For TypeScript, inspect language and runtime declarations, dependency locks,
build files, compiler or interpreter flags, generated-code settings, CI
matrices, native dependencies, packaging, and deployment documentation. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: TypeScript version, runtime targets, module system
  and resolution, strictness flags, emit owner, bundler, package manager,
  declaration consumers, and generated-code sources.
- Review doctrine for: Erased types, compiler options, narrowing, structural
  typing, declaration accuracy, module resolution, emit modes, runtime
  validation, decorators, generated types, build graph, and JS interoperability.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Runtime after compilation, compiler and module
  mode, bundler, browser or server targets, generated output, environment
  injection, source maps, and deployment artifact.

## Ask only when materially unresolved

- Which TypeScript version, tsconfig strictness, module mode, runtime, and
  generated-type sources apply?
- Where do untyped inputs, assertions, narrowing, serialization, async work, and
  JavaScript consumers cross the boundary?
- Align existing domain questions with this deployment guidance when it is
  material: Runtime after compilation, compiler and module mode, bundler,
  browser or server targets, generated output, environment injection, source
  maps, and deployment artifact. Do not repeat the core profile confirmation.

## Record in .grump

Record TypeScript answers in project technology, runtime, build, compatibility,
and deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Map existing TypeScript survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable TypeScript doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey TypeScript when supported language or runtime versions, compiler,
standard library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
