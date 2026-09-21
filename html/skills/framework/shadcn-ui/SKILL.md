---
name: gd-shadcn-ui
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review shadcn/ui engineering work for source ownership, registry trust, component composition, accessibility, theming, upgrades, and local divergence."
---

# shadcn/ui GrumpyDev review

## Quick checks

- Read the components configuration, registry sources, installed component source, Radix or
  other primitives, and styling setup.

- Compare local components with upstream assumptions without erasing intentional
  project-specific changes.

Watch especially for blindly overwriting modified components, copying examples
as production state management, trusting third-party registries as executable
source, broken dialog or menu focus after composition, and visual variants that
drop semantics.

- Assess unreviewed executable registry content, broken modal focus, or inaccessible critical
  actions under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the shadcn/ui
specialist.

## Verdict context

State registry sources, owned local code, dependency changes, divergence policy, accessibility
evidence, and update method.
