# shadcn/ui full-review guidance

## Operating conditions

Establish the project target: shadcn/ui generation version and configuration, framework,
registries, primitive libraries, styling and icon systems, component ownership, update policy,
accessibility targets, and accepted local divergence.

## Failure patterns

- Require source review for every registry item, dependency, configuration change, and script
  before it enters the project.
- Record local ownership and update strategy; never assume a later generator run can safely
  replace modified files.
- Verify controlled and uncontrolled state, focus restoration, portal layering, escape
  behavior, keyboard navigation, and screen-reader names.
- Keep design tokens and variants coherent across light, dark, forced-colors, motion, disabled,
  loading, and error states.
- Test composed application behavior rather than treating primitive-library accessibility
  claims as inherited proof.

## Verification to run or specify in the plan

- Diff generated or updated source, dependencies, and configuration, then review the effective
  code committed to the application.
- Exercise dialogs, menus, popovers, forms, tables, toasts, focus traps, reduced motion, and
  high contrast.
- Test local variants and wrapper components with keyboard, screen reader, responsive layouts,
  and application data.
