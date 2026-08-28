# Laravel caching, configuration, and deployment

Read this reference when the reviewed work directly or indirectly changes cache keys,
invalidation, sessions, generated
configuration, route or view caches, maintenance mode, release artifacts, storage links,
OPcache, worker restarts, health checks, rollback, or deployment sequencing.

## Caches, configuration, and deployment

- Check cache key ownership, tenant separation, serialization compatibility,
  TTL, invalidation, stampede behavior, tags, locks, and degraded operation when
  the cache is unavailable.
- Verify configuration, route, event, view, package, and service caches against
  the deployment artifact. Runtime environment changes do not necessarily alter
  an already generated configuration cache.
- Coordinate maintenance mode, health checks, symlink or immutable releases,
  static assets, storage links, migrations, queue draining, worker restarts,
  Octane reload, OPcache, scheduler ownership, and rollback.
- Reject rollback claims that ignore destructive migrations, incompatible job
  payloads, new cache formats, or external effects.

## Ask when evidence is missing

- If deployment caches or workers are affected, ask which artifacts are built,
  when workers drain and restart, and what rollback does with queued payloads
  and persisted formats.
