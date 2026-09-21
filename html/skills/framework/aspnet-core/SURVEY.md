# ASP.NET Core survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on ASP.NET Core.

## Inspect

- Establish the exact .NET, C#, ASP.NET Core, server, and hosting versions or
  modes.

## Ask when unresolved

- Which .NET, C#, ASP.NET Core, hosting, server, and deployment versions or
  modes apply?

- How are middleware order, dependency lifetimes, authentication, cancellation,
  errors, and shutdown handled?

- Which runtime or deployment differences are material for future reviews: .NET
  and hosting model, Kestrel, IIS or reverse proxy, in-process or out-of-
  process mode, worker count, forwarded headers, data protection, filesystem,
  deployment, and drain?

## Record

Map durable ASP.NET Core version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
