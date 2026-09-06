---
name: wordpress
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review WordPress engineering work for lifecycle hooks, plugins, themes, blocks, REST endpoints, capabilities, nonces, validation, escaping, database access, cron, caching, updates, multisite, and rollback."
---

# WordPress GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `php`,
applicable database and web-server, `application-security`, and deployment
skills. Every installed companion that remains applicable to the project
participates; the reviewed target does not select the roster. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

## Lean review

- Inspect WordPress and PHP targets, plugin and theme code, hook registrations,
  block metadata, REST routes, capability checks, nonce use, database queries,
  cron events, caches, filesystem access, update policy, and deployment
  runbooks.

- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.

Watch especially for nonces mistaken for authorization, sanitization mistaken
for output escaping, hook order and global state, unreliable pseudo-cron timing,
dbDelta assumed to perform arbitrary migrations safely, stale persistent caches,
and automatic updates without a recovery path.

Lean mode is insufficient when this material severity condition may apply:

- Treat capability bypass, remote code execution, destructive upgrade or
  uninstall, cross-site data exposure, or an update path that cannot recover as
  critical or high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/database-cron-cache-and-multisite.md):
  Read when the reviewed work directly or indirectly changes wpdb, schema, options,
  metadata, taxonomy, object or page
  caches, cache scope, WP-Cron, an external scheduler, background retries, multisite
  data, tenant scope, or production query behavior.
- [Focused rules](references/updates-migrations-and-rollback.md):
  Read when the reviewed work directly or indirectly changes plugin or theme activation,
  deactivation, uninstall, core
  or dependency updates, filesystem credentials, maintenance mode, database migrations,
  mixed-version requests, rollback, or security response ownership.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
core lifecycle and hooks, plugins, themes, blocks, REST endpoints, capabilities,
nonces, sanitization and escaping, database access, cron, caching, updates,
multisite, and rollback, verification evidence, deployment and recovery limits,
and any material assumption that remains unresolved.
