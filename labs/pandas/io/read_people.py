# ------------------------------------------------------------ #
# File: read_people.py
# Date: 2026-03-28
# Author: Florentino
# Description: Read people.csv from data/excel into a pandas DataFrame.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import EXCEL_PATH

IN_CSV = EXCEL_PATH / "people.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV)

    print(df)
    print()

if __name__ == "__main__":
    main()
