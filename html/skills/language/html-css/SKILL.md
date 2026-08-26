---
name: html-css
description: Review HTML and CSS plans for semantic structure, cascade, layout, responsive behavior, browser support, loading, accessibility, and maintainability risks. Use when a plan creates or changes web documents, component markup, stylesheets, design systems, or rendered content.
---

# HTML and CSS plan review

Apply this guidance alongside the core GrumpyDev review, the `web-accessibility`
skill, and the applicable installed web-framework specialist.

## Inspect evidence

- Read rendered HTML, stylesheet entry points, cascade layers, tokens, component
  styles, reset rules, media queries, assets, browser targets, and visual tests.
- Trace document structure, style ownership, intrinsic sizing, overflow, focus
  states, content growth, zoom, print, loading, and failure when CSS or assets
  are unavailable.

## Establish the operating model

Establish the project target: Supported browsers and assistive technologies,
device and viewport range, document encoding, CSS processing, design tokens,
rendering model, accessibility target, and fallback policy. The changed boundary
must define: Standards and browser behavior, semantic structure, cascade and
specificity, layout and containment, responsive behavior, forms, accessibility,
performance, progressive enhancement, and encoding.

Define ownership, errors, cancellation, and concurrency for Standards and
browser behavior, semantic structure, cascade and specificity, layout and
containment, responsive behavior. Verify version, package, native,
serialization, and artifact compatibility for forms, accessibility, performance,
progressive enhancement, encoding across every declared target and rollback
path.

## Challenge the plan

### Recurring traps

Watch especially for visual controls without native semantics, inaccessible
focus order, cascade and specificity fixes that leak globally, layout tied to
one viewport or font metric, browser-default form behavior left implicit, and
content hidden visually but still exposed interactively.

- Require valid semantic HTML and native interaction elements before adding
  roles, event handlers, or ARIA repairs.
- Define cascade ownership and selector scope; reject specificity escalation,
  uncontrolled global rules, and `!important` used as ordinary conflict
  resolution.
- Test layout with narrow and wide viewports, zoom, long and translated content,
  missing media, dynamic insertion, and user font settings.
- Check browser targets, feature fallbacks, logical properties, writing
  direction, form controls, print behavior, and forced-color or reduced-motion
  preferences.
- Keep critical rendering, font and image loading, layout stability, unused CSS,
  and generated utility output within measured budgets.

## Verify the claims

- Verify these behaviors through the declared HTML and CSS compiler and runtime
  targets: Standards and browser behavior, semantic structure, cascade and
  specificity, layout and containment, responsive behavior. Use the real
  compiler or interpreter and supported release modes rather than a development
  substitute.
- Exercise failure and edge behavior for: forms, accessibility, performance,
  progressive enhancement, encoding. Exercise boundary values, encoding,
  cancellation, resource exhaustion, concurrency, dependency failure, and
  termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which browsers, assistive technologies, input modes, languages, zoom levels,
  and rendering constraints are supported?
- How do semantics, source order, focus, responsive layout, overflow, fonts, and
  encoding behave with real content?

## Calibrate findings

- Treat an inaccessible core task, hidden critical content, or unsafe form
  semantics as critical.
- Downgrade when the content is decorative or semantic, responsive,
  internationalized, and assistive-technology tests pass.

## Add to the verdict

State semantic structure, cascade and layout ownership, responsive and browser
evidence, accessibility boundary, asset-loading behavior, and CSS cost.
