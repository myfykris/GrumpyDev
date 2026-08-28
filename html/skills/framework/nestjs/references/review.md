# NestJS standard review

## Inspect additional evidence

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when scope, pipeline order, transport semantics, and lifecycle are
  covered by integration tests.
