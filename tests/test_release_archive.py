"""Check the actual distributable produced before running this test suite."""

from pathlib import Path
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]


class ReleaseArchiveTests(unittest.TestCase):
    def test_distributed_archive_contains_license_and_only_runtime_files(self):
        with zipfile.ZipFile(ROOT / "dist/human-please.skill") as archive:
            expected = {
                "human-please/SKILL.md",
                "human-please/LICENSE",
                "human-please/references/context.md",
                "human-please/references/methods.md",
                "human-please/references/visuals.md",
            }
            self.assertEqual(set(archive.namelist()), expected)
            for relative in sorted(expected):
                self.assertEqual(archive.read(relative), (ROOT / relative).read_bytes(), relative)
            self.assertEqual(archive.read("human-please/LICENSE"), (ROOT / "LICENSE").read_bytes())


if __name__ == "__main__":
    unittest.main()
