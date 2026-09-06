---
name: spring-boot
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Spring Boot engineering work for bean scope, transaction boundaries, proxy behavior, configuration, serialization, security filters, asynchronous work, and deployment risks."
---

# Spring Boot GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Apply this guidance alongside the core GrumpyDev review and the `java` skill.

## Lean review

- Read Boot, Spring, and JVM versions, configuration and profiles, bean
  definitions, security filter chains, persistence, transactions, messaging,
  actuator, and tests.

- Trace requests and jobs through proxies, validation, authorization,
  transactions, async executors, serialization, startup, and shutdown.

Watch especially for proxy-based behavior bypassed by self-invocation,
transaction boundaries that end before asynchronous work, accidental
auto-configuration, blocking calls in reactive paths, configuration precedence
surprises, and management endpoints exposed beyond their trust boundary.

Lean mode is insufficient when this material severity condition may apply:

- Treat security-chain bypass, transaction boundary loss, or event-loop blocking
  in a reactive service as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Spring Boot evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State bean and proxy model, transaction and authorization boundaries,
configuration sources, asynchronous ownership, and packaged deployment evidence.
