---
name: astro
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Astro engineering work for rendering mode, islands, hydration, adapters, server endpoints, content, caching, and deployment boundaries."
---

# Astro GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `javascript`, `typescript` and
`web-accessibility` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
