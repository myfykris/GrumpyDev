---
name: svelte
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Svelte and SvelteKit plans and other engineering artifacts for reactivity, server and client boundaries, load functions, form actions, hooks, adapters, rendering, and deployment. Project applicability: the project uses or materially depends on Svelte and SvelteKit."
---

# Svelte and SvelteKit GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `javascript`, `typescript` and
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

- Read Svelte, SvelteKit, adapter, Vite, and package versions plus route and rendering
  configuration.

- Trace runes or legacy reactivity, component state, load functions, form actions, remote
  calls, endpoints, hooks, and stores.

Watch especially for secrets imported into universal modules, browser-only
values causing hydration mismatch, form actions assumed protected by page
guards, stale data after actions, streamed promises failing late, and adapter
differences ignored.

Lean mode is insufficient when this material severity condition may apply:

- Treat secret leakage, missing action authorization, cross-user cache leakage, or unsafe
  offline private data as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Svelte and SvelteKit evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State route modes, data and authorization boundaries, reactive ownership, adapter assumptions,
cache behavior, and production evidence.
