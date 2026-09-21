#!/usr/bin/env python3
"""Render complete skill cards from the public manifest."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "html" / "manifest.json"
DEFAULT_INDEX = ROOT / "html" / "skills" / "index.html"
ALLOWED_TYPES = {"core", "language", "framework", "paradigm", "storage", "platform"}
MARKER_RE = re.compile(
    r"<!-- (BEGIN|END) GENERATED SKILL CARDS: "
    r"(core|language|framework|paradigm|storage|platform) -->"
)
EXTERNAL_ICON = (
    '<svg class="size-4 shrink-0" width="16" height="16" '
    'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" '
    'stroke-linejoin="round" stroke-width="2" '
    'd="M14 3h7v7m0-7L10 14M5 7v14h14v-5"/></svg>'
)


class RenderError(ValueError):
    pass


def read_text(path: Path) -> str:
    data = path.read_bytes()
    if b"\r" in data:
        raise RenderError(f"{path}: CR line ending is not allowed")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RenderError(f"{path}: invalid UTF-8: {exc}") from exc


def read_manifest(path: Path) -> list[dict[str, object]]:
    try:
        manifest = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise RenderError(f"{path}: invalid JSON: {exc}") from exc
    skills = manifest.get("skills")
    if not isinstance(skills, list):
        raise RenderError("manifest skills must be an array")
    names: set[str] = set()
    for skill in skills:
        if not isinstance(skill, dict):
            raise RenderError("each manifest skill must be an object")
        name = skill.get("name")
        skill_type = skill.get("type")
        skill_path = skill.get("path")
        description = skill.get("description")
        subjects = skill.get("display_subjects")
        files = skill.get("files")
        if not all(isinstance(value, str) and value for value in (name, skill_path, description)):
            raise RenderError("skill name, path, and description must be non-empty strings")
        if name in names:
            raise RenderError(f"duplicate skill name: {name}")
        names.add(name)
        if skill_type not in ALLOWED_TYPES:
            raise RenderError(f"{name}: invalid skill type")
        if not isinstance(subjects, list) or not subjects:
            raise RenderError(f"{name}: display_subjects must be a non-empty array")
        if not isinstance(files, list) or not files:
            raise RenderError(f"{name}: files must be a non-empty array")
    return skills


def subject_html(subject: dict[str, object]) -> str:
    label = subject.get("label")
    url = subject.get("url")
    if not isinstance(label, str) or not label:
        raise RenderError("display subject label must be a non-empty string")
    escaped_label = html.escape(label)
    if url is None:
        return escaped_label
    if not isinstance(url, str) or not url.startswith("https://"):
        raise RenderError(f"{label}: display subject URL must use HTTPS")
    return (
        f'<a class="link link-hover flex items-center gap-1" href="{html.escape(url, quote=True)}" '
        f'target="_blank" rel="noopener noreferrer" '
        f'aria-label="{html.escape(label, quote=True)} website (opens in a new window)">'
        f"{escaped_label}{EXTERNAL_ICON}</a>"
    )


def render_card(skill: dict[str, object]) -> str:
    name = str(skill["name"])
    path = str(skill["path"])
    description = html.escape(str(skill["description"]))
    subjects = skill["display_subjects"]
    files = skill["files"]
    if not isinstance(subjects, list) or not isinstance(files, list):
        raise RenderError(f"{name}: invalid card arrays")
    rendered_subjects = [subject_html(subject) for subject in subjects]
    if len(rendered_subjects) == 1:
        title = f'<div><h3 class="card-title text-lg">{rendered_subjects[0]}</h3></div>'
    else:
        lines = "".join(
            f'<span class="catalog-subject-line">{subject}</span>'
            for subject in rendered_subjects
        )
        title = (
            '<div class="catalog-multi-header"><h3 class="card-title text-lg '
            f'catalog-multi-title">{lines}</h3></div>'
        )
    links = []
    for index, file in enumerate(files):
        if not isinstance(file, dict) or not isinstance(file.get("path"), str):
            raise RenderError(f"{name}: invalid file record")
        file_path = file["path"]
        href = PurePosixPath(path.removeprefix("skills/")) / file_path
        css = ' class="mt-2"' if index else ""
        links.append(
            f'<li{css}><a class="link link-primary catalog-file-link" '
            f'href="./{html.escape(href.as_posix(), quote=True)}">'
            f"{html.escape(PurePosixPath(file_path).name)}</a></li>"
        )
    return (
        '      <article class="card border soft-rule bg-base-200"><div class="card-body p-6">'
        f'{title}<p class="text-sm leading-6 text-base-content/60">{description}</p>'
        '<details class="mt-2 rounded-xl border soft-rule bg-base-300">'
        f'<summary class="p-3 text-sm font-bold text-base-content/70">{html.escape(name)} files ({len(files)})</summary>'
        f'<ul class="border-t soft-rule p-3 text-sm">{"".join(links)}</ul>'
        "</details></div></article>"
    )


def marker_regions(text: str) -> list[tuple[str, int, int]]:
    markers = list(MARKER_RE.finditer(text))
    if len(markers) != len(ALLOWED_TYPES) * 2:
        raise RenderError("catalog must contain exactly one marker pair per skill type")
    regions = []
    seen: set[str] = set()
    open_marker: re.Match[str] | None = None
    for marker in markers:
        action, skill_type = marker.groups()
        if action == "BEGIN":
            if open_marker is not None or skill_type in seen:
                raise RenderError("generated card markers are nested or duplicated")
            open_marker = marker
            seen.add(skill_type)
        else:
            if open_marker is None or open_marker.group(2) != skill_type:
                raise RenderError("generated card markers are mismatched")
            regions.append((skill_type, open_marker.end(), marker.start()))
            open_marker = None
    if open_marker is not None or seen != ALLOWED_TYPES:
        raise RenderError("generated card marker set is incomplete")
    return regions


def render(index_text: str, skills: list[dict[str, object]]) -> str:
    replacements = []
    for skill_type, start, end in marker_regions(index_text):
        cards = [render_card(skill) for skill in skills if skill["type"] == skill_type]
        replacement = "\n" + "\n".join(cards) + "\n      "
        replacements.append((start, end, replacement))
    for start, end, replacement in reversed(replacements):
        index_text = index_text[:start] + replacement + index_text[end:]
    return index_text


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    args = parser.parse_args()
    try:
        original = read_text(args.index)
        rendered = render(original, read_manifest(args.manifest))
    except (OSError, RenderError) as exc:
        print(exc)
        return 1
    if rendered != original:
        if args.write:
            args.index.write_text(rendered, encoding="utf-8", newline="\n")
        else:
            print(f"{args.index}: generated skill cards are out of date")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
