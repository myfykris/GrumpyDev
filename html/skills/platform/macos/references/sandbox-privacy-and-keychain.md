# macOS sandbox, privacy, and keychain

Read this reference when the reviewed work directly or indirectly changes sandboxing,
hardened-runtime entitlements,
privacy permissions, user consent, app groups, security-scoped URLs, bookmarks, helpers,
plugins, keychain groups, keychain accessibility, user presence, or credential
migration.

## Review requirements

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

## Verify the claims

- Exercise sandbox and privacy permissions in grant, deny, revoke,
  stale-bookmark, moved-file, and restored-machine states.
