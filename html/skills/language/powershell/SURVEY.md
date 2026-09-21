# PowerShell survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with PowerShell code, artifacts, or runtime behavior.

## Inspect

- Read module manifests, required PowerShell editions and versions, parameter
  declarations, remoting setup, execution policy assumptions, and tests.

## Ask when unresolved

- Which PowerShell edition and version, operating systems, remoting mode,
  execution policy, and module versions apply?

- How do object and text pipelines, quoting, native processes, credentials,
  errors, and encoding cross boundaries?

- Which runtime or deployment differences materially change future reviews:
  PowerShell edition and version, operating system, host process, remoting
  method, execution identity, modules, policy, non-interactive service context,
  and serialization boundary?

## Record

Map durable PowerShell version and compatibility requirements to `Requirements`
or `Constraints`, runtime facts to `Runtime and deployment`, and material gaps
to `Unknowns`.
