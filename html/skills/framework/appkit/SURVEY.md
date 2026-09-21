# AppKit survey contribution

## Applies when

Apply this contribution when the project uses AppKit or when its behavior constrains a
supported build, deployment, client, or operating environment.

## Inspect

- Inspect application delegates, scene or window controllers, responders, menus,
  bindings, document controllers, view code, drawing layers, concurrency
  boundaries, entitlements, and distribution settings.

## Ask when unresolved

- Which of these durable facts materially change future reviews: AppKit and
  macOS deployment targets, Swift or Objective-C use, lifecycle model, document
  model, sandbox and entitlements, persistence, accessibility targets, and
  distribution?

- Which runtime or deployment differences are material for future reviews:
  macOS range, architectures, sandbox, entitlements, helpers, document and file
  access, signing, notarization, packaging, update, and distribution?

## Record

Map durable AppKit version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
