---
name: web-accessibility
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review web-accessibility plans and other engineering artifacts for semantic structure, keyboard use, focus, names, contrast, motion, forms, live updates, and assistive-technology evidence. Project applicability: the project includes user-facing web interfaces or rendered web content."
---

# Web accessibility GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the relevant web
framework skill.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read rendered HTML, interaction states, forms, routing, CSS, content, error
  handling, automated checks, and manual keyboard and screen-reader results.

- Trace a task using keyboard only, zoom, reduced motion, high contrast, a
  screen reader, validation errors, loading, and dynamic updates.

Watch especially for generic elements imitating native controls, keyboard focus
lost after updates, meaning conveyed only by color or position, ARIA overriding
correct native semantics, dynamic changes never announced, focus traps, and
layouts that fail under zoom or text enlargement.

Lean mode is insufficient when this material severity condition may apply:

- Treat a blocker that prevents a user from completing a core task or receiving
  critical information as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Web accessibility evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State semantic and keyboard behavior, focus management, name and error
contracts, visual accommodations, and manual evidence.
