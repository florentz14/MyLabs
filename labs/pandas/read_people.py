# File: read_people.py
# Date: 2026-03-28
# Author: Florentino
# Description: Read people.csv from data/csv_files into a pandas DataFrame.

from __future__ import annotations

import pandas as pd

# Import the CSV_PATH from the settings module
from settings import CSV_PATH


def main() -> None:
    # Path comes from the CSV_PATH import
    csv_path = CSV_PATH / "people.csv"
    if not csv_path.is_file():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    # First row is treated as column names
    df = pd.read_csv(csv_path)

    # Print the DataFrame
    print(df)
    print()


if __name__ == "__main__":
    main()
