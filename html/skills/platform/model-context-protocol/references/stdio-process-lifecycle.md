# MCP stdio process lifecycle

Read this reference when the reviewed work directly or indirectly uses stdio, launches
or supervises a local server
process, passes an environment, handles stdout or stderr, cancellation, exit, restart,
or local credentials.

## Review requirements

- For stdio, keep stdout protocol-only, bound child-process lifetime, sanitize environment
  credentials, and handle cancellation and exit.
