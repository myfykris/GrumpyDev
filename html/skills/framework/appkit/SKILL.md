---
name: appkit
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review AppKit plans and other engineering artifacts for application and window lifecycle, responder routing, controllers, bindings, drawing, threading, accessibility, sandboxing, state restoration, and termination risks. Project applicability: the project uses or materially depends on AppKit."
---

# AppKit GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

Apply this guidance alongside the core GrumpyDev review and the `swift`,
`objective-c`, `macos`, `application-security`, and `testing-strategy` skills.
Every installed companion that remains applicable to the project participates;
the reviewed target does not select the roster. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Lean review

- Inspect application delegates, scene or window controllers, responders, menus,
  bindings, document controllers, view code, drawing layers, concurrency
  boundaries, entitlements, and distribution settings.

- Inspect generated and rendered artifacts in addition to source. Templates,
  designers, metadata, conventions, and lifecycle callbacks can own behavior
  that is invisible in the main code path.

Watch especially for responder-chain behavior that hides mutations, bindings or
observers that outlive their owners, AppKit access off the main thread,
persistence deferred until a termination callback that may never run, and stale
security-scoped file access.

Lean mode is insufficient when this material severity condition may apply:

- Treat user-data loss, an unsandboxed privilege boundary, an inaccessible core
  workflow, or lifecycle behavior that makes recovery impossible as critical or
  high according to blast radius and realistic likelihood.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/documents-and-state-restoration.md):
  Read when the reviewed work directly or indirectly changes document architecture,
  opening, autosave, undo, conflict
  handling, coordinated access, state restoration, close behavior, or document recovery.
- [Focused rules](references/sandbox-entitlements-and-file-access.md):
  Read when the reviewed work directly or indirectly changes sandboxing, entitlements,
  privacy permissions, security-scoped URLs, helper access, filesystem access,
  automation, hardware access, or denied
  permission behavior.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
application and window lifecycle, responder chain, controllers, bindings,
document architecture, drawing, concurrency, accessibility, state restoration,
SwiftUI interoperability, sandboxing, and termination, verification evidence,
deployment and recovery limits, and any material assumption that remains
unresolved.
