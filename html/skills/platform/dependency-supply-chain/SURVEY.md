# Dependency and supply-chain survey contribution

## Applicability

Apply this contribution when the project uses third-party dependencies, generated code,
build packages, images, or promoted artifacts.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For Dependency and supply-chain, inspect version declarations, effective
configuration sources, rendered artifacts, infrastructure and identity policy,
build and deployment workflows, service objectives, operational runbooks, and
project documentation. Read existing `.grump` doctrine and project documentation
before treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Package ecosystems, approved registries and
  sources, lock policy, update cadence, license policy, private dependencies,
  deployed inventory, vulnerability and exception process, end-of-life policy,
  and build isolation.
- Review doctrine for: Source trust, resolution, lockfiles, registries, scopes,
  transitive risk, build scripts, updates, vulnerabilities, licenses, vendoring,
  and recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: Build hosts, package sources, network access,
  install scripts, native toolchains, artifact promotion, dependency caches,
  signing authority if applicable, and emergency rebuild.

## Ask only when materially unresolved

- What canonical source, publisher, exact resolved version, and lockfile
  identify each new dependency?
- Which install scripts, build plugins, generated artifacts, licenses, and
  transitive updates enter the build boundary, inventory, and vulnerability
  response process?
- Align existing domain questions with this deployment guidance when it is
  material: Build hosts, package sources, network access, install scripts,
  native toolchains, artifact promotion, dependency caches, signing authority
  if applicable, and emergency rebuild. Do not repeat the core profile
  confirmation.

## Record in .grump

Record Dependency and supply-chain answers in project technology, runtime,
security, deployment, verification, and operational doctrine. Preserve source
and scope. Record a material unknown as unresolved doctrine instead of guessing.

Map existing Dependency and supply-chain survey answers to the affected
`DEP-###` profile. Reference a shared `INF-###` component rather than copying
its common contract. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable
Dependency and supply-chain doctrine. Do not duplicate facts owned by another
applicable contribution.

## Re-survey triggers

Re-survey Dependency and supply-chain when product or protocol version,
topology, environment, identity, trust boundary, resource model, configuration
authority, deployment process, or recovery objectives materially change, when
evidence conflicts with saved doctrine, or when the user requests a context
refresh.
