# Infrastructure identifier behavior

An existing `.grump` contains `DEP-002` for a production worker. A re-survey
corrects its name and process manager, retires it in favor of a planned worker,
and adds a new command-line maintenance profile.

Expected behavior:

- Preserve `DEP-002` while correcting and renaming it.
- Mark `DEP-002` as retiring rather than deleting it or reusing its identifier.
- Assign the next unused `DEP-###` identifier to the new profile.
- Keep current, planned, and retiring state separate from support commitment,
  ownership, and confidence.
- Preserve old review references so their historical meaning remains clear.
