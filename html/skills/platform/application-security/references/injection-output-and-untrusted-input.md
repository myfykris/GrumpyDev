# Application injection, output, and untrusted input

Read this reference when the reviewed work directly or indirectly lets untrusted
data reach HTML, attributes, URLs, CSS, JavaScript, SQL, NoSQL, operating-system
commands, code, templates, dynamic identifiers, parsers, canonicalization, or
other instruction-bearing sinks.

## Review requirements

- Define the complete transformation chain before validating input. Decode and
  normalize once, reject ambiguous or duplicate representations, and validate
  the value the dangerous sink will actually consume.

- Prevent cross-site scripting with output encoding for the exact HTML,
  attribute, URL, CSS, or JavaScript context. Avoid unsafe DOM and template
  sinks, sanitize intentionally supported markup, and use Content Security
  Policy as defense in depth rather than the primary control.

- Prevent SQL, NoSQL, operating-system command, code, and template injection
  with parameterized APIs or fixed command arguments. Allowlist dynamic
  identifiers and operations; escaping and deny lists are not general
  substitutes for separating data from instructions.
