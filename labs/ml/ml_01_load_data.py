# File: ml_01_load_data.py
# Description: Basic example to load students.csv for ML practice.

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH


def main() -> None:
    csv_path = EXCEL_PATH / "students.csv"
    df = pd.read_csv(csv_path)

    print("Rows, columns:", df.shape)
    print("Columns:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())


if __name__ == "__main__":
    main()
