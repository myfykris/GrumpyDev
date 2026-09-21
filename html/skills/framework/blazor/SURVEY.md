# Blazor survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Blazor.

## Inspect

- Establish the exact .NET, Blazor, hosting, rendering, and deployment versions
  or modes.

## Ask when unresolved

- Which .NET and Blazor versions and hosting mode, rendering mode, and
  deployment target apply?

- How are circuit lifetime, reconnection, state, authorization, prerendering,
  errors, and browser interop handled?

- Which runtime or deployment differences are material for future reviews:
  Server, WebAssembly, hybrid, and prerender modes; circuit topology; sticky
  sessions; client assets; data-protection state; proxy; and deployment
  differences?

## Record

Map durable Blazor version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
