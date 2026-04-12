# ------------------------------------------------------------ #
# File: 13_csv_dict_reader.py
# Date: 2026-04-01
# Author: Florentino
# Description: Read CSV rows as dicts keyed by the header row (DictReader).
# ------------------------------------------------------------ #

from __future__ import annotations

import csv

from settings import CSV_PATH

OUT = CSV_PATH / "csv_lab_dict_read.csv"

ROWS = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Chicago"],
]


def main() -> None:
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(ROWS)

    print(f"DictReader on {OUT}:\n")
    with open(OUT, "r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print(
                f"{row['Name']} is {row['Age']} years old, from {row['City']}"
            )


if __name__ == "__main__":
    main()
