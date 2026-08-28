# Windows standard review

## Inspect additional evidence

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

Identify owners and sources of truth for process and service identity, ACLs,
registry and filesystem state, COM or WinRT registration, package identity,
activation, architecture, signing, installer or Store packaging, updates,
logging, crash handling and recovery. Prove install, update, downgrade,
uninstall and restart under ordinary user privileges on every supported Windows
version without leaving privileged writable paths or unrecoverable state.

## Challenge the reviewed work

### Recurring traps

- Verify API, SDK, runtime, architecture, edition, policy, and feature
  assumptions on every supported Windows version. Development mode,
  administrator rights, or an installed SDK can hide missing deployment
  dependencies.
- Apply least-privilege ACLs to installation, program data, user data, logs,
  named pipes, services, registry keys, certificates, and update locations.
  Avoid writable executable search paths and privileged consumers of
  low-integrity data.
- Separate machine, user, roaming, package, and portable state. Handle path
  normalization, drive and UNC paths, long paths, reparse points, case behavior,
  sharing modes, antivirus interference, atomic replacement, and full disk.
## Verify the claims

- Test supported Windows versions and editions under ordinary user privileges,
  denied ACL paths, long and UNC paths, reparse points, file locks, antivirus
  delay, registry redirection, and low-disk conditions where applicable.

## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: Windows versions and
editions, architectures, app model, packaging and identity, installer or store
channel, service use, privilege requirements, signing, and update policy. For
the changed boundary, ask only about unresolved Processes, services, identity,
ACLs, registry, filesystems, COM and WinRT, application identity, packaging,
activation, architecture, updates, logging, crash handling, and recovery when
the answer can change the verdict or implementation.

## Calibrate findings

- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the reviewed work depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
