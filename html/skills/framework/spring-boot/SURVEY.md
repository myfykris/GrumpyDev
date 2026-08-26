# Spring Boot survey contribution

## Applicability

Apply this contribution when a Java or Kotlin plan changes Spring Boot services,
controllers, repositories, jobs, or configuration. Skip it when Spring Boot does
not constrain a supported build, runtime, client, data, deployment, or operating
boundary.

## Inspect before asking

For Spring Boot, inspect framework and runtime declarations, dependency locks,
application bootstrap, generated-code and build settings, routes or UI
composition, persistence and worker configuration, CI workflows, and deployment
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Spring Boot, Spring and Java versions, servlet or
  reactive stack, server, data and messaging dependencies, security model, build
  tool, and deployment environment.
- Review doctrine for: Application context, bean scopes, auto-configuration,
  transactions, persistence, security filters, validation, messaging,
  scheduling, actuator, shutdown, and upgrades.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile guidance: JDK, embedded or external server, servlet or
  reactive mode, proxy, thread pools, configuration authority, actuator
  boundary, packaging, JVM limits, and shutdown.

## Ask only when materially unresolved

- Which Java, Spring Boot, Spring Framework, servlet or reactive stack, and
  deployment versions apply?
- How do bean scopes, security filters, transactions, retries, async work,
  configuration, and shutdown interact?
- Align existing domain questions with this deployment guidance when it is
  material: JDK, embedded or external server, servlet or reactive mode, proxy,
  thread pools, configuration authority, actuator boundary, packaging, JVM
  limits, and shutdown. Do not repeat the core profile confirmation.

## Record in .grump

Record Spring Boot answers in project technology, architecture, runtime,
security, deployment, and verification doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Map existing Spring Boot survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep individual routes, components, temporary feature settings, one-off
migrations, and plan-only implementation choices out of durable Spring Boot
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Spring Boot when framework or runtime versions, lifecycle or rendering
model, dependency scopes, persistence, authentication, workers, supported
clients, or deployment process materially change, when evidence conflicts with
saved doctrine, or when the user requests a context refresh.
