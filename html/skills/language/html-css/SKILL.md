---
name: html-css
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review HTML and CSS plans and other engineering artifacts for semantic structure, cascade, layout, responsive behavior, browser support, loading, accessibility, and maintainability risks. Project applicability: the project contains or produces web documents, component markup, stylesheets, design systems, or rendered web content."
---

# HTML and CSS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review, the `web-accessibility`
skill, and the applicable installed web-framework specialist.

## Lean review

- Read rendered HTML, stylesheet entry points, cascade layers, tokens, component
  styles, reset rules, media queries, assets, browser targets, and visual tests.

- Trace document structure, style ownership, intrinsic sizing, overflow, focus
  states, content growth, zoom, print, loading, and failure when CSS or assets
  are unavailable.

Watch especially for visual controls without native semantics, inaccessible
focus order, cascade and specificity fixes that leak globally, layout tied to
one viewport or font metric, browser-default form behavior left implicit, and
content hidden visually but still exposed interactively.

Lean mode is insufficient when this material severity condition may apply:

- Treat an inaccessible core task, hidden critical content, or unsafe form
  semantics as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete HTML and CSS evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State semantic structure, cascade and layout ownership, responsive and browser
evidence, accessibility boundary, asset-loading behavior, and CSS cost.
