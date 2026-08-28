# PHP dependencies and deployment

Read this reference when the reviewed work directly or indirectly changes PHP or
extension versions, Composer
resolution, plugins or scripts, classmaps, OPcache, preloading, generated framework
artifacts, rolling releases, migrations, cache or queue payload compatibility, worker
draining, restart, rollback, or recovery.

## Dependencies and deployment

- Verify that the lockfile was resolved for the intended PHP and extension
  platform. Review Composer plugins, scripts, abandoned packages, replacement
  packages, autoload changes, and optimized or authoritative classmaps.
- Analyze OPcache and preloading behavior, generated containers, framework
  caches, route and template caches, and immutable artifacts. Old workers can
  retain old code or configuration after files change.
- Require a mixed-version compatibility window for rolling web and worker
  deployments. Coordinate database migrations, session formats, cache values,
  queued payloads, serialized objects, and API contracts across old and new
  processes.
- Define restart, drain, health, rollback, and recovery behavior for PHP-FPM,
  application servers, queue workers, schedulers, and web-server reloads. A code
  rollback does not reverse destructive data or incompatible queued messages.

## Verify the claims

- Test the exact supported PHP versions, SAPIs, extension sets, INI profiles,
  and dependency lockfile in CI or equivalent reproducible environments.

- Rehearse deployment with old and new web workers and queue workers active at
  the same time. Verify cache invalidation, OPcache refresh or restart,
  migration ordering, drain behavior, rollback limits, and observable health.


## Ask when evidence is missing

- If the plan uses version-specific syntax, runtime behavior, or dependencies,
  ask which PHP versions and extension versions execute the affected web, CLI,
  worker, CI, and test paths.
