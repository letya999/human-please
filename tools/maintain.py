"""Build the human-please runtime archive."""

import hashlib
from pathlib import Path
import zipfile


RUNTIME_FILES = (
    "human-please/SKILL.md", "human-please/LICENSE",
    "human-please/references/context.md", "human-please/references/methods.md",
    "human-please/references/visuals.md",
)


def package(root: Path) -> Path:
    root = root.resolve()
    for relative in (*RUNTIME_FILES, "dist", "dist/human-please.skill", "dist/human-please.skill.sha256"):
        path = root / relative
        parents = (p for p in (path, *path.parents) if p.is_relative_to(root))
        if not path.resolve().is_relative_to(root) or any(p.is_symlink() for p in parents):
            raise ValueError(f"Release paths must stay inside the repository without symlinks: {relative}")
    sources = {relative: (root / relative).read_bytes() for relative in RUNTIME_FILES}
    output = root / "dist/human-please.skill"
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in RUNTIME_FILES:
            info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, sources[relative], compress_type=zipfile.ZIP_DEFLATED)
    output.with_suffix(".skill.sha256").write_text(
        f"{hashlib.sha256(output.read_bytes()).hexdigest()}  {output.name}\n", encoding="utf-8")
    return output


if __name__ == "__main__":
    print(package(Path(__file__).resolve().parents[1]))
