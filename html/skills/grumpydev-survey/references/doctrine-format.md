# Doctrine format selection

Load this file for every initial survey. During re-survey, load it only when the
format policy is missing, contradictory, or being reconsidered.

## Ask Q001

After the evidence pass, make this the first question actually presented in an
initial survey:

```text
Q001. Should GrumpyDev keep `.grump` as compact as practical? Compact mode
preserves every decision-affecting fact, constraint, policy, unresolved
question, and evidence reference while removing duplication, extended
explanation, and survey history. Reply `compact` or `detailed`.
```

Record `Doctrine format: compact`, `Doctrine format: detailed`, or `Doctrine
format: unresolved` with `Q001` as the source. If the user declines, defers, or
answers ambiguously, record unresolved and serialize compactly without changing
meaning.

Do not repeat Q001 during re-survey when the existing value is unambiguous.

## Compact rules

Compact doctrine must:

- store only project-specific facts, decisions, policies, and material unknowns;
- preserve every decision-affecting constraint, tradeoff, profile, shared
  component, source scope, and evidence reference;
- preserve concise survey status and explicit inapplicability for installed
  specialist packages;
- use terse structured bullets and stable identifiers;
- record a fact once and refer to it elsewhere;
- point to project documents rather than copy them;
- omit generic GrumpyDev instructions, survey transcripts, raw answers,
  resolved questions, repeated rationale, and obvious defaults; and
- retain concise rationale when omitting it could change future application.

Compactness never permits collapsing operational state, support commitment,
confidence, and deployment ownership into one ambiguous status.

## Detailed rules

Detailed doctrine may retain more rationale, alternatives, evidence scope, and
operational explanation. It still deduplicates facts and never records raw
survey history or generic skill rules.

When changing formats, compare stable identifiers, policies, profiles,
relationships, material unknowns, and evidence references before and after.
The conversion must preserve meaning.

Never replace these rules with a vague instruction to summarize as best as
possible.
