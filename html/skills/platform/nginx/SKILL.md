---
name: gd-nginx
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Nginx engineering work for request processing, location matching, proxy and FastCGI behavior, TLS, buffering, streaming, caching, timeouts, limits, headers, static files, reload, logging, and failover."
---

# Nginx GrumpyDev review

## Quick checks

- Inspect Nginx version and modules, full include tree, listeners and server
  blocks, locations, maps, upstreams, proxy or FastCGI settings, TLS, caches,
  limits, logs, service configuration, and reload runbooks.

Watch especially for location precedence selecting the wrong handler, proxy_pass
rewriting URIs unexpectedly, buffering breaking streaming, client identity
trusted from unbounded proxies, timeout mismatches across layers, static files
bypassing intended controls, and reloads retaining old workers or sockets.

- Inspect arbitrary script execution, private-file exposure, authentication/cache
  cross-tenant leakage, default-host exposure, or a configuration change that
  causes an unrecoverable outage.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Nginx specialist.

- [Focused rules](references/routing-static-files-and-fastcgi.md):
  Read when the work changes listen or server-name
  selection, default servers, location
  matching, rewrites, internal redirects, URI normalization, root, alias, static file
  access, symlinks, try_files, MIME behavior, FastCGI, PHP-FPM, script mapping, path
  info, or request metadata.
- [Focused rules](references/proxy-streaming-caching-and-tls.md):
  Read when the work changes reverse proxying, upstream
  identity, forwarded headers,
  retries, timeouts, buffering, streaming, cancellation, cache keys, invalidation, stale
  behavior, TLS, certificates, HTTP versions, HSTS, backend encryption, graceful reload,
  old workers, or rollback.

## Verdict context

State the request phases, location matching, reverse proxying, FastCGI, TLS,
buffering, streaming, caching, timeouts, limits, headers, static files, reload,
logging, and failover, supporting evidence, deployment or recovery limits, and
unresolved material assumptions.
