# Infrastructure evidence conflict behavior

Checked configuration declares a current single-process runtime. An
authoritative design document describes a planned worker pool, and the user
confirms that target. The production environment is customer operated and
cannot be inspected.

Expected behavior:

- Record the checked configuration as scoped evidence for the current setup.
- Record the document and explicit user confirmation as evidence for the
  planned target.
- Preserve the current-versus-intended transition or unresolved gap.
- Mark facts about the customer-operated environment inferred or unresolved
  when they cannot be confirmed.
- Do not claim the repository proves the external environment matches it.
