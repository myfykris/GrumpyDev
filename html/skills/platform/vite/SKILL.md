---
name: gd-vite
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Vite engineering work for client and server environments, dependency handling, environment variables, base paths, production builds, SSR, plugins, browser targets, and deployment."
---

# Vite GrumpyDev review

## Quick checks

- Read Vite, framework plugin, runtime, package manager, TypeScript, browser target, and
  test-tool versions.

- Trace client, SSR, build, development, worker, and custom environment modules plus
  environment-variable exposure.

Watch especially for secrets exposed through client environment prefixes,
root-relative assets failing under subpaths, dependencies working only after dev
optimization, SSR importing browser-only modules, plugin order changing
transforms, and one build assumed valid for client and server.

- Assess client-bundled secrets, public source maps with sensitive source, or SSR authorization
  bypass under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Vite specialist.

## Verdict context

State environment boundaries, public values, build outputs, base and asset behavior, targets,
plugin trust, and production evidence.
