# Spring Boot survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Spring Boot.

## Inspect

- Read Boot, Spring, and JVM versions, configuration and profiles, bean
  definitions, security filter chains, persistence, transactions, messaging,
  actuator, and tests.

## Ask when unresolved

- Which Java, Spring Boot, Spring Framework, servlet or reactive stack, and
  deployment versions apply?

- How do bean scopes, security filters, transactions, retries, async work,
  configuration, and shutdown interact?

- Which runtime or deployment differences are material for future reviews: JDK,
  embedded or external server, servlet or reactive mode, proxy, thread pools,
  configuration authority, actuator boundary, packaging, JVM limits, and
  shutdown?

## Record

Map durable Spring Boot version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
