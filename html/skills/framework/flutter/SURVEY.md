# Flutter survey contribution

## Applicability

Apply this contribution when a Dart plan changes Flutter applications, widgets,
routes, state management, or native integration. Skip it when Flutter does not
constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Flutter, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Flutter and Dart versions, target platforms and
  minimum versions, state and navigation libraries, build flavors, plugin set,
  signing boundary, and distribution channels.
- Review doctrine for: Widget and element lifecycle, state ownership, async
  context, navigation, isolates, plugins, platform channels, rendering,
  accessibility, persistence, and release modes.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Mobile, desktop, web, or embedded targets; OS
  versions; architectures; platform services; signing; packaging; updates;
  storage; and backend connectivity.

## Ask only when materially unresolved

- Which Flutter and Dart versions, target platforms, rendering constraints, and
  state approach apply?
- How are widget lifetime, navigation, async cancellation, offline state,
  accessibility, and platform channels handled?
- Align existing domain questions with this deployment guidance when it is
  material: Mobile, desktop, web, or embedded targets; OS versions;
  architectures; platform services; signing; packaging; updates; storage; and
  backend connectivity. Do not repeat the core profile confirmation.

## Record in .grump

Record Flutter answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Flutter survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Flutter
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Flutter when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
