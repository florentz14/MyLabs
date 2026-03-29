# ------------------------------------------------------------ #
# File: exist_folder.py
# Date: 2026-03-29
# Author: Florentino
# Description: Check whether a folder exists; if not, create it (and parents if needed).
# ------------------------------------------------------------ #

from __future__ import annotations

from pathlib import Path

from settings import FILES_PATH

# Example target (e.g. avatars, uploads, cache).
TARGET_FOLDER = FILES_PATH / "avatars"


def ensure_folder(path: Path) -> None:
    """Create the folder and any missing parents; no-op if it already exists."""
    path.mkdir(parents=True, exist_ok=True)


def main() -> None:
    if TARGET_FOLDER.is_dir():
        print(f"Folder already exists: {TARGET_FOLDER}")
    else:
        print(f"Folder missing; creating: {TARGET_FOLDER}")

    ensure_folder(TARGET_FOLDER)
    print(f"Ready: {TARGET_FOLDER.resolve()}")


if __name__ == "__main__":
    main()
