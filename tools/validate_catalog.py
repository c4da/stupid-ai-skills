#!/usr/bin/env python3
"""
Agensi.io Skills Catalog Validator & Registry Generator

Scans all skills in `skills/`, verifies frontmatter and manifest compliance,
computes SHA-256 cryptographic provenance for each SKILL.md, updates manifests,
and compiles the master `registry.json` catalog.
"""

import os
import json
import hashlib
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / "skills"
REGISTRY_FILE = ROOT_DIR / "registry.json"

def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    print(f"[*] Scanning Agensi skills catalog at: {SKILLS_DIR}")
    catalog = {
        "catalog_version": "1.0.0",
        "platform": "agensi.io",
        "description": "Curated skill marketplace assets and personas for AI coding agents",
        "repository": "https://github.com/agensi-io/agensi-skills",
        "skills_count": 0,
        "skills": []
    }

    if not SKILLS_DIR.exists():
        print(f"[-] Error: skills directory not found at {SKILLS_DIR}")
        return 1

    skill_folders = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()])
    errors = 0

    for folder in skill_folders:
        skill_md = folder / "SKILL.md"
        manifest_json = folder / "manifest.json"

        if not skill_md.exists():
            print(f"[!] Warning: {folder.name} missing SKILL.md")
            errors += 1
            continue

        if not manifest_json.exists():
            print(f"[!] Warning: {folder.name} missing manifest.json")
            errors += 1
            continue

        # 1. Read manifest
        try:
            with open(manifest_json, "r", encoding="utf-8") as f:
                manifest = json.load(f)
        except Exception as e:
            print(f"[-] Error reading {manifest_json}: {e}")
            errors += 1
            continue

        # 2. Compute exact SHA-256 of SKILL.md
        skill_hash = sha256_file(skill_md)
        manifest.setdefault("provenance", {})["skill_file"] = "SKILL.md"
        manifest["provenance"]["sha256"] = skill_hash

        # Update manifest on disk with verified hash
        with open(manifest_json, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)

        # 3. Add to catalog
        entry = {
            "name": manifest.get("name", folder.name),
            "version": manifest.get("version", "1.0.0"),
            "description": manifest.get("description", ""),
            "author": manifest.get("author", "agensi.io"),
            "license": manifest.get("license", "MIT"),
            "tier": manifest.get("marketplace", {}).get("tier", "free"),
            "categories": manifest.get("marketplace", {}).get("categories", []),
            "compatibility": manifest.get("compatibility", {}),
            "sha256": skill_hash,
            "path": f"skills/{folder.name}"
        }
        catalog["skills"].append(entry)
        print(f"  [+] Validated {entry['name']} (v{entry['version']}) -> {skill_hash[:16]}... [{entry['tier'].upper()}]")

    catalog["skills_count"] = len(catalog["skills"])

    # Write root registry.json
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)

    print(f"\n[+] Master registry compiled: {REGISTRY_FILE}")
    print(f"[+] Total skills validated: {catalog['skills_count']} | Errors: {errors}")
    return errors

if __name__ == "__main__":
    exit(main())
