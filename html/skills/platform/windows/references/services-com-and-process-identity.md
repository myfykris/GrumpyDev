# Windows services, COM, and process identity

Read this reference when the reviewed work directly or indirectly changes Windows
services, service accounts, tokens,
impersonation, privileges, sessions, job objects, child processes, UAC, COM, WinRT,
apartment models, marshaling, registration, process boundaries, service recovery, or
shutdown.

## Review requirements

- Define process identity, integrity level, elevation, UAC, service account,
  token, impersonation, privileges, session, job object, environment, working
  directory, and child-process inheritance.

- For services, define start dependencies, delayed start, recovery actions,
  readiness, control handling, shutdown timeout, session isolation, credential
  rotation, logging, and upgrade while the service owns files or ports.

- For COM and WinRT, verify apartment model, marshaling, lifetime, registration
  or registration-free activation, threading, architecture, package identity,
  callback reentrancy, and cleanup across process boundaries.

## Verify the claims

- Test ACL denials, UAC boundaries, long/UNC/reparse paths, file locks,
  antivirus delay, low disk, registry redirection, and COM
  apartment/architecture paths.
