---
name: shadcn-ui
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review shadcn/ui engineering work for source ownership, registry trust, component composition, accessibility, theming, upgrades, and local divergence."
---

# shadcn/ui GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `react`, `tailwind-css` and
`web-accessibility` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read the components configuration, registry sources, installed component source, Radix or
  other primitives, and styling setup.

- Compare local components with upstream assumptions without erasing intentional
  project-specific changes.

Watch especially for blindly overwriting modified components, copying examples
as production state management, trusting third-party registries as executable
source, broken dialog or menu focus after composition, and visual variants that
drop semantics.

Lean mode is insufficient when this material severity condition may apply:

- Treat unreviewed executable registry content, broken modal focus, or inaccessible critical
  actions as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete shadcn/ui evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State registry sources, owned local code, dependency changes, divergence policy, accessibility
evidence, and update method.
