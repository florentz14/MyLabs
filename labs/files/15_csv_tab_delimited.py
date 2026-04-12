# ------------------------------------------------------------ #
# File: 15_csv_tab_delimited.py
# Date: 2026-04-01
# Author: Florentino
# Description: Tab-separated values (TSV) using csv.writer delimiter.
# ------------------------------------------------------------ #

from __future__ import annotations

import csv

from settings import CSV_PATH

OUT = CSV_PATH / "csv_lab_tab.tsv"

ROWS = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Chicago"],
]


def main() -> None:
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t").writerows(ROWS)

    print(f"Wrote TSV {OUT}\n\nFirst line (tabs visible as spacing in some viewers):")
    print(OUT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
