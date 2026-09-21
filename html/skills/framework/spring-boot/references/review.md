# Spring Boot full-review guidance

## Operating conditions

Establish the project target: Spring Boot, Spring and Java versions, servlet or
reactive stack, server, data and messaging dependencies, security model, build
tool, and deployment environment. The changed boundary must define: Application
context, bean scopes, auto-configuration, transactions, persistence, security
filters, validation, messaging, scheduling, actuator, shutdown, and upgrades.

## Failure patterns

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

## Verification to run or specify in the plan

- Boot the packaged application with production profiles and verify
  conditional beans and security filter-chain coverage. Exercise
  proxy-dependent transaction and authorization behavior through both external
  calls and relevant self-invocations.
- Fail transactions and scheduled work while executors or connection pools are
  saturated. Verify rollback, retry safety, health reporting, and shutdown
  with the deployed database and migration settings.
