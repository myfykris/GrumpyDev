# Nginx full-review guidance

## Operating conditions

Establish the project target: Nginx version and distribution, modules, server
blocks, TLS termination, upstream topology, PHP-FPM sockets or ports, buffering,
limits, configuration ownership, and reload process. The changed boundary must
define: Request phases, location matching, reverse proxying, FastCGI, TLS,
buffering, streaming, caching, timeouts, limits, headers, static files, reload,
logging, and failover.

## Failure patterns

- Review the complete effective configuration rather than an isolated include.
  Request phases, inherited directives, internal redirects, and distribution
  modules can change behavior that the edited file does not show by itself.

## Verification to run or specify in the plan

- Dump and test the effective configuration for every listener, expected host,
  unknown host, URI class, and internal redirect.
