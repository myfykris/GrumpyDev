# GTK survey contribution

## Applicability

Apply this contribution when the project uses GTK or when its behavior constrains a
supported build, deployment, client, or operating environment. Combine it with the
applicable language, `linux`, `application-security`, and `testing-strategy` skills.
Deduplicate shared version, runtime, architecture, identity, data, security, and
deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect GTK and GLib versions, UI definitions, GObject types, ownership
annotations, widget trees, signal connections, list models, actions, resources,
CSS, main-context use, and packaging metadata, dependency declarations, build
and deployment files, CI workflows, runbooks, and project documentation.
Distinguish a committed project fact from a local-machine default or a transient
environment value. Do not access or mutate an external system merely to complete
setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- GTK and GLib versions.
- Language binding and ownership conventions.
- Desktop and display backends.
- Packaging and distribution.
- Theme and accessibility requirements.
- Supported Linux distributions and architectures.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: GTK and GLib versions, display backend, desktop
  and distribution targets, sandbox or portal use, packaging, native
  dependencies, accessibility, and update channel.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later GTK reviews. Candidate subjects are: GTK version, language
binding, GLib version, desktop targets, display backends, packaging, theme and
accessibility requirements, and supported distributions.
- Align existing domain questions with this deployment guidance when it is
  material: GTK and GLib versions, display backend, desktop and distribution
  targets, sandbox or portal use, packaging, native dependencies,
  accessibility, and update channel. Do not repeat the core profile
  confirmation.

## Record in .grump

Record GTK answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing GTK survey answers to the affected `DEP-###` profile. Reference a
shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual UI objects, temporary feature settings, one-off migrations, and
plan-only implementation choices out of durable GTK doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a GTK or GLib major-version change, language-binding change, GTK
3 to 4 migration, display-backend change, packaging-format change, or
accessibility-target change. Also refresh the contribution when evidence
contradicts saved doctrine or the user explicitly requests a context refresh.
