---
name: android
description: Review Android plans for component lifecycle, process death, permissions, storage, background work, compatibility, signing, packaging, accessibility, and release behavior. Use when software targets Android devices.
---

# Android plan review

Apply this guidance alongside the core GrumpyDev review and the `kotlin`, `jetpack-compose` and
`application-security` skills.

## Inspect evidence

- Read minimum and target SDK, Android plugin, Gradle, language, UI toolkit, architecture, and
  dependency versions.
- Trace activity, fragment, service, receiver, provider, application, task, and process
  lifecycle behavior.
- Inspect permissions, intents, deep links, exported components, network security, storage,
  backups, keystore, and WebView use.
- Review background limits, WorkManager, notifications, foreground services, app links,
  signing, shrinking, and release tracks.

## Establish the operating model

Establish the project target: Minimum and target SDK, device and form-factor support, Android
plugin and build tools, UI toolkit, process and task model, permissions, exported components,
storage and backup policy, background execution, signing, application ID, and release channels.

Android may destroy and recreate processes without preserving in-memory state. The plan must
distinguish saved UI state, durable local data, account-scoped data, server authority, and work
that can safely resume.

## Challenge the plan

### Recurring traps

Watch especially for process death treated as logout, implicit exported components, broad
storage or notification permissions, background work assumed continuous, pending intents with
unsafe mutability, WebView bridges exposing native power, and signing ownership left informal.

- Require explicit lifecycle behavior for rotation, background, process death, task recreation,
  multi-window, and low memory.
- Minimize permissions and exported surface; validate every intent, deep link, provider path,
  pending intent, and WebView bridge.
- Choose WorkManager, foreground service, alarm, push, or in-process work based on actual
  delivery and timing guarantees.
- Define scoped storage, encryption, backup exclusion, account removal, device transfer, and
  secure deletion behavior.
- Keep credentials and sensitive data out of source, resources, logs, notifications,
  screenshots, clipboards, shared preferences without protection, and exported backup unless a
  documented requirement and control justify the exposure.
- Require TLS with normal platform trust validation, reject permissive trust managers and
  hostname checks, and define certificate-pinning recovery only when the threat model justifies
  pinning. Treat application-layer authorization as a server responsibility.
- Harden WebView content, JavaScript bridges, file and content access, deep links, app links,
  custom schemes, pending intents, and interprocess data so attacker-controlled applications or
  pages cannot invoke privileged behavior.
- Test screen readers, switch access, keyboard, font scaling, display size, contrast, touch
  targets, and adaptive layouts.
- Rehearse signing rotation, staged rollout, rollback, database migration, old clients, and
  Play policy changes.

## Verify the claims

- Run release builds on representative API levels, vendors, screen sizes, locales, input modes,
  and low-memory conditions.
- Exercise denied and revoked permissions, process kill, offline launch, deep links, backup
  restore, upgrade, downgrade, and account removal.
- Inspect the merged manifest, network policy, resources, shrinker output, signing
  configuration, and packaged artifacts.
- Inspect release packages and a normal device for credentials, sensitive logs and storage,
  backup contents, exported components, permissive network overrides, and debuggable behavior.

## Ask when evidence is missing

- Which Android SDK levels, devices, UI toolkit, process model, permissions, background work,
  and storage apply?
- How are exported components, deep links, backups, accessibility, signing, upgrades, rollback,
  and policy changes handled?

## Calibrate findings

- Treat exposed privileged components, unsafe WebView bridges, signing compromise, or
  cross-account data leakage as critical.
- Downgrade when lifecycle, permissions, storage, package output, accessibility, and release
  transitions are tested.

## Add to the verdict

State supported Android matrix, lifecycle and data owners, external surface, background
guarantees, signing owner, and release evidence.
