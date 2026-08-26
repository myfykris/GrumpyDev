#!/usr/bin/env python3
"""Validate the local GrumpyDev skill catalog without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"
SKILLS = HTML / "skills"
MANIFEST = HTML / "manifest.json"
INDEX = SKILLS / "index.html"
INFRASTRUCTURE_RUBRIC = ROOT / "tests" / "skills" / "infrastructure-survey-rubric.md"
SPECIALIST_TYPES = {"language", "framework", "paradigm", "storage", "platform"}
ALLOWED_TYPES = {"core", *SPECIALIST_TYPES}
REQUIRED_SECTIONS = (
    "## Inspect evidence",
    "## Establish the operating model",
    "## Challenge the plan",
    "## Verify the claims",
    "## Ask when evidence is missing",
    "## Calibrate findings",
    "## Add to the verdict",
)
REQUIRED_SURVEY_SECTIONS = (
    "## Applicability",
    "## Inspect before asking",
    "## Durable project facts",
    "## Ask only when materially unresolved",
    "## Record in .grump",
    "## Do not ask or record",
    "## Re-survey triggers",
)
CORE_PATTERN_SECTIONS = {
    "grumpydev": "### Recurring review traps",
    "grumpydev-survey": "### Survey failure patterns",
}
REQUIRED_FIXTURE_SECTIONS = (
    "## Material-gap case",
    "## Resolved-evidence case",
    "## Evidence-resolved survey case",
    "## Material survey-gap case",
    "## Ordinary-review loading case",
    "## Companion-overlap case",
    "## Infrastructure-profile case",
)
BAD_PUNCTUATION = "\u00a9\u2018\u2019\u201c\u201d\u2013\u2014\u2026\u2192\u2212\u2713"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
COMPANION_RE = re.compile(r"Apply this guidance alongside[^\n]*")
BACKTICK_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`")
UNRESOLVED_TEMPLATE_RE = re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\[[^\]]+\]\}")
LEGACY_BOILERPLATE = (
    "Include the target versions and operating model",
    "Ask only what can change the verdict, severity, or required action",
)
EXPECTED_EXTERNAL_TITLE_LINKS = 97
CATALOG_SUMMARY_OVERRIDES = {
    "Survey an existing software repository and create or update its human-owned .grump "
    "project doctrine.": (
        "Surveys a repository and creates or updates its project review rules in .grump."
    ),
}
CATALOG_DISPLAY_ORDER = {
    "core": "grumpydev grumpydev-survey".split(),
    "languages": (
        "typescript python javascript html-css sql java csharp php shell cpp go c rust "
        "powershell kotlin dart ruby swift r scala elixir objective-c"
    ).split(),
    "frameworks": (
        "react nextjs express tailwind-css angular vue aspnet-core spring-boot wordpress "
        "django fastapi laravel svelte shadcn-ui flutter react-native nestjs rails expo "
        "blazor symfony astro tanstack jetpack-compose swiftui authjs htmx gin wpf "
        "winforms qt quarkus phoenix ktor appkit gtk echo axum actix-web winui-3 vapor "
        "sinatra"
    ).split(),
    "paradigms": (
        "object-oriented-design distributed-systems microservices "
        "event-driven-architecture concurrent-systems data-pipelines agentic-systems "
        "functional-programming domain-driven-design modular-monoliths event-sourcing-cqrs"
    ).split(),
    "storage": (
        "postgresql mysql sqlite mongodb redis sql-server mariadb dynamodb "
        "elasticsearch-opensearch object-storage data-warehousing cassandra neo4j"
    ).split(),
    "platform": (
        "nodejs rest-api-design application-security testing-strategy containers ci-cd "
        "linux vite oauth secrets-configuration performance-capacity nginx observability "
        "vercel firebase supabase llm-applications model-context-protocol cloudflare "
        "serverless kubernetes terraform graphql-api-design background-jobs message-queues "
        "realtime-web data-privacy web-accessibility dependency-supply-chain schema-evolution "
        "windows android ios macos aws-ecs grpc-protobuf apache-http-server"
    ).split(),
}


def fail(errors: list[str], path: Path | str, message: str) -> None:
    errors.append(f"{path}: {message}")


def read_text(path: Path, errors: list[str]) -> str:
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail(errors, path.relative_to(ROOT), f"invalid UTF-8: {exc}")
        return ""
    if b"\r" in data:
        fail(errors, path.relative_to(ROOT), "must use LF line endings")
    if data and not data.endswith(b"\n"):
        fail(errors, path.relative_to(ROOT), "missing final newline")
    if data.endswith(b"\n\n"):
        fail(errors, path.relative_to(ROOT), "blank line at end of file")
    for char in BAD_PUNCTUATION:
        if char in text:
            fail(
                errors,
                path.relative_to(ROOT),
                f"prohibited typographic character U+{ord(char):04X}",
            )
    return text


def parse_frontmatter(path: Path, text: str, errors: list[str]) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        fail(errors, path.relative_to(ROOT), "invalid YAML frontmatter boundary")
        return {}
    values: dict[str, str] = {}
    for number, line in enumerate(match.group(1).splitlines(), 1):
        if not line or line.startswith(" ") or ":" not in line:
            fail(errors, path.relative_to(ROOT), f"unsupported frontmatter syntax on line {number}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key in values:
            fail(errors, path.relative_to(ROOT), f"duplicate frontmatter key {key}")
        values[key] = value
    if set(values) != {"name", "description"}:
        fail(
            errors,
            path.relative_to(ROOT),
            "frontmatter must contain exactly name and description",
        )
    name = values.get("name", "")
    description = values.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        fail(errors, path.relative_to(ROOT), f"invalid skill name {name!r}")
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        fail(errors, path.relative_to(ROOT), "invalid description")
    return values


def validate_body_lines(path: Path, text: str, errors: list[str], *, frontmatter: bool) -> None:
    body = text
    line_offset = 0
    if frontmatter:
        match = FRONTMATTER_RE.match(text)
        if match:
            line_offset = text[: match.end()].count("\n")
            body = text[match.end() :]
    for number, line in enumerate(body.splitlines(), line_offset + 1):
        if len(line) > 100:
            fail(errors, path.relative_to(ROOT), f"body line {number} exceeds 100 characters")
        if re.match(r"^\s*-\s{2,}", line):
            fail(
                errors,
                path.relative_to(ROOT),
                f"body line {number} has an inconsistent list marker",
            )


def validate_section_order(
    path: Path, text: str, sections: tuple[str, ...], errors: list[str]
) -> None:
    positions: list[int] = []
    for section in sections:
        if text.count(section) != 1:
            fail(errors, path.relative_to(ROOT), f"section must occur exactly once: {section}")
        positions.append(text.find(section))
    if -1 not in positions and positions != sorted(positions):
        fail(errors, path.relative_to(ROOT), "required sections are out of order")


def expected_skill_path(entry: dict[str, object]) -> Path:
    name = str(entry["name"])
    skill_type = str(entry["type"])
    if skill_type == "core":
        return SKILLS / name / "SKILL.md"
    return SKILLS / skill_type / name / "SKILL.md"


def expected_survey_path(entry: dict[str, object]) -> Path:
    return expected_skill_path(entry).with_name("SURVEY.md")


def catalog_summary(description: str) -> str:
    summary = description.split(" Use when ", 1)[0]
    if summary in CATALOG_SUMMARY_OVERRIDES:
        return CATALOG_SUMMARY_OVERRIDES[summary]
    for source, replacement in (
        ("Review ", "Reviews "),
        ("Perform ", "Performs "),
        ("Survey ", "Surveys "),
    ):
        if summary.startswith(source):
            return replacement + summary[len(source) :]
    return summary


def validate() -> list[str]:
    errors: list[str] = []
    manifest_text = read_text(MANIFEST, errors)
    index_text = read_text(INDEX, errors)
    if "Use when " in index_text:
        fail(
            errors,
            INDEX.relative_to(ROOT),
            "agent trigger metadata must not appear in the human-facing catalog",
        )
    try:
        manifest = json.loads(manifest_text)
    except json.JSONDecodeError as exc:
        fail(errors, MANIFEST.relative_to(ROOT), f"invalid JSON: {exc}")
        return errors

    if manifest.get("schema_version") != 1:
        fail(errors, MANIFEST.relative_to(ROOT), "unreleased schema_version must remain 1")
    if manifest.get("grumpydev_version") != 1:
        fail(errors, MANIFEST.relative_to(ROOT), "unreleased grumpydev_version must remain 1")
    if manifest.get("publisher") != "grumpydev.ai":
        fail(errors, MANIFEST.relative_to(ROOT), "publisher must be grumpydev.ai")

    entries = manifest.get("skills")
    if not isinstance(entries, list):
        fail(errors, MANIFEST.relative_to(ROOT), "skills must be a list")
        return errors

    for section_id, expected_order in CATALOG_DISPLAY_ORDER.items():
        section_match = re.search(
            rf'<section id="{re.escape(section_id)}"[^>]*>.*?</section>',
            index_text,
            re.DOTALL,
        )
        if not section_match:
            fail(errors, INDEX.relative_to(ROOT), f"missing catalog section {section_id}")
            continue
        actual_order = re.findall(
            r'<span class="catalog-directory font-mono text-xs">([^<]+)</span>',
            section_match.group(0),
        )
        if actual_order != expected_order:
            fail(
                errors,
                INDEX.relative_to(ROOT),
                f"{section_id} cards are not in usage-first display order",
            )

    card_titles = re.findall(
        r'<h3 class="card-title text-lg(?: catalog-multi-title)?">(.*?)</h3>',
        index_text,
        re.DOTALL,
    )
    if len(card_titles) != len(entries):
        fail(errors, INDEX.relative_to(ROOT), "catalog title count does not match manifest")
    if "catalog-card-header" in index_text:
        fail(errors, INDEX.relative_to(ROOT), "catalog titles must not contain directory names")
    if index_text.count('class="card-title text-lg catalog-multi-title"') != 4:
        fail(errors, INDEX.relative_to(ROOT), "dual-technology catalog titles are not synchronized")
    if index_text.count("catalog-multi-header") != 4:
        fail(errors, INDEX.relative_to(ROOT), "dual-technology card headers are not synchronized")
    if index_text.count('class="catalog-subject-line"') != 8:
        fail(errors, INDEX.relative_to(ROOT), "dual-technology title lines are not synchronized")
    external_title_links: list[str] = []
    for title in card_titles:
        links = re.findall(
            r'<a\b(?=[^>]*\bhref="https://)[^>]*>.*?</a>',
            title,
            re.DOTALL,
        )
        external_title_links.extend(links)
        if title.count("<a ") != len(links):
            fail(errors, INDEX.relative_to(ROOT), "catalog titles may link only to HTTPS sites")
    if len(external_title_links) != EXPECTED_EXTERNAL_TITLE_LINKS:
        fail(
            errors,
            INDEX.relative_to(ROOT),
            "catalog external title-link count is not synchronized",
        )
    for link in external_title_links:
        required_link_markup = (
            'class="link link-hover flex items-center gap-1"',
            'target="_blank"',
            'rel="noopener noreferrer"',
            "(opens in a new window)",
            '<svg class="size-4 shrink-0"',
            'width="16"',
            'height="16"',
            'aria-hidden="true"',
        )
        for marker in required_link_markup:
            if marker not in link:
                fail(
                    errors,
                    INDEX.relative_to(ROOT),
                    f"external catalog title link is missing {marker}",
                )

    if ">Read:</span>" in index_text:
        fail(errors, INDEX.relative_to(ROOT), "catalog action rows must use directory names")
    directory_action_rows = re.findall(
        r'<div class="card-actions mt-2 items-center gap-1 text-sm">'
        r'<span class="catalog-directory font-mono text-xs">([^<]+)</span>'
        r'<span aria-hidden="true">/</span><a class="link link-primary font-bold" '
        r'href="[^"]+/SKILL\.md">SKILL\.md</a>',
        index_text,
    )
    if len(directory_action_rows) != len(entries):
        fail(errors, INDEX.relative_to(ROOT), "catalog directory action rows are not synchronized")
    if index_text.count(">SKILL.md</a>") != len(entries):
        fail(errors, INDEX.relative_to(ROOT), "catalog SKILL.md links are not synchronized")
    expected_survey_links = sum(
        isinstance(entry, dict) and entry.get("type") in SPECIALIST_TYPES
        for entry in entries
    )
    if index_text.count(">SURVEY.md</a>") != expected_survey_links:
        fail(errors, INDEX.relative_to(ROOT), "catalog SURVEY.md links are not synchronized")
    survey_separator = '>SKILL.md</a><span aria-hidden="true">|</span><a'
    if index_text.count(survey_separator) != expected_survey_links:
        fail(errors, INDEX.relative_to(ROOT), "catalog survey separators are not synchronized")

    names: set[str] = set()
    aliases: set[str] = set()
    urls: set[str] = set()
    manifest_paths: set[Path] = set()
    manifest_survey_paths: set[Path] = set()
    entry_by_name: dict[str, dict[str, object]] = {}

    for entry in entries:
        if not isinstance(entry, dict):
            fail(errors, MANIFEST.relative_to(ROOT), "skill entry must be an object")
            continue
        skill_type = entry.get("type")
        expected_fields = {"name", "type", "url", "aliases", "publisher"}
        if skill_type in SPECIALIST_TYPES:
            expected_fields.add("survey_url")
        if set(entry) != expected_fields:
            fail(
                errors,
                MANIFEST.relative_to(ROOT),
                f"invalid fields for skill entry {entry.get('name')!r}",
            )
            continue
        name = entry.get("name")
        url = entry.get("url")
        publisher = entry.get("publisher")
        entry_aliases = entry.get("aliases")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            fail(errors, MANIFEST.relative_to(ROOT), f"invalid manifest skill name {name!r}")
            continue
        if skill_type not in ALLOWED_TYPES:
            fail(errors, MANIFEST.relative_to(ROOT), f"invalid type for {name}: {skill_type!r}")
            continue
        if publisher != "grumpydev.ai":
            fail(errors, MANIFEST.relative_to(ROOT), f"publisher for {name} must be grumpydev.ai")
        expected_url = "https://grumpydev.ai/skills/"
        if skill_type == "core":
            expected_url += f"{name}/SKILL.md"
        else:
            expected_url += f"{skill_type}/{name}/SKILL.md"
        if url != expected_url:
            fail(errors, MANIFEST.relative_to(ROOT), f"noncanonical URL for {name}")
        if name in names or name in aliases:
            fail(errors, MANIFEST.relative_to(ROOT), f"name collision for {name}")
        names.add(name)
        if not isinstance(entry_aliases, list) or not all(
            isinstance(alias, str) for alias in entry_aliases
        ):
            fail(errors, MANIFEST.relative_to(ROOT), f"aliases for {name} must be strings")
            entry_aliases = []
        for alias in entry_aliases:
            if not NAME_RE.fullmatch(alias) or alias in names or alias in aliases:
                fail(
                    errors,
                    MANIFEST.relative_to(ROOT),
                    f"alias collision or invalid alias {alias!r}",
                )
            aliases.add(alias)
        if not isinstance(url, str) or url in urls:
            fail(errors, MANIFEST.relative_to(ROOT), f"duplicate or invalid URL for {name}")
        else:
            urls.add(url)
        path = expected_skill_path(entry)
        manifest_paths.add(path)
        if skill_type in SPECIALIST_TYPES:
            survey_url = entry.get("survey_url")
            expected_survey_url = expected_url.removesuffix("SKILL.md") + "SURVEY.md"
            if survey_url != expected_survey_url:
                fail(errors, MANIFEST.relative_to(ROOT), f"noncanonical survey URL for {name}")
            if not isinstance(survey_url, str) or survey_url in urls:
                fail(
                    errors,
                    MANIFEST.relative_to(ROOT),
                    f"duplicate or invalid survey URL for {name}",
                )
            else:
                urls.add(survey_url)
            manifest_survey_paths.add(expected_survey_path(entry))
        entry_by_name[name] = entry

    disk_paths = set(SKILLS.glob("**/SKILL.md"))
    for path in sorted(manifest_paths - disk_paths):
        fail(errors, path.relative_to(ROOT), "manifest entry has no skill file")
    for path in sorted(disk_paths - manifest_paths):
        fail(errors, path.relative_to(ROOT), "skill file has no manifest entry")

    disk_survey_paths = set(SKILLS.glob("**/SURVEY.md"))
    for path in sorted(manifest_survey_paths - disk_survey_paths):
        fail(errors, path.relative_to(ROOT), "specialist manifest entry has no survey file")
    for path in sorted(disk_survey_paths - manifest_survey_paths):
        fail(errors, path.relative_to(ROOT), "survey file has no specialist manifest entry")

    for path in sorted(disk_paths):
        text = read_text(path, errors)
        values = parse_frontmatter(path, text, errors)
        validate_body_lines(path, text, errors, frontmatter=True)
        name = values.get("name", "")
        entry = entry_by_name.get(name)
        if not entry:
            continue
        if path != expected_skill_path(entry):
            fail(errors, path.relative_to(ROOT), "name, type, and directory do not agree")
        description = values.get("description", "")
        summary = catalog_summary(description)
        if summary and summary not in index_text:
            fail(
                errors,
                path.relative_to(ROOT),
                "human-facing summary is not synchronized to html/skills/index.html",
            )
        relative = path.relative_to(SKILLS)
        is_specialist = relative.parts[0] in SPECIALIST_TYPES
        if is_specialist:
            validate_section_order(path, text, REQUIRED_SECTIONS, errors)
            if text.count("### Recurring traps") != 1:
                fail(
                    errors,
                    path.relative_to(ROOT),
                    "specialist must contain exactly one Recurring traps subsection",
                )
            for phrase in LEGACY_BOILERPLATE:
                if phrase in text:
                    fail(errors, path.relative_to(ROOT), "legacy generic expansion boilerplate")
            if UNRESOLVED_TEMPLATE_RE.search(text):
                fail(errors, path.relative_to(ROOT), "unresolved generator placeholder")
            survey = path.with_name("SURVEY.md")
            if survey.exists():
                survey_text = read_text(survey, errors)
                validate_body_lines(survey, survey_text, errors, frontmatter=False)
                if survey_text.startswith("---"):
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "survey file must not have YAML frontmatter",
                    )
                first_line = survey_text.splitlines()[0] if survey_text else ""
                if not re.fullmatch(r"# [A-Za-z0-9.+# /-]+ survey contribution", first_line):
                    fail(errors, survey.relative_to(ROOT), "invalid survey contribution title")
                validate_section_order(survey, survey_text, REQUIRED_SURVEY_SECTIONS, errors)
                if UNRESOLVED_TEMPLATE_RE.search(survey_text):
                    fail(errors, survey.relative_to(ROOT), "unresolved generator placeholder")
                if re.search(
                    r"(?:Deployment-profile (?:facts|guidance)|"
                    r"Conditional deployment boundary):\s+(?:Preserve|Strengthen)\b|"
                    r"material:\s+(?:Preserve|Strengthen)\b",
                    survey_text,
                ):
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "internal survey-editing language leaked into runtime guidance",
                    )
                if re.search(r"\bQ\d{3}\b", survey_text):
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "survey candidates must not contain assigned Q identifiers",
                    )
                if re.search(r"https?://", survey_text):
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "survey runtime instructions must not contain external URLs",
                    )
                distribution_hash = re.compile(
                    r"\b(?:sha-?256|sha-?512|distribution[_ -]?hash|"
                    r"content[_ -]?hash)\b",
                    re.IGNORECASE,
                )
                if distribution_hash.search(survey_text):
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "prohibited GrumpyDev distribution-hash mechanism",
                    )
                deployment_markers = sum(
                    survey_text.count(marker)
                    for marker in (
                        "Deployment-profile facts:",
                        "Deployment-profile guidance:",
                        "Conditional deployment boundary:",
                    )
                )
                if deployment_markers != 1:
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "survey must contain exactly one deployment-profile contribution",
                    )
                if "`DEP-###`" not in survey_text or "`INF-###`" not in survey_text:
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "survey must define DEP and INF recording destinations",
                    )
                survey_href = f'./{relative.parts[0]}/{name}/SURVEY.md'
                if survey_href not in index_text:
                    fail(
                        errors,
                        survey.relative_to(ROOT),
                        "survey link is not synchronized to html/skills/index.html",
                    )
            fixture = (
                ROOT
                / "tests"
                / "skills"
                / "specialists"
                / relative.parts[0]
                / f"{name}.md"
            )
            if not fixture.exists():
                fail(errors, fixture.relative_to(ROOT), "missing specialist behavioral fixture")
            else:
                fixture_text = read_text(fixture, errors)
                for heading in (*REQUIRED_FIXTURE_SECTIONS, "Expected behavior:"):
                    if heading not in fixture_text:
                        fail(errors, fixture.relative_to(ROOT), f"missing fixture marker {heading}")
        elif name in CORE_PATTERN_SECTIONS:
            pattern_section = CORE_PATTERN_SECTIONS[name]
            if text.count(pattern_section) != 1:
                fail(
                    errors,
                    path.relative_to(ROOT),
                    f"core skill must contain exactly one {pattern_section} subsection",
                )
        companion = COMPANION_RE.search(text)
        if companion:
            for referenced in BACKTICK_RE.findall(companion.group(0)):
                if referenced not in names:
                    fail(errors, path.relative_to(ROOT), f"unknown companion skill {referenced}")
        if re.search(r"https?://", text):
            fail(
                errors,
                path.relative_to(ROOT),
                "skill runtime instructions must not contain external URLs",
            )
        distribution_hash = re.compile(
            r"\b(?:sha-?256|sha-?512|distribution[_ -]?hash|content[_ -]?hash)\b",
            re.IGNORECASE,
        )
        if distribution_hash.search(text):
            fail(
                errors,
                path.relative_to(ROOT),
                "prohibited GrumpyDev distribution-hash mechanism",
            )
        if re.search(
            r"^\s*(?:hash|digest|checksum)\s*:",
            text,
            re.IGNORECASE | re.MULTILINE,
        ):
            fail(errors, path.relative_to(ROOT), "prohibited distribution integrity field")

    core_fixtures = sorted((ROOT / "tests" / "skills" / "core").glob("*.md"))
    if not core_fixtures:
        fail(errors, "tests/skills/core", "missing core behavioral fixtures")
    for fixture in core_fixtures:
        fixture_text = read_text(fixture, errors)
        if "Expected behavior:" not in fixture_text:
            fail(errors, fixture.relative_to(ROOT), "missing Expected behavior marker")

    rubric_text = read_text(INFRASTRUCTURE_RUBRIC, errors)
    if "# Infrastructure survey behavioral rubric" not in rubric_text:
        fail(errors, INFRASTRUCTURE_RUBRIC.relative_to(ROOT), "missing rubric title")
    for number in range(1, 14):
        if f"{number}. " not in rubric_text:
            fail(
                errors,
                INFRASTRUCTURE_RUBRIC.relative_to(ROOT),
                f"missing behavioral criterion {number}",
            )

    read_text(HTML / "spec" / "grump.md", errors)
    read_text(HTML / "spec" / "skill-authoring.md", errors)

    public_text_suffixes = {".css", ".html", ".js", ".json", ".md", ".txt", ".xml"}
    for path in sorted(HTML.rglob("*")):
        if path.is_file() and (path.suffix in public_text_suffixes or path.name == "robots.txt"):
            public_text = read_text(path, errors)
            if path.suffix == ".html" and re.search(
                r"<(?:script|img)\b[^>]*\bsrc=[\"'](?:https?:)?//|"
                r"<link\b(?=[^>]*\brel=[\"']stylesheet[\"'])"
                r"[^>]*\bhref=[\"'](?:https?:)?//",
                public_text,
                re.IGNORECASE,
            ):
                fail(
                    errors,
                    path.relative_to(ROOT),
                    "public page includes an externally hosted asset",
                )

    for path in (ROOT / "README.md", ROOT / "SECURITY.md", ROOT / "LICENSE"):
        if not path.exists():
            fail(errors, path.relative_to(ROOT), "required repository document is missing")
        else:
            read_text(path, errors)

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(error)
        print(f"FAILED: {len(errors)} catalog error(s)")
        return 1
    count = len(list(SKILLS.glob("**/SKILL.md")))
    print(f"OK: validated {count} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
