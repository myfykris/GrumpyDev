# WPF survey contribution

## Applicability

Apply this contribution when the project uses WPF or when its behavior constrains a
supported build, deployment, client, or operating environment. Combine it with the
`csharp`, `windows`, `application-security`, and `testing-strategy` skills. Deduplicate
shared version, runtime, architecture, identity, data, security, and deployment
questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect target frameworks, XAML, dependency properties, bindings, resources,
styles, templates, commands, dispatchers, windows, native interop, manifests,
packaging, and deployment configuration, dependency declarations, build and
deployment files, CI workflows, runbooks, and project documentation. Distinguish
a committed project fact from a local-machine default or a transient environment
value. Do not access or mutate an external system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- .NET and WPF versions.
- Windows targets and architecture.
- Packaging and deployment.
- DPI and localization targets.
- Native interoperability.
- Application lifecycle and distribution.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: Windows and .NET versions, architecture, desktop
  session, native interop, rendering mode, installer, signing, configuration,
  update, and file access.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later WPF reviews. Candidate subjects are: .NET and WPF versions,
Windows targets, architecture, packaging, deployment, DPI and localization
targets, interop, and application lifecycle.
- Align existing domain questions with this deployment guidance when it is
  material: Windows and .NET versions, architecture, desktop session, native
  interop, rendering mode, installer, signing, configuration, update, and file
  access. Do not repeat the core profile confirmation.

## Record in .grump

Record WPF answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing WPF survey answers to the affected `DEP-###` profile. Reference a
shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual UI objects, temporary feature settings, one-off migrations, and
plan-only implementation choices out of durable WPF doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a .NET or WPF target change, minimum Windows/architecture
change, UI architecture or resource-system change, native interop change,
packaging/updater change, or accessibility-target change. Also refresh the
contribution when evidence contradicts saved doctrine or the user explicitly
requests a context refresh.
