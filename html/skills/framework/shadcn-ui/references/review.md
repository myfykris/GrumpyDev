# shadcn/ui standard review

## Inspect additional evidence

- Trace composition, controlled state, focus, portals, overlays, forms, validation, keyboard
  behavior, and responsive layout.
- Inspect registry authentication, fetched dependencies, post-install changes, license data,
  and review provenance.

## Establish the operating model

Establish the project target: shadcn/ui generation version and configuration, framework,
registries, primitive libraries, styling and icon systems, component ownership, update policy,
accessibility targets, and accepted local divergence.

Installed components are application source code, not a centrally upgraded binary library. The
project owns their behavior, security, accessibility, tests, and future merges.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Diff generated or updated source, dependencies, and configuration, then review the effective
  code committed to the application.
- Exercise dialogs, menus, popovers, forms, tables, toasts, focus traps, reduced motion, and
  high contrast.
- Test local variants and wrapper components with keyboard, screen reader, responsive layouts,
  and application data.

## Ask when evidence is missing

- Which shadcn/ui setup, framework, registries, primitives, styling system, and local component
  modifications apply?
- Who owns registry trust, source review, upgrades, accessibility, design tokens, and merge
  behavior?

## Calibrate findings

- Downgrade when source provenance, local ownership, composition, accessibility, and update
  diffs are tested.
