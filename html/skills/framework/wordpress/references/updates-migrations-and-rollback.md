# WordPress updates, migrations, and rollback

Read this reference when the reviewed work directly or indirectly changes plugin or
theme activation, deactivation,
uninstall, core or dependency updates, filesystem credentials, maintenance mode,
database migrations, mixed-version requests, rollback, or security response ownership.

## Review requirements

- Namespace functions, classes, options, metadata, routes, script handles, cron
  hooks, and database objects. Define activation, deactivation, uninstall,
  upgrade, and failed-upgrade behavior without deleting user data unexpectedly.

- Define ownership for core, plugin, theme, translation, and dependency updates;
  staging evidence; maintenance mode; filesystem credentials; mixed-version
  requests; database migration; rollback; and security response.

## Verify the claims

- Exercise activation, upgrade from supported versions, failure during
  migration, rollback, deactivation, and uninstall with preserved content.
