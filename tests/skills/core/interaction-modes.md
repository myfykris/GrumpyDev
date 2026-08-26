# Review interaction behavior

## Interactive case

The plan omits a decision that can change the verdict. The review preference is
interactive.

Expected behavior:

- Complete the initial evidence pass before asking anything.
- Ask only the material missing question using an `RQ###` identifier.
- Resume the same evaluation after the answer.
- Ask no question when the available evidence is sufficient.

## Non-interactive case

The same plan is reviewed with a non-interactive preference.

Expected behavior:

- Do not pause for plan questions.
- Complete the strongest defensible review.
- Identify each material question and the conclusion it could change under
  `Evidence gaps`.
