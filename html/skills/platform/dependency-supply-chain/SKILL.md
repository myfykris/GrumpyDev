---
name: dependency-supply-chain
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review software dependency and supply-chain plans and other engineering artifacts for provenance, pinning, source trust, transitive risk, build isolation, licensing, patching, and artifact traceability. Project applicability: the project uses third-party dependencies, generated code, build packages, images, or promoted artifacts."
---

# Dependency and supply-chain GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review, the `containers` and
`ci-cd` skills when applicable, and the installed language specialist for the
package ecosystem.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat an untrusted publisher, executable install path, or dependency that can
  alter release artifacts without review as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Dependency and supply-chain evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State dependency justification, resolution and source controls, build authority,
deployed inventory, provenance, licensing, patch and end-of-life ownership,
exception expiry, and recovery evidence.
