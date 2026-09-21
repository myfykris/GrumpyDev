---
name: gd-dependency-supply-chain
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review software dependency and supply-chain engineering work for provenance, pinning, source trust, transitive risk, build isolation, licensing, patching, and artifact traceability."
---

# Dependency and supply-chain GrumpyDev review

## Quick checks

- Read manifests, lockfiles, canonical registries, publishers, install scripts,
  build plugins, generated artifacts, licenses, vulnerability reports, and
  update ownership. Include direct and transitive components present in the
  deployed artifact, not only the top-level manifest.

- Trace a dependency from selection through resolution, download, build
  execution, packaging, deployment, patching, and removal.

Watch especially for lookalike packages, transitive drift hidden by direct
dependency review, install scripts executing with broad authority, abandoned
maintainers, build tools downloading undeclared inputs, lockfiles mistaken for
provenance, vulnerable packages dismissed because no direct call is obvious,
development tools and IDE extensions outside inventory, and emergency upgrades
with no compatibility evidence.

- Assess an untrusted publisher, executable install path, or dependency that can
  alter release artifacts without review under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Dependency and
supply-chain specialist.

## Verdict context

State dependency justification, resolution and source controls, build authority,
deployed inventory, provenance, licensing, patch and end-of-life ownership,
exception expiry, and recovery evidence.
