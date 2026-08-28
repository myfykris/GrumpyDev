# AppKit survey contribution

## Applicability

Apply this contribution when the project uses AppKit or when its behavior constrains a
supported build, deployment, client, or operating environment. Combine it with the
`swift`, `objective-c`, `macos`, `application-security`, and `testing-strategy` skills.
Deduplicate shared version, runtime, architecture, identity, data, security, and
deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect application delegates, scene or window controllers, responders, menus,
bindings, document controllers, view code, drawing layers, concurrency
boundaries, entitlements, and distribution settings, dependency declarations,
build and deployment files, CI workflows, runbooks, and project documentation.
Distinguish a committed project fact from a local-machine default or a transient
environment value. Do not access or mutate an external system merely to complete
setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- AppKit and macOS deployment targets.
- Swift or Objective-C use.
- Application and window lifecycle.
- Document model.
- Sandbox and entitlements.
- Persistence and restoration.
- Accessibility targets.
- Distribution channel.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: macOS range, architectures, sandbox,
  entitlements, helpers, document and file access, signing, notarization,
  packaging, update, and distribution.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later AppKit reviews. Candidate subjects are: AppKit and macOS
deployment targets, Swift or Objective-C use, lifecycle model, document model,
sandbox and entitlements, persistence, accessibility targets, and distribution.
- Align existing domain questions with this deployment guidance when it is
  material: macOS range, architectures, sandbox, entitlements, helpers,
  document and file access, signing, notarization, packaging, update, and
  distribution. Do not repeat the core profile confirmation.

## Record in .grump

Record AppKit answers in project technology, architecture, runtime, security,
deployment, and verification doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing AppKit survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep individual UI objects, temporary feature settings, one-off migrations, and
plan-only implementation choices out of durable AppKit doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a minimum macOS or AppKit target change, Swift/Objective-C
boundary change, lifecycle or document-model redesign, sandbox or entitlement
change, SwiftUI adoption, or distribution change. Also refresh the contribution
when evidence contradicts saved doctrine or the user explicitly requests a
context refresh.
