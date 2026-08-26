---
name: tailwind-css
description: Review Tailwind CSS plans for source detection, generated utilities, design tokens, responsive states, accessibility, build size, and integration boundaries. Use when a plan changes Tailwind configuration or utility-based styling.
---

# Tailwind CSS plan review

Apply this guidance alongside the core GrumpyDev review and the `html-css` and
`web-accessibility` skills.

## Inspect evidence

- Read the Tailwind version, CSS entrypoints, source detection, theme tokens, plugins,
  framework integration, and build command.
- Trace class names produced by templates, component variants, content data, libraries,
  monorepos, and generated files.
- Inspect responsive, dark, forced-color, motion, print, hover, focus, disabled, loading,
  error, and high-contrast states.
- Review arbitrary values, important rules, resets, third-party CSS ordering, asset paths, and
  final generated CSS.

## Establish the operating model

Establish the project target: Tailwind version, framework and build integration, source roots,
monorepo working directory, theme tokens, plugins, class-generation conventions, browser
targets, CSS ordering, and performance budgets.

Tailwind scans source text, not runtime values. Every class needed in production must appear in
detectable source or an explicit source or safelist rule.

## Challenge the plan

### Recurring traps

Watch especially for dynamically assembled class names disappearing from production CSS,
monorepo packages omitted from scanning, broad safelists bloating output, preflight breaking
embedded widgets, and arbitrary values bypassing design tokens.

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

## Verify the claims

- Run the production build from the actual workspace root and inspect expected utilities and
  final CSS size.
- Render representative variants driven by data, shared packages, error states, dark mode,
  forced colors, and responsive breakpoints.
- Test CSS ordering and resets with embedded components, portals, third-party widgets, and
  lazy-loaded routes.

## Ask when evidence is missing

- Which Tailwind version, framework integration, source roots, theme tokens, plugins, and
  browser targets apply?
- How are dynamic variants, shared packages, production scanning, accessibility states, CSS
  ordering, and size verified?

## Calibrate findings

- Treat invisible focus, unreadable critical content, or missing production styles that block a
  core flow as critical.
- Downgrade when source detection, tokens, state coverage, accessibility, ordering, and
  production CSS are verified.

## Add to the verdict

State source roots, dynamic-class policy, token ownership, accessibility states, final CSS size,
and production-build evidence.
