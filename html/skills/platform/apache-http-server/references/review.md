# Apache HTTP Server standard review

## Inspect additional evidence

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

Identify the authoritative configuration and owners for the Apache build, MPM,
modules, virtual hosts, TLS, proxy routes, PHP SAPI, worker identity, limits,
reload, and rollback. Prove the effective configuration, not just source
fragments, and show how a reload handles in-flight requests and mixed old and
new workers without bypassing routing or access controls.

## Challenge the reviewed work

### Recurring traps

- Treat MPM choice as a concurrency and compatibility decision. Match
  process/thread behavior, module thread safety, PHP integration, keep-alive,
  capacity, memory, and shutdown to the installed build.
## Verify the claims

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

- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the reviewed work depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
