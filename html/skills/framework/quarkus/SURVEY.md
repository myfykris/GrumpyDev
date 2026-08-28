# Quarkus survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Quarkus.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Quarkus, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Quarkus and Java versions, JVM or native mode,
  extensions, reactive stack, build tool, configuration sources, container
  platform, and database drivers.
- Review doctrine for: CDI scopes, build-time augmentation, reactive and
  imperative boundaries, transactions, configuration, native image, extensions,
  dev services, startup, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: JVM versus native image, build-time versus
  runtime configuration, container limits, HTTP or reactive worker model,
  generated resources, packaging, and startup or shutdown.

## Ask only when materially unresolved

- Which Java, Quarkus, build mode, native-image toolchain, extension, and
  deployment versions apply?
- How do dependency injection scopes, reactive and blocking work, configuration,
  transactions, and startup differ by mode?
- Align existing domain questions with this deployment guidance when it is
  material: JVM versus native image, build-time versus runtime configuration,
  container limits, HTTP or reactive worker model, generated resources,
  packaging, and startup or shutdown. Do not repeat the core profile
  confirmation.

## Record in .grump

Record Quarkus answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Quarkus survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Quarkus
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Quarkus when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
