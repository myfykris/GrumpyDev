# HTML and CSS full-review guidance

## Operating conditions

Establish the project target: Supported browsers and assistive technologies,
device and viewport range, document encoding, CSS processing, design tokens,
rendering model, accessibility target, and fallback policy. The changed boundary
must define: Standards and browser behavior, semantic structure, cascade and
specificity, layout and containment, responsive behavior, forms, accessibility,
performance, progressive enhancement, and encoding.

## Failure patterns

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

## Verification to run or specify in the plan

- Inspect the delivered HTML, CSS, fonts, images, and browser behavior in the
  supported browsers, not only the development preview. Check relevant build
  transformations when the project uses them.
- Verify semantics, accessible names, focus order, keyboard operation, forms,
  error messages, and supported assistive technologies.
- Check layout and readability at supported viewport sizes, enlarged text,
  long content, missing assets, and relevant user preferences.
- Verify encoding, responsive behavior, loading failures, progressive
  enhancement, and rendering or layout-shift claims against actual output.
