# Node.js survey contribution

## Applicability

Apply this contribution when the project uses Node.js or when its behavior
constrains a supported build, deployment, client, or operating environment.
Combine it with the `javascript` or `typescript`, framework, storage,
`dependency-supply-chain`, and deployment skills. Deduplicate shared version,
runtime, architecture, identity, data, security, and deployment questions.

## Inspect before asking

Inspect Node and package-manager declarations, lockfiles, module configuration,
runtime flags, entry points, async and stream code, worker or process topology,
native addons, signal handling, diagnostics, build output, and deployment
images, dependency declarations, build and deployment files, CI workflows,
runbooks, and project documentation. Distinguish a committed project fact from a
local-machine default or a transient environment value. Do not access or mutate
an external system merely to complete setup.

## Durable project facts

Collect only durable facts that will improve later reviews:

- Node.js versions and LTS policy.
- ECMAScript module mode.
- Package manager and lock policy.
- Worker, process, and cluster topology.
- Operating systems and architectures.
- Native addons.
- Runtime flags and permissions.
- Deployment form.
- Ownership of configuration, builds, deployment, updates, incidents, and
  recovery, plus meaningful differences among development, CI, test, staging,
  production, worker, desktop, or client environments.
- Required compatibility, security, accessibility, performance, availability,
  and recovery policies that apply across plans in this domain.
- Deployment-profile guidance: Node.js version, module mode, process
  and worker topology, event loop, native add-ons, runtime flags, proxy,
  filesystem, signals, packaging, and deployment coverage.

## Ask only when materially unresolved

Ask only when inspection cannot establish a durable fact above and the answer
will change later Node.js reviews. Candidate subjects are: Node.js versions, LTS
policy, module mode, package manager, lock policy, worker and process topology,
OS and architecture, native addons, runtime flags, and deployment form.
- Align existing domain questions with this deployment guidance when it is
  material: Node.js version, module mode, process and worker topology,
  event loop, native add-ons, runtime flags, proxy, filesystem, signals,
  packaging, and deployment coverage. Do not repeat the core profile
  confirmation.

## Record in .grump

Record Node.js answers in project technology, runtime, security, deployment,
verification, and operational doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Map existing Node.js survey answers to the affected `DEP-###` profile.
Reference a shared `INF-###` component rather than copying its common contract.
Preserve separate state, support, ownership, confidence, source, and scope
fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Node.js
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey after a Node major version or LTS-policy change, package
manager/module mode change, worker/process topology change, native-addon or
OS/architecture change, runtime-permission change, or deployment redesign. Also
refresh the contribution when evidence contradicts saved doctrine or the user
explicitly requests a context refresh.
