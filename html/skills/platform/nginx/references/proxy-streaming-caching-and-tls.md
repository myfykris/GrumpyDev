# Nginx proxying, streaming, caching, and TLS

Read this reference when the reviewed work directly or indirectly changes reverse
proxying, upstream identity, forwarded
headers, retries, timeouts, buffering, streaming, cancellation, cache keys,
invalidation, stale behavior, TLS, certificates, HTTP versions, HSTS, backend
encryption, graceful reload, old workers, or rollback.

## Review requirements

- Match TLS protocols, certificates, stapling, client authentication, HTTP
  versions, redirects, HSTS, session behavior, and backend encryption to the
  actual termination and trust boundaries.

- Define cache keys, tenant and authorization variance, stale behavior, locks,
  bypass, invalidation, poisoning protection, disk ownership, capacity, and
  recovery after corrupt or missing cache state.

- Validate before graceful reload, then account for old workers, long-lived
  streams, changed listeners, certificates, logs, upstream pools, and memory.
  Define rollback to a complete known-good configuration tree.

## Verify the claims

- Run configuration validation and rehearse graceful reload, rollback,
  certificate rotation, long-lived streams, and upstream failure.

- Load test buffering, streaming, upstream pools, timeouts, retries, cache, file
  descriptors, connections, and worker capacity.
