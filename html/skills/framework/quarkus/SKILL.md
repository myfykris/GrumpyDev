---
name: quarkus
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Quarkus engineering work for build-time augmentation, CDI scope, reactive and blocking boundaries, native images, configuration, persistence, and deployment risks."
---

# Quarkus GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `java` skill.

## Lean review

- Read Quarkus, Java, and extension versions, build configuration, CDI scopes,
  REST stack, persistence, messaging, native-image settings, and tests.

- Trace request and message execution, blocking work, transactions,
  configuration phases, reflection, serialization, startup, and shutdown.

Watch especially for build-time configuration treated as runtime mutable, CDI
proxy and lifecycle surprises, reflection or resources omitted from native
images, blocking work on reactive threads, and dev-mode behavior used as
evidence for packaged or native deployments.

Lean mode is insufficient when this material severity condition may apply:

- Treat event-loop blocking, scope leakage, or native-only failure on a critical
  deployment as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Quarkus evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State runtime mode, configuration phases, execution and CDI model, native-image
constraints, persistence behavior, and artifact-specific evidence.
