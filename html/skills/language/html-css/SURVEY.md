# HTML and CSS survey contribution

## Applicability

Apply this contribution when the project contains or produces web documents, component
markup, stylesheets, design systems, or rendered web content.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

For HTML and CSS, inspect language and runtime declarations, dependency locks,
build files, compiler or interpreter flags, generated-code settings, CI
matrices, native dependencies, packaging, and deployment documentation. Read
existing `.grump` doctrine and project documentation before treating a durable
fact as unresolved.

## Durable project facts

- Target and operating model: Supported browsers and assistive technologies,
  device and viewport range, document encoding, CSS processing, design tokens,
  rendering model, accessibility target, and fallback policy.
- Review doctrine for: Standards and browser behavior, semantic structure,
  cascade and specificity, layout and containment, responsive behavior, forms,
  accessibility, performance, progressive enhancement, and encoding.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Browser and webview targets, base path, static
  serving, proxy and cache behavior, content security policy, asset build,
  localization, and offline requirements.

## Ask only when materially unresolved

- Which browsers, assistive technologies, input modes, languages, zoom levels,
  and rendering constraints are supported?
- How do semantics, source order, focus, responsive layout, overflow, fonts, and
  encoding behave with real content?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Browser and webview targets, base path,
  static serving, proxy and cache behavior, content security policy, asset
  build, localization, and offline requirements? Ask only when evidence and the
  core profile confirmation do not resolve them.

## Record in .grump

Record HTML and CSS answers in project technology, runtime, build,
compatibility, and deployment doctrine. Preserve source and scope. Record a
material unknown as unresolved doctrine instead of guessing.

Record confirmed HTML and CSS deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep local tool paths, one-off build flags, transient process details, and
plan-only implementation choices out of durable HTML and CSS doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey HTML and CSS when supported language or runtime versions, compiler,
standard library, package tool, operating systems, architectures, build modes,
concurrency model, native dependencies, or deployment form materially change,
when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
