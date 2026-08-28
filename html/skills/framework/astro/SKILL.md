---
name: astro
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Astro plans and other engineering artifacts for rendering mode, islands, hydration, adapters, server endpoints, content, caching, and deployment boundaries. Project applicability: the project uses or materially depends on Astro."
---

# Astro GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `javascript`, `typescript` and
`web-accessibility` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read the Astro, adapter, integration, and UI framework versions plus output mode and route
  settings.

- Classify every changed route as prerendered, on-demand rendered, client island, or server
  island.

Watch especially for adding client hydration to static content, assuming a
server route works under static output, leaking secrets through serialized
island props, adapter behavior treated as portable, and personalized content
cached as public HTML.

Lean mode is insufficient when this material severity condition may apply:

- Treat secret disclosure, missing server authorization, or private responses stored in shared
  caches as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Astro evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State each changed route mode, server and client boundary, adapter assumptions, cache scope,
hydration cost, and production-build evidence.
