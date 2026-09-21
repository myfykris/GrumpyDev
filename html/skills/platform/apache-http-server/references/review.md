# Apache HTTP Server full-review guidance

## Operating conditions

Establish the project target: Apache version, MPM, enabled modules, virtual
hosts, TLS termination, proxy topology, PHP SAPI, user and privilege model,
configuration ownership, and reload process. The changed boundary must define:
MPM choice, request routing, virtual hosts, modules, reverse proxying, TLS,
authentication, authorization, headers, rewrites, PHP integration, timeouts,
limits, logs, reload, and rollback.

## Failure patterns

- Treat MPM choice as a concurrency and compatibility decision. Match
  process/thread behavior, module thread safety, PHP integration, keep-alive,
  capacity, memory, and shutdown to the installed build.

## Verification to run or specify in the plan

- Test access control, forwarded-header trust, path normalization, rewrites,
  uploads, body limits, status endpoints, and PHP execution boundaries.
- Load test the selected MPM, keep-alive, proxy pools, limits, and application
  process topology with representative traffic.
