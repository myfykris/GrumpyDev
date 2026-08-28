# macOS survey contribution

## Applicability

Apply this contribution when the project uses macOS or when its behavior constrains a
supported build, deployment, client, or operating environment. Combine it with the
`swift` or `objective-c`, applicable UI framework, `application-security`, and
deployment skills. Deduplicate shared version, runtime, architecture, identity, data,
security, and deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect deployment target and architectures, app and helper bundles, Info.plist
files, entitlements, sandbox containers, privacy strings, signing settings,
launch registrations, keychain use, packaging, updater, and crash/recovery
configuration, dependency declarations, build and deployment files, CI
workflows, runbooks, and project documentation. Distinguish a committed project
fact from a local-machine default or a transient environment value. Do not
access or mutate an external system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- MacOS deployment range and supported hardware.
- Architectures.
- Sandbox and entitlements.
- Signing ownership.
- App Store, Developer ID, managed, or internal distribution.
- Update model.
- Privacy permissions.
- Application and helper topology.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: OS range, architecture, app model,
  sandbox, entitlements, privacy permissions, signing, notarization, packaging,
  updates, filesystem, and recovery.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later macOS reviews. Candidate subjects are: macOS deployment range,
architectures, sandbox and entitlements, signing ownership, distribution
channel, update model, privacy permissions, and supported hardware.
- Align existing domain questions with this deployment guidance when it is
  material: OS range, architecture, app model, sandbox, entitlements,
  privacy permissions, signing, notarization, packaging, updates, filesystem,
  and recovery. Do not repeat the core profile confirmation.

## Record in .grump

Record macOS answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing macOS survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable macOS
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a minimum macOS or architecture change,
sandbox/entitlement/privacy change, helper or extension redesign, signing-team
or distribution change, keychain model change, or updater redesign. Also refresh
the contribution when evidence contradicts saved doctrine or the user explicitly
requests a context refresh.
