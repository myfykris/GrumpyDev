# Blazor survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Blazor.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Blazor, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: .NET and Blazor versions, render modes by route,
  hosting and proxy, browser targets, authentication, trimming and AOT, CDN
  prohibition or asset policy, and offline needs.
- Review doctrine for: Server, WebAssembly, auto and hybrid modes, circuit
  lifecycle, prerendering, hydration, state persistence, JS interop,
  authentication, payloads, and deployment.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Server, WebAssembly, hybrid, and prerender
  modes; circuit topology; sticky sessions; client assets; data-protection
  state; proxy; and deployment differences.

## Ask only when materially unresolved

- Which .NET and Blazor versions and hosting mode, rendering mode, and
  deployment target apply?
- How are circuit lifetime, reconnection, state, authorization, prerendering,
  errors, and browser interop handled?
- Align existing domain questions with this deployment guidance when it is
  material: Server, WebAssembly, hybrid, and prerender modes; circuit topology;
  sticky sessions; client assets; data-protection state; proxy; and deployment
  differences. Do not repeat the core profile confirmation.

## Record in .grump

Record Blazor answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Blazor survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Blazor doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Blazor when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
