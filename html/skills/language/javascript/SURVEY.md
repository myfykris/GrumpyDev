# JavaScript survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with JavaScript code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For JavaScript, inspect language and runtime declarations, dependency locks,
build files, compiler or interpreter flags, generated-code settings, CI
matrices, native dependencies, packaging, and deployment documentation. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: Node, browser, edge, or embedded runtimes and
  versions, module system, package manager, bundler, transpilation targets,
  worker model, and supported client matrix.
- Review doctrine for: ECMAScript semantics, event loops, promises,
  cancellation, modules, package resolution, runtime globals, serialization,
  prototype and injection hazards, workers, memory, and build output.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Browser, Node.js, edge, worker, embedded, or
  build-only execution; supported engines; event-loop ownership; bundling;
  environment injection; and deployment artifact.

## Ask only when materially unresolved

- Which ECMAScript, Node.js or browser versions, module mode, package
  resolution, and runtime globals apply?
- How do promises, cancellation, event-loop work, coercion, serialization, and
  untrusted input cross the boundary?
- Align existing domain questions with this deployment guidance when it is
  material: Browser, Node.js, edge, worker, embedded, or build-only execution;
  supported engines; event-loop ownership; bundling; environment injection; and
  deployment artifact. Do not repeat the core profile confirmation.

## Record in .grump

Record JavaScript answers in project technology, runtime, build, compatibility,
and deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Map existing JavaScript survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable JavaScript doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey JavaScript when supported language or runtime versions, compiler,
standard library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
