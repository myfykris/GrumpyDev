# Application files, uploads, SSRF, and deserialization

Read this reference when the reviewed work directly or indirectly changes file or
archive handling, uploads, path
resolution, symlinks, temporary files, decompression, server-side URL fetching,
redirects, DNS resolution, private network access, object deserialization, or schema and
allocation limits.

## Review requirements

- Constrain file reads, writes, and archive extraction to an intended root or
  object authority. Cover absolute and alternate paths, traversal, symlinks,
  archive entries, replacement races, filename collisions, and cleanup.

- Treat uploads as untrusted content. Bound bytes, item count, nesting, and
  decompression; establish type from content where relevant; store outside an
  executable web path; randomize server names; scan or transform when the risk
  requires it; and serve with safe type and disposition headers.

- For every server-side URL fetch, allow only required schemes, destinations,
  ports, redirects, and response sizes. Recheck resolved addresses, block local,
  link-local, metadata, and private ranges when not explicitly required, and
  enforce network egress boundaries plus timeouts.

- Reject unsafe deserialization of attacker-controlled types or executable
  object graphs. Apply schema and size limits to messages before allocation or
  side effects, including signed or otherwise integrity-protected data.

## Verify the claims

- Exercise encoded and duplicate parameters, output contexts, parser and
  archive bombs, path and symlink changes, redirect and DNS changes, oversized
  third-party responses, upload handling, and unsafe deserialization where
  those boundaries exist.
