---
name: gd-web-accessibility
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review web-accessibility engineering work for semantic structure, keyboard use, focus, names, contrast, motion, forms, live updates, and assistive-technology evidence."
---

# Web accessibility GrumpyDev review

## Quick checks

- Read rendered HTML, interaction states, forms, routing, CSS, content, error
  handling, automated checks, and manual keyboard and screen-reader results.

- Trace a task using keyboard only, zoom, reduced motion, high contrast, a
  screen reader, validation errors, loading, and dynamic updates.

Watch especially for generic elements imitating native controls, keyboard focus
lost after updates, meaning conveyed only by color or position, ARIA overriding
correct native semantics, dynamic changes never announced, focus traps, and
layouts that fail under zoom or text enlargement.

- Assess a blocker that prevents a user from completing a core task or receiving
  critical information under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Web accessibility
specialist.

## Verdict context

State semantic and keyboard behavior, focus management, name and error
contracts, visual accommodations, and manual evidence.
