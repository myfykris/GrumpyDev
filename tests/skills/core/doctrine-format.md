# Doctrine format behavior

Run an initial survey and a later re-survey against equivalent evidence.
Use `data/doctrine-detailed.md` and `data/doctrine-compact.md` as the semantic
and context-size fixture pair.

Expected behavior:

- Inspect evidence before asking questions.
- Ask the compact-versus-detailed format preference as `Q001`, the first
  question actually presented during initial survey.
- Preserve an existing unambiguous format during re-survey unless the user asks
  to change it.
- Use compact serialization when the format answer is unresolved.
- Preserve identical purpose, policies, stable identifiers, constraints,
  tradeoffs, decisions, profiles, shared components, material unknowns, source
  scope, and evidence references in compact and detailed forms.
- Compact form contains no generic skill instructions, raw survey transcript,
  or resolved question history.
- A format conversion is semantically lossless and preserves manual wording
  that does not conflict with the requested format.
