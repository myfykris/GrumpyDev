---
name: macos
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review macOS plans and other engineering artifacts for application lifecycle, sandboxing, entitlements, privacy permissions, signing, notarization, bundles, launch services, filesystem and keychain boundaries, updates, compatibility, and crash recovery. Project applicability: software targets macOS."
---

# macOS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `swift` or
`objective-c`, applicable UI framework, `application-security`, and deployment
skills. Every installed companion that remains applicable to the project
participates; the reviewed target does not select the roster. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

## Lean review

- Inspect deployment target and architectures, app and helper bundles,
  Info.plist files, entitlements, sandbox containers, privacy strings, signing
  settings, launch registrations, keychain use, packaging, updater, and
  crash/recovery configuration.

- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.

Watch especially for signing, entitlements, and sandbox behavior tested
separately but not together, stale security-scoped bookmarks, privacy prompts
with no denied path, hardened-runtime differences, bundle resources with
case-sensitive failures, and updates that cannot migrate or roll back user
state.

Lean mode is insufficient when this material severity condition may apply:

- Treat signature or entitlement failure that prevents launch, privacy-boundary
  bypass, destructive update, credential exposure, or loss of user documents as
  critical or high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/sandbox-privacy-and-keychain.md):
  Read when the reviewed work directly or indirectly changes sandboxing,
  hardened-runtime entitlements, privacy
  permissions, user consent, app groups, security-scoped URLs, bookmarks, helpers,
  plugins, keychain groups, keychain accessibility, user presence, or credential
  migration.
- [Focused rules](references/signing-notarization-updates-and-recovery.md):
  Read when the reviewed work directly or indirectly changes bundles, nested code,
  identifiers, resources, document or
  URL types, architectures, signing identity, notarization, stapling, Gatekeeper, App
  Store or managed distribution, updates, rollback, crash reporting, symbols, uninstall,
  or recovery.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
application lifecycle, sandbox, entitlements, privacy permissions, signing,
notarization, bundles, launch services, filesystem and keychain boundaries,
updates, compatibility, and crash handling, verification evidence, deployment
and recovery limits, and any material assumption that remains unresolved.
