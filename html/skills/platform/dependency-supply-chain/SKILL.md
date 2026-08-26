---
name: dependency-supply-chain
description: Review software dependency and supply-chain plans for provenance, pinning, source trust, transitive risk, build isolation, licensing, patching, and artifact traceability. Use when a plan adds dependencies or changes how software is built and distributed.
---

# Dependency and supply-chain plan review

Apply this guidance alongside the core GrumpyDev review, the `containers` and
`ci-cd` skills when applicable, and the installed language specialist for the
package ecosystem.

## Inspect evidence

- Read manifests, lockfiles, canonical registries, publishers, install scripts,
  build plugins, generated artifacts, licenses, vulnerability reports, and
  update ownership. Include direct and transitive components present in the
  deployed artifact, not only the top-level manifest.
- Trace a dependency from selection through resolution, download, build
  execution, packaging, deployment, patching, and removal.

## Establish the operating model

Establish the project target: Package ecosystems, approved registries and
sources, lock policy, update cadence, license policy, private dependencies,
vulnerability process, and build isolation. The changed boundary must define:
Source trust, resolution, lockfiles, registries, scopes, transitive risk, build
scripts, updates, vulnerabilities, licenses, vendoring, and recovery.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Source trust, resolution, lockfiles, registries,
scopes, transitive risk. Prove build scripts, updates, vulnerabilities,
licenses, vendoring, recovery through rotation, overload, partial rollout,
drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for lookalike packages, transitive drift hidden by direct
dependency review, install scripts executing with broad authority, abandoned
maintainers, build tools downloading undeclared inputs, lockfiles mistaken for
provenance, vulnerable packages dismissed because no direct call is obvious,
development tools and IDE extensions outside inventory, and emergency upgrades
with no compatibility evidence.

- Require a concrete payoff for each dependency relative to its transitive code,
  privileges, maintenance, and replacement cost.
- Pin resolved versions and record the canonical source and publisher; names and
  version ranges alone do not establish provenance.
- Treat install hooks, generators, compilers, package managers, and CI plugins
  as code execution with bounded credentials and network access.
- Check maintainer health, release provenance, typosquatting, license
  compatibility, abandoned packages, vulnerabilities, and patch latency.
- Maintain a software bill of materials for direct, transitive, build, generated,
  bundled, native, image, and runtime components. Tie it to the promoted
  artifact and preserve enough source and version identity to find every
  affected deployment.
- Prioritize vulnerability response by active exploitation, reachability,
  privileges, exposed data, deployment presence, and available mitigation, not
  severity score alone. Define owners, response targets, emergency change,
  validation, rollout, rollback, and exception expiry.
- Require an exit plan for unmaintained, end-of-life, unpatchable, or
  irreplaceable components. A scanner exception is not remediation.
- Protect registries, namespaces, publisher accounts, package scopes, mirrors,
  dependency caches, IDE extensions, generators, and build services against
  substitution or unauthorized release.
- Produce traceable artifacts with verified provenance or signatures where the
  ecosystem supports them. Promote the same reviewed artifact across
  environments instead of rebuilding from mutable inputs.

## Verify the claims

- Verify these behaviors through the effective Dependency and supply-chain
  configuration and runtime topology: Source trust, resolution, lockfiles,
  registries, scopes, transitive risk. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: build scripts, updates,
  vulnerabilities, licenses, vendoring, recovery. Exercise startup, readiness,
  normal load, overload, dependency loss, rotation, graceful drain, forced stop,
  failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Compare the bill of materials with the installed and deployed output. Exercise
  registry or maintainer compromise, package removal, revoked credentials,
  cache poisoning, urgent replacement, and rollback to a known supported build.

## Ask when evidence is missing

- What canonical source, publisher, exact resolved version, and lockfile
  identify each new dependency?
- Which install scripts, build plugins, generated artifacts, licenses, and
  transitive updates enter the build boundary, inventory, and vulnerability
  response process?

## Calibrate findings

- Treat an untrusted publisher, executable install path, or dependency that can
  alter release artifacts without review as critical.
- Downgrade when provenance, exact resolution, isolation, licensing, and update
  ownership are established by ecosystem evidence.

## Add to the verdict

State dependency justification, resolution and source controls, build authority,
deployed inventory, provenance, licensing, patch and end-of-life ownership,
exception expiry, and recovery evidence.
