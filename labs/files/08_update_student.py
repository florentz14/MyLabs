# ------------------------------------------------------------ #
# File: 08_update_student.py
# Date: 2026-03-29
# Author: Florentino
# Description: Upsert a row in student.txt by id (update if present, else append).
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH

STUDENT_FILE = "student.txt"

# Change these for any record: id must match the first CSV field of NEW_ROW.
TARGET_ID = "3"
NEW_ROW = "3,Carol Williams,carol.w@example.com,2024,Data Structures"


def _is_header_line(line: str) -> bool:
    return line.strip().lower().startswith("id,")


def _row_id(line: str) -> str | None:
    if not line.strip() or _is_header_line(line):
        return None
    # Only the first CSV field is the row id
    return line.split(",", 1)[0].strip()


def upsert_row_by_id(lines: list[str], target_id: str, new_row: str) -> tuple[list[str], bool]:
    """Replace the data line whose first field equals target_id, or append new_row."""
    tid = target_id.strip()
    out: list[str] = []
    replaced = False
    for line in lines:
        if _row_id(line) == tid:
            # Replace existing row for this id
            out.append(new_row)
            replaced = True
        else:
            out.append(line)
    if not replaced:
        # New id: add line at end of file
        out.append(new_row)
    return out, replaced


def main() -> None:
    file_path = FILES_PATH / STUDENT_FILE
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Lines without line-break characters; trailing blank line from EOF is dropped
    lines = file_path.read_text(encoding="utf-8").splitlines()
    new_lines, updated = upsert_row_by_id(lines, TARGET_ID, NEW_ROW)
    # POSIX text files usually end with a newline
    file_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    action = "Updated" if updated else "Appended"
    print(f"{action} id {TARGET_ID.strip()!r} and saved: {file_path}")
    print(NEW_ROW)


if __name__ == "__main__":
    main()
