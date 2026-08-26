# Windows Forms survey contribution

## Applicability

Apply this contribution when the project uses Windows Forms or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the `csharp`, `windows`, `application-security`, and
`testing-strategy` skills. Deduplicate shared version, runtime, architecture,
identity, data, security, and deployment questions.

## Inspect before asking

Inspect target frameworks, forms and controls, designer files, event wiring,
data bindings, synchronization contexts, resources, manifests, DPI settings,
native interop, installers, and update configuration, dependency declarations,
build and deployment files, CI workflows, runbooks, and project documentation.
Distinguish a committed project fact from a local-machine default or a transient
environment value. Do not access or mutate an external system merely to complete
setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- .NET and Windows Forms versions.
- Windows targets and architecture.
- DPI and localization targets.
- Packaging and deployment.
- Native interoperability.
- Application identity and support constraints.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: Windows and .NET versions, architecture, desktop
  session, native interop, DPI, installer, signing, update, configuration, file
  access, and support channel.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Windows Forms reviews. Candidate subjects are: .NET and
WinForms versions, Windows targets, architecture, DPI and localization targets,
packaging, deployment, native interop, and support constraints.
- Align existing domain questions with this deployment guidance when it is
  material: Windows and .NET versions, architecture, desktop session, native
  interop, DPI, installer, signing, update, configuration, file access, and
  support channel. Do not repeat the core profile confirmation.

## Record in .grump

Record Windows Forms answers in project technology, architecture, runtime,
security, deployment, and verification doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing Windows Forms survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual UI objects, temporary feature settings, one-off migrations, and
plan-only implementation choices out of durable Windows Forms doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a .NET or WinForms target change, Windows minimum or
architecture change, DPI policy change, new native interop, packaging or updater
change, or accessibility-target change. Also refresh the contribution when
evidence contradicts saved doctrine or the user explicitly requests a context
refresh.
