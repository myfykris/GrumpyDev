# Node.js standard review

Apply this guidance alongside the core GrumpyDev review and the `javascript` or
`typescript`, framework, storage, `dependency-supply-chain`, and deployment
skills. Every installed companion that remains applicable to the project
participates; the reviewed target does not select the roster. Verify behavior
against the project's declared targets; do not silently substitute the newest
version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect Node and package-manager declarations, lockfiles, module
  configuration, runtime flags, entry points, async and stream code, worker or
  process topology, native addons, signal handling, diagnostics, build output,
  and deployment images.
- Inspect the effective built, installed, or rendered result.
  Development-machine state and source configuration can hide dependencies or
  policies that the deployed system will not have.
- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: Node.js versions, LTS policy, module mode, package
manager, lock policy, worker and process topology, OS and architecture, native
addons, runtime flags, and deployment form. The changed boundary must define:
Event loop and worker pool, modules, packages, async context, streams, buffers,
filesystem and process behavior, workers and child processes, signals, native
addons, permissions, diagnostics, and shutdown.

Identify the exact runtime and module mode, package and lockfile authority,
native addon and platform builds, process manager, worker and child-process
ownership, filesystem and network permissions, diagnostics, signal handling,
and shutdown contract. Prove event-loop and worker-pool saturation, stream
backpressure, rejected async work, native failure and termination do not lose
required work or leave the process silently unhealthy.

## Challenge the reviewed work

### Recurring traps

Watch especially for event-loop or worker-pool blocking, rejected promises
without an owner, asynchronous context lost across libraries, streams that
ignore backpressure, ESM and CommonJS resolution differences, native add-ons
tied to one ABI, and signal handling that prevents graceful process exit.

- Keep CPU-heavy JavaScript off the event loop and account for work that
  consumes the shared worker pool, including filesystem, crypto, compression,
  and DNS operations. One blocked loop can stall every request in that process.
## Verify the claims

- Use event-loop delay, CPU, worker-pool, heap, handle, request, stream, and
  native diagnostics under representative load.
- Exercise aborts, client disconnects, slow streams, unhandled errors, worker
  crashes, child-process failures, dependency loss, and forced shutdown.
- Inspect built module resolution, bundled output, native-addon ABI, runtime
  flags, permissions, signals, and container/process-manager behavior.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Node.js versions,
LTS policy, module mode, package manager, lock policy, worker and process
topology, OS and architecture, native addons, runtime flags, and deployment
form. For the changed boundary, ask only about unresolved Event loop and worker
pool, modules, packages, async context, streams, buffers, filesystem and process
behavior, workers and child processes, signals, native addons, permissions,
diagnostics, and shutdown when the answer can change the verdict or
implementation.

## Calibrate findings

- Treat remote code execution, event-loop starvation that destroys availability,
  unbounded memory growth, unsafe child-process invocation, or shutdown behavior
  that loses committed work as critical or high according to blast radius and
  realistic likelihood.
- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the reviewed work depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
event loop and worker pool, modules, packages, async context, streams, buffers,
filesystem and process behavior, workers and child processes, signals, native
addons, permissions, diagnostics, and shutdown, verification evidence,
deployment and recovery limits, and any material assumption that remains
unresolved.
