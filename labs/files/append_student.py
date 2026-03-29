# ------------------------------------------------------------ #
# File: append_student.py
# Date: 2026-03-29
# Author: Florentino
# Description: Append several student rows to student.txt with one file.write() per line ("a" mode).
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH

STUDENT_FILE = "student.txt"

NEW_RECORD_LINE = "8,Henry Adams,henry.adams@example.com,2025,Python Lab\n"
NEW_RECORD_LINE_2 = "9,Ivy Chen,ivy.chen@example.com,2025,Data Structures\n"
NEW_RECORD_LINE_3 = "10,Jack Ortiz,jack.ortiz@example.com,2024,Algorithms\n"


def main() -> None:
    file_path = FILES_PATH / STUDENT_FILE
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Append after existing content; cursor starts at end of file
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(NEW_RECORD_LINE)
        file.write(NEW_RECORD_LINE_2)
        file.write(NEW_RECORD_LINE_3)

    print(f"Appended 3 lines to {file_path}")


if __name__ == "__main__":
    main()
