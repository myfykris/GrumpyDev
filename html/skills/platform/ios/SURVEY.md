# iOS and iPadOS survey contribution

## Applicability

Apply this contribution when software targets Apple mobile devices. Skip it when iOS and
iPadOS do not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for iOS and iPadOS. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Minimum iOS and iPadOS versions, devices and form factors, Xcode
  and SDK, UI framework, scene and process model, entitlements, privacy permissions, storage and
  backup policy, background modes, bundle identifiers, signing, and release channels.
- Review doctrine: The operating system may suspend or terminate the process at any time. The
  plan must distinguish restorable UI state, durable local data, protected credentials, server
  authority, and resumable background work.
- Deployment-profile facts: OS and device matrix, Xcode and SDK versions, bundle IDs,
  build configurations, entitlements, privacy manifest, data protection, background modes,
  signing and provisioning, extensions, and release tracks.

## Ask only when materially unresolved

- Which Apple mobile OS versions, devices, UI framework, lifecycle, permissions, entitlements,
  and storage apply?
- How are background work, restoration, accessibility, signing, privacy manifests, upgrades,
  rollback, and review handled?

## Record in .grump

Record confirmed iOS and iPadOS answers as project technology, architecture, security,
deployment, verification, and operational doctrine. Preserve source, scope, confidence, and
environment differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable iOS and iPadOS doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey iOS and iPadOS when the supported OS or device classes, entitlement or
permission set, application lifecycle, background modes, data-protection policy,
signing identity, or distribution channel materially changes. Also re-survey when
evidence conflicts with saved doctrine or the user requests a context refresh.
