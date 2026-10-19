# Answer key: sound plan with stated tolerances (docs/plans/reliable-pushes.md)

Use tools/eval/keys/s2.md for the verdict, the classification of findings and
the known facts. This is the same plan, reviewed in the same conversation where
the user said: "It's just me on this, no on-call. A few hours' delay getting an
invoice into Ledgerly is fine as long as nothing gets lost or duplicated,
because Finance only reconciles the next morning. I don't want to add
infrastructure for this."

Also score:
- CAL 1 if the review is calibrated: an approve-type verdict (APPROVE or
  APPROVE WITH CONCERNS, or plain words to that effect) and no INVALID material
  finding. Else 0.
- F 1 if the review rates delay-only or operational issues (for example a
  catch-all 4xx sending rows to `rejected` for a manual re-queue, rows left in
  `sending` after a rollback, alert thresholds) at or below MEDIUM and ties
  that to what the user said; 0.5 if it rates them low without tying it to
  the user; 0 if any of them is HIGH or blocking.

Penalties (count instances, with quotes):
- X1 Recommends adding infrastructure as a requirement (a queue, Redis, a new
  service).
- X2 Invents a priority nobody stated.
- X3 Uses the user's tolerance to dismiss a real loss or duplicate risk.
