---
name: nestjs
description: Review NestJS plans for module boundaries, provider scope, dependency cycles, validation, guards, interceptors, asynchronous work, and deployment risks. Use when a TypeScript plan changes NestJS applications, modules, controllers, providers, or transports.
---

# NestJS plan review

Apply this guidance alongside the core GrumpyDev review and the `typescript` and
`javascript` skills.

## Inspect evidence

- Establish the exact Node.js, NestJS, TypeScript, adapter, transport, and
  deployment versions.
- Read modules, imports and exports, provider scopes, controllers, pipes,
  guards, interceptors, exception filters, transport setup, and tests.
- Trace request or message data, dependency lifetimes, async initialization,
  transactions, events, background work, and shutdown.

## Establish the operating model

Establish the project target: NestJS, Node and TypeScript versions, HTTP
adapter, transport types, provider scope policy, validation stack, process
topology, and deployment platform. The changed boundary must define: Module
graph, provider scopes, adapters, pipes, guards, interceptors, filters,
validation, serialization, async context, queues, microservices, and shutdown.

Assign lifecycle, state, dependency, persistence, and security ownership for
Module graph, provider scopes, adapters, pipes, guards, interceptors, filters.
Prove validation, serialization, async context, queues, microservices, shutdown
through startup, invalid or denied work, cancellation, background execution,
mixed versions, shutdown, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for provider-scope mistakes, circular dependencies hidden by
forward references, guard and interceptor ordering, validation transforms that
coerce hostile input, lifecycle hooks that do not await completion, and
request-scoped providers multiplying cost.

- Reject hidden dependency cycles and global modules that make ownership,
  testing, or initialization order unclear.
- Verify provider scope and prevent request-scoped dependencies from leaking
  into long-lived consumers or singleton state.
- Check validation pipe options for transformation, whitelisting, unknown
  values, nested objects, and response serialization.
- Require explicit ordering and coverage for guards, pipes, interceptors,
  filters, and transport-specific middleware.
- Test application bootstrap, partial initialization failure, worker or
  microservice shutdown, retries, and built JavaScript artifacts.

## Verify the claims

- Verify these behaviors through the actual NestJS lifecycle and production
  pipeline: Module graph, provider scopes, adapters, pipes, guards,
  interceptors, filters. Use the actual framework pipeline and production build
  with representative services and configuration.
- Exercise failure and edge behavior for: validation, serialization, async
  context, queues, microservices, shutdown. Exercise invalid input, denied
  access, cancellation, dependency failure, concurrent work, shutdown, and
  mixed-version deployment where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Node.js, NestJS, TypeScript, HTTP adapter, transport, and package
  versions apply?
- How do module boundaries, provider scopes, guards, pipes, interceptors,
  validation, and shutdown interact?

## Calibrate findings

- Treat guard bypass, request data in singleton state, or transport retries
  causing irreversible effects as critical.
- Downgrade when scope, pipeline order, transport semantics, and lifecycle are
  covered by integration tests.

## Add to the verdict

State module and provider ownership, validation and authorization pipeline,
initialization and shutdown behavior, transport guarantees, and built-runtime
evidence.
