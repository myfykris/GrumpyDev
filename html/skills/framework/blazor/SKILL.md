---
name: blazor
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Blazor engineering work for rendering mode, circuit or WebAssembly state, dependency lifetimes, JavaScript interop, navigation, security, accessibility, and deployment risks."
---

# Blazor GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `csharp` skill.

## Lean review

- Establish the exact .NET, Blazor, hosting, rendering, and deployment versions
  or modes.

- Read rendering-mode configuration, component routes, service lifetimes,
  authentication state, persistence, JavaScript interop, publish settings, and
  browser tests.

Watch especially for server-circuit state surviving longer than intended,
WebAssembly and server execution assumptions being mixed, prerendering that runs
initialization twice, JavaScript interop after component disposal, and UI
visibility mistaken for authorization.

Lean mode is insufficient when this material severity condition may apply:

- Treat server-only authorization missing, cross-circuit state leakage, or
  unrecoverable core interaction loss as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Blazor evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State rendering mode, state and service lifetimes, authorization boundary,
interop lifecycle, reconnection behavior, and published-browser evidence.
