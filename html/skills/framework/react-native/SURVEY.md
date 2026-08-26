# React Native survey contribution

## Applicability

Apply this contribution when a plan builds or changes react native applications. Skip it when
React Native does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
React Native. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: React Native and React versions, New Architecture status,
  JavaScript engine, target platforms and OS versions, native modules, navigation, state
  ownership, build variants, permissions, signing, updates, and release channels.
- Review doctrine: The plan must separate JavaScript-thread work, UI-thread work, native module
  work, and durable platform services. A library claim is not enough without compatibility on
  each target architecture and OS.
- Conditional deployment boundary: React Native, React, engine and architecture
  versions, native toolchains, minimum OS levels, build variants, identifiers, permissions,
  signing, bundle source, updates, and distribution channels.

## Ask only when materially unresolved

- Which React Native, React, engine, architecture, platforms, OS versions, and native modules
  apply?
- How are threads, lifecycle, navigation, permissions, offline state, accessibility, signing,
  and release behavior handled?

## Record in .grump

Record confirmed React Native answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable React Native doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey React Native when its version, target platform, rendering or execution model, trust
boundary, deployment adapter, persistent state, update process, or recovery policy materially
changes, when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
