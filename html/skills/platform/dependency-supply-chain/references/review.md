# Dependency and supply-chain standard review

## Establish the operating model

Establish the project target: Package ecosystems, approved registries and
sources, lock policy, update cadence, license policy, private dependencies,
vulnerability process, and build isolation. The changed boundary must define:
Source trust, resolution, lockfiles, registries, scopes, transitive risk, build
scripts, updates, vulnerabilities, licenses, vendoring, and recovery.

Identify the authoritative manifests, lockfiles, registries, namespaces,
mirrors, build scripts, generated artifacts, update automation, vulnerability
policy, license policy, vendored sources, and emergency-removal owner. Trace
what code executes during resolution, install, build, test, and packaging, and
prove a compromised, yanked, or unavailable dependency can be contained and
replaced reproducibly.

## Challenge the reviewed work

### Recurring traps

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

- Resolve and build from a clean environment using only declared registries,
  mirrors, manifests, lockfiles and toolchains. Compare the installed and
  shipped dependency graph with the reviewed bill of materials.
- Review all install and build scripts, native binaries, generated code,
  credentials and network access exercised before application startup.
- Simulate a compromised namespace or maintainer, removed package, unavailable
  registry, revoked credential and urgent vulnerable-dependency replacement,
  including a rebuild from a known supported input set.
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

- Downgrade when provenance, exact resolution, isolation, licensing, and update
  ownership are established by ecosystem evidence.
