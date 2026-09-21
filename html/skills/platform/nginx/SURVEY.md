# Nginx survey contribution

## Applies when

Apply this contribution when the project uses Nginx or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect Nginx version and modules, full include tree, listeners and server
  blocks, locations, maps, upstreams, proxy or FastCGI settings, TLS, caches,
  limits, logs, service configuration, and reload runbooks.

## Ask when unresolved

- Which of these durable facts materially change future reviews: Nginx version
  and distribution, modules, server blocks, TLS termination, upstream topology,
  PHP-FPM sockets or ports, buffering, limits, configuration ownership, and
  reload process?

- Which runtime or deployment differences are material for future reviews:
  version, modules, server blocks, location and FastCGI behavior, upstreams,
  TLS, buffering, caching, limits, privileges, reload, and failover coverage?

## Record

Map durable Nginx requirements and constraints to the matching doctrine
sections, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
