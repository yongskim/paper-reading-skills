"""Verify installation safety and release portability without touching user data."""

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts" / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def test_install_six_siblings(self):
        dest = self.base / "skills"
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "install.py"), "--dest", str(dest)],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in dest.iterdir()}, set(installer.SKILLS))
        for name in installer.SKILLS:
            self.assertEqual((dest / name / "SKILL.md").read_bytes(), (ROOT / name / "SKILL.md").read_bytes())
        self.assertFalse((dest / "examples").exists())

    def test_collision_preflight_and_update(self):
        dest = self.base / "skills"
        existing = dest / installer.SKILLS[-1]
        existing.mkdir(parents=True)
        custom = existing / "custom.txt"
        custom.write_text("keep", encoding="utf-8")
        with self.assertRaises(ValueError):
            installer.install(dest)
        self.assertEqual(list(dest.iterdir()), [existing])
        installer.install(dest, update=True)
        self.assertEqual(custom.read_text(encoding="utf-8"), "keep")

    def test_dry_run_and_source_overlap(self):
        dest = self.base / "skills"
        installer.install(dest, dry_run=True)
        self.assertFalse(dest.exists())
        with self.assertRaises(ValueError):
            installer.install(ROOT / "nested")

    def test_relocated_release_and_leak_detection(self):
        moved = self.base / "relocated"
        shutil.copytree(ROOT, moved, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        self.assertEqual(validator.validate(moved), [])
        private = moved / "example.local.json"
        private.write_text("{}", encoding="utf-8")
        self.assertTrue(any("Private/generated" in e for e in validator.validate(moved)))
        private.unlink()
        with (moved / "README.md").open("a", encoding="utf-8") as handle:
            handle.write("\n[missing](missing-reference.md)\n")
        self.assertTrue(any("relative link" in e for e in validator.validate(moved)))


if __name__ == "__main__":
    unittest.main()
