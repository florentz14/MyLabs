# ------------------------------------------------------------ #
# File: write_fruits.py
# Date: 2026-03-29
# Author: Florentino
# Description: Write a list of lines to a file using writelines().
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH


def main() -> None:
    # Plain list; read_fruits.py reads this file back
    file_path = FILES_PATH / "test2.txt"
    # Items have no trailing newlines yet
    line_list = [
        "apple",
        "banana",
        "orange",
        "grape",
        "mango",
    ]
    # writelines() does not add newlines; append "\n" to each string.
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(line + "\n" for line in line_list)
    print(f"Wrote {file_path}")

if __name__ == "__main__":
    main()
