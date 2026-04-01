# ------------------------------------------------------------ #
# File: append_log.py
# Date: 2026-04-01
# Author: Florentino
# Description: Append lines with mode "a"; create the file once if it does not exist.
# ------------------------------------------------------------ #

from __future__ import annotations

from settings import FILES_PATH

NOTES = FILES_PATH / "birdwatch.txt"


def main() -> None:
    if not NOTES.is_file():
        NOTES.write_text("Log — backyard window\n", encoding="utf-8")
    with open(NOTES, "a", encoding="utf-8") as f:
        f.write("• Robin, 07:40\n")
        f.write("• Blue jay, 08:05\n")
    print(NOTES.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
