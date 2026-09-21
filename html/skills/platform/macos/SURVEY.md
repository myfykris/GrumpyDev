# macOS survey contribution

## Applies when

Apply this contribution when the project uses macOS or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect deployment target and architectures, app and helper bundles,
  Info.plist files, entitlements, sandbox containers, privacy strings, signing
  settings, launch registrations, keychain use, packaging, updater, and
  crash/recovery configuration.

## Ask when unresolved

- Which of these durable facts materially change future reviews: macOS
  deployment range, architectures, sandbox and entitlements, signing ownership,
  distribution channel, update model, privacy permissions, and supported
  hardware?

- Which runtime or deployment differences are material for future reviews: OS
  range, architecture, app model, sandbox, entitlements, privacy permissions,
  signing, notarization, packaging, updates, filesystem, and recovery?

## Record

Map durable macOS requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
