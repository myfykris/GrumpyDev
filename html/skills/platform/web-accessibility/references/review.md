# Web accessibility full-review guidance

## Operating conditions

Establish the project target: Accessibility target and standard, browser and
assistive-technology matrix, input methods, localization, design-system
constraints, test tooling, and exception process. The changed boundary must
define: Semantic structure, keyboard behavior, focus, names and roles, forms,
errors, contrast, motion, zoom, dynamic updates, media, and assistive testing.

## Failure patterns

- Prefer native elements and semantics; ARIA does not repair a div that behaves
  like a broken button.
- Require logical focus order, visible focus, safe focus movement, escape
  behavior, and no keyboard traps in every interactive state.
- Verify accessible names, headings, landmarks, labels, instructions, error
  association, status announcements, and route-title updates.
- Test contrast, zoom and reflow, target size, color independence, reduced
  motion, captions, and content at realistic lengths.
- Use automated checks as a floor, then require manual keyboard and
  representative assistive-technology evidence for critical flows.

## Verification to run or specify in the plan

- Complete critical flows with keyboard only and with representative screen
  readers across the supported browser matrix. Inspect semantics, names, roles,
  states, focus order, focus movement, errors and live announcements.
- Test zoom and reflow, text spacing, high contrast, reduced motion, target size,
  realistic localized content, delayed updates, validation failure and media
  alternatives.
- Use automated checks as a regression floor, then retain manual evidence for
  interactions whose behavior cannot be established from static markup.
