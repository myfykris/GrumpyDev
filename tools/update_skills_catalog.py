#!/usr/bin/env python3
"""Synchronize human-facing skill summaries with manifest descriptions."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "html" / "manifest.json"
DEFAULT_INDEX = ROOT / "html" / "skills" / "index.html"

CORE_INVOCATION_PREFIX = (
    "Use only for an explicitly invoked GrumpyDev review, an explicit request to "
    "add GrumpyDev execution rules, or an explicit request to remove GrumpyDev from "
    "the current project. Do not activate merely because work is being planned, "
    "created, revised, discussed, implemented, or generically reviewed. "
)
SPECIALIST_INVOCATION_PREFIX = (
    "Use only when the user explicitly asks for a GrumpyDev review. Never start a "
    "review automatically. If installed and not marked inapplicable, use this skill "
    "in every GrumpyDev review. "
)
SURVEY_INVOCATION_PREFIX = (
    "Use only during GrumpyDev installation or setup, or for an explicitly requested "
    "re-survey or doctrine refresh. Do not activate during ordinary planning, plan "
    "creation, revision, review, or implementation. "
)
CATALOG_SUMMARY_OVERRIDES = {
    "Survey an existing software repository and create or update its human-owned .grump "
    "project doctrine.": (
        "Surveys a repository and creates or updates its project review rules in .grump."
    ),
}
ARTICLE_START = '<article class="card '
ARTICLE_END = "</article>"
DIRECTORY_RE = re.compile(
    r'<summary class="p-3 text-sm font-bold text-base-content/70">'
    r'([^<]+) files \(\d+\)</summary>'
)
DESCRIPTION_RE = re.compile(
    r'(<p class="text-sm leading-6 text-base-content/60">)(.*?)(</p>)',
    re.DOTALL,
)


class CatalogUpdateError(ValueError):
    """Raised when catalog structure or input encoding is invalid."""


@dataclass(frozen=True)
class CatalogRecord:
    """Manifest data needed to identify and update one catalog card."""

    name: str
    skill_href: str
    summary: str


def read_utf8_lf(path: Path) -> str:
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CatalogUpdateError(f"{path}: invalid UTF-8: {exc}") from exc
    if b"\r" in data:
        raise CatalogUpdateError(f"{path}: CR line ending is not allowed")
    return text


def catalog_summary(description: str) -> str:
    for prefix in (
        CORE_INVOCATION_PREFIX,
        SPECIALIST_INVOCATION_PREFIX,
        SURVEY_INVOCATION_PREFIX,
    ):
        if description.startswith(prefix):
            description = description[len(prefix) :]
            break
    summary = re.split(r" Applies (?:when|during) | Use when ", description, maxsplit=1)[0]
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


def manifest_catalog_records(manifest_path: Path) -> dict[str, CatalogRecord]:
    try:
        manifest = json.loads(read_utf8_lf(manifest_path))
    except json.JSONDecodeError as exc:
        raise CatalogUpdateError(f"{manifest_path}: invalid JSON: {exc}") from exc
    entries = manifest.get("skills")
    if not isinstance(entries, list):
        raise CatalogUpdateError(f"{manifest_path}: skills must be an array")
    records: dict[str, CatalogRecord] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise CatalogUpdateError(f"{manifest_path}: skill entry must be an object")
        name = entry.get("name")
        skill_type = entry.get("type")
        description = entry.get("description")
        if not all(isinstance(value, str) for value in (name, skill_type, description)):
            raise CatalogUpdateError(
                f"{manifest_path}: invalid name, type, or description"
            )
        assert isinstance(name, str)
        assert isinstance(skill_type, str)
        assert isinstance(description, str)
        if name in records:
            raise CatalogUpdateError(f"{manifest_path}: duplicate skill name {name}")
        if skill_type == "core":
            skill_href = f"./{name}/SKILL.md"
        else:
            skill_href = f"./{skill_type}/{name}/SKILL.md"
        records[name] = CatalogRecord(
            name=name,
            skill_href=skill_href,
            summary=catalog_summary(description),
        )
    return records


def _card_bounds(index_text: str, link_position: int, name: str) -> tuple[int, int]:
    start = index_text.rfind(ARTICLE_START, 0, link_position)
    if start < 0:
        raise CatalogUpdateError(f"catalog SKILL.md link for {name} has no card start")
    previous_end = index_text.rfind(ARTICLE_END, 0, link_position)
    if previous_end > start:
        raise CatalogUpdateError(f"catalog SKILL.md link for {name} is outside its card")
    end = index_text.find(ARTICLE_END, link_position)
    if end < 0:
        raise CatalogUpdateError(f"catalog card for {name} has no closing article tag")
    nested_start = index_text.find(ARTICLE_START, start + len(ARTICLE_START), end)
    if nested_start >= 0:
        raise CatalogUpdateError(f"catalog card boundary for {name} is ambiguous")
    return start, end + len(ARTICLE_END)


def render_catalog(index_text: str, records: dict[str, CatalogRecord]) -> str:
    replacements: list[tuple[int, int, str]] = []
    card_bounds: set[tuple[int, int]] = set()

    for name, record in records.items():
        escaped_href = html.escape(record.skill_href, quote=True)
        link_marker = f'href="{escaped_href}">SKILL.md</a>'
        link_count = index_text.count(link_marker)
        if link_count != 1:
            raise CatalogUpdateError(
                f"catalog must contain exactly one SKILL.md link for {name}; found {link_count}"
            )
        link_position = index_text.find(link_marker)
        start, end = _card_bounds(index_text, link_position, name)
        if (start, end) in card_bounds:
            raise CatalogUpdateError("catalog card is associated with more than one skill")
        card_bounds.add((start, end))
        card = index_text[start:end]

        directory_matches = DIRECTORY_RE.findall(card)
        if len(directory_matches) != 1:
            raise CatalogUpdateError(
                f"catalog card for {name} must contain one directory file-list label"
            )
        directory_name = html.unescape(directory_matches[0])
        if directory_name != name:
            raise CatalogUpdateError(
                f"catalog SKILL.md link for {name} is in the {directory_name} card"
            )

        summary_matches = list(DESCRIPTION_RE.finditer(card))
        if len(summary_matches) != 1:
            raise CatalogUpdateError(
                f"catalog card for {name} must contain one summary paragraph"
            )
        summary_match = summary_matches[0]
        summary_start = start + summary_match.start(2)
        summary_end = start + summary_match.end(2)
        replacements.append(
            (summary_start, summary_end, html.escape(record.summary, quote=False))
        )

    for start in reversed([match.start() for match in re.finditer(ARTICLE_START, index_text)]):
        end = index_text.find(ARTICLE_END, start)
        if end < 0:
            raise CatalogUpdateError("catalog card has no closing article tag")
        bounds = (start, end + len(ARTICLE_END))
        if bounds not in card_bounds:
            card = index_text[bounds[0] : bounds[1]]
            if ">SKILL.md</a>" in card or DIRECTORY_RE.search(card):
                raise CatalogUpdateError("catalog contains a card not associated with a manifest skill")

    rendered = index_text
    for start, end, replacement in sorted(replacements, reverse=True):
        rendered = rendered[:start] + replacement + rendered[end:]
    return rendered


def atomic_write(path: Path, text: str) -> None:
    encoded = text.encode("utf-8")
    permissions = stat.S_IMODE(path.stat().st_mode)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=path.parent, prefix=f".{path.name}.", delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, permissions)
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def update_catalog(manifest_path: Path, index_path: Path, *, write: bool) -> bool:
    records = manifest_catalog_records(manifest_path)
    original = read_utf8_lf(index_path)
    rendered = render_catalog(original, records)
    if rendered == original:
        return True
    if write:
        atomic_write(index_path, rendered)
        return True
    return False


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    args = parser.parse_args(argv)
    try:
        current = update_catalog(args.manifest, args.index, write=args.write)
    except (CatalogUpdateError, OSError) as exc:
        print(exc)
        return 1
    if not current:
        print(f"{args.index}: catalog summaries are out of date")
        return 1
    if args.write:
        print(f"updated {args.index}")
    else:
        print(f"OK: {args.index} summaries match the manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
