# Python serialization, execution, and filesystem security

Read this reference when the reviewed work directly or indirectly handles untrusted
pickle, marshal, shelve, YAML,
dynamic import, eval, exec, templates, subprocesses, paths, symlinks, archives,
decompression, XML, images, regexes, or other attacker-controlled parsing.

## Review requirements

- Reject `pickle`, `marshal`, `shelve`, unsafe YAML constructors, and equivalent
  object loading for untrusted data. A signature does not make an executable
  object graph appropriate; use a bounded data schema and explicit types.

- Keep untrusted input out of `eval`, `exec`, dynamic imports, format-driven
  templates, and shell command strings. Pass fixed executables and separated
  arguments, then validate option-like values and the invoked program's own
  argument semantics.

- Constrain filesystem and archive operations to intended roots while covering
  absolute paths, alternate separators, symlinks, temporary-file races, archive
  traversal, special files, and decompression limits.

- Bound request, parser, regular-expression, image, XML, decompression, and
  collection work before allocation or event-loop execution.
