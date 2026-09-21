---
name: gd-tailwind-css
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Tailwind CSS engineering work for source detection, generated utilities, design tokens, responsive states, accessibility, build size, and integration boundaries."
---

# Tailwind CSS GrumpyDev review

## Quick checks

- Read the Tailwind version, CSS entrypoints, source detection, theme tokens, plugins,
  framework integration, and build command.

- Trace class names produced by templates, component variants, content data, libraries,
  monorepos, and generated files.

Watch especially for dynamically assembled class names disappearing from
production CSS, monorepo packages omitted from scanning, broad safelists
bloating output, preflight breaking embedded widgets, and arbitrary values
bypassing design tokens.

- Assess invisible focus, unreadable critical content, or missing production styles that block a
  core flow under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Tailwind CSS
specialist.

## Verdict context

State source roots, dynamic-class policy, token ownership, accessibility states, final CSS size,
and production-build evidence.
