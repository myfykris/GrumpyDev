# macOS signing, notarization, updates, and recovery

Read this reference when the reviewed work directly or indirectly changes bundles,
nested code, identifiers, resources,
document or URL types, architectures, signing identity, notarization, stapling,
Gatekeeper, App Store or managed distribution, updates, rollback, crash reporting,
symbols, uninstall, or recovery.

## Review requirements

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

- Run clean install, first launch, update, interrupted update, rollback,
  quarantine/Gatekeeper, crash, restart, and uninstall tests.
