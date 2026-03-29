# File: read_people.py
# Date: 2026-03-28
# Author: Florentino
# Description: Read people.csv from data/csv_files into a pandas DataFrame.

from __future__ import annotations

import pandas as pd
from settings import CSV_PATH


def main() -> None:
    csv_path = CSV_PATH / "people.csv"
    if not csv_path.is_file():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)
    print(df)
    print()


if __name__ == "__main__":
    main()
