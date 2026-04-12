# ------------------------------------------------------------ #
# File: 05_read_student.py
# Date: 2026-03-29
# Author: Florentino
# Description: Read student.txt one line at a time.
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH

STUDENT_FILE = "student.txt"


def main() -> None:
    file_path = FILES_PATH / STUDENT_FILE
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        # Stream lines instead of read(); keeps memory low on large files
        for line_number, line in enumerate(file, start=1):
            # line still includes the trailing newline; strip for display
            print(f"{line_number:3}: {line.rstrip()}")


if __name__ == "__main__":
    main()
