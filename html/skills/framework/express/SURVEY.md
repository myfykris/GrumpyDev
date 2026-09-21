# Express survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Express.

## Inspect

- Read application setup, Express and Node versions, routers, middleware order,
  validation, authentication, proxy settings, server timeouts, and integration
  tests.

## Ask when unresolved

- Which Node.js and Express versions, module mode, proxy topology, and server
  runtime apply?

- How do middleware order, trust proxy, body limits, async errors,
  authentication, and shutdown behave?

- Which runtime or deployment differences are material for future reviews:
  Node.js and Express versions, proxy topology, trust proxy, worker or cluster
  model, process manager, sessions, body limits, timeouts, signals, and
  graceful shutdown?

## Record

Map durable Express version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
