# ------------------------------------------------------------ #
# File: 18_password_secret_check.py
# Date: 2026-04-02
# Author: Florentino
# Description: Read secret from text file; compare with input (if / elif / else).
# ------------------------------------------------------------ #

"""Lab sample: compare stdin to a password stored in data/text (not for real secrets)."""

from __future__ import annotations

from pathlib import Path

from settings import FILES_PATH

SECRET_FILE = FILES_PATH / "SecretPasswordFile.txt"


def load_secret(path: Path) -> str:
    """Return the first line of the secret file, stripped of surrounding whitespace."""
    if not path.is_file():
        raise FileNotFoundError(f"Missing secret file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return f.read().strip()


def main() -> None:
    secret_password = load_secret(SECRET_FILE)
    print("Enter your password.")
    typed_password = input()

    if typed_password == secret_password:
        print("Access granted")
    elif typed_password == "12345":
        print("That password is one that an idiot puts on their luggage.")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
