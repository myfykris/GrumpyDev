# Apache HTTP Server survey contribution

## Applies when

Apply this contribution when the project uses Apache HTTP Server or when its behavior
constrains a supported build, deployment, client, or operating environment.

## Inspect

- Inspect Apache build and version, loaded modules and MPM, include tree,
  virtual hosts, listeners, proxies, rewrites, access rules, TLS, PHP
  integration, limits, logs, service configuration, and reload runbooks.

## Ask when unresolved

- Which of these durable facts materially change future reviews: Apache
  version, MPM, enabled modules, virtual hosts, TLS termination, proxy
  topology, PHP SAPI, user and privilege model, configuration ownership, and
  reload process?

- Which runtime or deployment differences are material for future reviews:
  version, distribution, MPM, modules, virtual hosts, listeners, TLS, proxying,
  PHP SAPI, privileges, limits, reload, and rollback coverage?

## Record

Map durable Apache HTTP Server requirements and constraints to the matching
doctrine sections, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
