# Objective-C survey contribution

## Applicability

Apply this contribution when the project uses Objective-C or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the `c`, `cpp`, `swift`, `macos`, and applicable Apple UI
framework skills. Deduplicate shared version, runtime, architecture, identity,
data, security, and deployment questions.

## Inspect before asking

Inspect compiler and target settings, headers, module maps, ownership
annotations, bridging headers, categories, blocks, observers, native boundaries,
and build products, dependency declarations, build and deployment files, CI
workflows, runbooks, and project documentation. Distinguish a committed project
fact from a local-machine default or a transient environment value. Do not
access or mutate an external system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Compiler and language mode.
- ARC policy and manual-ownership islands.
- Target macOS versions.
- Apple and third-party frameworks.
- Swift bridging and module boundaries.
- Objective-C++ use.
- Architectures and ABI.
- Deployment form.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: macOS or iOS targets, architectures, runtime and
  framework versions, app or helper process, sandbox, entitlements, signing,
  packaging, and Swift or C++ interop.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Objective-C reviews. Candidate subjects are: Compiler and
language mode, ARC policy, target macOS versions, frameworks, Swift bridging,
Objective-C++ use, architectures, and deployment form.
- Align existing domain questions with this deployment guidance when it is
  material: macOS or iOS targets, architectures, runtime and framework
  versions, app or helper process, sandbox, entitlements, signing, packaging,
  and Swift or C++ interop. Do not repeat the core profile confirmation.

## Record in .grump

Record Objective-C answers in project technology, runtime, build, compatibility,
and deployment doctrine. Preserve source and scope. Record a material unknown as
unresolved doctrine instead of guessing.

Map existing Objective-C survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable Objective-C doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a compiler or language-mode change, ARC-policy change, new
Objective-C++ or Swift bridge, architecture change, framework or minimum-OS
change, or deployment-form change. Also refresh the contribution when evidence
contradicts saved doctrine or the user explicitly requests a context refresh.
