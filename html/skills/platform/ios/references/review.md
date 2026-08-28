# iOS and iPadOS standard review

## Inspect additional evidence

- Inspect entitlements, privacy usage descriptions, keychain access groups, data protection,
  app groups, universal links, and extensions.
- Review background modes, tasks, notifications, local storage, backups, network policy,
  signing, provisioning, and release tracks.

## Establish the operating model

Establish the project target: Minimum iOS and iPadOS versions, devices and form factors, Xcode
and SDK, UI framework, scene and process model, entitlements, privacy permissions, storage and
backup policy, background modes, bundle identifiers, signing, and release channels.

The operating system may suspend or terminate the process at any time. The plan must distinguish
restorable UI state, durable local data, protected credentials, server authority, and resumable
background work.

## Challenge the reviewed work

### Recurring traps

- Define lifecycle behavior for cold launch, multiple scenes, background, suspension,
  termination, memory pressure, and restoration.
- Request permissions only in context and handle denial, restriction, revocation, limited
  access, and settings changes.
- Choose data protection classes, keychain accessibility, backup exclusion, app groups, account
  removal, and secure deletion deliberately.
- Keep credentials and sensitive data out of source, property lists, logs, notifications,
  screenshots, pasteboards, weakly protected files, and backups unless a documented requirement
  and control justify the exposure.
- Require TLS with normal platform trust validation, reject permissive challenge handlers, and
  define certificate-pinning recovery only when the threat model justifies pinning. Treat local
  biometrics and client checks as gates to credentials, not server authorization.
- Validate universal links, custom schemes, document and share extensions, pasteboard input,
  web views, script bridges, and app-group data before they invoke privileged behavior.
- Use supported background APIs with explicit expiration, cancellation, duplicate delivery,
  retry, and server reconciliation.
- Test VoiceOver, Voice Control, keyboard, Dynamic Type, contrast, reduced motion, touch
  targets, orientation, and multitasking.
- Rehearse signing rotation, entitlement changes, staged release, rollback, migration, old
  clients, and App Store review constraints.

## Verify the claims

- Run release builds on representative devices, OS versions, text sizes, accessibility
  settings, network states, and memory pressure.
- Exercise permission changes, termination, restoration, background expiration, universal
  links, backup restore, upgrade, and account removal.
- Inspect effective entitlements, privacy manifest, bundle contents, signing, embedded
  provisioning, and archived artifacts.
- Inspect release archives and a normal device for credentials, sensitive logs and storage,
  backup contents, excessive entitlements, permissive network overrides, and debug behavior.

## Ask when evidence is missing

- Which Apple mobile OS versions, devices, UI framework, lifecycle, permissions, entitlements,
  and storage apply?
- How are background work, restoration, accessibility, signing, privacy manifests, upgrades,
  rollback, and review handled?

## Calibrate findings

- Downgrade when lifecycle, permissions, data protection, accessibility, package output, and
  release transitions are tested.
