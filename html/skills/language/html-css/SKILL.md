---
name: html-css
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review HTML and CSS engineering work for semantic structure, cascade, layout, responsive behavior, browser support, loading, accessibility, and maintainability risks."
---

# HTML and CSS GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
