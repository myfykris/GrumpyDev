# Tailwind CSS full-review guidance

## Operating conditions

Establish the project target: Tailwind version, framework and build integration, source roots,
monorepo working directory, theme tokens, plugins, class-generation conventions, browser
targets, CSS ordering, and performance budgets.

## Failure patterns

- Require complete static class tokens for variants or map dynamic inputs to a finite,
  inspectable class table.
- Verify source roots for shared packages, generated templates, registries, and
  working-directory differences in every build environment.
- Keep colors, spacing, typography, breakpoints, z-index, motion, and component states tied to
  maintained design tokens.
- Test keyboard focus, contrast, forced colors, reduced motion, zoom, text scaling, touch
  targets, and print where relevant.
- Inspect final CSS ordering, size, unused growth, plugin output, asset URLs, and conflicts
  with component or vendor styles.

## Verification to run or specify in the plan

- Run the production build from the actual workspace root and inspect expected utilities and
  final CSS size.
- Render representative variants driven by data, shared packages, error states, dark mode,
  forced colors, and responsive breakpoints.
- Test CSS ordering and resets with embedded components, portals, third-party widgets, and
  lazy-loaded routes.
