---
name: expo
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review Expo plans and other engineering artifacts for SDK and React Native compatibility, native configuration, EAS builds, updates, permissions, plugins, routing, and release safety. Project applicability: the project uses or materially depends on Expo."
---

# Expo GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `react-native`, `javascript` and
`typescript` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read Expo SDK, React Native, React, router, module, config-plugin, and native project
  versions.

- Identify managed or prebuild workflow, development builds, EAS Build profiles, credentials,
  channels, and runtime versions.

Watch especially for Expo Go treated as production evidence, config plugins that
mutate native projects unpredictably, over-the-air updates crossing native
compatibility, secrets placed in public app config, and permissions tested on
only one platform.

Lean mode is insufficient when this material severity condition may apply:

- Treat signing compromise, secret exposure, incompatible updates that brick a core flow, or
  unsafe permission use as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Expo evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State the SDK and native matrix, workflow, generated changes, update compatibility, permission
behavior, signing owner, and release evidence.
