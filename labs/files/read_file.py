# ------------------------------------------------------------ #
# File: read_file.py
# Date: 2026-03-29
# Author: Florentino
# Description: Read a file from the data/files directory.
# ------------------------------------------------------------ #

from __future__ import annotations

import os
from settings import FILES_PATH

def main() -> None:
    file_path = FILES_PATH / "test.txt"
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r") as file:
        content = file.read()
        print(content)
        print()

if __name__ == "__main__":
    main()