# Android survey contribution

## Applicability

Apply this contribution when software targets android devices. Skip it when Android does not
constrain a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Android. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Minimum and target SDK, device and form-factor support, Android
  plugin and build tools, UI toolkit, process and task model, permissions, exported components,
  storage and backup policy, background execution, signing, application ID, and release
  channels.
- Review doctrine: Android may destroy and recreate processes without preserving in-memory
  state. The plan must distinguish saved UI state, durable local data, account-scoped data,
  server authority, and work that can safely resume.
- Deployment-profile facts: SDK and build-tool versions, device matrix, application
  ID, build variants, permissions, exported components, network policy, storage and backup
  rules, signing, shrinker configuration, and release tracks.

## Ask only when materially unresolved

- Which Android SDK levels, devices, UI toolkit, process model, permissions, background work,
  and storage apply?
- How are exported components, deep links, backups, accessibility, signing, upgrades, rollback,
  and policy changes handled?

## Record in .grump

Record confirmed Android answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Android doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Android when its version, target platform, execution model, trust boundary, deployment
topology, persistent state, update process, or recovery policy materially changes, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
