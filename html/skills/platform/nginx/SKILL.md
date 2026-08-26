---
name: nginx
description: Review Nginx plans for request processing, location matching, proxy and FastCGI behavior, TLS, buffering, streaming, caching, timeouts, limits, headers, static files, reload, logging, and failover. Use when a plan changes Nginx-hosted traffic or configuration.
---

# Nginx plan review

Apply this guidance alongside the core GrumpyDev review and the application
runtime, `application-security`, `performance-capacity`, and deployment skills.
Select only companions that match the plan's real boundaries. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect Nginx version and modules, full include tree, listeners and server
  blocks, locations, maps, upstreams, proxy or FastCGI settings, TLS, caches,
  limits, logs, service configuration, and reload runbooks.
- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.
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

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Request phases, location matching, reverse proxying,
FastCGI, TLS, buffering, streaming, caching. Prove timeouts, limits, headers,
static files, reload, logging, failover through rotation, overload, partial
rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for location precedence selecting the wrong handler, proxy_pass
rewriting URIs unexpectedly, buffering breaking streaming, client identity
trusted from unbounded proxies, timeout mismatches across layers, static files
bypassing intended controls, and reloads retaining old workers or sockets.

- Trace listen-address and server-name selection, including the default server
  for every socket. Unknown or malformed hosts must not fall into a sensitive
  application.
- Evaluate exact, prefix, regular-expression, named, and nested location
  matching plus internal redirects. Configuration order and URI normalization
  can route a request differently than the visual layout suggests.
- For static files, verify `root` versus `alias`, trailing slashes, normalized
  paths, symlinks, index and try-files redirects, error pages, MIME types,
  ranges, and cache headers without exposing private files.
- For proxy and FastCGI traffic, define URI rewriting, upstream identity, Host
  and forwarded headers, client IP trust, connection reuse, retries, timeouts,
  body limits, buffering, streaming, cancellation, and temporary-file behavior.
- For PHP-FPM, prove the script filename and path-info mapping from the
  normalized request to an existing intended file. Never let user-controlled
  path construction select arbitrary scripts.
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

- Dump and test the effective configuration for every listener, expected host,
  unknown host, URI class, and internal redirect.
- Run configuration validation and rehearse graceful reload, rollback,
  certificate rotation, long-lived streams, and upstream failure.
- Test path normalization, root/alias behavior, static/private file separation,
  forwarded headers, limits, caching, and PHP script mapping.
- Load test buffering, streaming, upstream pools, timeouts, retries, cache, file
  descriptors, connections, and worker capacity.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Nginx version and
distribution, modules, server blocks, TLS termination, upstream topology,
PHP-FPM sockets or ports, buffering, limits, configuration ownership, and reload
process. For the changed boundary, ask only about unresolved Request phases,
location matching, reverse proxying, FastCGI, TLS, buffering, streaming,
caching, timeouts, limits, headers, static files, reload, logging, and failover
when the answer can change the verdict or implementation.

## Calibrate findings

- Treat arbitrary script execution, private-file exposure, authentication/cache
  cross-tenant leakage, default-host exposure, or a configuration change that
  causes an unrecoverable outage as critical or high according to blast radius
  and realistic likelihood.
- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the plan depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
request phases, location matching, reverse proxying, FastCGI, TLS, buffering,
streaming, caching, timeouts, limits, headers, static files, reload, logging,
and failover, verification evidence, deployment and recovery limits, and any
material assumption that remains unresolved.
