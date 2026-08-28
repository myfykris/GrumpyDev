# Draft, merge, and finish doctrine

## Draft `.grump`

Follow the canonical `.grump` specification. Include concise sections for:

- purpose and success conditions;
- system boundaries;
- project documentation and what each relevant document establishes;
- doctrine format policy and the answer to Q001;
- review output policy, including whether plan addenda are allowed;
- review interaction policy for interactive or non-interactive plan questions;
- doctrine maintenance policy for explicitly confirmed decisions;
- plan readiness policy for unresolved decision-affecting research;
- research execution policy;
- deployment and execution profiles with stable `DEP-###` identifiers,
  operational state, support commitment, confidence, deployment ownership,
  evidence, and material environment differences;
- shared infrastructure with stable `INF-###` identifiers when more than one
  profile depends on the same material component;
- specialist survey status for installed packages, including current,
  incomplete, not surveyed, and explicitly inapplicable contributions;
- technology and runtime;
- non-negotiable constraints with `CON-###` identifiers;
- accepted tradeoffs with `ACC-###` identifiers;
- durable decisions with `DEC-###` identifiers;
- data and integration invariants;
- delivery, operations, and rollback;
- test and evidence expectations;
- unresolved material unknowns with `UNK-###` identifiers;
- survey evidence mapping repository paths to conclusions.

Use `None identified` when a deliberately surveyed section has no entries.
Never conceal an incomplete survey by omitting the section.
## Merge instead of replacing

When `.grump` already exists:

- preserve manual content and accepted items;
- keep existing `CON-###`, `ACC-###`, `DEC-###`, `UNK-###`, `DEP-###`, and
  `INF-###` identifiers stable through correction and rename;
- propose retirement rather than deleting obsolete statements silently;
- add new evidence and mark contradictions;
- show material doctrine changes before applying them when the user's request
  did not already authorize the update.
## Finish the survey

Write `.grump` when setup or re-survey was explicitly requested. Summarize the
evidence used, important inferences, unresolved user decisions, and proposed
specialist skills. Identify which installed specialist survey contributions
are current, incomplete, not surveyed, or explicitly inapplicable. Do not copy
the package inventory or uninstalled catalog into `.grump`. State whether the
infrastructure applicability gate
applied and whether every material profile has a workload path, operational
state, support commitment, deployment ownership, confidence, and scoped
evidence. Call out unresolved profile conflicts and re-survey triggers. Do not
claim the project is understood when critical system boundaries remain
inaccessible.
