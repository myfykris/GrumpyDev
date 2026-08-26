# Web accessibility survey contribution

## Applicability

Apply this contribution when a plan creates or changes user-facing web
interfaces. Skip it when Web accessibility does not constrain a supported build,
runtime, client, data, deployment, or operating boundary.

## Inspect before asking

For Web accessibility, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Accessibility target and standard, browser and
  assistive-technology matrix, input methods, localization, design-system
  constraints, test tooling, and exception process.
- Review doctrine for: Semantic structure, keyboard behavior, focus, names and
  roles, forms, errors, contrast, motion, zoom, dynamic updates, media, and
  assistive testing.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Conditional deployment boundary: Record supported browsers, webviews,
  assistive technologies, input modes, operating systems, rendering modes, and
  content delivery only when they affect the accessibility target.

## Ask only when materially unresolved

- Which changed interactions must work by keyboard, screen reader, zoom, reduced
  motion, and high-contrast settings?
- How are focus, accessible names, errors, live updates, and semantic
  relationships verified?
- Do not add a standing infrastructure question for this specialist. Record
  supported browsers, webviews, assistive technologies, input modes, operating
  systems, rendering modes, and content delivery only when they affect the
  accessibility target.

## Record in .grump

Record Web accessibility answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

If the Web accessibility boundary becomes material, record it on the affected
`DEP-###` profile or referenced `INF-###` component. Preserve separate state,
support, ownership, confidence, source, and scope fields. Otherwise add no
infrastructure doctrine for this contribution.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable Web
accessibility doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey Web accessibility when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
