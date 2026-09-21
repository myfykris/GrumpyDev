# Node.js full-review guidance

## Operating conditions

Establish the project target: Node.js versions, LTS policy, module mode, package
manager, lock policy, worker and process topology, OS and architecture, native
addons, runtime flags, and deployment form. The changed boundary must define:
Event loop and worker pool, modules, packages, async context, streams, buffers,
filesystem and process behavior, workers and child processes, signals, native
addons, permissions, diagnostics, and shutdown.

## Failure patterns

Watch especially for event-loop or worker-pool blocking, rejected promises
without an owner, asynchronous context lost across libraries, streams that
ignore backpressure, ESM and CommonJS resolution differences, native add-ons
tied to one ABI, and signal handling that prevents graceful process exit.

- Keep CPU-heavy JavaScript off the event loop and account for work that
  consumes the shared worker pool, including filesystem, crypto, compression,
  and DNS operations. One blocked loop can stall every request in that process.

## Verification to run or specify in the plan

- Use event-loop delay, CPU, worker-pool, heap, handle, request, stream, and
  native diagnostics under representative load.
- Exercise aborts, client disconnects, slow streams, unhandled errors, worker
  crashes, child-process failures, dependency loss, and forced shutdown.
- Inspect built module resolution, bundled output, native-addon ABI, runtime
  flags, permissions, signals, and container/process-manager behavior.
