#!/usr/bin/env python3
"""Report deterministic GrumpyDev instruction word counts by loading mode."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "html"
SKILLS = HTML / "skills"
MANIFEST = HTML / "manifest.json"
DOCTRINE_FIXTURES = ROOT / "tests" / "skills" / "core" / "data"

BASELINE = {
    "selectable_words": 82852,
    "specialist_median": 507,
    "specialist_p90": 851,
    "core_review_words": 4116,
    "survey_words": 3042,
}

SCENARIOS = {
    "MERN": {
        "skills": [
            "javascript",
            "typescript",
            "nodejs",
            "react",
            "express",
            "mongodb",
            "application-security",
            "dependency-supply-chain",
        ],
        "focused": {
            "nodejs": ["async-context-streams-and-backpressure.md"],
            "react": ["untrusted-content-and-browser-security.md"],
            "application-security": ["injection-output-and-untrusted-input.md"],
        },
    },
    "MEAN": {
        "skills": [
            "javascript",
            "typescript",
            "nodejs",
            "angular",
            "express",
            "mongodb",
            "application-security",
            "dependency-supply-chain",
        ],
        "focused": {
            "nodejs": ["modules-packages-and-native-addons.md"],
            "application-security": ["identity-sessions-and-authorization.md"],
        },
    },
    "LAMP": {
        "skills": [
            "php",
            "apache-http-server",
            "mysql",
            "linux",
            "application-security",
        ],
        "focused": {
            "php": ["request-and-process-lifecycle.md"],
            "apache-http-server": ["routing-proxy-and-php-integration.md"],
            "linux": ["services-processes-and-resource-limits.md"],
            "application-security": ["identity-sessions-and-authorization.md"],
        },
    },
    "LNMP": {
        "skills": [
            "php",
            "nginx",
            "mysql",
            "linux",
            "application-security",
        ],
        "focused": {
            "php": ["request-and-process-lifecycle.md"],
            "nginx": ["routing-static-files-and-fastcgi.md"],
            "linux": ["services-processes-and-resource-limits.md"],
            "application-security": ["identity-sessions-and-authorization.md"],
        },
    },
    "Windows desktop": {
        "skills": ["csharp", "windows", "wpf", "application-security"],
        "focused": {
            "windows": ["packaging-signing-updates-and-recovery.md"],
            "wpf": ["native-interop-packaging-and-updates.md"],
            "application-security": ["identity-sessions-and-authorization.md"],
        },
    },
    "Containerized service": {
        "skills": [
            "typescript",
            "nodejs",
            "containers",
            "linux",
            "rest-api-design",
            "application-security",
            "observability",
        ],
        "focused": {
            "nodejs": ["signals-shutdown-and-deployment.md"],
            "linux": ["services-processes-and-resource-limits.md"],
            "rest-api-design": ["versioning-upstreams-and-evolution.md"],
            "application-security": ["identity-sessions-and-authorization.md"],
        },
    },
    "Kubernetes service": {
        "skills": [
            "typescript",
            "nodejs",
            "containers",
            "kubernetes",
            "rest-api-design",
            "application-security",
            "observability",
        ],
        "focused": {
            "nodejs": ["signals-shutdown-and-deployment.md"],
            "kubernetes": [
                "health-lifecycle-and-rollouts.md",
                "resources-placement-and-scaling.md",
                "networking-identity-and-secrets.md",
            ],
            "rest-api-design": ["authorization-input-and-abuse.md"],
            "application-security": ["identity-sessions-and-authorization.md"],
        },
    },
    "Agentic application": {
        "skills": [
            "python",
            "agentic-systems",
            "llm-applications",
            "model-context-protocol",
            "application-security",
            "observability",
        ],
        "focused": {
            "python": ["async-processes-and-shutdown.md"],
            "agentic-systems": [
                "tool-authority-sandboxing-and-code-execution.md",
                "delegation-inter-agent-trust-and-containment.md",
            ],
            "llm-applications": [
                "retrieval-data-and-poisoning.md",
                "tools-output-and-authority.md",
            ],
            "model-context-protocol": [
                "http-authorization-and-discovery.md",
                "sessions-tool-identity-and-revocation.md",
            ],
            "application-security": [
                "identity-sessions-and-authorization.md",
                "injection-output-and-untrusted-input.md",
            ],
        },
    },
}
SCENARIO_REVIEW_BASELINE = {
    "MERN": 9600,
    "MEAN": 9290,
    "LAMP": 8686,
    "LNMP": 8686,
    "Windows desktop": 7286,
    "Containerized service": 9262,
    "Kubernetes service": 9790,
    "Agentic application": 8696,
}

BOUNDARY_SCENARIOS = {
    "PostgreSQL query and index": ("postgresql", ["queries-and-indexes.md"]),
    "PostgreSQL schema migration": ("postgresql", ["schema-migrations-and-locking.md"]),
    "PostgreSQL concurrency": ("postgresql", ["transactions-and-concurrency.md"]),
    "PostgreSQL recovery": ("postgresql", ["operations-replication-and-recovery.md"]),
    "PHP types": ("php", ["types-and-boundary-data.md"]),
    "PHP request lifecycle": ("php", ["request-and-process-lifecycle.md"]),
    "PHP untrusted upload": ("php", ["security-and-external-input.md"]),
    "PHP rolling deployment": ("php", ["dependencies-and-deployment.md"]),
    "Kubernetes rollout": ("kubernetes", ["health-lifecycle-and-rollouts.md"]),
    "Kubernetes autoscaling": ("kubernetes", ["resources-placement-and-scaling.md"]),
    "Kubernetes identity": ("kubernetes", ["networking-identity-and-secrets.md"]),
    "Kubernetes stateful recovery": ("kubernetes", ["stateful-work-and-recovery.md"]),
    "Laravel HTTP": ("laravel", ["http-validation-and-authorization.md"]),
    "Laravel migration": ("laravel", ["eloquent-transactions-and-migrations.md"]),
    "Laravel queued job": ("laravel", ["queues-events-and-workers.md"]),
    "Laravel cached release": ("laravel", ["caching-configuration-and-deployment.md"]),
    "React client only": ("react", []),
    "React server-rendered hostile content": (
        "react",
        ["server-rendering-and-hydration.md", "untrusted-content-and-browser-security.md"],
    ),
    "Next.js rendering cache": ("nextjs", ["rendering-caching-and-hydration.md"]),
    "Next.js server action": ("nextjs", ["server-actions-routes-and-security.md"]),
    "Node.js module": ("nodejs", ["modules-packages-and-native-addons.md"]),
    "Node.js stream": ("nodejs", ["async-context-streams-and-backpressure.md"]),
    "Node.js worker": ("nodejs", ["filesystem-child-processes-and-workers.md"]),
    "Node.js shutdown": ("nodejs", ["signals-shutdown-and-deployment.md"]),
    "MCP stdio": ("model-context-protocol", ["stdio-process-lifecycle.md"]),
    "MCP authenticated HTTP": (
        "model-context-protocol",
        ["http-authorization-and-discovery.md", "sessions-tool-identity-and-revocation.md"],
    ),
    "LLM without retrieval or tools": ("llm-applications", []),
    "LLM retrieval": ("llm-applications", ["retrieval-data-and-poisoning.md"]),
    "LLM tool effects": ("llm-applications", ["tools-output-and-authority.md"]),
    "Single agent": ("agentic-systems", ["tool-authority-sandboxing-and-code-execution.md"]),
    "Delegated agents": (
        "agentic-systems",
        ["delegation-inter-agent-trust-and-containment.md"],
    ),
    "Linux library only": ("linux", []),
    "Linux service package": (
        "linux",
        ["services-processes-and-resource-limits.md", "packaging-updates-and-recovery.md"],
    ),
    "Windows filesystem only": ("windows", []),
    "Windows service installer": (
        "windows",
        ["services-com-and-process-identity.md", "packaging-signing-updates-and-recovery.md"],
    ),
    "macOS lifecycle only": ("macos", []),
    "macOS sandboxed signed update": (
        "macos",
        ["sandbox-privacy-and-keychain.md", "signing-notarization-updates-and-recovery.md"],
    ),
    "MariaDB query": ("mariadb", ["schema-locking-and-query-plans.md"]),
    "MariaDB Galera recovery": ("mariadb", ["replication-galera-and-recovery.md"]),
}


def words(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def package_dir(entry: dict[str, object]) -> Path:
    name = str(entry["name"])
    if entry["type"] == "core":
        return SKILLS / name
    return SKILLS / str(entry["type"]) / name


def paths_for(entry: dict[str, object], roles: set[str]) -> list[Path]:
    directory = package_dir(entry)
    return [
        directory / str(item["path"])
        for item in entry["files"]
        if item["role"] in roles
    ]


def reference_path(entry: dict[str, object], filename: str) -> Path:
    target = f"references/{filename}"
    matches = [
        package_dir(entry) / str(item["path"])
        for item in entry["files"]
        if item["role"] == "reference" and item["path"] == target
    ]
    if len(matches) != 1:
        raise ValueError(f"{entry['name']} does not contain exactly one {target}")
    return matches[0]


def percentile_90(values: list[int]) -> int:
    ordered = sorted(values)
    return ordered[max(0, int(len(ordered) * 0.9) - 1)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report deterministic GrumpyDev context word counts."
    )
    parser.add_argument(
        "--doctrine",
        choices=("compact", "detailed", "none"),
        default="compact",
        help="Doctrine fixture to include in the external-input breakdown.",
    )
    parser.add_argument("--plan-words", type=int, default=0)
    parser.add_argument("--project-document-words", type=int, default=0)
    args = parser.parse_args()
    if args.plan_words < 0 or args.project_document_words < 0:
        parser.error("external context word counts cannot be negative")
    return args


manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
entries = {entry["name"]: entry for entry in manifest["skills"]}
args = parse_args()

doctrine_words = 0
if args.doctrine != "none":
    doctrine_words = words(DOCTRINE_FIXTURES / f"doctrine-{args.doctrine}.md")

entrypoint_counts = {
    name: sum(words(path) for path in paths_for(entry, {"entrypoint"}))
    for name, entry in entries.items()
}
specialist_counts = [
    entrypoint_counts[name]
    for name, entry in entries.items()
    if entry["type"] != "core"
]

print("Selectable entrypoints")
print(f"  words: {sum(entrypoint_counts.values())} (baseline {BASELINE['selectable_words']})")
print(f"  core review: {entrypoint_counts['grumpydev']} (baseline {BASELINE['core_review_words']})")
print(f"  survey: {entrypoint_counts['grumpydev-survey']} (baseline {BASELINE['survey_words']})")
print(f"  specialist median: {int(median(specialist_counts))} (baseline {BASELINE['specialist_median']})")
print(f"  specialist p90: {percentile_90(specialist_counts)} (baseline {BASELINE['specialist_p90']})")

print("\nRepresentative installed-package loading")
survey_core_words = sum(
    words(path)
    for path in paths_for(entries["grumpydev-survey"], {"entrypoint", "reference"})
)
for scenario, definition in SCENARIOS.items():
    names = definition["skills"]
    focused = definition["focused"]
    selected = [entries["grumpydev"], *(entries[name] for name in names)]
    lean_paths = [path for entry in selected for path in paths_for(entry, {"entrypoint"})]
    common_paths = [reference_path(entries["grumpydev"], "standard-review.md")]
    common_paths.extend(reference_path(entries[name], "review.md") for name in names)
    focused_paths = [
        reference_path(entries[name], filename)
        for name, filenames in focused.items()
        for filename in filenames
    ]
    all_focused_paths = [
        path
        for name in names
        for path in paths_for(entries[name], {"reference"})
        if path.name != "review.md"
    ]
    standard_paths = [*lean_paths, *common_paths, *focused_paths]
    one_reference_equivalent_paths = [
        *lean_paths,
        *common_paths,
        *all_focused_paths,
    ]
    deep_paths = [
        *standard_paths,
        reference_path(entries["grumpydev"], "deep-review.md"),
    ]
    survey_selected = [entries["grumpydev-survey"], *(entries[name] for name in names)]
    survey_paths = [
        path
        for entry in survey_selected
        for path in paths_for(entry, {"entrypoint", "survey", "reference"})
        if entry["name"] == "grumpydev-survey" or path.name == "SURVEY.md"
    ]
    survey_count = sum(map(words, survey_paths))
    baseline_survey = survey_count - survey_core_words + BASELINE["survey_words"]
    print(
        f"  {scenario}: review baseline={SCENARIO_REVIEW_BASELINE[scenario]} "
        f"one_ref_equivalent={sum(map(words, one_reference_equivalent_paths))} "
        f"lean={sum(map(words, lean_paths))} "
        f"standard={sum(map(words, standard_paths))} "
        f"deep={sum(map(words, deep_paths))}"
    )
    print(
        f"    entrypoints={sum(map(words, lean_paths))} "
        f"common_refs={sum(map(words, common_paths))} "
        f"focused_refs={sum(map(words, focused_paths))} "
        f"doctrine={doctrine_words} plan={args.plan_words} "
        f"project_docs={args.project_document_words}"
    )
    print(
        f"    initial survey baseline={baseline_survey} current={survey_count}"
    )

print("\nBoundary-specific specialist loading")
for scenario, (name, filenames) in BOUNDARY_SCENARIOS.items():
    entrypoint = paths_for(entries[name], {"entrypoint"})
    common = [reference_path(entries[name], "review.md")]
    focused = [reference_path(entries[name], filename) for filename in filenames]
    print(
        f"  {scenario}: entrypoint={sum(map(words, entrypoint))} "
        f"common={sum(map(words, common))} focused={sum(map(words, focused))} "
        f"standard={sum(map(words, [*entrypoint, *common, *focused]))}"
    )

print("\nLargest entrypoints")
for name, count in sorted(entrypoint_counts.items(), key=lambda item: item[1], reverse=True)[:15]:
    print(f"  {count:5d} {name}")

detailed_doctrine = words(DOCTRINE_FIXTURES / "doctrine-detailed.md")
compact_doctrine = words(DOCTRINE_FIXTURES / "doctrine-compact.md")
reduction = 100 * (detailed_doctrine - compact_doctrine) / detailed_doctrine
print("\nDoctrine format fixture")
print(
    f"  detailed={detailed_doctrine} compact={compact_doctrine} "
    f"reduction={reduction:.1f}%"
)
