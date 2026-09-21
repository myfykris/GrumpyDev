#!/usr/bin/env python3
"""Validate GrumpyDev manifest, skill files, links, and static site structure."""

from __future__ import annotations

import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

import render_skills_catalog


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"
MANIFEST_PATH = HTML / "manifest.json"
INDEX_PATH = HTML / "skills" / "index.html"
ALLOWED_TYPES = {"core", "language", "framework", "paradigm", "storage", "platform"}
CORE_NAMES = {"grumpydev", "grumpydev-survey", "grumpydev-update-remove"}
ROLES = {"entrypoint", "survey", "reference"}
TOP_KEYS = {"schema_version", "grumpydev_version", "name", "publisher", "base_url", "installer", "skills"}
TEXT_SUFFIXES = {".md", ".html", ".json", ".js", ".css", ".py", ".sh", ".txt", ".xml"}
BANNED_PUNCTUATION = {
    "\u2013": "en dash",
    "\u2014": "em dash",
    "\u2018": "curly apostrophe",
    "\u2019": "curly apostrophe",
    "\u201c": "curly quote",
    "\u201d": "curly quote",
    "\u2026": "Unicode ellipsis",
    "\u2192": "Unicode arrow",
    "\u2212": "Unicode minus",
    "\u00a0": "nonbreaking space",
}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def read_utf8(path: Path, validation: Validation) -> str | None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        validation.errors.append(f"{path}: cannot read: {exc}")
        return None
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        validation.errors.append(f"{path}: invalid UTF-8: {exc}")
        return None
    validation.require(b"\r" not in data, f"{path}: CR line ending is not allowed")
    validation.require(data.endswith(b"\n"), f"{path}: missing final newline")
    for character, name in BANNED_PUNCTUATION.items():
        validation.require(character not in text, f"{path}: contains {name}")
    return text


