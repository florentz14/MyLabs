# ------------------------------------------------------------ #
# File: read_fruits.py
# Date: 2026-03-29
# Author: Florentino
# Description: Read test2.txt (fruit list written by write_fruits.py).
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH

FRUIT_LIST_FILE = "test2.txt"


def main() -> None:
    file_path = FILES_PATH / FRUIT_LIST_FILE
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
        print()


if __name__ == "__main__":
    main()
