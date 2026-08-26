# SwiftUI survey contribution

## Applicability

Apply this contribution when a Swift plan changes SwiftUI views, models,
navigation, data flow, or app structure. Skip it when SwiftUI does not constrain
a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For SwiftUI, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Swift and Xcode versions, target platforms and
  minimum OS versions, observation and navigation model, concurrency mode,
  persistence, and distribution targets.
- Review doctrine for: View identity, state wrappers, observation, rendering,
  navigation, tasks, actors, persistence, platform lifecycle, accessibility,
  previews, and OS availability.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Apple OS range, architectures, app lifecycle,
  sandbox, entitlements, state restoration, helpers, signing, packaging,
  update, and distribution.

## Ask only when materially unresolved

- Which Swift, SwiftUI, OS versions, device classes, and concurrency model
  apply?
- Who owns observable state, navigation, task cancellation, persistence,
  accessibility, and scene restoration?
- Align existing domain questions with this deployment guidance when it is
  material: Apple OS range, architectures, app lifecycle, sandbox,
  entitlements, state restoration, helpers, signing, packaging, update, and
  distribution. Do not repeat the core profile confirmation.

## Record in .grump

Record SwiftUI answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing SwiftUI survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable SwiftUI
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey SwiftUI when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
