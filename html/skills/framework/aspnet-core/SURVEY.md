# ASP.NET Core survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on ASP.NET Core.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For ASP.NET Core, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: .NET and ASP.NET Core versions, hosting model,
  reverse proxy, authentication scheme, data providers, deployment mode,
  trimming or AOT, and worker services.
- Review doctrine for: Middleware ordering, DI lifetimes, async and
  cancellation, model binding, authentication and authorization, configuration,
  EF boundaries, hosted services, Kestrel, and graceful shutdown.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: .NET and hosting model, Kestrel, IIS or reverse
  proxy, in-process or out-of-process mode, worker count, forwarded headers,
  data protection, filesystem, deployment, and drain.

## Ask only when materially unresolved

- Which .NET, C#, ASP.NET Core, hosting, server, and deployment versions or
  modes apply?
- How are middleware order, dependency lifetimes, authentication, cancellation,
  errors, and shutdown handled?
- Align existing domain questions with this deployment guidance when it is
  material: .NET and hosting model, Kestrel, IIS or reverse proxy, in-process
  or out-of-process mode, worker count, forwarded headers, data protection,
  filesystem, deployment, and drain. Do not repeat the core profile
  confirmation.

## Record in .grump

Record ASP.NET Core answers in project technology, architecture, runtime,
security, deployment, and verification doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing ASP.NET Core survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable ASP.NET Core
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey ASP.NET Core when framework or runtime versions, lifecycle or
rendering model, dependency scopes, persistence, authentication, workers,
supported clients, or deployment process materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
