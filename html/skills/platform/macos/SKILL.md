---
name: macos
description: Review macOS plans for application lifecycle, sandboxing, entitlements, privacy permissions, signing, notarization, bundles, launch services, filesystem and keychain boundaries, updates, compatibility, and crash recovery. Use when software targets macOS.
---

# macOS plan review

Apply this guidance alongside the core GrumpyDev review and the `swift` or
`objective-c`, applicable UI framework, `application-security`, and deployment
skills. Select only companions that match the plan's real boundaries. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect deployment target and architectures, app and helper bundles,
  Info.plist files, entitlements, sandbox containers, privacy strings, signing
  settings, launch registrations, keychain use, packaging, updater, and
  crash/recovery configuration.
- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.
- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: macOS deployment range, architectures, sandbox and
entitlements, signing ownership, distribution channel, update model, privacy
permissions, and supported hardware. The changed boundary must define:
Application lifecycle, sandbox, entitlements, privacy permissions, signing,
notarization, bundles, launch services, filesystem and keychain boundaries,
updates, compatibility, and crash handling.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Application lifecycle, sandbox, entitlements, privacy
permissions, signing, notarization. Prove bundles, launch services, filesystem
and keychain boundaries, updates, compatibility, crash handling through
rotation, overload, partial rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for signing, entitlements, and sandbox behavior tested
separately but not together, stale security-scoped bookmarks, privacy prompts
with no denied path, hardened-runtime differences, bundle resources with
case-sensitive failures, and updates that cannot migrate or roll back user
state.

- Match APIs, frameworks, weak linking, availability checks, deployment target,
  SDK, architecture slices, Rosetta assumptions, and hardware features to every
  supported macOS version and machine class.
- Trace application, window, helper, login item, agent, service, extension, XPC,
  and command-line lifecycle. Define state persistence and recovery for crash,
  force quit, logout, restart, update, and power loss.
- Grant the minimum sandbox and hardened-runtime entitlements. Verify
  containers, app groups, security-scoped URLs, bookmarks, helper inheritance,
  plugin needs, and behavior when access is denied or stale.
- Match privacy usage descriptions, entitlements, user consent, system settings,
  and fallback UX for files, automation, accessibility, screen capture, input
  monitoring, camera, microphone, location, contacts, and other protected
  resources.
- Protect keychain items with the intended access group, accessibility class,
  synchronization, user-presence policy, and migration behavior. Define what
  happens after reinstall, signing-team change, password change, or restored
  backup.
- Build a coherent bundle: identifiers, versions, resources, localized strings,
  document and URL types, icons, nested-code signing, frameworks, helpers,
  plugins, and launch registrations must agree.
- Define signing identity custody, hardened runtime, notarization where
  applicable, stapling, Gatekeeper/quarantine behavior, App Store or managed
  requirements, and reproducibility of every nested signature.
- Test update atomicity, running helpers, migrations, signature and entitlement
  continuity, downgrade limits, rollback, crash reporting privacy, symbol
  ownership, and recovery when an update is interrupted.

## Verify the claims

- Test the oldest and newest supported macOS releases and all supported
  native/Rosetta architecture paths on representative hardware.
- Exercise sandbox and privacy permissions in grant, deny, revoke,
  stale-bookmark, moved-file, and restored-machine states.
- Inspect the final bundle, nested code, signatures, designated requirements,
  entitlements, privacy strings, architecture slices, and minimum OS.
- Run clean install, first launch, update, interrupted update, rollback,
  quarantine/Gatekeeper, crash, restart, and uninstall tests.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: macOS deployment
range, architectures, sandbox and entitlements, signing ownership, distribution
channel, update model, privacy permissions, and supported hardware. For the
changed boundary, ask only about unresolved Application lifecycle, sandbox,
entitlements, privacy permissions, signing, notarization, bundles, launch
services, filesystem and keychain boundaries, updates, compatibility, and crash
handling when the answer can change the verdict or implementation.

## Calibrate findings

- Treat signature or entitlement failure that prevents launch, privacy-boundary
  bypass, destructive update, credential exposure, or loss of user documents as
  critical or high according to blast radius and realistic likelihood.
- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the plan depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
application lifecycle, sandbox, entitlements, privacy permissions, signing,
notarization, bundles, launch services, filesystem and keychain boundaries,
updates, compatibility, and crash handling, verification evidence, deployment
and recovery limits, and any material assumption that remains unresolved.
