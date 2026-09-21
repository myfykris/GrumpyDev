# FastAPI full-review guidance

## Operating conditions

Establish the project target: FastAPI, Pydantic and Python versions, ASGI
server, worker model, proxy path, schema consumers, dependency lifetimes, and
deployment topology. The changed boundary must define: Dependency scopes, async
and blocking work, Pydantic validation, OpenAPI contracts, lifespan, background
tasks, streaming, errors, workers, and deployment.

## Failure patterns

- Check whether blocking database, filesystem, SDK, or CPU work enters the event
  loop and how concurrency is bounded.
- Require correct dependency scope and cleanup for sessions, clients, files, and
  resources during exceptions and cancellation.
- Treat validation coercion, aliases, defaults, extra fields, response
  filtering, and Pydantic-version behavior as public contract choices.
- Reject in-process background tasks for work that must survive process loss;
  define durable ownership and retry behavior.
- Test generated OpenAPI, error schemas, lifespan, worker deployment, graceful
  drain, and mixed-version clients.

## Verification to run or specify in the plan

- Call endpoints with coercible, extra, missing, and privileged fields;
  compare validation, response filtering, and error responses with the
  generated OpenAPI contract.
- Fail dependencies, disconnect streaming clients, and stop workers during
  pending work. Check dependency cleanup, event-loop responsiveness, lifespan
  behavior, and recovery for work that must survive process loss.
