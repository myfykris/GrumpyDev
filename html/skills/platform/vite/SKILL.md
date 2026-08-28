---
name: vite
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Vite plans and other engineering artifacts for client and server environments, dependency handling, environment variables, base paths, production builds, SSR, plugins, browser targets, and deployment. Project applicability: the project builds or serves applications with Vite."
---

# Vite GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `javascript`, `typescript` and
`dependency-supply-chain` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read Vite, framework plugin, runtime, package manager, TypeScript, browser target, and
  test-tool versions.

- Trace client, SSR, build, development, worker, and custom environment modules plus
  environment-variable exposure.

Watch especially for secrets exposed through client environment prefixes,
root-relative assets failing under subpaths, dependencies working only after dev
optimization, SSR importing browser-only modules, plugin order changing
transforms, and one build assumed valid for client and server.

Lean mode is insufficient when this material severity condition may apply:

- Treat client-bundled secrets, public source maps with sensitive source, or SSR authorization
  bypass as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Vite evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State environment boundaries, public values, build outputs, base and asset behavior, targets,
plugin trust, and production evidence.
