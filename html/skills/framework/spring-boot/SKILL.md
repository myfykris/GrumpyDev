---
name: gd-spring-boot
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Spring Boot engineering work for bean scope, transaction boundaries, proxy behavior, configuration, serialization, security filters, asynchronous work, and deployment risks."
---

# Spring Boot GrumpyDev review

## Quick checks

- Read Boot, Spring, and JVM versions, configuration and profiles, bean
  definitions, security filter chains, persistence, transactions, messaging,
  actuator, and tests.

- Trace requests and jobs through proxies, validation, authorization,
  transactions, async executors, serialization, startup, and shutdown.

Watch especially for proxy-based behavior bypassed by self-invocation,
transaction boundaries that end before asynchronous work, accidental
auto-configuration, blocking calls in reactive paths, configuration precedence
surprises, and management endpoints exposed beyond their trust boundary.

- Assess security-chain bypass, transaction boundary loss, or event-loop blocking
  in a reactive service under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Spring Boot
specialist.

## Verdict context

State bean and proxy model, transaction and authorization boundaries,
configuration sources, asynchronous ownership, and packaged deployment evidence.
