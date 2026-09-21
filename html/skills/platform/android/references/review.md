# Android full-review guidance

## Operating conditions

Establish the project target: Minimum and target SDK, device and form-factor support, Android
plugin and build tools, UI toolkit, process and task model, permissions, exported components,
storage and backup policy, background execution, signing, application ID, and release channels.

## Failure patterns

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

## Verification to run or specify in the plan

- Run release builds on representative API levels, vendors, screen sizes, locales, input modes,
  and low-memory conditions.
- Exercise denied and revoked permissions, process kill, offline launch, deep links, backup
  restore, upgrade, downgrade, and account removal.
- Inspect the merged manifest, network policy, resources, shrinker output, signing
  configuration, and packaged artifacts.
- Inspect release packages and a normal device for credentials, sensitive logs and storage,
  backup contents, exported components, permissive network overrides, and debuggable behavior.