def safe_relative(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    parsed = urlsplit(value)
    path = PurePosixPath(value)
    return (
        not parsed.scheme
        and not parsed.netloc
        and not parsed.query
        and not parsed.fragment
        and not path.is_absolute()
        and ".." not in path.parts
        and "." not in path.parts
    )


def frontmatter_name(path: Path, expected_name: str, validation: Validation) -> None:
    text = read_utf8(path, validation)
    if text is None:
        return
    match = FRONTMATTER_RE.match(text)
    validation.require(match is not None, f"{path}: missing YAML frontmatter")
    if match is None:
        return
    names = re.findall(r"^name:\s*([^\s]+)\s*$", match.group(1), re.MULTILINE)
    validation.require(len(names) == 1, f"{path}: frontmatter must contain one name")
    if names:
        validation.require(names[0] == expected_name, f"{path}: frontmatter name does not match manifest")
    descriptions = re.findall(r"^description:[ \t]*(.*(?:\n[ \t]+[^\n]*)*)", match.group(1), re.MULTILINE)
    description = " ".join(descriptions[0].strip(" \t\"'|>+-").split()) if len(descriptions) == 1 else ""
    validation.require(bool(description), f"{path}: frontmatter must contain one nonempty description")
    if not description:
        return
    validation.require(bool(re.search(r"\b(?:use|run|activate) only\b", description, re.I)) and bool(re.search(r"\bexplicit(?:ly)?\b", description, re.I)), f"{path}: description must require explicit-only activation")
    if expected_name.startswith("gd-"):
        validation.require("Use only during an explicitly requested GrumpyDev review" in description and "Never start or continue a review automatically." in description, f"{path}: description is missing the specialist discovery safeguards")
    else:
        scopes = {
            "grumpydev": r"\breview\b",
            "grumpydev-survey": r"\b(?:survey|re-survey|doctrine refresh)\b",
            "grumpydev-update-remove": r"(?=.*\bupdate\b)(?=.*\b(?:remove|uninstall)\b)",
            "grumpydev-install": r"\b(?:install|set up)\b",
        }
        scope = scopes.get(expected_name)
        validation.require(scope is not None and bool(re.search(scope, description, re.I)), f"{path}: description does not identify its operation scope")


def validate_manifest(validation: Validation) -> tuple[dict[str, object], list[dict[str, object]]]:
    text = read_utf8(MANIFEST_PATH, validation)
    if text is None:
        return {}, []
    try:
        manifest = json.loads(text)
    except json.JSONDecodeError as exc:
        validation.errors.append(f"{MANIFEST_PATH}: invalid JSON: {exc}")
        return {}, []
    validation.require(isinstance(manifest, dict), "manifest root must be an object")
    if not isinstance(manifest, dict):
        return {}, []
    validation.require(set(manifest) == TOP_KEYS, "manifest top-level fields do not match the version 1 contract")
    validation.require(manifest.get("schema_version") == 1, "unsupported manifest schema_version")
    validation.require(manifest.get("grumpydev_version") == 1, "unsupported grumpydev_version")
    validation.require(manifest.get("name") == "GrumpyDev", "manifest name must be GrumpyDev")
    validation.require(manifest.get("publisher") == "grumpydev.ai", "manifest publisher must be grumpydev.ai")
    base_url = manifest.get("base_url")
    validation.require(base_url == "https://grumpydev.ai", "base_url must be exactly https://grumpydev.ai")
    installer = manifest.get("installer")
    validation.require(isinstance(installer, dict) and set(installer) == {"path"}, "installer must contain only path")
    if isinstance(installer, dict):
        path = installer.get("path")
        validation.require(safe_relative(path), "installer path is unsafe")
        if safe_relative(path):
            validation.require((HTML / str(path)).is_file(), "installer path does not exist")
    skills = manifest.get("skills")
    validation.require(isinstance(skills, list), "manifest skills must be an array")
    return manifest, skills if isinstance(skills, list) else []


def validate_skills(skills: list[dict[str, object]], validation: Validation) -> None:
    names: set[str] = set()
    paths: set[str] = set()
    manifest_dirs: dict[Path, str] = {}
    owned_files: dict[Path, str] = {}
    seen_core: set[str] = set()

    for record in skills:
        if not isinstance(record, dict):
            validation.errors.append("manifest skill record is not an object")
            continue
        name = record.get("name")
        skill_type = record.get("type")
        path_value = record.get("path")
        expected_keys = {"name", "type", "path", "description", "display_subjects", "files"}
        if skill_type != "core":
            expected_keys.add("install_when")
            if "do_not_install_when" in record:
                expected_keys.add("do_not_install_when")
        validation.require(set(record) == expected_keys, f"{name}: unexpected manifest fields")
        validation.require(isinstance(name, str) and bool(NAME_RE.fullmatch(name)), f"{name}: unsafe skill name")
        if not isinstance(name, str):
            continue
        validation.require(name not in names, f"duplicate skill name: {name}")
        names.add(name)
        validation.require(skill_type in ALLOWED_TYPES, f"{name}: invalid skill type")
        validation.require(safe_relative(path_value), f"{name}: unsafe skill path")
        if not isinstance(path_value, str) or not safe_relative(path_value):
            continue
        validation.require(path_value not in paths, f"duplicate skill path: {path_value}")
        paths.add(path_value)
        if skill_type == "core":
            expected_path = f"skills/{name}"
        else:
            validation.require(name.startswith("gd-"), f"{name}: specialist name must begin with gd-")
            expected_path = f"skills/{skill_type}/{name.removeprefix('gd-')}"
        validation.require(path_value == expected_path, f"{name}: path does not match name and type")
        skill_dir = (HTML / path_value).resolve()
        validation.require(skill_dir.is_dir(), f"{name}: skill directory does not exist")
        manifest_dirs[skill_dir] = name
        if skill_type == "core":
            seen_core.add(name)
        else:
            install_when = record.get("install_when")
            validation.require(isinstance(install_when, list) and bool(install_when) and all(isinstance(item, str) and item for item in install_when), f"{name}: install_when must contain strings")
            exclusions = record.get("do_not_install_when")
            validation.require(exclusions is None or (isinstance(exclusions, list) and bool(exclusions) and all(isinstance(item, str) and item for item in exclusions)), f"{name}: do_not_install_when must be omitted or non-empty")
        description = record.get("description")
        validation.require(isinstance(description, str) and bool(description.strip()), f"{name}: description is empty")
        subjects = record.get("display_subjects")
        validation.require(isinstance(subjects, list) and bool(subjects), f"{name}: display_subjects is empty")
        if isinstance(subjects, list):
            for subject in subjects:
                validation.require(isinstance(subject, dict) and set(subject).issubset({"label", "url"}) and set(subject).issuperset({"label"}), f"{name}: invalid display subject fields")
                if not isinstance(subject, dict):
                    continue
                validation.require(isinstance(subject.get("label"), str) and bool(subject.get("label", "").strip()), f"{name}: empty display label")
                if "url" in subject:
                    url = subject["url"]
                    parsed = urlsplit(url) if isinstance(url, str) else None
                    validation.require(parsed is not None and parsed.scheme == "https" and bool(parsed.netloc), f"{name}: display URL must use HTTPS")
        files = record.get("files")
        validation.require(isinstance(files, list) and bool(files), f"{name}: files is empty")
        roles: list[str] = []
        local_paths: set[str] = set()
        if isinstance(files, list):
            for file in files:
                validation.require(isinstance(file, dict) and set(file) == {"path", "role"}, f"{name}: invalid file record fields")
                if not isinstance(file, dict):
                    continue
                relative = file.get("path")
                role = file.get("role")
                validation.require(safe_relative(relative), f"{name}: unsafe file path {relative}")
                validation.require(role in ROLES, f"{name}: invalid file role {role}")
                if not isinstance(relative, str) or not safe_relative(relative):
                    continue
                validation.require(relative not in local_paths, f"{name}: duplicate file path {relative}")
                local_paths.add(relative)
                actual = (skill_dir / relative).resolve()
                validation.require(actual.is_relative_to(skill_dir), f"{name}: file escapes skill directory")
                validation.require(actual.is_file(), f"{name}: listed file missing: {relative}")
                validation.require(actual not in owned_files, f"{name}: file is owned by more than one record: {relative}")
                owned_files[actual] = name
                if isinstance(role, str):
                    roles.append(role)
                expected_role = "entrypoint" if relative == "SKILL.md" else "survey" if relative == "SURVEY.md" else "reference" if relative.startswith("references/") else None
                validation.require(role == expected_role, f"{name}: role does not match path {relative}")
        validation.require(roles.count("entrypoint") == 1, f"{name}: must have one entrypoint")
        if skill_type != "core":
            validation.require(roles.count("survey") == 1, f"{name}: specialist must have one survey")
        frontmatter_name(skill_dir / "SKILL.md", name, validation)
        if skill_dir.is_dir():
            for item in skill_dir.rglob("*"):
                if item.is_file():
                    validation.require(not (item.stat().st_mode & 0o111), f"{item}: executable skill file is not allowed")

    validation.require(seen_core == CORE_NAMES, "manifest must contain exactly the three core skills")
    installer = (HTML / "skills" / "grumpydev-install" / "SKILL.md").resolve()
    frontmatter_name(installer, "grumpydev-install", validation)
    discovered_dirs = {path.parent.resolve() for path in (HTML / "skills").rglob("SKILL.md") if path.resolve() != installer}
    validation.require(discovered_dirs == set(manifest_dirs), "on-disk skill directories and manifest records differ")
    for directory in discovered_dirs:
        for path in [directory / "SKILL.md", directory / "SURVEY.md", *sorted((directory / "references").glob("*.md"))]:
            if path.exists():
                validation.require(path.resolve() in owned_files, f"{path}: on-disk skill file is missing from manifest")
        for path in directory.rglob("*.md"):
            validation.require(path.resolve() in owned_files, f"{path}: Markdown skill file is missing from manifest")
    for path in owned_files:
        text = read_utf8(path, validation)
        if text is None:
            continue
        for target in LINK_RE.findall(text):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            linked = (path.parent / parsed.path).resolve()
            skill_dir = next(directory for directory, owner in manifest_dirs.items() if owner == owned_files[path])
            core_links = {
                ("grumpydev-survey", (HTML / "skills/grumpydev/references/review-preferences.md").resolve()),
                ("grumpydev", (HTML / "skills/grumpydev-survey/references/doctrine-format.md").resolve()),
            }
            local = linked.is_relative_to(skill_dir)
            core_reference = (owned_files[path], linked) in core_links
            validation.require((local or core_reference) and linked.is_file() and linked in owned_files, f"{path}: broken, unlisted, or escaping local Markdown link {target}")


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str, str, list[str]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        rel = (values.get("rel") or "").split()
        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.links.append((tag, attribute, value, rel))


def validate_site(validation: Validation, manifest: dict[str, object], skills: list[dict[str, object]]) -> None:
    for path in HTML.rglob("*.html"):
        text = read_utf8(path, validation)
        if text is None:
            continue
        parser = SiteParser()
        parser.feed(text)
        for tag, attribute, value, rel in parser.links:
            parsed = urlsplit(value)
            external = parsed.scheme in {"http", "https"}
            runtime = (tag == "script" and attribute == "src") or (tag == "link" and "stylesheet" in rel) or (tag in {"img", "source", "audio", "video"} and attribute == "src")
            validation.require(not (external and runtime), f"{path}: external runtime asset {value}")
            if external or parsed.scheme in {"mailto", "tel", "data"} or value.startswith("#"):
                continue
            validation.require(not parsed.path.startswith("/"), f"{path}: internal link must be relative: {value}")
            target = (path.parent / parsed.path).resolve()
            if parsed.path.endswith("/") or target.is_dir():
                target = target / "index.html"
            validation.require(target.exists(), f"{path}: broken local link or asset {value}")
    for path in HTML.rglob("*.css"):
        text = read_utf8(path, validation)
        if text is None:
            continue
        validation.require(not re.search(r"@import\s+(?:url\()?['\"]?https?://", text, re.I), f"{path}: external CSS import")
        for value in re.findall(r"url\(([^)]+)\)", text, re.I):
            clean = value.strip(" \t\"'")
            parsed = urlsplit(clean)
            validation.require(parsed.scheme not in {"http", "https"}, f"{path}: external CSS asset {clean}")
            if not parsed.scheme and not clean.startswith("data:"):
                validation.require((path.parent / parsed.path).resolve().exists(), f"{path}: broken CSS asset {clean}")
    index = read_utf8(INDEX_PATH, validation)
    if index is not None and skills:
        try:
            rendered = render_skills_catalog.render(index, skills)
        except render_skills_catalog.RenderError as exc:
            validation.errors.append(f"catalog renderer failed: {exc}")
        else:
            validation.require(rendered == index, "generated skill card regions do not match the manifest")


def validate_all_text(validation: Validation) -> None:
    excluded = {".git", "scratch", "__pycache__", "node_modules"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or excluded.intersection(path.relative_to(ROOT).parts):
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in {"LICENSE"}:
            read_utf8(path, validation)


def main() -> int:
    validation = Validation()
    manifest, skills = validate_manifest(validation)
    validate_skills(skills, validation)
    validate_site(validation, manifest, skills)
    validate_all_text(validation)
    if validation.errors:
        for error in sorted(set(validation.errors)):
            print(f"ERROR: {error}")
        print(f"FAILED: {len(set(validation.errors))} structural validation error(s)")
        return 1
    print(f"OK: validated {len(skills)} installable skills and the static site")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
