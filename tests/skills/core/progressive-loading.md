# Progressive loading behavior

The project has complete local GrumpyDev and applicable specialist packages.
No review requires network access.

Expected behavior:

- Lean mode loads the main entrypoint and every installed specialist entrypoint
  not explicitly marked inapplicable.
- Lean mode loads a conditional reference only when its documented trigger
  applies.
- Standard mode loads `standard-review.md`, then loads a specialist
  `review.md` only when its entrypoint identifies a plausible direct or
  indirect material effect. It loads only focused references whose documented
  boundaries the work affects.
- Deep mode also loads `deep-review.md` and broadens evidence for every affected
  boundary without loading focused references for unaffected modes, products,
  runtimes, or deployment models.
- No mode loads supporting references for an installed specialist whose
  entrypoint finds no plausible material effect.
- Persistence, execution, doctrine, infrastructure, and research references
  load only when their own triggers apply.
- No ordinary review loads the survey skill or any specialist `SURVEY.md`.
- A high-risk lean review recommends standard or deep review without silently
  changing the requested depth.
- Missing evidence follows the configured material-question or uncertainty
  policy instead of causing every focused reference to load.
- Approved installation downloads every manifest-listed focused reference even
  when the first review will load only a subset.
