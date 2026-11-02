import tempfile
import unittest
from pathlib import Path

from tools.validate_catalog import package_files, package_hash, parse_frontmatter


class CatalogValidatorTests(unittest.TestCase):
    def test_package_hash_includes_reference_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "SKILL.md").write_text(
                "---\n"
                "name: example-skill\n"
                "description: Example\n"
                "license: MIT\n"
                "compatibility: any\n"
                "metadata:\n"
                "  version: \"1.0.0\"\n"
                "---\n"
                "# Example\n",
                encoding="utf-8",
            )
            references = folder / "references"
            references.mkdir()
            reference = references / "table.md"
            reference.write_text("original\n", encoding="utf-8")

            original_hash = package_hash(folder, package_files(folder))
            reference.write_text("changed\n", encoding="utf-8")

            self.assertNotEqual(
                original_hash,
                package_hash(folder, package_files(folder)),
            )

    def test_frontmatter_extracts_required_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            skill_file = Path(temp_dir) / "SKILL.md"
            skill_file.write_text(
                "---\n"
                "name: example-skill\n"
                "description: Example skill\n"
                "license: MIT\n"
                "compatibility: any\n"
                "metadata:\n"
                "  version: \"1.2.3\"\n"
                "---\n"
                "content\n",
                encoding="utf-8",
            )

            self.assertEqual(
                parse_frontmatter(skill_file),
                {
                    "name": "example-skill",
                    "description": "Example skill",
                    "license": "MIT",
                    "version": "1.2.3",
                },
            )

    def test_package_hash_normalizes_text_line_endings(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            skill_file = folder / "SKILL.md"
            skill_file.write_bytes(b"line one\r\nline two\r\n")

            first_hash = package_hash(folder, package_files(folder))
            skill_file.write_bytes(b"line one\nline two\n")

            self.assertEqual(
                first_hash,
                package_hash(folder, package_files(folder)),
            )


if __name__ == "__main__":
    unittest.main()
