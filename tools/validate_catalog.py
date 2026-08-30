#!/usr/bin/env python3
"""Validate the local GrumpyDev skill catalog without external dependencies."""

from __future__ import annotations

import json
import html as html_lib
import re
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"
SKILLS = HTML / "skills"
MANIFEST = HTML / "manifest.json"
INDEX = SKILLS / "index.html"
INSTALLER = SKILLS / "grumpydev-install" / "SKILL.md"
HOME = HTML / "index.html"
HOW_IT_WORKS = HTML / "how-it-works" / "index.html"
SECURITY = HTML / "security" / "index.html"
AUTHOR = HTML / "author" / "index.html"
INFRASTRUCTURE_RUBRIC = ROOT / "tests" / "skills" / "infrastructure-survey-rubric.md"
DOCTRINE_FIXTURES = ROOT / "tests" / "skills" / "core" / "data"
SPECIALIST_TYPES = {"language", "framework", "paradigm", "storage", "platform"}
ALLOWED_TYPES = {"core", *SPECIALIST_TYPES}
REQUIRED_SECTIONS = (
    "## Inspect evidence",
    "## Establish the operating model",
    "## Challenge the reviewed work",
    "## Verify the claims",
    "## Ask when evidence is missing",
    "## Calibrate findings",
    "## Add to the verdict",
)
REQUIRED_REFERENCE_SECTIONS = REQUIRED_SECTIONS[1:-1]
COMPACT_ENTRYPOINT_MARKERS = (
    "## Lean review",
    "## Load local references",
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
CORE_INVOCATION_PREFIX = (
    "Use only for an explicitly invoked GrumpyDev review, an explicit request to "
    "add GrumpyDev execution rules, or an explicit request to remove GrumpyDev from "
    "the current project. Do not activate merely because work is being planned, "
    "created, revised, discussed, implemented, or generically reviewed. "
)
REVIEW_INVOCATION_PREFIX = (
    "Use only during an explicitly invoked GrumpyDev review. Do not activate during "
    "ordinary planning, creation, revision, discussion, implementation, or generic "
    "review. For a project where this specialist is installed and not explicitly "
    "marked inapplicable, use it in every GrumpyDev review to evaluate direct and "
    "indirect effects. "
)
PROJECT_APPLICABILITY_MARKER = " Project applicability: "
SURVEY_INVOCATION_PREFIX = (
    "Use only during GrumpyDev installation or setup, or for an explicitly requested "
    "re-survey or doctrine refresh. Do not activate during ordinary planning, plan "
    "creation, revision, review, or implementation. "
)
EXPECTED_EXTERNAL_TITLE_LINKS = 97
STATE_TOP_LEVEL_KEYS = {
    "grumpydev_version",
    "host",
    "project_scope",
    "manifest_url",
    "last_successful_check",
    "packages",
}
STATE_PACKAGE_KEYS = {"name", "type", "publisher", "files"}
STATE_FILE_KEYS = {"role", "local_path", "source_url"}
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
EXPECTED_FOCUSED_REFERENCES = {
    "framework/appkit": (
        "documents-and-state-restoration.md",
        "sandbox-entitlements-and-file-access.md",
    ),
    "framework/gtk": ("version-migration-packaging-and-display-backends.md",),
    "framework/laravel": (
        "http-validation-and-authorization.md",
        "eloquent-transactions-and-migrations.md",
        "queues-events-and-workers.md",
        "caching-configuration-and-deployment.md",
    ),
    "framework/nextjs": (
        "rendering-caching-and-hydration.md",
        "server-actions-routes-and-security.md",
    ),
    "framework/react": (
        "server-rendering-and-hydration.md",
        "untrusted-content-and-browser-security.md",
    ),
    "framework/winforms": ("native-interop-packaging-and-updates.md",),
    "framework/winui-3": ("activation-identity-and-deployment.md",),
    "framework/wordpress": (
        "database-cron-cache-and-multisite.md",
        "updates-migrations-and-rollback.md",
    ),
    "framework/wpf": ("native-interop-packaging-and-updates.md",),
    "language/objective-c": (
        "dynamic-runtime-kvo-and-notifications.md",
        "swift-c-cpp-and-abi-interop.md",
    ),
    "language/php": (
        "types-and-boundary-data.md",
        "request-and-process-lifecycle.md",
        "security-and-external-input.md",
        "dependencies-and-deployment.md",
    ),
    "language/python": (
        "async-processes-and-shutdown.md",
        "serialization-execution-and-filesystem-security.md",
        "packaging-native-and-deployment.md",
    ),
    "paradigm/agentic-systems": (
        "tool-authority-sandboxing-and-code-execution.md",
        "memory-data-and-supply-chain-trust.md",
        "delegation-inter-agent-trust-and-containment.md",
    ),
    "paradigm/distributed-systems": (
        "partial-failure-retries-and-overload.md",
        "consistency-replication-and-caches.md",
        "messaging-ordering-and-reconciliation.md",
        "coordination-clocks-and-leadership.md",
        "evolution-operations-and-recovery.md",
    ),
    "platform/apache-http-server": (
        "routing-proxy-and-php-integration.md",
        "tls-access-control-and-reload.md",
    ),
    "platform/application-security": (
        "identity-sessions-and-authorization.md",
        "injection-output-and-untrusted-input.md",
        "files-uploads-ssrf-and-deserialization.md",
        "cryptography-abuse-and-incident-response.md",
    ),
    "platform/graphql-api-design": ("subscriptions-and-persisted-operations.md",),
    "platform/kubernetes": (
        "health-lifecycle-and-rollouts.md",
        "resources-placement-and-scaling.md",
        "networking-identity-and-secrets.md",
        "stateful-work-and-recovery.md",
    ),
    "platform/linux": (
        "services-processes-and-resource-limits.md",
        "packaging-updates-and-recovery.md",
    ),
    "platform/llm-applications": (
        "retrieval-data-and-poisoning.md",
        "tools-output-and-authority.md",
        "evaluations-budgets-and-fallbacks.md",
    ),
    "platform/macos": (
        "sandbox-privacy-and-keychain.md",
        "signing-notarization-updates-and-recovery.md",
    ),
    "platform/model-context-protocol": (
        "http-authorization-and-discovery.md",
        "stdio-process-lifecycle.md",
        "sessions-tool-identity-and-revocation.md",
    ),
    "platform/nginx": (
        "routing-static-files-and-fastcgi.md",
        "proxy-streaming-caching-and-tls.md",
    ),
    "platform/nodejs": (
        "modules-packages-and-native-addons.md",
        "async-context-streams-and-backpressure.md",
        "filesystem-child-processes-and-workers.md",
        "signals-shutdown-and-deployment.md",
    ),
    "platform/rest-api-design": (
        "authorization-input-and-abuse.md",
        "idempotency-pagination-and-caching.md",
        "versioning-upstreams-and-evolution.md",
    ),
    "platform/windows": (
        "services-com-and-process-identity.md",
        "packaging-signing-updates-and-recovery.md",
    ),
    "storage/mariadb": (
        "schema-locking-and-query-plans.md",
        "replication-galera-and-recovery.md",
    ),
    "storage/postgresql": (
        "schema-migrations-and-locking.md",
        "transactions-and-concurrency.md",
        "queries-and-indexes.md",
        "operations-replication-and-recovery.md",
    ),
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
        if value.startswith('"'):
            try:
                parsed_value = json.loads(value)
            except json.JSONDecodeError as exc:
                fail(
                    errors,
                    path.relative_to(ROOT),
                    f"invalid quoted frontmatter value on line {number}: {exc}",
                )
                continue
            if not isinstance(parsed_value, str):
                fail(
                    errors,
                    path.relative_to(ROOT),
                    f"frontmatter value on line {number} must be a string",
                )
                continue
            value = parsed_value
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


def validate_nonempty_sections(
    path: Path, text: str, sections: tuple[str, ...], errors: list[str]
) -> None:
    """Require content beneath each named level-two section."""
    for section in sections:
        start = text.find(section)
        if start < 0:
            continue
        body_start = start + len(section)
        next_section = text.find("\n## ", body_start)
        body = text[body_start : next_section if next_section >= 0 else len(text)]
        substantive_lines = [
            line
            for line in body.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]
        if not substantive_lines:
            fail(errors, path.relative_to(ROOT), f"section has no content: {section}")


def substantive_blocks(text: str) -> set[str]:
    blocks: set[str] = set()
    for block in re.split(r"\n\s*\n", text):
        normalized = " ".join(block.split())
        if len(normalized.split()) >= 8 and not normalized.startswith("#"):
            blocks.add(normalized)
    return blocks


def expected_package_path(entry: dict[str, object]) -> Path:
    name = str(entry["name"])
    skill_type = str(entry["type"])
    if skill_type == "core":
        return SKILLS / name
    return SKILLS / skill_type / name


def expected_skill_path(entry: dict[str, object]) -> Path:
    return expected_package_path(entry) / "SKILL.md"


def expected_survey_path(entry: dict[str, object]) -> Path:
    return expected_skill_path(entry).with_name("SURVEY.md")


def expected_file_url(entry: dict[str, object], relative: str) -> str:
    name = str(entry["name"])
    skill_type = str(entry["type"])
    base = "https://grumpydev.ai/skills/"
    if skill_type == "core":
        return f"{base}{name}/{relative}"
    return f"{base}{skill_type}/{name}/{relative}"


def valid_package_path(value: object) -> bool:
    if not isinstance(value, str) or not value:
        return False
    if "\\" in value or "?" in value or "#" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(part not in {"", ".", ".."} for part in path.parts)


def catalog_summary(description: str) -> str:
    for prefix in (CORE_INVOCATION_PREFIX, REVIEW_INVOCATION_PREFIX, SURVEY_INVOCATION_PREFIX):
        if description.startswith(prefix):
            description = description[len(prefix) :]
            break
    summary = re.split(
        rf"{re.escape(PROJECT_APPLICABILITY_MARKER)}| Applies (?:when|during) | Use when ",
        description,
        maxsplit=1,
    )[0]
    summary = summary.replace(
        " plans and other engineering artifacts", " engineering work"
    )
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


def expected_catalog_file_href(entry: dict[str, object], relative: str) -> str:
    name = str(entry["name"])
    skill_type = str(entry["type"])
    if skill_type == "core":
        return f"./{name}/{relative}"
    return f"./{skill_type}/{name}/{relative}"


def metadata_description(
    path: Path,
    text: str,
    attribute: str,
    value: str,
    errors: list[str],
) -> str:
    match = re.search(
        rf'<meta {attribute}="{re.escape(value)}" content="([^"]+)">',
        text,
    )
    if not match:
        fail(errors, path.relative_to(ROOT), f"missing {value} metadata description")
        return ""
    return match.group(1)


def state_has_prohibited_key(value: object) -> bool:
    if isinstance(value, dict):
        for key, child in value.items():
            lowered = key.lower()
            if any(marker in lowered for marker in ("hash", "checksum", "digest")):
                return True
            if state_has_prohibited_key(child):
                return True
    if isinstance(value, list):
        return any(state_has_prohibited_key(item) for item in value)
    return False


def validate() -> list[str]:
    errors: list[str] = []
    manifest_text = read_text(MANIFEST, errors)
    public_html_texts = {
        path: read_text(path, errors) for path in sorted(HTML.rglob("*.html"))
    }
    index_text = public_html_texts[INDEX]
    home_text = public_html_texts[HOME]
    how_it_works_text = public_html_texts[HOW_IT_WORKS]
    security_text = public_html_texts[SECURITY]
    author_text = public_html_texts[AUTHOR]
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

    expected_top_fields = {
        "schema_version",
        "grumpydev_version",
        "name",
        "publisher",
        "installer",
        "doctrine_spec_url",
        "skill_authoring_spec_url",
        "skills",
    }
    if set(manifest) != expected_top_fields:
        fail(errors, MANIFEST.relative_to(ROOT), "invalid top-level manifest fields")

    installer = manifest.get("installer")
    if not isinstance(installer, dict) or set(installer) != {
        "name",
        "description",
        "url",
        "publisher",
    }:
        fail(errors, MANIFEST.relative_to(ROOT), "invalid installer record")
        installer = {}
    if installer.get("name") != "grumpydev-install":
        fail(errors, MANIFEST.relative_to(ROOT), "invalid installer name")
    if installer.get("publisher") != "grumpydev.ai":
        fail(errors, MANIFEST.relative_to(ROOT), "invalid installer publisher")
    if installer.get("url") != "https://grumpydev.ai/skills/grumpydev-install/SKILL.md":
        fail(errors, MANIFEST.relative_to(ROOT), "invalid installer URL")

    displayed_installer_url = str(installer.get("url", "")).removeprefix("https://")
    if displayed_installer_url not in home_text:
        fail(errors, HOME.relative_to(ROOT), "install prompt does not use the manifest installer URL")
    for path, text in public_html_texts.items():
        if "install.txt" in text:
            fail(errors, path.relative_to(ROOT), "public HTML references the deleted install.txt route")

    for verdict in (
        "APPROVE",
        "APPROVE WITH CONCERNS",
        "REVISE",
        "REJECT",
        "INSUFFICIENT EVIDENCE",
    ):
        if f">{verdict}</span>" not in home_text:
            fail(errors, HOME.relative_to(ROOT), f"homepage is missing verdict {verdict}")
    if "AGENT-GENERATED / HUMAN-OWNED" not in home_text:
        fail(errors, HOME.relative_to(ROOT), "homepage .grump ownership label is incomplete")
    if "Link every review finding to repository evidence" in home_text:
        fail(errors, HOME.relative_to(ROOT), "homepage doctrine stores a generic review rule")
    for path, text in public_html_texts.items():
        if re.search(
            r"\.grump.{0,100}configuration file|configuration file.{0,100}\.grump",
            text,
            re.IGNORECASE | re.DOTALL,
        ):
            fail(errors, path.relative_to(ROOT), ".grump must be described as doctrine")

    count_match = re.search(r"(\d+) AVAILABLE SKILLS", index_text)
    if not count_match or int(count_match.group(1)) != len(manifest.get("skills", [])):
        fail(errors, INDEX.relative_to(ROOT), "available-skill badge does not match the manifest")
    if index_text.count("1 ONE-SHOT INSTALLER") != 1:
        fail(errors, INDEX.relative_to(ROOT), "one-shot installer badge is not synchronized")

    for path, text in (
        (HOW_IT_WORKS, how_it_works_text),
        (INDEX, index_text),
        (SECURITY, security_text),
        (AUTHOR, author_text),
    ):
        descriptions = {
            metadata_description(path, text, "name", "description", errors),
            metadata_description(path, text, "property", "og:description", errors),
            metadata_description(path, text, "name", "twitter:description", errors),
        }
        descriptions.discard("")
        if len(descriptions) > 1:
            fail(errors, path.relative_to(ROOT), "page metadata descriptions are not synchronized")

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
            r'<summary class="p-3 text-sm font-bold text-base-content/70">'
            r'([^<]+) files \(\d+\)</summary>',
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
        fail(errors, INDEX.relative_to(ROOT), "multi-technology catalog titles are not synchronized")
    if index_text.count("catalog-multi-header") != 4:
        fail(errors, INDEX.relative_to(ROOT), "multi-technology card headers are not synchronized")
    if index_text.count('class="catalog-subject-line"') != 9:
        fail(errors, INDEX.relative_to(ROOT), "multi-technology title lines are not synchronized")
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

    if "catalog-directory" in index_text or "card-actions" in index_text:
        fail(errors, INDEX.relative_to(ROOT), "catalog files must be grouped in the collapsed file list")
    if index_text.count(">SKILL.md</a>") != len(entries):
        fail(errors, INDEX.relative_to(ROOT), "catalog SKILL.md links are not synchronized")
    expected_survey_links = sum(
        isinstance(entry, dict) and entry.get("type") in SPECIALIST_TYPES
        for entry in entries
    )
    if index_text.count(">SURVEY.md</a>") != expected_survey_links:
        fail(errors, INDEX.relative_to(ROOT), "catalog SURVEY.md links are not synchronized")

    names: set[str] = set()
    aliases: set[str] = set()
    urls: set[str] = set()
    manifest_paths: set[Path] = set()
    manifest_survey_paths: set[Path] = set()
    manifest_reference_paths: set[Path] = set()
    entry_by_name: dict[str, dict[str, object]] = {}

    for entry in entries:
        if not isinstance(entry, dict):
            fail(errors, MANIFEST.relative_to(ROOT), "skill entry must be an object")
            continue
        skill_type = entry.get("type")
        expected_fields = {
            "name",
            "type",
            "description",
            "aliases",
            "publisher",
            "files",
        }
        if set(entry) != expected_fields:
            fail(
                errors,
                MANIFEST.relative_to(ROOT),
                f"invalid fields for skill entry {entry.get('name')!r}",
            )
            continue
        name = entry.get("name")
        description = entry.get("description")
        publisher = entry.get("publisher")
        entry_aliases = entry.get("aliases")
        entry_files = entry.get("files")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            fail(errors, MANIFEST.relative_to(ROOT), f"invalid manifest skill name {name!r}")
            continue
        if skill_type not in ALLOWED_TYPES:
            fail(errors, MANIFEST.relative_to(ROOT), f"invalid type for {name}: {skill_type!r}")
            continue
        if publisher != "grumpydev.ai":
            fail(errors, MANIFEST.relative_to(ROOT), f"publisher for {name} must be grumpydev.ai")
        if not isinstance(description, str) or not description:
            fail(errors, MANIFEST.relative_to(ROOT), f"invalid description for {name}")
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
        if not isinstance(entry_files, list):
            fail(errors, MANIFEST.relative_to(ROOT), f"files for {name} must be a list")
            entry_files = []
        roles: list[str] = []
        file_paths: set[str] = set()
        expected_order: list[tuple[int, str]] = []
        for item in entry_files:
            if not isinstance(item, dict) or set(item) != {"path", "role", "url"}:
                fail(errors, MANIFEST.relative_to(ROOT), f"invalid file record for {name}")
                continue
            relative = item.get("path")
            role = item.get("role")
            url = item.get("url")
            if not valid_package_path(relative):
                fail(errors, MANIFEST.relative_to(ROOT), f"unsafe package path for {name}: {relative!r}")
                continue
            assert isinstance(relative, str)
            if relative in file_paths:
                fail(errors, MANIFEST.relative_to(ROOT), f"duplicate package path for {name}: {relative}")
            file_paths.add(relative)
            if role not in {"entrypoint", "survey", "reference"}:
                fail(errors, MANIFEST.relative_to(ROOT), f"invalid file role for {name}: {role!r}")
                continue
            roles.append(role)
            if role == "entrypoint" and relative != "SKILL.md":
                fail(errors, MANIFEST.relative_to(ROOT), f"entrypoint path for {name} must be SKILL.md")
            if role == "survey" and relative != "SURVEY.md":
                fail(errors, MANIFEST.relative_to(ROOT), f"survey path for {name} must be SURVEY.md")
            if role == "reference" and not (
                relative.startswith("references/") and relative.endswith(".md")
            ):
                fail(errors, MANIFEST.relative_to(ROOT), f"invalid reference path for {name}: {relative}")
            expected_url = expected_file_url(entry, relative)
            if url != expected_url:
                fail(errors, MANIFEST.relative_to(ROOT), f"noncanonical file URL for {name}: {relative}")
            if not isinstance(url, str) or url in urls:
                fail(errors, MANIFEST.relative_to(ROOT), f"duplicate or invalid URL for {name}: {url!r}")
            else:
                urls.add(url)
            local_path = expected_package_path(entry) / relative
            if role == "entrypoint":
                manifest_paths.add(local_path)
            if role == "survey":
                manifest_survey_paths.add(local_path)
            if role == "reference":
                manifest_reference_paths.add(local_path)
            role_rank = {"entrypoint": 0, "survey": 1, "reference": 2}[role]
            expected_order.append((role_rank, relative))
        if roles.count("entrypoint") != 1:
            fail(errors, MANIFEST.relative_to(ROOT), f"{name} must have exactly one entrypoint")
        expected_surveys = 1 if skill_type in SPECIALIST_TYPES else 0
        if roles.count("survey") != expected_surveys:
            fail(errors, MANIFEST.relative_to(ROOT), f"invalid survey count for {name}")
        if expected_order != sorted(expected_order):
            fail(errors, MANIFEST.relative_to(ROOT), f"nondeterministic file order for {name}")
        entry_by_name[name] = entry

    catalog_cards = re.findall(
        r'<article class="card border soft-rule bg-base-200">.*?</article>',
        index_text,
        re.DOTALL,
    )
    if len(catalog_cards) != len(entries):
        fail(errors, INDEX.relative_to(ROOT), "catalog card count does not match the manifest")
    catalog_file_total = 0
    seen_file_cards: set[str] = set()
    for card in catalog_cards:
        details_matches = re.findall(
            r'<details class="mt-2 rounded-xl border soft-rule bg-base-300">'
            r'<summary class="p-3 text-sm font-bold text-base-content/70">'
            r'([^<]+) files \((\d+)\)</summary>'
            r'<ul class="[^"]+">(.*?)</ul></details>',
            card,
            re.DOTALL,
        )
        if len(details_matches) != 1:
            fail(errors, INDEX.relative_to(ROOT), "each catalog card must have one directory file list")
            continue
        name, displayed_count, file_markup = details_matches[0]
        entry = entry_by_name.get(name)
        if entry is None:
            fail(errors, INDEX.relative_to(ROOT), f"catalog card has unknown skill {name}")
            continue
        if name in seen_file_cards:
            fail(errors, INDEX.relative_to(ROOT), f"catalog has duplicate skill card {name}")
            continue
        seen_file_cards.add(name)
        files = entry.get("files")
        expected_files = [item for item in files if isinstance(item, dict)] if isinstance(files, list) else []
        catalog_file_total += len(expected_files)
        if int(displayed_count) != len(expected_files):
            fail(errors, INDEX.relative_to(ROOT), f"{name} file count does not match manifest")
        actual_links = re.findall(
            r'<a class="link link-primary" style="overflow-wrap:anywhere" '
            r'href="([^"]+)">([^<]+)</a>',
            file_markup,
        )
        expected_links = [
            (
                expected_catalog_file_href(entry, str(item["path"])),
                PurePosixPath(str(item["path"])).name,
            )
            for item in expected_files
        ]
        if actual_links != expected_links:
            fail(errors, INDEX.relative_to(ROOT), f"{name} file links do not match manifest")
    if seen_file_cards != set(entry_by_name):
        fail(errors, INDEX.relative_to(ROOT), "catalog file lists do not cover every skill")
    file_summary_count = len(
        re.findall(
            r'<summary class="p-3 text-sm font-bold text-base-content/70">'
            r'[^<]+ files \(\d+\)</summary>',
            index_text,
        )
    )
    if file_summary_count != len(entries):
        fail(errors, INDEX.relative_to(ROOT), "catalog file summary count is not synchronized")
    expected_file_total = sum(
        len(entry["files"]) if isinstance(entry.get("files"), list) else 0
        for entry in entry_by_name.values()
    )
    if catalog_file_total != expected_file_total:
        fail(errors, INDEX.relative_to(ROOT), "catalog file-link total is not synchronized")

    state_match = re.search(
        r'<code id="state-example">(.*?)</code>',
        security_text,
        re.DOTALL,
    )
    state_example: object = None
    if not state_match:
        fail(errors, SECURITY.relative_to(ROOT), "missing machine-readable state example")
    else:
        state_source = re.sub(r"<[^>]+>", "", state_match.group(1))
        try:
            state_example = json.loads(html_lib.unescape(state_source))
        except json.JSONDecodeError as exc:
            fail(errors, SECURITY.relative_to(ROOT), f"invalid state example JSON: {exc}")
    if isinstance(state_example, dict):
        if set(state_example) != STATE_TOP_LEVEL_KEYS:
            fail(errors, SECURITY.relative_to(ROOT), "state example has incorrect top-level keys")
        if state_example.get("grumpydev_version") != 1:
            fail(errors, SECURITY.relative_to(ROOT), "state example has incorrect version")
        if not isinstance(state_example.get("host"), str) or not state_example.get("host"):
            fail(errors, SECURITY.relative_to(ROOT), "state example host must be a non-empty string")
        if state_example.get("project_scope") != ".":
            fail(errors, SECURITY.relative_to(ROOT), "state example project scope must be repository root")
        if state_example.get("manifest_url") != "https://grumpydev.ai/manifest.json":
            fail(errors, SECURITY.relative_to(ROOT), "state example manifest URL is incorrect")
        checked = state_example.get("last_successful_check")
        if not isinstance(checked, str) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
            checked,
        ):
            fail(errors, SECURITY.relative_to(ROOT), "state example check time is not ISO 8601 UTC")
        packages = state_example.get("packages")
        if not isinstance(packages, list) or len(packages) != 1:
            fail(errors, SECURITY.relative_to(ROOT), "state example must contain one package")
        else:
            package = packages[0]
            if not isinstance(package, dict) or set(package) != STATE_PACKAGE_KEYS:
                fail(errors, SECURITY.relative_to(ROOT), "state example package keys are incorrect")
            elif package.get("name") != "react":
                fail(errors, SECURITY.relative_to(ROOT), "state example must use React")
            else:
                react = entry_by_name.get("react", {})
                if package.get("type") != react.get("type"):
                    fail(errors, SECURITY.relative_to(ROOT), "state example React type is incorrect")
                if package.get("publisher") != react.get("publisher"):
                    fail(errors, SECURITY.relative_to(ROOT), "state example React publisher is incorrect")
                package_files = package.get("files")
                manifest_files = react.get("files")
                if not isinstance(package_files, list) or not isinstance(manifest_files, list):
                    fail(errors, SECURITY.relative_to(ROOT), "state example React files are invalid")
                else:
                    for item in package_files:
                        if not isinstance(item, dict) or set(item) != STATE_FILE_KEYS:
                            fail(errors, SECURITY.relative_to(ROOT), "state example file keys are incorrect")
                            break
                    actual_sources = [
                        item.get("source_url") for item in package_files if isinstance(item, dict)
                    ]
                    expected_sources = [
                        item.get("url") for item in manifest_files if isinstance(item, dict)
                    ]
                    if actual_sources != expected_sources:
                        fail(errors, SECURITY.relative_to(ROOT), "state example React files are incomplete")
                    for state_file, manifest_file in zip(package_files, manifest_files):
                        if not isinstance(state_file, dict) or not isinstance(manifest_file, dict):
                            continue
                        if state_file.get("role") != manifest_file.get("role"):
                            fail(errors, SECURITY.relative_to(ROOT), "state example file role is incorrect")
                        local_path = state_file.get("local_path")
                        relative = manifest_file.get("path")
                        if not isinstance(local_path, str) or not isinstance(relative, str):
                            fail(errors, SECURITY.relative_to(ROOT), "state example local path is invalid")
                            continue
                        expected_suffix = ("react", *PurePosixPath(relative).parts)
                        if PurePosixPath(local_path).parts[-len(expected_suffix) :] != expected_suffix:
                            fail(errors, SECURITY.relative_to(ROOT), "state example local path is incorrect")
        if state_has_prohibited_key(state_example):
            fail(errors, SECURITY.relative_to(ROOT), "state example contains an integrity field")
    elif state_example is not None:
        fail(errors, SECURITY.relative_to(ROOT), "state example must be a JSON object")

    disk_paths = set(SKILLS.glob("**/SKILL.md")) - {INSTALLER}
    for path in sorted(manifest_paths - disk_paths):
        fail(errors, path.relative_to(ROOT), "manifest entry has no skill file")
    for path in sorted(disk_paths - manifest_paths):
        fail(errors, path.relative_to(ROOT), "skill file has no manifest entry")

    disk_survey_paths = set(SKILLS.glob("**/SURVEY.md"))
    for path in sorted(manifest_survey_paths - disk_survey_paths):
        fail(errors, path.relative_to(ROOT), "specialist manifest entry has no survey file")
    for path in sorted(disk_survey_paths - manifest_survey_paths):
        fail(errors, path.relative_to(ROOT), "survey file has no specialist manifest entry")

    disk_reference_paths = set(SKILLS.glob("**/references/*.md"))
    for path in sorted(manifest_reference_paths - disk_reference_paths):
        fail(errors, path.relative_to(ROOT), "manifest reference has no local file")
    for path in sorted(disk_reference_paths - manifest_reference_paths):
        fail(errors, path.relative_to(ROOT), "reference file has no manifest entry")

    expected_focused_paths = {
        SKILLS / package / "references" / filename
        for package, filenames in EXPECTED_FOCUSED_REFERENCES.items()
        for filename in filenames
    }
    specialist_reference_paths = {
        path
        for path in disk_reference_paths
        if path.relative_to(SKILLS).parts[0] in SPECIALIST_TYPES
    }
    actual_focused_paths = {
        path for path in specialist_reference_paths if path.name != "review.md"
    }
    if len(EXPECTED_FOCUSED_REFERENCES) != 28:
        fail(errors, "tools/validate_catalog.py", "focused-reference package set must contain 28 packages")
    if len(expected_focused_paths) != 71:
        fail(errors, "tools/validate_catalog.py", "focused-reference path set must contain 71 files")
    if len(specialist_reference_paths) != 196:
        fail(
            errors,
            SKILLS.relative_to(ROOT),
            "specialist catalog must contain exactly 196 reference files",
        )
    for path in sorted(expected_focused_paths - actual_focused_paths):
        fail(errors, path.relative_to(ROOT), "required focused reference is missing")
    for path in sorted(actual_focused_paths - expected_focused_paths):
        fail(errors, path.relative_to(ROOT), "unplanned focused reference is present")

    actual_multi_reference_packages = {
        path.parent.parent.relative_to(SKILLS).as_posix()
        for path in actual_focused_paths
    }
    expected_multi_reference_packages = set(EXPECTED_FOCUSED_REFERENCES)
    if actual_multi_reference_packages != expected_multi_reference_packages:
        fail(
            errors,
            SKILLS.relative_to(ROOT),
            "multi-reference specialist package set does not match the fixed layout",
        )

    for package, filenames in EXPECTED_FOCUSED_REFERENCES.items():
        package_path = SKILLS / package
        entrypoint_text = read_text(package_path / "SKILL.md", errors)
        fixture_path = (
            ROOT
            / "tests"
            / "skills"
            / "specialists"
            / f"{package}.md"
        )
        fixture_text = read_text(fixture_path, errors)
        lowered_entrypoint = entrypoint_text.lower()
        for prohibited_route in ("read all references", "read references as needed"):
            if prohibited_route in lowered_entrypoint:
                fail(
                    errors,
                    (package_path / "SKILL.md").relative_to(ROOT),
                    f"undefined focused-reference routing: {prohibited_route}",
                )
        normalized_entrypoint = " ".join(entrypoint_text.split())
        if normalized_entrypoint.count(
            "Read when the reviewed work directly or indirectly"
        ) != len(filenames):
            fail(
                errors,
                (package_path / "SKILL.md").relative_to(ROOT),
                "every focused route must cover direct and indirect effects",
            )
        seen_blocks: dict[str, str] = {}
        package_references = [package_path / "references" / "review.md"]
        package_references.extend(
            package_path / "references" / filename for filename in filenames
        )
        for reference in package_references:
            reference_text = read_text(reference, errors)
            if reference.name != "review.md":
                first_line = reference_text.splitlines()[0] if reference_text else ""
                if not first_line.startswith("# ") or len(first_line) == 2:
                    fail(
                        errors,
                        reference.relative_to(ROOT),
                        "focused reference must begin with one plain-text title",
                    )
                if reference_text.count("Read this reference when") != 1:
                    fail(
                        errors,
                        reference.relative_to(ROOT),
                        "focused reference must contain exactly one loading trigger",
                    )
                if (
                    "Read this reference when the reviewed work directly or indirectly "
                    not in " ".join(reference_text.split())
                ):
                    fail(
                        errors,
                        reference.relative_to(ROOT),
                        "focused reference trigger must cover direct and indirect effects",
                    )
                if not re.search(r"(?m)^- ", reference_text):
                    fail(
                        errors,
                        reference.relative_to(ROOT),
                        "focused reference must contain actionable review guidance",
                    )
            for block in substantive_blocks(reference_text):
                owner = seen_blocks.get(block)
                if owner is not None:
                    fail(
                        errors,
                        reference.relative_to(ROOT),
                        f"duplicates a substantive block from {owner}",
                    )
                else:
                    seen_blocks[block] = reference.relative_to(ROOT).as_posix()
        for filename in filenames:
            relative = f"references/{filename}"
            if entrypoint_text.count(relative) != 1:
                fail(
                    errors,
                    (package_path / "SKILL.md").relative_to(ROOT),
                    f"focused reference must be routed exactly once: {relative}",
                )
            fixture_heading = f"### `{relative}`"
            if fixture_text.count(fixture_heading) != 1:
                fail(
                    errors,
                    fixture_path.relative_to(ROOT),
                    f"missing focused fixture heading for {relative}",
                )
            fixture_section = fixture_text.split(fixture_heading, 1)[1]
            fixture_section = fixture_section.split("\n### `references/", 1)[0]
            for marker in (
                "Positive trigger:",
                "Negative trigger:",
                f"loads `{relative}`",
                f"does not load `{relative}`",
            ):
                if marker not in fixture_section:
                    fail(
                        errors,
                        fixture_path.relative_to(ROOT),
                        f"focused fixture for {relative} is missing {marker}",
                    )

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
        if description != entry.get("description"):
            fail(errors, path.relative_to(ROOT), "frontmatter description does not match manifest")
        if name == "grumpydev":
            if not description.startswith(CORE_INVOCATION_PREFIX):
                fail(errors, path.relative_to(ROOT), "core review description lacks invocation gate")
            if text.count("## Explicit invocation only") != 1:
                fail(errors, path.relative_to(ROOT), "core review lacks one explicit invocation boundary")
            if "it does not invoke a review" not in text:
                fail(errors, path.relative_to(ROOT), "execution-rules-only request is not separated from review")
        elif name == "grumpydev-survey":
            if not description.startswith(SURVEY_INVOCATION_PREFIX):
                fail(errors, path.relative_to(ROOT), "survey description lacks invocation gate")
            if text.count("## Invocation boundary") != 1:
                fail(errors, path.relative_to(ROOT), "survey lacks one invocation boundary")
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
            if not description.startswith(REVIEW_INVOCATION_PREFIX):
                fail(errors, path.relative_to(ROOT), "specialist description lacks review invocation gate")
            if description.count(PROJECT_APPLICABILITY_MARKER) != 1:
                fail(errors, path.relative_to(ROOT), "specialist description lacks one project-applicability field")
            else:
                project_applicability = description.split(PROJECT_APPLICABILITY_MARKER, 1)[1]
                if re.search(r"\bplan\b", project_applicability, re.IGNORECASE):
                    fail(errors, path.relative_to(ROOT), "specialist applicability is plan-scoped")
            if text.count("## Invocation and participation boundary") != 1:
                fail(errors, path.relative_to(ROOT), "specialist lacks one participation boundary")
            for marker in (
                "This specialist cannot start a GrumpyDev review.",
                "use this entrypoint during every explicitly invoked GrumpyDev",
                "Evaluate direct and indirect effects even when the reviewed work does",
                "Produce no finding when no material effect",
            ):
                if marker not in text:
                    fail(errors, path.relative_to(ROOT), f"specialist participation boundary is missing {marker}")
            if "When this entrypoint identifies a plausible direct or indirect material effect" not in text:
                fail(errors, path.relative_to(ROOT), "specialist review reference is not impact-routed")
            review_reference = path.parent / "references" / "review.md"
            if not review_reference.exists():
                fail(
                    errors,
                    path.relative_to(ROOT),
                    "specialist is missing references/review.md",
                )
            else:
                for marker in COMPACT_ENTRYPOINT_MARKERS:
                    if marker not in text:
                        fail(errors, path.relative_to(ROOT), f"compact entrypoint missing {marker}")
                if "Lean mode is insufficient" not in text:
                    fail(
                        errors,
                        path.relative_to(ROOT),
                        "compact entrypoint is missing a lean escalation condition",
                    )
                link = "references/review.md"
                if link not in text:
                    fail(errors, path.relative_to(ROOT), "compact entrypoint does not route review.md")
                review_text = read_text(review_reference, errors)
                validate_body_lines(review_reference, review_text, errors, frontmatter=False)
                validate_section_order(
                    review_reference,
                    review_text,
                    REQUIRED_REFERENCE_SECTIONS,
                    errors,
                )
                validate_nonempty_sections(
                    review_reference,
                    review_text,
                    REQUIRED_REFERENCE_SECTIONS,
                    errors,
                )
                if review_text.startswith("---"):
                    fail(errors, review_reference.relative_to(ROOT), "reference must not have frontmatter")
                if review_text.count("### Recurring traps") != 1:
                    fail(errors, review_reference.relative_to(ROOT), "review reference must contain Recurring traps")
                duplicated_blocks = substantive_blocks(text) & substantive_blocks(
                    review_text
                )
                if duplicated_blocks:
                    fail(
                        errors,
                        review_reference.relative_to(ROOT),
                        "standard review repeats substantive entrypoint text",
                    )
                for detailed_section in REQUIRED_SECTIONS[:-1]:
                    if detailed_section in text:
                        fail(
                            errors,
                            path.relative_to(ROOT),
                            f"detailed section leaked into compact entrypoint: {detailed_section}",
                        )
                if "### Recurring traps" in text:
                    fail(
                        errors,
                        path.relative_to(ROOT),
                        "detailed Recurring traps subsection leaked into compact entrypoint",
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
                for marker in (
                    "This is project-level applicability, not a current-plan trigger.",
                    "participates in every explicitly invoked GrumpyDev review.",
                ):
                    if marker not in " ".join(survey_text.split()):
                        fail(
                            errors,
                            survey.relative_to(ROOT),
                            f"survey applicability contract is missing {marker}",
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
                for marker in (
                    "Lean mode loads",
                    "Deep mode loads",
                    "No ordinary review loads",
                    "every explicitly invoked GrumpyDev review loads its `SKILL.md`",
                    "evaluates direct and indirect effects",
                    "produces no finding",
                ):
                    if marker not in fixture_text:
                        fail(
                            errors,
                            fixture.relative_to(ROOT),
                            f"fixture is missing mode-aware loading marker {marker}",
                        )
                normalized_fixture = " ".join(fixture_text.split())
                standard_loading = (
                    "Standard mode loads `SKILL.md` and loads "
                    "`references/review.md` only when the entrypoint identifies a "
                    "plausible direct or indirect material effect."
                )
                if standard_loading not in normalized_fixture:
                    fail(
                        errors,
                        fixture.relative_to(ROOT),
                        "fixture does not make standard reference loading impact-routed",
                    )
        elif name in CORE_PATTERN_SECTIONS:
            pattern_section = CORE_PATTERN_SECTIONS[name]
            package_text = text
            for reference in sorted(path.parent.glob("references/*.md")):
                package_text += "\n" + read_text(reference, errors)
            if package_text.count(pattern_section) != 1:
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

    if INSTALLER.exists():
        installer_text = read_text(INSTALLER, errors)
        installer_values = parse_frontmatter(INSTALLER, installer_text, errors)
        validate_body_lines(INSTALLER, installer_text, errors, frontmatter=True)
        if installer_values.get("name") != "grumpydev-install":
            fail(errors, INSTALLER.relative_to(ROOT), "installer frontmatter name mismatch")
        if installer_values.get("description") != installer.get("description"):
            fail(errors, INSTALLER.relative_to(ROOT), "installer description does not match manifest")
        state_section_match = re.search(
            r"## Record local state\n(.*?)(?=\n## )",
            installer_text,
            re.DOTALL,
        )
        if not state_section_match:
            fail(errors, INSTALLER.relative_to(ROOT), "missing state contract")
        else:
            state_section = state_section_match.group(1)
            declared_keys = set(
                re.findall(r"^- `([a-z_]+)`:", state_section, re.MULTILINE)
            )
            if declared_keys != STATE_TOP_LEVEL_KEYS:
                fail(errors, INSTALLER.relative_to(ROOT), "state contract top-level keys are incorrect")
            package_match = re.search(
                r"Each package record uses exactly (.*?)\.",
                state_section,
                re.DOTALL,
            )
            package_keys = set(re.findall(r"`([a-z_]+)`", package_match.group(1))) if package_match else set()
            file_match = re.search(
                r"Each\s+file record uses exactly (.*?)\.",
                state_section,
                re.DOTALL,
            )
            file_keys = set(re.findall(r"`([a-z_]+)`", file_match.group(1))) if file_match else set()
            if package_keys != STATE_PACKAGE_KEYS:
                fail(errors, INSTALLER.relative_to(ROOT), "state package keys are not exact")
            if file_keys != STATE_FILE_KEYS:
                fail(errors, INSTALLER.relative_to(ROOT), "state file keys are not exact")
    else:
        fail(errors, INSTALLER.relative_to(ROOT), "missing one-shot installer skill")

    for reference in sorted(disk_reference_paths):
        reference_text = read_text(reference, errors)
        validate_body_lines(reference, reference_text, errors, frontmatter=False)
        if reference_text.startswith("---"):
            fail(errors, reference.relative_to(ROOT), "reference must not have frontmatter")
        if re.search(r"https?://", reference_text):
            fail(errors, reference.relative_to(ROOT), "runtime reference must not contain external URLs")
        package = reference.parent.parent
        relative_link = reference.relative_to(package).as_posix()
        entrypoint_text = (package / "SKILL.md").read_text(encoding="utf-8")
        survey_path = package / "SURVEY.md"
        survey_text = survey_path.read_text(encoding="utf-8") if survey_path.exists() else ""
        if relative_link not in entrypoint_text and relative_link not in survey_text:
            fail(errors, reference.relative_to(ROOT), "reference is not routed from SKILL.md or SURVEY.md")

    core_fixtures = sorted((ROOT / "tests" / "skills" / "core").glob("*.md"))
    if not core_fixtures:
        fail(errors, "tests/skills/core", "missing core behavioral fixtures")
    for fixture in core_fixtures:
        fixture_text = read_text(fixture, errors)
        if "Expected behavior:" not in fixture_text:
            fail(errors, fixture.relative_to(ROOT), "missing Expected behavior marker")

    gitignore_fixture = ROOT / "tests" / "skills" / "core" / "gitignore-preference.md"
    gitignore_fixture_text = read_text(gitignore_fixture, errors)
    for marker in (
        "repository-root `.gitignore`",
        "`.grump`",
        "`.grumpydev/`",
        "Do not add the installed skill directory",
        "Never ask this preference during re-survey",
        "`.gitignore` itself is authoritative",
    ):
        if marker not in gitignore_fixture_text:
            fail(
                errors,
                gitignore_fixture.relative_to(ROOT),
                f"gitignore preference fixture is missing {marker}",
            )

    presentation_fixture = ROOT / "tests" / "skills" / "core" / "review-presentation.md"
    presentation_fixture_text = read_text(presentation_fixture, errors)
    presentation_fixture_normalized = " ".join(presentation_fixture_text.split())
    for marker in (
        "preferred finding tables and enabled status icons",
        "`Finding tables: disabled`",
        "`Status icons: disabled`",
        "target-scoped `GD-###` identifier",
        "same repository-relative artifact",
        "Never infer target continuity",
        "evaluation-scoped `TMP-###` IDs without lifecycle status",
        "`NEW`, `OPEN`, `RESOLVED`, or `REGRESSED`",
        "Require current evidence before marking an issue `RESOLVED`",
        "one `Summary:` sentence",
        "When finding tables are preferred",
        "ID | Severity | Issue | Why it matters | Required action",
        "Pair every icon with a text verdict",
        "evidence -> failure condition -> impact -> required action",
        "final `Review scope` footer",
    ):
        if marker not in presentation_fixture_normalized:
            fail(
                errors,
                presentation_fixture.relative_to(ROOT),
                f"review presentation fixture is missing {marker}",
            )

    project_specialist_fixture = ROOT / "tests" / "skills" / "core" / "project-wide-specialists.md"
    project_specialist_text = read_text(project_specialist_fixture, errors)
    for marker in (
        "Every active specialist entrypoint evaluates direct and indirect effects.",
        "Both specialist entrypoints participate.",
        "Report incomplete specialist coverage",
        "Do not fetch the Kubernetes package",
    ):
        if marker not in project_specialist_text:
            fail(
                errors,
                project_specialist_fixture.relative_to(ROOT),
                f"project-wide specialist fixture is missing {marker}",
            )

    detailed_doctrine_path = DOCTRINE_FIXTURES / "doctrine-detailed.md"
    compact_doctrine_path = DOCTRINE_FIXTURES / "doctrine-compact.md"
    detailed_doctrine = read_text(detailed_doctrine_path, errors)
    compact_doctrine = read_text(compact_doctrine_path, errors)
    if len(compact_doctrine.split()) >= len(detailed_doctrine.split()):
        fail(
            errors,
            compact_doctrine_path.relative_to(ROOT),
            "compact doctrine fixture is not smaller than detailed fixture",
        )
    detailed_ids = set(re.findall(r"\b[A-Z]{3}-\d{3}\b", detailed_doctrine))
    compact_ids = set(re.findall(r"\b[A-Z]{3}-\d{3}\b", compact_doctrine))
    if detailed_ids != compact_ids:
        fail(
            errors,
            compact_doctrine_path.relative_to(ROOT),
            "compact and detailed doctrine identifiers differ",
        )
    normalized_detailed = " ".join(detailed_doctrine.lower().split())
    normalized_compact = " ".join(compact_doctrine.lower().split())
    doctrine_markers = (
        "plan addenda: allowed",
        "review interaction: interactive",
        "doctrine promotion: ask first",
        "open research: blocks readiness",
        "research execution: grumpydev may perform it",
        "node.js 22",
        "linux",
        "container",
        "postgresql 17",
        "managed vendor",
        "point-in-time restore",
        "15-minute recovery point objective",
        "tenant-scoped idempotency key",
        "15 minutes",
        "object storage",
        "mixed-version",
        "cross-tenant access",
        "object-storage retention",
    )
    for marker in doctrine_markers:
        if marker not in normalized_detailed or marker not in normalized_compact:
            fail(
                errors,
                compact_doctrine_path.relative_to(ROOT),
                f"doctrine fixture pair is missing shared semantic marker {marker!r}",
            )

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
    count = len(set(SKILLS.glob("**/SKILL.md")) - {INSTALLER})
    print(f"OK: validated {count} installable skills and installer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
