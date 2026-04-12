# ------------------------------------------------------------ #
# File: 02_write_test.py
# Date: 2026-03-29
# Author: Florentino
# Description: Write a file to the data/files directory.
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH


def main() -> None:
    # File must already exist (create manually or via another script)
    file_path = FILES_PATH / "test.txt"
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Truncate and replace whole contents
    with open(file_path, "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("This file is written by the 02_write_test.py script.\n")


if __name__ == "__main__":
    main()
