# WinUI 3 survey contribution

## Applicability

Apply this contribution when the project uses WinUI 3 or when its behavior constrains a
supported build, deployment, client, or operating environment. Combine it with the
`csharp` or `cpp`, `windows`, `application-security`, and `testing-strategy` skills.
Deduplicate shared version, runtime, architecture, identity, data, security, and
deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect Windows App SDK and target settings, XAML, view models, bindings,
activation registration, windows, dispatch queues, resources, manifests,
identity, packaging, bootstrapper, and deployment output, dependency
declarations, build and deployment files, CI workflows, runbooks, and project
documentation. Distinguish a committed project fact from a local-machine default
or a transient environment value. Do not access or mutate an external system
merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Windows App SDK and WinUI versions.
- C# or C++ implementation.
- Minimum Windows versions.
- Packaged, externally located, or unpackaged deployment.
- Architectures.
- Application lifecycle and activation.
- Package identity.
- Distribution and update model.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: Windows App SDK, packaged or unpackaged
  identity, Windows versions, architecture, activation, app services,
  permissions, signing, installer or Store, and updates.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later WinUI 3 reviews. Candidate subjects are: Windows App SDK and
WinUI versions, C# or C++, Windows minimums, packaged or unpackaged deployment,
architectures, app lifecycle, identity, and distribution.
- Align existing domain questions with this deployment guidance when it is
  material: Windows App SDK, packaged or unpackaged identity, Windows versions,
  architecture, activation, app services, permissions, signing, installer or
  Store, and updates. Do not repeat the core profile confirmation.

## Record in .grump

Record WinUI 3 answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing WinUI 3 survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual UI objects, temporary feature settings, one-off migrations, and
plan-only implementation choices out of durable WinUI 3 doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a Windows App SDK or minimum-Windows change, language or
architecture change, packaging/identity change, activation model change,
lifecycle redesign, or distribution change. Also refresh the contribution when
evidence contradicts saved doctrine or the user explicitly requests a context
refresh.
