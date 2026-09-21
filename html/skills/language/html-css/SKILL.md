---
name: gd-html-css
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review HTML and CSS engineering work for semantic structure, cascade, layout, responsive behavior, browser support, loading, accessibility, and maintainability risks."
---

# HTML and CSS GrumpyDev review

## Quick checks

- Read rendered HTML, stylesheet entry points, cascade layers, tokens, component
  styles, reset rules, media queries, assets, browser targets, and visual tests.

- Trace document structure, style ownership, intrinsic sizing, overflow, focus
  states, content growth, zoom, print, loading, and failure when CSS or assets
  are unavailable.

Watch especially for visual controls without native semantics, inaccessible
focus order, cascade and specificity fixes that leak globally, layout tied to
one viewport or font metric, browser-default form behavior left implicit, and
content hidden visually but still exposed interactively.

- Assess an inaccessible core task, hidden critical content, or unsafe form
  semantics under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the HTML and CSS
specialist.

## Verdict context

State semantic structure, cascade and layout ownership, responsive and browser
evidence, accessibility boundary, asset-loading behavior, and CSS cost.
