# ------------------------------------------------------------ #
# File: write_student.py
# Date: 2026-03-29
# Author: Florentino
# Description: Create or overwrite student.txt with student records (write "w" mode, not append).
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH

STUDENT_FILE = "student.txt"


def main() -> None:
    # CSV header plus data rows
    file_path = FILES_PATH / STUDENT_FILE

    # Overwrite existing file completely
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("id,name,email,year,course\n")
        file.write("1,Alice Johnson,alice.johnson@example.com,2025,Python Lab\n")
        file.write("2,Bob Smith,bob.smith@example.com,2025,Python Lab\n")
        file.write("3,Carol Williams,carol.w@example.com,2024,Data Structures\n")
        file.write("4,David Brown,david.brown@example.com,2025,Python Lab\n")
        file.write("5,Eva Garcia,eva.garcia@example.com,2024,Algorithms\n")

    print(f"Wrote {file_path} (file replaced; use write mode, not append).")


if __name__ == "__main__":
    main()
