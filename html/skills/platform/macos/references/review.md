# macOS full-review guidance

## Operating conditions

Establish the project target: macOS deployment range, architectures, sandbox and
entitlements, signing ownership, distribution channel, update model, privacy
permissions, and supported hardware. The changed boundary must define:
Application lifecycle, sandbox, entitlements, privacy permissions, signing,
notarization, bundles, launch services, filesystem and keychain boundaries,
updates, compatibility, and crash handling.

## Failure patterns

- Match APIs, frameworks, weak linking, availability checks, deployment target,
  SDK, architecture slices, Rosetta assumptions, and hardware features to every
  supported macOS version and machine class.
- Trace application, window, helper, login item, agent, service, extension, XPC,
  and command-line lifecycle. Define state persistence and recovery for crash,
  force quit, logout, restart, update, and power loss.

## Verification to run or specify in the plan

- Test the oldest and newest supported macOS releases and all supported
  native/Rosetta architecture paths on representative hardware.
- Inspect the final bundle, nested code, signatures, designated requirements,
  entitlements, privacy strings, architecture slices, and minimum OS.
