# File: read_people.py
# Date: 2026-03-28
# Author: Florentino
# Description: Read people.csv from data/excel into a pandas DataFrame.

from __future__ import annotations

import pandas as pd

# EXCEL_PATH hosts both CSV and XLSX practice files.
from settings import EXCEL_PATH


def main() -> None:
    # Read CSV from the shared spreadsheet directory.
    csv_path = EXCEL_PATH / "people.csv"
    if not csv_path.is_file():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    # First row is treated as column names.
    df = pd.read_csv(csv_path)

    # Print the DataFrame.
    print(df)
    print()


if __name__ == "__main__":
    main()
