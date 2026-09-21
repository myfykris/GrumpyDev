# Windows full-review guidance

## Operating conditions

Establish the project target: Windows versions and editions, architectures, app
model, packaging and identity, installer or store channel, service use,
privilege requirements, signing, and update policy. The changed boundary must
define: Processes, services, identity, ACLs, registry, filesystems, COM and
WinRT, application identity, packaging, activation, architecture, updates,
logging, crash handling, and recovery.

## Failure patterns

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

## Verification to run or specify in the plan

- Test supported Windows versions and editions under ordinary user privileges,
  denied ACL paths, long and UNC paths, reparse points, file locks, antivirus
  delay, registry redirection, and low-disk conditions where applicable.
