---
name: shadcn-ui
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review shadcn/ui plans and other engineering artifacts for source ownership, registry trust, component composition, accessibility, theming, upgrades, and local divergence. Project applicability: the project uses or materially depends on shadcn/ui."
---

# shadcn/ui GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `react`, `tailwind-css` and
`web-accessibility` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

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
