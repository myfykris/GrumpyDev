---
name: vite
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Vite engineering work for client and server environments, dependency handling, environment variables, base paths, production builds, SSR, plugins, browser targets, and deployment."
---

# Vite GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `javascript`, `typescript` and
`dependency-supply-chain` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
