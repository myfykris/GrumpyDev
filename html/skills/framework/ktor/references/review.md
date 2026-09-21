# Ktor full-review guidance

## Operating conditions

Establish the project target: Ktor, Kotlin and JDK versions, engine,
serialization, authentication, coroutine and dispatcher policy, proxy topology,
and deployment environment. The changed boundary must define: Plugin order,
coroutine context, routing, content negotiation, authentication, serialization,
client and server engines, streaming, shutdown, and deployment.

## Failure patterns

- Verify plugin order and route coverage for authentication, status handling,
  content negotiation, compression, CORS, and observability.
- Keep blocking work off constrained dispatchers and require structured
  ownership for launched coroutines and background services.
- Check serializer configuration, polymorphism, defaults, unknown fields,
  content type, and contract evolution.
- Bound request bodies, streams, concurrency, client pools, timeouts, retries,
  and decompression.
- Test the actual engine and deployment for proxy headers, graceful shutdown,
  connection drain, and mixed-version clients.

## Verification to run or specify in the plan

- Exercise protected routes through the configured plugins and serializers,
  including unsupported content types, unknown fields, and failed
  authentication. Check error responses match the API contract.
- Run the selected server engine with slow dependencies and disconnected
  streams. Verify coroutine cancellation, bounded client pools, and drain
  behavior under the deployment proxy.
