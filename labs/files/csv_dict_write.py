# ------------------------------------------------------------ #
# File: csv_dict_write.py
# Date: 2026-04-01
# Author: Florentino
# Description: Write CSV with DictWriter (header + rows), then read back.
# ------------------------------------------------------------ #

from __future__ import annotations

import csv

from settings import CSV_PATH

OUT = CSV_PATH / "csv_lab_inventory.csv"
FIELDNAMES = ["Product", "Price", "Quantity"]


def main() -> None:
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerow({"Product": "Apple", "Price": 1.50, "Quantity": 10})
        w.writerow({"Product": "Banana", "Price": 0.75, "Quantity": 20})

    print(f"Wrote {OUT}\n\nReading:")
    with open(OUT, "r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print(row)


if __name__ == "__main__":
    main()
