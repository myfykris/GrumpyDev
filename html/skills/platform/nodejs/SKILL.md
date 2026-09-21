---
name: gd-nodejs
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review Node.js engineering work for event-loop and worker-pool behavior, modules, packages, async context, streams, buffers, filesystem and process boundaries, workers, signals, native addons, diagnostics, and shutdown."
---

# Node.js GrumpyDev review

## Quick checks

- Establish Node and package-manager versions, module mode, lock policy,
  process topology, native addons, runtime flags, operating targets, and the
  deployed artifact.
- Trace startup, async failure and cancellation, streams, worker or child
  processes, signals, shutdown, update, and recovery.
- Challenge event-loop or worker-pool blocking, unowned rejections, lost async
  context, ignored backpressure, unbounded buffers, module drift, unsafe path or
  process handling, native ABI assumptions, and shutdown that does not stop
  admission and drain work.
- Specify encoding and serialization across application, process, native,
  storage, and network boundaries.

## References

- For a material Node.js effect or uncertainty in a full review, read
  [review.md](references/review.md).
- For module resolution, package installation, lockfiles, or native addons,
  read [modules-packages-and-native-addons.md](references/modules-packages-and-native-addons.md).
- For async context, promises, streams, buffers, or backpressure, read
  [async-context-streams-and-backpressure.md](references/async-context-streams-and-backpressure.md).
- For filesystem, child-process, or worker boundaries, read
  [filesystem-child-processes-and-workers.md](references/filesystem-child-processes-and-workers.md).
- For signals, process managers, containers, draining, or deployment, read
  [signals-shutdown-and-deployment.md](references/signals-shutdown-and-deployment.md).

## Verdict context

Name the effective Node version, module and package boundary, process topology,
blocking or backpressure risk, and shutdown evidence.
