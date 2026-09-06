---
name: nodejs
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Node.js engineering work for event-loop and worker-pool behavior, modules, packages, async context, streams, buffers, filesystem and process boundaries, workers, signals, native addons, diagnostics, and shutdown."
---

# Node.js GrumpyDev review

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

Coordinate findings with the active language, framework, storage, dependency,
and deployment specialists for the project's Node.js boundaries.

## Lean review

- Establish Node and package-manager versions, module mode, lock policy,
  process and worker topology, operating targets, native addons, runtime flags,
  build output, and deployment form.
- Trace startup, async success and failure, cancellation, streams, worker or
  child-process behavior, signals, shutdown, update, and recovery.
- Challenge event-loop or worker-pool blocking, unowned rejections, lost async
  context, ignored backpressure, unbounded buffers, ESM and CommonJS drift,
  native ABI assumptions, unsafe shell or path handling, and graceful shutdown
  that does not stop admission and drain work.
- Treat lockfiles, lifecycle scripts, optional dependencies, native packages,
  and package-manager versions as build inputs. Verify the effective deployed
  artifact, not a successful developer install.
- Specify encoding and serialization across application, process, native,
  storage, and network boundaries.

Lean mode is insufficient for module-system migration, native addon or runtime
upgrade, worker topology changes, high-volume streaming, child-process command
execution, permission-model changes, or shutdown and rollout redesign.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md)
for the shared detailed review contract.

Load these focused references only when their stated boundary applies:

- [Focused rules](references/modules-packages-and-native-addons.md):
  Read when the reviewed work directly or indirectly changes CommonJS or ESM, package
  type, exports or imports maps,
  loaders, conditional resolution, lockfiles, lifecycle scripts, package-manager
  versions, native addons, optional platform packages, ABI, OS, architecture, build
  output, or reproducible installation.
- [Focused rules](references/async-context-streams-and-backpressure.md):
  Read when the reviewed work directly or indirectly changes promises, callbacks,
  events, timers, async iterators,
  AsyncLocalStorage, abort signals, streams, buffers, pipelines, backpressure,
  half-close, encoding, slow peers, or unbounded in-memory accumulation.
- [Focused rules](references/filesystem-child-processes-and-workers.md):
  Read when the reviewed work directly or indirectly changes paths, permissions,
  symlinks, temporary files, durability,
  file descriptors, child processes, shell use, process arguments, stdio, worker
  threads, shared memory, message transfer, restart, or orphan prevention.
- [Focused rules](references/signals-shutdown-and-deployment.md):
  Read when the reviewed work directly or indirectly changes process managers,
  containers, signals, readiness, admission
  draining, HTTP or upgraded connections, background jobs, telemetry flush, pool
  closure, termination deadlines, runtime flags, permissions, rolling deployment, or
  forced shutdown.

Do not load every focused reference merely because this specialist is installed.
Never load `SURVEY.md` during an ordinary review.

## Add to the verdict

Name the effective Node version, module and package boundary, process topology,
blocking or backpressure risk, and shutdown evidence behind each finding.
