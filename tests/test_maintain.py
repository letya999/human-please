"""Release packaging behavior with synthetic temporary sources."""

import hashlib
import os
from pathlib import Path
import shutil
import tempfile
import unittest

from tools import maintain


SOURCE = Path(__file__).resolve().parents[1]


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="human-please-test-")
        self.base = Path(directory.name).resolve()
        self.assertTrue(self.base.is_relative_to(Path(tempfile.gettempdir()).resolve()))
        self.addCleanup(directory.cleanup)
        self.root = self.base / "repo"
        self.root.mkdir()
        for relative in maintain.RUNTIME_FILES:
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / relative, path)

    def test_checksum_describes_the_exact_archive_bytes(self):
        path = maintain.package(self.root)
        checksum = self.root / "dist/human-please.skill.sha256"
        self.assertTrue(checksum.is_file(), "Archive needs a SHA-256 sidecar")
        self.assertEqual(checksum.read_text(encoding="utf-8"),
                         hashlib.sha256(path.read_bytes()).hexdigest() + "  human-please.skill\n")

    def test_archive_bytes_do_not_depend_on_source_modification_times(self):
        first = hashlib.sha256(maintain.package(self.root).read_bytes()).hexdigest()
        os.utime(self.root / "human-please/references/context.md", (1700000000, 1700000000))
        second = hashlib.sha256(maintain.package(self.root).read_bytes()).hexdigest()
        self.assertEqual(first, second, "Identical source bytes must produce an identical archive")

    def test_release_rejects_source_and_output_links(self):
        for kind in ("source", "output"):
            with self.subTest(kind=kind):
                root = self.base / kind
                root.mkdir()
                for relative in maintain.RUNTIME_FILES:
                    path = root / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(SOURCE / relative, path)
                outside = self.base / (kind + "-outside")
                if kind == "source":
                    outside.write_text("outside marker", encoding="utf-8")
                    link = root / "human-please/references/context.md"
                    link.unlink()
                else:
                    outside.mkdir()
                    link = root / "dist"
                try:
                    link.symlink_to(outside, target_is_directory=(kind == "output"))
                except OSError as exc:
                    self.skipTest(f"Symlink creation unavailable: {exc}")
                with self.assertRaises(ValueError):
                    maintain.package(root)
                if kind == "output":
                    self.assertEqual(list(outside.iterdir()), [], "Rejected release must write nothing outside")

    def test_missing_source_preserves_the_previous_release(self):
        path = maintain.package(self.root)
        original = path.read_bytes()
        checksum = path.with_suffix(".skill.sha256").read_bytes()
        (self.root / "human-please/references/context.md").unlink()
        with self.assertRaises(OSError):
            maintain.package(self.root)
        self.assertEqual(path.read_bytes(), original, "A failed build must preserve the existing archive")
        self.assertEqual(path.with_suffix(".skill.sha256").read_bytes(), checksum)


if __name__ == "__main__":
    unittest.main()
