# macOS standard review

## Inspect additional evidence

- Establish declared and effective versions in development, CI, test, and every
  supported deployment environment. Record differences that change behavior.
- Trace one representative operation through startup, success, cancellation,
  failure, shutdown, update, and recovery. Include encoding and serialization at
  every application, process, native, storage, and network boundary.
- Prefer observable artifacts, focused experiments, and project documentation
  over assertions based on a framework or product name.

## Establish the operating model

Establish the project target: macOS deployment range, architectures, sandbox and
entitlements, signing ownership, distribution channel, update model, privacy
permissions, and supported hardware. The changed boundary must define:
Application lifecycle, sandbox, entitlements, privacy permissions, signing,
notarization, bundles, launch services, filesystem and keychain boundaries,
updates, compatibility, and crash handling.

Identify the owners and sources of truth for bundle identity, sandbox,
entitlements, privacy usage descriptions, signing, notarization, packaging,
Launch Services registration, updates, keychain access, state restoration, and
crash recovery. Prove the shipped bundle works on every supported macOS version
from a clean machine and that update, downgrade or interrupted replacement does
not break identity, permissions, user data, or launch behavior.

## Challenge the reviewed work

### Recurring traps

- Match APIs, frameworks, weak linking, availability checks, deployment target,
  SDK, architecture slices, Rosetta assumptions, and hardware features to every
  supported macOS version and machine class.
- Trace application, window, helper, login item, agent, service, extension, XPC,
  and command-line lifecycle. Define state persistence and recovery for crash,
  force quit, logout, restart, update, and power loss.
## Verify the claims

- Test the oldest and newest supported macOS releases and all supported
  native/Rosetta architecture paths on representative hardware.
- Inspect the final bundle, nested code, signatures, designated requirements,
  entitlements, privacy strings, architecture slices, and minimum OS.
## Ask when evidence is missing

Ask only when evidence cannot establish the durable target: macOS deployment
range, architectures, sandbox and entitlements, signing ownership, distribution
channel, update model, privacy permissions, and supported hardware. For the
changed boundary, ask only about unresolved Application lifecycle, sandbox,
entitlements, privacy permissions, signing, notarization, bundles, launch
services, filesystem and keychain boundaries, updates, compatibility, and crash
handling when the answer can change the verdict or implementation.

## Calibrate findings

- Treat privilege escalation, unrecoverable deployment, unsupported target
  failure, data loss, or an operating assumption that removes the stated
  availability as material when the reviewed work depends on it and lacks either a safe
  design or credible evidence.
- Downgrade or close findings when target-specific documentation, representative
  builds, focused tests, failure exercises, and recovery evidence establish the
  required behavior.
