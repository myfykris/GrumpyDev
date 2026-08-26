---
name: apache-http-server
description: Review Apache HTTP Server plans for MPM behavior, virtual hosts, routing, modules, proxying, TLS, access control, headers, rewrites, PHP integration, limits, reload, and rollback. Use when a plan changes Apache-hosted web traffic or configuration.
---

# Apache HTTP Server plan review

Apply this guidance alongside the core GrumpyDev review and the application
runtime, `application-security`, `performance-capacity`, and deployment skills.
Select only companions that match the plan's real boundaries. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect Apache build and version, loaded modules and MPM, include tree,
  virtual hosts, listeners, proxies, rewrites, access rules, TLS, PHP
  integration, limits, logs, service configuration, and reload runbooks.
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

Establish the project target: Apache version, MPM, enabled modules, virtual
hosts, TLS termination, proxy topology, PHP SAPI, user and privilege model,
configuration ownership, and reload process. The changed boundary must define:
MPM choice, request routing, virtual hosts, modules, reverse proxying, TLS,
authentication, authorization, headers, rewrites, PHP integration, timeouts,
limits, logs, reload, and rollback.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for MPM choice, request routing, virtual hosts, modules,
reverse proxying, TLS, authentication, authorization. Prove headers, rewrites,
PHP integration, timeouts, limits, logs, reload, rollback through rotation,
overload, partial rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for directives applied in the wrong context, rewrite loops or
surprising rule order, forwarded identity trusted from arbitrary clients, MPM
and module thread-safety mismatches, .htaccess drift, and graceful reloads
leaving old processes or configuration active.

- Treat MPM choice as a concurrency and compatibility decision. Match
  process/thread behavior, module thread safety, PHP integration, keep-alive,
  capacity, memory, and shutdown to the installed build.
- Trace address/port listeners, name-based virtual-host selection, defaults,
  aliases, document roots, directory rules, and forwarded host behavior. Unknown
  hosts must not fall into a sensitive site accidentally.
- Review configuration merge and override order across server, virtual host,
  directory, location, files, includes, and `.htaccess`. Prohibit
  user-controlled overrides unless their cost and authority are intentional.
- Analyze proxy routing, URI normalization, path joining, WebSocket or streaming
  behavior, connection reuse, request and response buffering, retries, timeouts,
  body limits, and trusted forwarded headers.
- Keep authentication and authorization ordering, filesystem access, symlink
  rules, CGI or handler execution, upload paths, status endpoints, and module
  privileges least-authority.
- Match TLS protocols, ciphers, certificates, OCSP behavior, client
  authentication, HTTP versions, redirects, HSTS, and backend encryption to the
  actual termination boundaries.
- For PHP, distinguish mod_php from proxy/FastCGI arrangements and ensure MPM
  compatibility, script filename mapping, path info, environment variables,
  timeouts, process ownership, and error isolation.
- Validate configuration before a graceful reload, then account for
  old-generation connections, changed certificates, module state, log
  descriptors, stuck requests, and rollback to the previous known-good include
  tree.

## Verify the claims

- Dump the effective virtual-host and module configuration and test routing for
  expected, unknown, malformed, HTTP, and HTTPS hosts.
- Run configuration validation and rehearse graceful reload, rollback,
  long-lived requests, backend loss, and certificate rotation.
- Test access control, forwarded-header trust, path normalization, rewrites,
  uploads, body limits, status endpoints, and PHP execution boundaries.
- Load test the selected MPM, keep-alive, proxy pools, limits, and application
  process topology with representative traffic.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Apache version, MPM,
enabled modules, virtual hosts, TLS termination, proxy topology, PHP SAPI, user
and privilege model, configuration ownership, and reload process. For the
changed boundary, ask only about unresolved MPM choice, request routing, virtual
hosts, modules, reverse proxying, TLS, authentication, authorization, headers,
rewrites, PHP integration, timeouts, limits, logs, reload, and rollback when the
answer can change the verdict or implementation.

## Calibrate findings

- Treat remote code execution, access-control bypass, private-site exposure
  through default routing, or a reload/configuration path that creates an outage
  without recovery as critical or high according to blast radius and realistic
  likelihood.
- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the plan depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant MPM
choice, request routing, virtual hosts, modules, reverse proxying, TLS,
authentication, authorization, headers, rewrites, PHP integration, timeouts,
limits, logs, reload, and rollback, verification evidence, deployment and
recovery limits, and any material assumption that remains unresolved.
