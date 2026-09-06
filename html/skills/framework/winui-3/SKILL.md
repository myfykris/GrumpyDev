---
name: winui-3
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review WinUI 3 engineering work for Windows App SDK lifecycle, XAML behavior, binding, dispatcher and asynchronous work, activation, navigation, resources, accessibility, packaging, identity, and deployment."
---

# WinUI 3 GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `csharp` or
`cpp`, `windows`, `application-security`, and `testing-strategy` skills. Every
installed companion that remains applicable to the project participates; the
reviewed target does not select the roster. Verify behavior against
the project's declared targets; do not silently substitute the newest version, a
development default, or a neighboring product's semantics.

## Lean review

- Inspect Windows App SDK and target settings, XAML, view models, bindings,
  activation registration, windows, dispatch queues, resources, manifests,
  identity, packaging, bootstrapper, and deployment output.

- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.

Watch especially for packaged and unpackaged identity differences, activation
paths that assume one window, dispatcher access after teardown, compiled and
runtime binding differences, UWP lifecycle rules incorrectly applied to WinUI 3,
and XAML resources resolved only in one packaging mode.

Lean mode is insufficient when this material severity condition may apply:

- Treat an identity or deployment mismatch that prevents launch, unsafe
  activation, inaccessible primary workflow, or state loss during ordinary
  lifecycle events as critical or high according to blast radius and realistic
  likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/activation-identity-and-deployment.md):
  Read when the reviewed work directly or indirectly changes launch or activation kinds,
  multiple instances, multiple
  windows, package identity, packaged versus unpackaged execution, Windows App SDK
  runtime initialization, file or protocol activation, native dependencies, signing,
  installation, update, rollback, repair, or uninstall behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
Windows App SDK lifecycle, XAML, dependency properties, binding, dispatcher and
async behavior, windows, activation, navigation, resources, accessibility,
packaging, and deployment, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
