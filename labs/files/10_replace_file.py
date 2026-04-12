# ------------------------------------------------------------ #
# File: 10_replace_file.py
# Date: 2026-03-29
# Author: Florentino
# Description: Ensure folder exists, replace a file if present or create it (e.g. user avatar).
# ------------------------------------------------------------ #

from __future__ import annotations

from pathlib import Path

from settings import FILES_PATH

# Destination folder and filename (image, text, etc.).
AVATAR_DIR = FILES_PATH / "avatars"
AVATAR_FILE = AVATAR_DIR / "avatar.txt"

# New content to place at the path (in production this might be image bytes).
NEW_CONTENT = "avatar_id=user_42\nupdated=2026-03-29\nformat=png\n"


def ensure_folder(path: Path) -> None:
    # Create intermediate directories in one call
    path.mkdir(parents=True, exist_ok=True)


def write_replacing(path: Path, text: str, encoding: str = "utf-8") -> None:
    """
    If the file exists, remove it and write again.
    Ensures a true replace (useful if another process watches the path).
    """
    if path.is_file():
        # Remove old inode so watchers see a true replace
        path.unlink()
    path.write_text(text, encoding=encoding)


def main() -> None:
    ensure_folder(AVATAR_DIR)

    if AVATAR_FILE.is_file():
        print(f"File exists; replacing: {AVATAR_FILE}")
    else:
        print(f"No file yet; creating: {AVATAR_FILE}")

    write_replacing(AVATAR_FILE, NEW_CONTENT)
    print("Current contents:")
    print(AVATAR_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
