---
name: gd-quarkus
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Quarkus engineering work for build-time augmentation, CDI scope, reactive and blocking boundaries, native images, configuration, persistence, and deployment risks."
---

# Quarkus GrumpyDev review

## Quick checks

- Read Quarkus, Java, and extension versions, build configuration, CDI scopes,
  REST stack, persistence, messaging, native-image settings, and tests.

- Trace request and message execution, blocking work, transactions,
  configuration phases, reflection, serialization, startup, and shutdown.

Watch especially for build-time configuration treated as runtime mutable, CDI
proxy and lifecycle surprises, reflection or resources omitted from native
images, blocking work on reactive threads, and dev-mode behavior used as
evidence for packaged or native deployments.

- Assess event-loop blocking, scope leakage, or native-only failure on a critical
  deployment under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Quarkus specialist.

## Verdict context

State runtime mode, configuration phases, execution and CDI model, native-image
constraints, persistence behavior, and artifact-specific evidence.
