# PowerShell survey contribution

## Applicability

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with PowerShell code, artifacts, or runtime behavior.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For PowerShell, inspect language and runtime declarations, dependency locks,
build files, compiler or interpreter flags, generated-code settings, CI
matrices, native dependencies, packaging, and deployment documentation. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: PowerShell editions and versions, operating
  systems, remoting transport, required modules, execution policy, native tools,
  host process, encoding, and automation environment.
- Review doctrine for: Edition and version differences, object pipelines,
  streams, errors, remoting, serialization, modules, scopes, providers, quoting,
  native-process boundaries, encoding, and execution policy.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: PowerShell edition and version, operating system,
  host process, remoting method, execution identity, modules, policy,
  non-interactive service context, and serialization boundary.

## Ask only when materially unresolved

- Which PowerShell edition and version, operating systems, remoting mode,
  execution policy, and module versions apply?
- How do object and text pipelines, quoting, native processes, credentials,
  errors, and encoding cross boundaries?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: PowerShell edition and version,
  operating system, host process, remoting method, execution identity, modules,
  policy, non-interactive service context, and serialization boundary? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record PowerShell answers in project technology, runtime, build, compatibility,
and deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed PowerShell deployment facts on the affected `DEP-###` profile.
Use a referenced `INF-###` entry for a material component shared by several
profiles. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable PowerShell doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey PowerShell when supported language or runtime versions, compiler,
standard library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
