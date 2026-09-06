---
name: tailwind-css
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Tailwind CSS engineering work for source detection, generated utilities, design tokens, responsive states, accessibility, build size, and integration boundaries."
---

# Tailwind CSS GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `html-css` and
`web-accessibility` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read the Tailwind version, CSS entrypoints, source detection, theme tokens, plugins,
  framework integration, and build command.

- Trace class names produced by templates, component variants, content data, libraries,
  monorepos, and generated files.

Watch especially for dynamically assembled class names disappearing from
production CSS, monorepo packages omitted from scanning, broad safelists
bloating output, preflight breaking embedded widgets, and arbitrary values
bypassing design tokens.

Lean mode is insufficient when this material severity condition may apply:

- Treat invisible focus, unreadable critical content, or missing production styles that block a
  core flow as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Tailwind CSS evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State source roots, dynamic-class policy, token ownership, accessibility states, final CSS size,
and production-build evidence.
