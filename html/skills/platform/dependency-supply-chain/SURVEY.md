# Dependency and supply-chain survey contribution

## Applies when

Apply this contribution when the project uses third-party dependencies, generated code,
build packages, images, or promoted artifacts.

## Inspect

- Read manifests, lockfiles, canonical registries, publishers, install scripts,
  build plugins, generated artifacts, licenses, vulnerability reports, and
  update ownership. Include direct and transitive components present in the
  deployed artifact, not only the top-level manifest.

## Ask when unresolved

- What canonical source, publisher, exact resolved version, and lockfile
  identify each new dependency?

- Which install scripts, build plugins, generated artifacts, licenses, and
  transitive updates enter the build boundary, inventory, and vulnerability
  response process?

- Which runtime or deployment differences are material for future reviews:
  Build hosts, package sources, network access, install scripts, native
  toolchains, artifact promotion, dependency caches, signing authority if
  applicable, and emergency rebuild?

## Record

Map durable Dependency and supply-chain requirements and constraints to the
matching doctrine sections, runtime facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
