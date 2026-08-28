# Jetpack Compose survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Jetpack Compose.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
Jetpack Compose. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Compose, Kotlin, and Android plugin versions, minimum and target
  SDK, navigation, state and dependency injection model, lifecycle owners, saved-state policy,
  accessibility targets, supported form factors, and test devices.
- Review doctrine: Compose state is not automatically durable application state. The plan must
  distinguish recomposition state, screen state, saved instance state, persisted data, and
  server authority.
- Conditional deployment boundary: Compose, Kotlin, Android plugin and SDK versions,
  build variants, application ID, signing owner, permissions, form factors, shrinker rules,
  native dependencies, and distribution channel.

## Ask only when materially unresolved

- Which Compose, Kotlin, Android plugin, SDK, navigation, state, and dependency injection
  versions apply?
- How do state, effects, process recreation, accessibility, adaptive layouts, permissions, and
  performance behave?

## Record in .grump

Record confirmed Jetpack Compose answers as project technology, architecture, security,
deployment, verification, and operational doctrine. Preserve source, scope, confidence, and
environment differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Jetpack Compose doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Jetpack Compose when its Compose Compiler or Kotlin version, target platform,
minimum Android API, state ownership, navigation model, lifecycle integration, theme,
or accessibility requirements materially change. Also re-survey when evidence
conflicts with saved doctrine or the user requests a context refresh.
