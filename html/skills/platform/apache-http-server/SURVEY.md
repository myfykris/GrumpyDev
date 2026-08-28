# Apache HTTP Server survey contribution

## Applicability

Apply this contribution when the project uses Apache HTTP Server or when its behavior
constrains a supported build, deployment, client, or operating environment. Combine it
with the application runtime, `application-security`, `performance-capacity`, and
deployment skills. Deduplicate shared version, runtime, architecture, identity, data,
security, and deployment questions.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect Apache build and version, loaded modules and MPM, include tree, virtual
hosts, listeners, proxies, rewrites, access rules, TLS, PHP integration, limits,
logs, service configuration, and reload runbooks, dependency declarations, build
and deployment files, CI workflows, runbooks, and project documentation.
Distinguish a committed project fact from a local-machine default or a transient
environment value. Do not access or mutate an external system merely to complete
setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Apache version and distribution.
- MPM and enabled modules.
- Virtual hosts and listeners.
- TLS termination.
- Proxy topology.
- PHP SAPI.
- Service user and privilege model.
- Configuration ownership.
- Validation and graceful reload process.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: version, distribution, MPM, modules,
  virtual hosts, listeners, TLS, proxying, PHP SAPI, privileges, limits,
  reload, and rollback coverage.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Apache HTTP Server reviews. Candidate subjects are: Apache
version, MPM, enabled modules, virtual hosts, TLS termination, proxy topology,
PHP SAPI, user and privilege model, configuration ownership, and reload process.
- Align existing domain questions with this deployment guidance when it is
  material: version, distribution, MPM, modules, virtual hosts,
  listeners, TLS, proxying, PHP SAPI, privileges, limits, reload, and rollback
  coverage. Do not repeat the core profile confirmation.

## Record in .grump

Record Apache HTTP Server answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing Apache HTTP Server survey answers to the affected `DEP-###`
profile. Reference a shared `INF-###` component rather than copying its common
contract. Preserve separate state, support, ownership, confidence, source, and
scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Apache
HTTP Server doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey after a Apache version/build or MPM change, enabled-module change, new
virtual host or proxy topology, TLS boundary change, PHP SAPI change, privilege
change, or reload-process redesign. Also refresh the contribution when evidence
contradicts saved doctrine or the user explicitly requests a context refresh.
