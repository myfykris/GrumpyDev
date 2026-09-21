---
name: gd-macos
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review macOS engineering work for application lifecycle, sandboxing, entitlements, privacy permissions, signing, notarization, bundles, launch services, filesystem and keychain boundaries, updates, compatibility, and crash recovery."
---

# macOS GrumpyDev review

## Quick checks

- Inspect deployment target and architectures, app and helper bundles,
  Info.plist files, entitlements, sandbox containers, privacy strings, signing
  settings, launch registrations, keychain use, packaging, updater, and
  crash/recovery configuration.

Watch especially for signing, entitlements, and sandbox behavior tested
separately but not together, stale security-scoped bookmarks, privacy prompts
with no denied path, hardened-runtime differences, bundle resources with
case-sensitive failures, and updates that cannot migrate or roll back user
state.

- Inspect signature or entitlement failure that prevents launch, privacy-boundary
  bypass, destructive update, credential exposure, or loss of user documents.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the macOS specialist.

- [Focused rules](references/sandbox-privacy-and-keychain.md):
  Read when the work changes sandboxing,
  hardened-runtime entitlements, privacy
  permissions, user consent, app groups, security-scoped URLs, bookmarks, helpers,
  plugins, keychain groups, keychain accessibility, user presence, or credential
  migration.
- [Focused rules](references/signing-notarization-updates-and-recovery.md):
  Read when the work changes bundles, nested code,
  identifiers, resources, document or
  URL types, architectures, signing identity, notarization, stapling, Gatekeeper, App
  Store or managed distribution, updates, rollback, crash reporting, symbols, uninstall,
  or recovery.

## Verdict context

State the application lifecycle, sandbox, entitlements, privacy permissions,
signing, notarization, bundles, launch services, filesystem and keychain
boundaries, updates, compatibility, and crash handling, supporting evidence,
deployment or recovery limits, and unresolved material assumptions.
