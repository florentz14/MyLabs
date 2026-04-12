"""List files under project ``data/`` with size and extension counts."""

from __future__ import annotations

from collections import Counter

from settings import DATA_PATH


def main() -> None:
    files: list[tuple[str, str, int]] = []
    for path in sorted(DATA_PATH.rglob("*")):
        if path.is_file():
            rel = path.relative_to(DATA_PATH)
            files.append((str(rel), path.suffix.lower() or "(no ext)", path.stat().st_size))

    print("=" * 60)
    print(f"DATA inventory: {DATA_PATH}")
    print("=" * 60)
    print(f"{'Path':<48} {'Ext':<10} {'Bytes':>10}")
    print("-" * 60)
    for rel, ext, size in files:
        print(f"{rel:<48} {ext:<10} {size:>10,}")

    by_ext = Counter(ext for _, ext, _ in files)
    print("-" * 60)
    print("By extension:")
    for ext, n in sorted(by_ext.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {ext or '(none)'}: {n}")


if __name__ == "__main__":
    main()
