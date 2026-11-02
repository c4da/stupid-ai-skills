#!/usr/bin/env python3
"""Validate and compile the SkillsMarket catalog.

The catalog records reproducible SHA-256 digests for every file in a skill
package except its generated manifest. The digest covers the prompt and all
reference material, so changing a referenced file invalidates the package
provenance as well.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / "skills"
REGISTRY_FILE = ROOT_DIR / "registry.json"
ROOT_SKILL_FILE = ROOT_DIR / "SKILL.md"
EXPECTED_REPOSITORY = "https://github.com/c4da/stupid-ai-skills"
EXPECTED_MARKETPLACE = "aiskillsmarket"
CATALOG_VERSION = "1.1.0"
TEXT_SUFFIXES = {".csv", ".json", ".md", ".toml", ".txt", ".yaml", ".yml"}
DISCOVERY_TAGS = [
    "ai-skills",
    "agent-skills",
    "skill-md",
    "coding-persona",
    "debugging-game",
    "prompt-based",
    "open-source",
]
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def json_dump(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_file_bytes(path: Path) -> bytes:
    """Return stable bytes for hashing text files across operating systems."""
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_SUFFIXES:
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def package_files(folder: Path) -> list[Path]:
    """Return stable package contents, excluding the generated manifest."""
    return sorted(
        (
            path
            for path in folder.rglob("*")
            if path.is_file()
            and path.name != "manifest.json"
            and "__pycache__" not in path.parts
        ),
        key=lambda path: path.relative_to(folder).as_posix(),
    )


def package_hash(folder: Path, files: list[Path]) -> str:
    """Hash relative names and bytes so file renames are also detectable."""
    digest = hashlib.sha256()
    for path in files:
        relative = path.relative_to(folder).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(canonical_file_bytes(path))
        digest.update(b"\0")
    return digest.hexdigest()


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")

    try:
        end = next(
            index for index, line in enumerate(lines[1:], 1) if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    frontmatter = lines[1:end]

    def find_scalar(key: str) -> str | None:
        prefix = f"{key}:"
        for line in frontmatter:
            if line.startswith(prefix):
                return unquote(line[len(prefix) :].strip())
        return None

    version = None
    for line in frontmatter:
        match = re.match(r"^\s+version:\s*(.+?)\s*$", line)
        if match:
            version = unquote(match.group(1))
            break

    required_sections = {
        "compatibility": any(line.startswith("compatibility:") for line in frontmatter),
        "metadata": any(line.startswith("metadata:") for line in frontmatter),
    }
    missing_sections = [
        name for name, present in required_sections.items() if not present
    ]
    if missing_sections:
        raise ValueError(f"missing frontmatter section(s): {', '.join(missing_sections)}")

    values = {
        "name": find_scalar("name"),
        "description": find_scalar("description"),
        "license": find_scalar("license"),
        "version": version,
    }
    missing_values = [name for name, value in values.items() if not value]
    if missing_values:
        raise ValueError(f"missing frontmatter value(s): {', '.join(missing_values)}")
    return {name: value for name, value in values.items() if value is not None}


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("JSON root must be an object")
    return value


def validate_manifest(
    folder: Path,
    manifest: dict[str, Any],
    frontmatter: dict[str, str],
    expected_provenance: dict[str, Any],
    check_provenance: bool,
) -> list[str]:
    errors: list[str] = []
    required = (
        "name",
        "version",
        "description",
        "author",
        "license",
        "repository",
        "marketplace",
        "compatibility",
    )
    for key in required:
        if key not in manifest:
            errors.append(f"{folder.name}: manifest missing {key!r}")

    name = manifest.get("name")
    version = manifest.get("version")
    marketplace = manifest.get("marketplace")
    compatibility = manifest.get("compatibility")

    if name != folder.name or not isinstance(name, str) or not SLUG_RE.fullmatch(name):
        errors.append(
            f"{folder.name}: manifest name must be a lowercase slug matching its folder"
        )
    if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
        errors.append(f"{folder.name}: manifest version must be semantic version text")
    if manifest.get("repository") != EXPECTED_REPOSITORY:
        errors.append(f"{folder.name}: repository must be {EXPECTED_REPOSITORY}")
    if manifest.get("license") != "MIT":
        errors.append(f"{folder.name}: license must remain MIT for this catalog")

    if not isinstance(marketplace, dict):
        errors.append(f"{folder.name}: marketplace must be an object")
    else:
        if marketplace.get("platform") != EXPECTED_MARKETPLACE:
            errors.append(
                f"{folder.name}: marketplace.platform must be {EXPECTED_MARKETPLACE}"
            )
        if marketplace.get("tier") not in {"free", "paid", "freemium"}:
            errors.append(
                f"{folder.name}: marketplace.tier must be free, paid, or freemium"
            )
        categories = marketplace.get("categories")
        if not isinstance(categories, list) or not categories:
            errors.append(
                f"{folder.name}: marketplace.categories must be a non-empty list"
            )
        tags = marketplace.get("tags")
        if (
            not isinstance(tags, list)
            or not tags
            or any(not isinstance(tag, str) or not tag for tag in tags)
        ):
            errors.append(
                f"{folder.name}: marketplace.tags must be a non-empty list of strings"
            )

    if not isinstance(compatibility, dict):
        errors.append(f"{folder.name}: compatibility must be an object")
    else:
        for key in ("agents", "interfaces"):
            if not isinstance(compatibility.get(key), list) or not compatibility[key]:
                errors.append(
                    f"{folder.name}: compatibility.{key} must be a non-empty list"
                )
        for key in ("tools", "writes_files", "network"):
            if compatibility.get(key) is not False:
                errors.append(f"{folder.name}: compatibility.{key} must be false")

    if frontmatter.get("name") != name:
        errors.append(f"{folder.name}: SKILL.md name does not match manifest")
    if frontmatter.get("description") != manifest.get("description"):
        errors.append(f"{folder.name}: SKILL.md description does not match manifest")
    if frontmatter.get("version") != version:
        errors.append(f"{folder.name}: SKILL.md version does not match manifest")
    if frontmatter.get("license") != manifest.get("license"):
        errors.append(f"{folder.name}: SKILL.md license does not match manifest")

    provenance = manifest.get("provenance")
    if check_provenance and provenance != expected_provenance:
        errors.append(
            f"{folder.name}: provenance is stale or incomplete; run the catalog validator"
        )

    return errors


def build_catalog(
    check_provenance: bool,
) -> tuple[dict[str, Any], dict[Path, dict[str, Any]], list[str]]:
    errors: list[str] = []
    manifests: dict[Path, dict[str, Any]] = {}
    entries: list[dict[str, Any]] = []
    seen_names: set[str] = set()

    if not SKILLS_DIR.exists():
        return {}, {}, [f"skills directory not found: {SKILLS_DIR}"]

    for folder in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_file = folder / "SKILL.md"
        manifest_file = folder / "manifest.json"
        if not skill_file.exists():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        if not manifest_file.exists():
            errors.append(f"{folder.name}: missing manifest.json")
            continue

        try:
            manifest = load_json(manifest_file)
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{folder.name}: {exc}")
            continue

        files = package_files(folder)
        if not files:
            errors.append(f"{folder.name}: package has no content files")
            continue
        relative_files = [path.relative_to(folder).as_posix() for path in files]
        skill_hash = sha256_bytes(canonical_file_bytes(skill_file))
        digest = package_hash(folder, files)
        expected_provenance = {
            "hash_algorithm": "SHA-256",
            "files": relative_files,
            "skill_file": "SKILL.md",
            "skill_file_sha256": skill_hash,
            "package_sha256": digest,
        }

        errors.extend(
            validate_manifest(
                folder,
                manifest,
                frontmatter,
                expected_provenance,
                check_provenance,
            )
        )
        name = manifest.get("name")
        if isinstance(name, str):
            if name in seen_names:
                errors.append(f"duplicate skill name: {name}")
            seen_names.add(name)

        manifests[folder] = {
            "manifest": manifest,
            "expected_provenance": expected_provenance,
        }
        marketplace_data = manifest.get("marketplace")
        if not isinstance(marketplace_data, dict):
            marketplace_data = {}
        entries.append(
            {
                "name": manifest.get("name", folder.name),
                "version": manifest.get("version", "0.0.0"),
                "description": manifest.get("description", ""),
                "author": manifest.get("author", ""),
                "license": manifest.get("license", ""),
                "repository": manifest.get("repository", ""),
                "tier": marketplace_data.get("tier", "free"),
                "categories": marketplace_data.get("categories", []),
                "tags": marketplace_data.get("tags", []),
                "compatibility": manifest.get("compatibility", {}),
                "sha256": digest,
                "skill_md_sha256": skill_hash,
                "files": relative_files,
                "path": f"skills/{folder.name}",
            }
        )

    catalog = {
        "catalog_version": CATALOG_VERSION,
        "entrypoint": "SKILL.md",
        "platform": EXPECTED_MARKETPLACE,
        "discovery_tags": DISCOVERY_TAGS,
        "description": "Unofficial prompt-only coding personas and interactive debugging games for AI agents.",
        "repository": EXPECTED_REPOSITORY,
        "skills_count": len(entries),
        "skills": entries,
    }
    return catalog, manifests, errors


def write_catalog(
    catalog: dict[str, Any],
    manifests: dict[Path, dict[str, Any]],
) -> None:
    for folder, data in manifests.items():
        manifest = copy.deepcopy(data["manifest"])
        manifest["provenance"] = data["expected_provenance"]
        (folder / "manifest.json").write_text(json_dump(manifest), encoding="utf-8")
    REGISTRY_FILE.write_text(json_dump(catalog), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate without writing manifests or registry.json",
    )
    args = parser.parse_args()

    if not ROOT_SKILL_FILE.exists():
        print("[-] Missing repository SKILL.md file")
        return 1
    try:
        root_frontmatter = parse_frontmatter(ROOT_SKILL_FILE)
    except ValueError as exc:
        print(f"[-] repository SKILL.md: {exc}")
        return 1
    if root_frontmatter.get("name") != "stupid-ai-skills":
        print("[-] repository SKILL.md: name must be stupid-ai-skills")
        return 1
    if not (ROOT_DIR / "LICENSE").exists():
        print("[-] Missing repository LICENSE file")
        return 1
    if not (ROOT_DIR / "NOTICE.md").exists():
        print("[-] Missing repository NOTICE.md file")
        return 1

    catalog, manifests, errors = build_catalog(args.check)
    if errors:
        for error in errors:
            print(f"[-] {error}")
        return 1

    if args.check:
        try:
            existing_registry = load_json(REGISTRY_FILE)
        except ValueError as exc:
            print(f"[-] registry.json: {exc}")
            return 1
        if existing_registry != catalog:
            print("[-] registry.json is stale; run `python tools/validate_catalog.py`")
            return 1
        print(
            f"[+] Catalog is valid: {catalog['skills_count']} package(s), no files changed"
        )
        return 0

    write_catalog(catalog, manifests)
    print(f"[+] Catalog compiled: {REGISTRY_FILE}")
    print(
        f"[+] Validated {catalog['skills_count']} package(s) with complete package hashes"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
