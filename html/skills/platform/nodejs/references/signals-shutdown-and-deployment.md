# Node.js signals, shutdown, and deployment

Read this reference when the reviewed work directly or indirectly changes process
managers, containers, signals,
readiness, admission draining, HTTP or upgraded connections, background jobs, telemetry
flush, pool closure, termination deadlines, runtime flags, permissions, rolling
deployment, or forced shutdown.

## Review requirements

- Handle readiness and shutdown explicitly: stop admission, drain HTTP and
  upgraded connections, cancel or finish jobs, flush bounded telemetry, close
  pools, honor platform signals, and force exit after a justified deadline.
