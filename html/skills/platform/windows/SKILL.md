---
name: windows
description: Review Windows plans for process, service, identity, ACL, registry, filesystem, COM and WinRT, application identity, packaging, activation, architecture, update, logging, crash, and recovery risks. Use when software depends on Windows desktop or server behavior.
---

# Windows plan review

Apply this guidance alongside the core GrumpyDev review and the implementation
language, UI framework, `application-security`, packaging, and deployment
skills. Select only companions that match the plan's real boundaries. Verify
behavior against the project's declared targets; do not silently substitute the
newest version, a development default, or a neighboring product's semantics.

## Inspect evidence

- Inspect supported Windows versions and architectures, manifests, services,
  users and service accounts, ACLs, registry use, files, COM/WinRT registration,
  package identity, installers, signatures, updates, event logs, dumps, and
  recovery runbooks.
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

Establish the project target: Windows versions and editions, architectures, app
model, packaging and identity, installer or store channel, service use,
privilege requirements, signing, and update policy. The changed boundary must
define: Processes, services, identity, ACLs, registry, filesystems, COM and
WinRT, application identity, packaging, activation, architecture, updates,
logging, crash handling, and recovery.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Processes, services, identity, ACLs, registry,
filesystems, COM and WinRT, application identity. Prove packaging, activation,
architecture, updates, logging, crash handling, recovery through rotation,
overload, partial rollout, drain, forced stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for ACLs evaluated under the wrong identity, path normalization
and case assumptions, services interacting with an absent desktop session,
registry-view differences by architecture, UAC virtualization hiding writes, COM
apartment violations, and installers unable to recover from partial updates.

- Verify API, SDK, runtime, architecture, edition, policy, and feature
  assumptions on every supported Windows version. Development mode,
  administrator rights, or an installed SDK can hide missing deployment
  dependencies.
- Define process identity, integrity level, elevation, UAC, service account,
  token, impersonation, privileges, session, job object, environment, working
  directory, and child-process inheritance.
- Apply least-privilege ACLs to installation, program data, user data, logs,
  named pipes, services, registry keys, certificates, and update locations.
  Avoid writable executable search paths and privileged consumers of
  low-integrity data.
- Separate machine, user, roaming, package, and portable state. Handle path
  normalization, drive and UNC paths, long paths, reparse points, case behavior,
  sharing modes, antivirus interference, atomic replacement, and full disk.
- For services, define start dependencies, delayed start, recovery actions,
  readiness, control handling, shutdown timeout, session isolation, credential
  rotation, logging, and upgrade while the service owns files or ports.
- For COM and WinRT, verify apartment model, marshaling, lifetime, registration
  or registration-free activation, threading, architecture, package identity,
  callback reentrancy, and cleanup across process boundaries.
- Choose packaged, unpackaged, installer, Store, portable, or managed
  distribution deliberately. Trace identity, capabilities, registration,
  file/protocol activation, runtime dependencies, signing, repair, uninstall,
  and per-user versus per-machine scope.
- Make updates transactional where possible and define compatibility, process
  shutdown, locked-file handling, settings/data migrations, interrupted
  installation, rollback, signing-key continuity, event logging, dumps, and
  offline recovery.

## Verify the claims

- Test every supported Windows version, edition, architecture, identity,
  privilege, and installation scope on clean machines.
- Exercise install, repair, upgrade, interrupted upgrade, rollback, uninstall,
  reboot, service recovery, activation, and multiple-user scenarios.
- Test ACL denials, UAC boundaries, long/UNC/reparse paths, file locks,
  antivirus delay, low disk, registry redirection, and COM
  apartment/architecture paths.
- Inspect manifests, package identity, capabilities, signatures, ACLs, service
  settings, dependencies, event logs, crash dumps, and recovery media or
  procedures.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Windows versions and
editions, architectures, app model, packaging and identity, installer or store
channel, service use, privilege requirements, signing, and update policy. For
the changed boundary, ask only about unresolved Processes, services, identity,
ACLs, registry, filesystems, COM and WinRT, application identity, packaging,
activation, architecture, updates, logging, crash handling, and recovery when
the answer can change the verdict or implementation.

## Calibrate findings

- Treat privilege escalation, arbitrary code loading, cross-user data exposure,
  destructive update, or platform/identity assumptions that prevent recovery as
  critical or high according to blast radius and realistic likelihood.
- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the plan depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.

## Add to the verdict

State the target versions and modes, operating and ownership model, relevant
processes, services, identity, ACLs, registry, filesystems, COM and WinRT,
application identity, packaging, activation, architecture, updates, logging,
crash handling, and recovery, verification evidence, deployment and recovery
limits, and any material assumption that remains unresolved.
