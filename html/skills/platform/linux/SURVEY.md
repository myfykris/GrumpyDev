# Linux survey contribution

## Applicability

Apply this contribution when the project uses Linux or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the implementation language, framework, packaging,
`application-security`, and deployment skills. Deduplicate shared version,
runtime, architecture, identity, data, security, and deployment questions.

## Inspect before asking

Inspect distribution and kernel targets, architecture and libc, packages,
service units, users and groups, capabilities, filesystem layout, permissions,
sockets, namespaces, limits, security modules, logs, crash handling, and update
scripts, dependency declarations, build and deployment files, CI workflows,
runbooks, and project documentation. Distinguish a committed project fact from a
local-machine default or a transient environment value. Do not access or mutate
an external system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Linux distributions and versions.
- Architectures and libc.
- Init and service manager.
- Package and update format.
- Filesystem and security modules.
- Desktop environment and display protocol when applicable.
- Server, desktop, container, or appliance deployment targets.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: distribution, kernel, architecture,
  libc, service manager, user, capabilities, filesystem, security modules,
  packages, sockets, limits, updates, and recovery.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Linux reviews. Candidate subjects are: Distributions and
versions, architectures, libc, init and service manager, package format,
filesystem and security modules, desktop environment when applicable, and
deployment targets.
- Align existing domain questions with this deployment guidance when it is
  material: distribution, kernel, architecture, libc, service manager,
  user, capabilities, filesystem, security modules, packages, sockets, limits,
  updates, and recovery. Do not repeat the core profile confirmation.

## Record in .grump

Record Linux answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Linux survey answers to the affected `DEP-###` profile. Reference
a shared `INF-###` component rather than copying its common contract. Preserve
separate state, support, ownership, confidence, source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Linux
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a distribution/kernel/libc/architecture change, init or
packaging change, security-module policy change, server-to-desktop/container
shift, filesystem change, or update/recovery redesign. Also refresh the
contribution when evidence contradicts saved doctrine or the user explicitly
requests a context refresh.
