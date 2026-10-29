"""Check release structure, relative links and common private-data leaks (stdlib only)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote

SKILLS = (
    "paper-reading", "paper-reading-skim", "paper-reading-deep",
    "paper-reading-lineage", "paper-reading-synthesis", "paper-reading-archive",
)
SKIP = {".git", "__pycache__", ".venv", "node_modules"}
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
PRIVATE = (
    ("personal home path", re.compile(r"(?:[A-Za-z]:[/\\][U]sers[/\\]|/[U]sers/|/[h]ome/)[^\s/\\]+", re.I)),
    ("real SiYuan block ID", re.compile(r"\b20\d{12}-[a-z0-9]{7}\b")),
    ("fixed local endpoint", re.compile(r"https?://(?:127\.0\.0\.1|localhost):\d+", re.I)),
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for name in SKILLS:
        manifest = root / name / "SKILL.md"
        if not manifest.is_file():
            errors.append(f"Missing skill: {name}")
            continue
        source = manifest.read_text(encoding="utf-8")
        header = source.split("---", 2)
        if len(header) < 3 or header[0].strip():
            errors.append(f"{name}: missing frontmatter")
        elif not re.search(rf"^name: {re.escape(name)}\s*$", header[1], re.M) or not re.search(r"^description:\s*\S", header[1], re.M):
            errors.append(f"{name}: invalid name/description")
        if not (root / name / "agents" / "openai.yaml").is_file():
            errors.append(f"{name}: missing UI metadata")
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in SKIP for part in rel.parts):
            continue
        if path.is_symlink():
            errors.append(f"Symlink in release: {rel}")
            continue
        if not path.is_file():
            continue
        if (path.name.endswith((".local.json", ".private.json"))
                or path.suffix.lower() in {".pdf", ".sy", ".db", ".sqlite", ".sqlite3", ".log"}
                or path.name == ".env" or path.name.startswith(".env.")
                or rel.parts[0] in {"work", "outputs", ".paper-reading"}):
            errors.append(f"Private/generated file: {rel}")
        try:
            source = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"Unexpected binary/non-UTF-8 file: {rel}")
            continue
        for label, pattern in PRIVATE:
            if pattern.search(source):
                errors.append(f"{rel}: {label}")
        if path.suffix == ".json":
            try:
                json.loads(source)
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON ({exc})")
        if path.suffix != ".md":
            continue
        for raw in LINK.findall(source):
            target = raw.strip().strip("<>")
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f"{rel}: broken/outside relative link: {raw}")
    config = root / "examples" / "siyuan.config.example.json"
    if config.is_file():
        try:
            data = json.loads(config.read_text(encoding="utf-8"))
            if any(data.get(key) is not None for key in ("base_url_hint", "notebook_id", "root_doc_id")) or data.get("domains") != {}:
                errors.append("Example configuration must have empty connection IDs and domains")
        except json.JSONDecodeError:
            pass  # Already reported above.
    else:
        errors.append("Missing blank configuration example")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate(parser.parse_args().root)
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Validation {'failed' if errors else 'passed'}: {len(errors)} error(s).")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
