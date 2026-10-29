"""Install the six sibling skills without copying local configuration."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "paper-reading", "paper-reading-skim", "paper-reading-deep",
    "paper-reading-lineage", "paper-reading-synthesis", "paper-reading-archive",
)


def install(destination: Path, *, update: bool = False, dry_run: bool = False) -> None:
    destination = destination.expanduser().resolve()
    if destination == ROOT or destination.is_relative_to(ROOT) or ROOT.is_relative_to(destination):
        raise ValueError("Destination must be outside the source repository and its parents.")
    for name in SKILLS:
        if not (ROOT / name / "SKILL.md").is_file():
            raise ValueError(f"Source skill missing: {name}")
        target = destination / name
        if target.is_symlink() or (target.exists() and not target.is_dir()):
            raise ValueError(f"Destination is not a regular directory: {target}")
        if target.exists() and not update:
            raise ValueError(f"Skill already exists: {target}. Review it, then use --update if intended.")
    for name in SKILLS:
        target = destination / name
        print(f"{'Would install' if dry_run else 'Installing'} {name} -> {target}")
        if not dry_run:
            shutil.copytree(
                ROOT / name, target, dirs_exist_ok=update,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )


def main() -> int:
    codex_dir = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=codex_dir / "skills")
    parser.add_argument("--update", action="store_true", help="Merge into existing skill folders; preserve extra files.")
    parser.add_argument("--dry-run", action="store_true", help="Show the installation plan without writing files.")
    args = parser.parse_args()
    try:
        install(args.dest, update=args.update, dry_run=args.dry_run)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Installation stopped: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
