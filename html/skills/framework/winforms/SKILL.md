---
name: winforms
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Windows Forms engineering work for control lifetime, UI-thread behavior, events, data binding, scaling, resources, asynchronous work, native interoperability, accessibility, configuration, and deployment."
---

# Windows Forms GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `csharp`,
`windows`, `application-security`, and `testing-strategy` skills. Every installed
companion that remains applicable to the project participates; the reviewed
target does not select the roster. Verify behavior against the project's
declared targets; do not silently substitute the newest version, a development
default, or a neighboring product's semantics.

## Lean review

- Inspect target frameworks, forms and controls, designer files, event wiring,
  data bindings, synchronization contexts, resources, manifests, DPI settings,
  native interop, installers, and update configuration.

- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.

Watch especially for synchronous Invoke deadlocks, event subscriptions retaining
controls, async-void failures, DPI and layout assumptions baked into designer
output, resources drifting across localization, and deployment bitness that
breaks native interop.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-thread corruption, inaccessible primary UI, destructive
  configuration migration, or deployment behavior that prevents safe startup or
  recovery as critical or high according to blast radius and realistic
  likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/native-interop-packaging-and-updates.md):
  Read when the reviewed work directly or indirectly changes P/Invoke, COM, ActiveX,
  handles, native ownership,
  architecture, string encoding, registration, application settings migration,
  packaging, signing, install scope, repair, update, rollback, or uninstall behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
control and window lifetime, UI thread, message loop, events, data binding,
scaling, resources, async work, interoperability, accessibility, configuration,
and deployment, verification evidence, deployment and recovery limits, and any
material assumption that remains unresolved.
