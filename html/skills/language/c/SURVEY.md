# C survey contribution

## Applicability

Apply this contribution when a plan changes C libraries, services, embedded
code, system utilities, or foreign-function interfaces. Skip it when C does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For C, inspect language and runtime declarations, dependency locks, build files,
compiler or interpreter flags, generated-code settings, CI matrices, native
dependencies, packaging, and deployment documentation. Read existing `.grump`
doctrine and project documentation before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: C standard and extensions, compilers and versions,
  targets and architectures, ABI and libc, build profiles, required warnings,
  sanitizers, and supported operating systems.
- Review doctrine for: Language standard, compiler behavior, undefined behavior,
  object lifetime, memory ownership, integer rules, ABI, linkage, FFI,
  concurrency, signals, build flags, sanitizers, and platform portability.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Target OS, architecture, ABI, libc, compiler,
  dynamic libraries, privilege, packaging, and process or embedded environment.

## Ask only when materially unresolved

- Which C standard, compiler, target ABI, operating system, and build flags
  define the program?
- Who owns each allocation, buffer, file descriptor, thread, and error path
  across the changed boundary?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Target OS, architecture, ABI, libc,
  compiler, dynamic libraries, privilege, packaging, and process or embedded
  environment? Ask only when evidence and the core profile confirmation do not
  resolve them.

## Record in .grump

Record C answers in project technology, runtime, build, compatibility, and
deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Record confirmed C deployment facts on the affected `DEP-###` profile. Use a
referenced `INF-###` entry for a material component shared by several profiles.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable C doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey C when supported language or runtime versions, compiler, standard
library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
