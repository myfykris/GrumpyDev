# GrumpyDev

GrumpyDev is a project-local engineering review system for challenging plans
before implementation. It gives a coding agent explicit review doctrine,
technology-specific guidance, and a structured way to record durable project
facts in `.grump`.

The website and skill distribution are static files. GrumpyDev does not require
a hosted application, server-side runtime, account, or repository upload.

## Repository layout

- `html/` contains the complete static site and every published skill file.
- `tests/` contains behavioral review scenarios used to inspect skill coverage.
- `tools/validate_catalog.py` validates catalog structure and consistency.
- `serve.sh` serves `html/` on port 8000 and listens on all interfaces.

The behavioral fixtures are written review scenarios. They are not automated
model evaluations and should not be represented as such.

## Run locally

```sh
./serve.sh
```

Then open `http://127.0.0.1:8000/`.

## Validate

```sh
python3 tools/validate_catalog.py
```

The validator checks the manifest, skill and survey structure, public catalog
links, text encoding, prohibited typography, and behavioral fixture shape.

## Installation model

The agent-facing bootstrap instructions are in `html/install.txt`. Installation
is project-local and requires explicit approval before specialist skills are
fetched or installed.

## Security

Read [SECURITY.md](SECURITY.md) before reporting a vulnerability. Do not place
secrets or exploit details in a public issue.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
