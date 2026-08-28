# Spring Boot standard review

## Establish the operating model

Establish the project target: Spring Boot, Spring and Java versions, servlet or
reactive stack, server, data and messaging dependencies, security model, build
tool, and deployment environment. The changed boundary must define: Application
context, bean scopes, auto-configuration, transactions, persistence, security
filters, validation, messaging, scheduling, actuator, shutdown, and upgrades.

Assign lifecycle, state, dependency, persistence, and security ownership for
Application context, bean scopes, auto-configuration, transactions, persistence,
security filters. Prove validation, messaging, scheduling, actuator, shutdown,
upgrades through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

- Check bean scope, constructor cycles, conditional configuration,
  initialization order, and proxy-dependent annotations invoked through
  self-calls.
- Require explicit transaction boundaries and analyze lazy loading, propagation,
  isolation, retries, and work performed after commit.
- Verify security filter-chain matching, method authorization, CSRF policy,
  request validation, and error-detail exposure.
- Bound executors, queues, connection pools, retries, and scheduled work;
  require cancellation and graceful shutdown.
- Test packaged artifacts with production profiles, database migrations, health
  probes, proxy headers, and rolling-version compatibility.

## Verify the claims

- Verify these behaviors through the actual Spring Boot lifecycle and production
  pipeline: Application context, bean scopes, auto-configuration, transactions,
  persistence, security filters. Use the actual framework pipeline and
  production build with representative services and configuration.
- Exercise failure and edge behavior for: validation, messaging, scheduling,
  actuator, shutdown, upgrades. Exercise invalid input, denied access,
  cancellation, dependency failure, concurrent work, shutdown, and mixed-version
  deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Java, Spring Boot, Spring Framework, servlet or reactive stack, and
  deployment versions apply?
- How do bean scopes, security filters, transactions, retries, async work,
  configuration, and shutdown interact?

## Calibrate findings

- Downgrade when stack-specific scopes, security, transactions, and lifecycle
  are covered by integration tests.
