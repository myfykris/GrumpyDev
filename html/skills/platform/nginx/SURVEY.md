# Nginx survey contribution

## Applicability

Apply this contribution when the project uses Nginx or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the application runtime, `application-security`,
`performance-capacity`, and deployment skills. Deduplicate shared version,
runtime, architecture, identity, data, security, and deployment questions.

## Inspect before asking

Inspect Nginx version and modules, full include tree, listeners and server
blocks, locations, maps, upstreams, proxy or FastCGI settings, TLS, caches,
limits, logs, service configuration, and reload runbooks, dependency
declarations, build and deployment files, CI workflows, runbooks, and project
documentation. Distinguish a committed project fact from a local-machine default
or a transient environment value. Do not access or mutate an external system
merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Nginx version and distribution.
- Compiled and dynamic modules.
- Server blocks and listeners.
- TLS termination.
- Upstream topology.
- PHP-FPM sockets or ports.
- Buffering, caching, and limits.
- Configuration ownership.
- Validation and graceful reload process.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: version, modules, server blocks,
  location and FastCGI behavior, upstreams, TLS, buffering, caching, limits,
  privileges, reload, and failover coverage.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Nginx reviews. Candidate subjects are: Nginx version and
distribution, modules, server blocks, TLS termination, upstream topology,
PHP-FPM sockets or ports, buffering, limits, configuration ownership, and reload
process.
- Align existing domain questions with this deployment guidance when it is
  material: version, modules, server blocks, location and FastCGI
  behavior, upstreams, TLS, buffering, caching, limits, privileges, reload, and
  failover coverage. Do not repeat the core profile confirmation.

## Record in .grump

Record Nginx answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Nginx survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Nginx
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a Nginx version/distribution/module change, new listener or
server block, location/proxy/FastCGI redesign, TLS boundary change, cache
change, or reload-process redesign. Also refresh the contribution when evidence
contradicts saved doctrine or the user explicitly requests a context refresh.
