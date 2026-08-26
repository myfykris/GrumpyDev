---
name: nodejs
description: Review Node.js plans for event-loop and worker-pool behavior, modules, packages, async context, streams, buffers, filesystem and process boundaries, workers, signals, native addons, diagnostics, and shutdown. Use when JavaScript or TypeScript executes on Node.js.
---

# Node.js plan review

Apply this guidance alongside the core GrumpyDev review and the `javascript` or
`typescript`, framework, storage, `dependency-supply-chain`, and deployment
skills. Select only companions that match the plan's real boundaries. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

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

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Event loop and worker pool, modules, packages, async
context, streams, buffers, filesystem and process behavior. Prove workers and
child processes, signals, native addons, permissions, diagnostics, shutdown
through rotation, overload, partial rollout, drain, forced stop, rollback, and
recovery.

## Challenge the plan

### Recurring traps

Watch especially for event-loop or worker-pool blocking, rejected promises
without an owner, asynchronous context lost across libraries, streams that
ignore backpressure, ESM and CommonJS resolution differences, native add-ons
tied to one ABI, and signal handling that prevents graceful process exit.

- Keep CPU-heavy JavaScript off the event loop and account for work that
  consumes the shared worker pool, including filesystem, crypto, compression,
  and DNS operations. One blocked loop can stall every request in that process.
- Trace promises, timers, callbacks, events, async iterators, AsyncLocalStorage,
  abort signals, and unhandled rejection or exception policy. Async context and
  cancellation must survive the actual library boundaries.
- Choose CommonJS and ECMAScript module behavior deliberately. Verify package
  type, exports/imports maps, resolution, file extensions, conditional exports,
  dual-package state, loader hooks, build output, and test execution.
- Treat lockfiles, lifecycle scripts, native addons, optional dependencies,
  platform packages, and package-manager versions as build inputs. A successful
  developer install is not a reproducible deployment.
- Design streams for backpressure, errors, abort, half-close, encoding, buffer
  bounds, pipeline cleanup, and slow peers. Do not concatenate unbounded
  request, file, or child-process output in memory.
- Validate paths, permissions, symlinks, temporary files, atomicity, durability,
  file descriptor lifetime, child-process arguments, shell use, environment,
  stdio, exit, and cross-platform signal differences.
- For worker threads and child processes, define ownership, message
  serialization or transfer, shared memory synchronization, startup failure,
  health, restart, capacity, shutdown, and orphan prevention.
- Handle readiness and shutdown explicitly: stop admission, drain HTTP and
  upgraded connections, cancel or finish jobs, flush bounded telemetry, close
  pools, honor platform signals, and force exit after a justified deadline.

## Verify the claims

- Run the declared Node and package-manager versions on every supported OS and
  architecture from a clean locked install.
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
  availability as material when the plan depends on it and lacks either a safe
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
