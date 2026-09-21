---
name: gd-wordpress
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review WordPress engineering work for lifecycle hooks, plugins, themes, blocks, REST endpoints, capabilities, nonces, validation, escaping, database access, cron, caching, updates, multisite, and rollback."
---

# WordPress GrumpyDev review

## Quick checks

- Inspect WordPress and PHP targets, plugin and theme code, hook registrations,
  block metadata, REST routes, capability checks, nonce use, database queries,
  cron events, caches, filesystem access, update policy, and deployment
  runbooks.

Watch especially for nonces mistaken for authorization, sanitization mistaken
for output escaping, hook order and global state, unreliable pseudo-cron timing,
dbDelta assumed to perform arbitrary migrations safely, stale persistent caches,
and automatic updates without a recovery path.

- Inspect capability bypass, remote code execution, destructive upgrade or
  uninstall, cross-site data exposure, or an update path that cannot recover.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the WordPress
specialist.

- [Focused rules](references/database-cron-cache-and-multisite.md):
  Read when the work changes wpdb, schema, options,
  metadata, taxonomy, object or page
  caches, cache scope, WP-Cron, an external scheduler, background retries, multisite
  data, tenant scope, or production query behavior.
- [Focused rules](references/updates-migrations-and-rollback.md):
  Read when the work changes plugin or theme activation,
  deactivation, uninstall, core
  or dependency updates, filesystem credentials, maintenance mode, database migrations,
  mixed-version requests, rollback, or security response ownership.

## Verdict context

State the core lifecycle and hooks, plugins, themes, blocks, REST endpoints,
capabilities, nonces, sanitization and escaping, database access, cron,
caching, updates, multisite, and rollback, supporting evidence, deployment or
recovery limits, and unresolved material assumptions.
