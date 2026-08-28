# FastAPI standard review

## Establish the operating model

Establish the project target: FastAPI, Pydantic and Python versions, ASGI
server, worker model, proxy path, schema consumers, dependency lifetimes, and
deployment topology. The changed boundary must define: Dependency scopes, async
and blocking work, Pydantic validation, OpenAPI contracts, lifespan, background
tasks, streaming, errors, workers, and deployment.

Assign lifecycle, state, dependency, persistence, and security ownership for
Dependency scopes, async and blocking work, Pydantic validation, OpenAPI
contracts, lifespan. Prove background tasks, streaming, errors, workers,
deployment through startup, invalid or denied work, cancellation, background
execution, mixed versions, shutdown, rollback, and recovery.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the actual FastAPI lifecycle and production
  pipeline: Dependency scopes, async and blocking work, Pydantic validation,
  OpenAPI contracts, lifespan. Use the actual framework pipeline and production
  build with representative services and configuration.
- Exercise failure and edge behavior for: background tasks, streaming, errors,
  workers, deployment. Exercise invalid input, denied access, cancellation,
  dependency failure, concurrent work, shutdown, and mixed-version deployment
  where plausible.
- Inspect effective configuration, generated output, persistence effects, and
  deployable artifacts, then rehearse recovery from irreversible steps.

## Ask when evidence is missing

- Which Python, FastAPI, Starlette, and Pydantic versions and server-worker
  model apply?
- How do validation, dependency lifetimes, sync work, async cancellation,
  errors, and schema compatibility behave?

## Calibrate findings

- Downgrade when exact-version behavior, dependency order, limits, and async
  failure paths are tested.
