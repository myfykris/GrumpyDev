# Expo survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Expo.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
Expo. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Expo SDK and React Native versions, target platforms, workflow,
  native directories, EAS profiles, signing ownership, update channels and runtime policy,
  router, plugins, permissions, and minimum OS versions.
- Review doctrine: The plan must distinguish JavaScript updates from native binary changes.
  Runtime version policy must prevent an update from loading on an incompatible binary.
- Conditional deployment boundary: Expo SDK and native versions, build profiles,
  credentials owner, application identifiers, update channels, runtime policy, store targets,
  environment sources, native plugins, and rollback path.

## Ask only when materially unresolved

- Which Expo SDK, React Native version, platforms, workflow, native modules, EAS profiles, and
  minimum OS versions apply?
- What runtime-version, channel, rollout, rollback, signing, permission, and
  generated-native-code policy applies?

## Record in .grump

Record confirmed Expo answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Expo doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Expo when its SDK or React Native version, native project ownership, build
profile, update channel or runtime version, target platform, permission set, or deep
link contract materially changes. Also re-survey when evidence conflicts with saved
doctrine or the user requests a context refresh.
