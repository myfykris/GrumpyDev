---
name: tanstack
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review TanStack plans and other engineering artifacts across Start, Router, Query, DB, Store, Table, Form, Virtual, Pacer, AI, Charts, Hotkeys, Markdown, Highlight, Devtools, Config, CLI, Intent, and related packages for state, data, rendering, authorization, accessibility, performance, build, and deployment risks. Project applicability: the project uses or materially depends on one or more TanStack products."
---

# TanStack GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `react`, `typescript` and `vite`
skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Identify every TanStack product and version in use. Classify it as routing or
  full stack, remote data or client state, data presentation or input,
  scheduling or virtualization, AI or content rendering, or development and
  build tooling. Do not assume one product's guarantees apply to another.

- Inspect the product-specific sources of truth: route trees, loaders, server
  functions and middleware; query clients and keys; DB collections and sync;
  stores and selectors; table, form and virtualizer state; pacer controls; AI
  streams and tools; content renderers; and generated build or configuration
  artifacts.

Watch especially for cross-user cache or dehydrated-state leakage, optimistic
effects without persistence or rollback, server functions trusted because
callers are generated, competing data owners, unstable row or item identities,
async validation races, inaccessible virtualization or table behavior,
debounced work lost on teardown, untrusted model or Markdown output rendered as
safe, development tooling exposed in production, and generated artifacts that
silently diverge from their source.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user data leakage, missing server-function authorization,
  untrusted output reaching an executable or HTML sink, or unreconciled
  irreversible optimistic effects as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete TanStack evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the products in use, source of truth and identity model for each, data and
authorization boundaries, persistence and failure behavior, accessibility and
performance limits, generated-artifact ownership, and representative runtime
evidence.
