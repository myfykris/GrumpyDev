# Nginx standard review

## Inspect additional evidence

- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: Nginx version and distribution, modules, server
blocks, TLS termination, upstream topology, PHP-FPM sockets or ports, buffering,
limits, configuration ownership, and reload process. The changed boundary must
define: Request phases, location matching, reverse proxying, FastCGI, TLS,
buffering, streaming, caching, timeouts, limits, headers, static files, reload,
logging, and failover.

Identify the authoritative expanded configuration and owners for listener and
server selection, location precedence, rewrites, proxy or FastCGI upstreams,
TLS, forwarded headers, buffering, streaming, caching, limits, logging, reload,
and rollback. Test the effective match and request-phase behavior, then prove a
reload and upstream replacement preserve in-flight traffic and security rules.

## Challenge the reviewed work

### Recurring traps

- Review the complete effective configuration rather than an isolated include.
  Request phases, inherited directives, internal redirects, and distribution
  modules can change behavior that the edited file does not show by itself.

## Verify the claims

- Dump and test the effective configuration for every listener, expected host,
  unknown host, URI class, and internal redirect.
## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Nginx version and
distribution, modules, server blocks, TLS termination, upstream topology,
PHP-FPM sockets or ports, buffering, limits, configuration ownership, and reload
process. For the changed boundary, ask only about unresolved Request phases,
location matching, reverse proxying, FastCGI, TLS, buffering, streaming,
caching, timeouts, limits, headers, static files, reload, logging, and failover
when the answer can change the verdict or implementation.

## Calibrate findings

- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the reviewed work depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
