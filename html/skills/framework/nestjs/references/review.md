# NestJS full-review guidance

## Operating conditions

Establish the project target: NestJS, Node and TypeScript versions, HTTP
adapter, transport types, provider scope policy, validation stack, process
topology, and deployment platform. The changed boundary must define: Module
graph, provider scopes, adapters, pipes, guards, interceptors, filters,
validation, serialization, async context, queues, microservices, and shutdown.

## Failure patterns

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

## Verification to run or specify in the plan

- Exercise protected operations through the actual HTTP, queue, or
  microservice transport in use. Check guard, pipe, interceptor, and filter
  ordering with malformed input and concurrent identities.
- Boot and stop the built application with a dependency failing during
  initialization or work in flight. Verify provider lifetimes, cleanup hooks,
  and retry ownership without development-only loading.
