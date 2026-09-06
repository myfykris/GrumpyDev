---
name: react-native
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review React Native engineering work for architecture compatibility, native bridges, lifecycle, navigation, state, permissions, performance, accessibility, and release behavior."
---

# React Native GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `react`, `javascript` and
`typescript` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read React Native, React, platform, engine, native module, navigation, and state-library
  versions.

- Identify New Architecture support, code generation, bridged or bridgeless modules, native
  build settings, and minimum OS levels.

Watch especially for old native modules assumed compatible with the New
Architecture, JavaScript-thread stalls hidden by simulators, lifecycle work lost
in background state, navigation state duplicated, and platform permission
differences ignored.

Lean mode is insufficient when this material severity condition may apply:

- Treat unsafe native memory behavior, secret exposure, inaccessible core flows, or lost
  committed data as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete React Native evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State the architecture matrix, native boundaries, lifecycle and state owners, platform
differences, accessibility, and release evidence.
