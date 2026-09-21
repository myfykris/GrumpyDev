# TanStack survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on one or
more TanStack products, including Start, Router, Query, DB, Store, Table, Form,
Virtual, Pacer, AI, Charts, Hotkeys, Markdown, Highlight, Devtools, Config, CLI,
Intent, or related packages.

## Inspect

- Identify every TanStack product and version in use. Classify it as routing or
  full stack, remote data or client state, data presentation or input,
  scheduling or virtualization, AI or content rendering, or development and
  build tooling. Do not assume one product's guarantees apply to another.

## Ask when unresolved

- Which TanStack products and versions apply, which framework and runtime host
  them, and what project concern does each product own?

- For the selected products, which identity, state, persistence, authorization,
  trust, accessibility, performance, build, and deployment rules materially
  affect later reviews?

## Record

Map durable TanStack version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
