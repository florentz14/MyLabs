# ------------------------------------------------------------ #
# File: csv_read_write.py
# Date: 2026-04-01
# Author: Florentino
# Description: Write and read a CSV with csv.writer and csv.reader.
# ------------------------------------------------------------ #

from __future__ import annotations

import csv

from settings import CSV_PATH

OUT = CSV_PATH / "csv_lab_basic.csv"

ROWS = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Chicago"],
]


def main() -> None:
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(ROWS)

    print(f"Wrote {OUT}\n\nReading:")
    with open(OUT, "r", newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            print(row)


if __name__ == "__main__":
    main()
