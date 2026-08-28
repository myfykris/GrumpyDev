# PHP types and boundary data

Read this reference when the reviewed work directly or indirectly changes weak or strict
scalar coercion, union or
nullable types, array shapes, numeric strings, truthiness, JSON conversion, reflection,
magic access, encoding, locale, or data entering from requests, storage, queues, or
environment.

## Types and boundary data

- Trace weak coercion, strict typing boundaries, union and nullable types,
  array-shape assumptions, numeric strings, truthiness, comparison, and JSON
  conversion across public inputs and stored data. `strict_types` affects
  caller-side scalar argument coercion and is not a whole-application runtime
  mode.
- Require explicit validation before converting request, environment, database,
  queue, or deserialized data into domain values. Static analysis annotations do
  not validate runtime payloads.
- Check dynamic properties, magic accessors, reflection, attributes, named
  arguments, and method-signature compatibility against every supported PHP
  version and framework proxy behavior.
- Specify UTF-8 and error behavior at HTML, JSON, database, filesystem, mail,
  subprocess, and logging boundaries. Do not rely on a default locale or
  internal encoding to align independent systems.
