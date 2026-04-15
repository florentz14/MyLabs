# ------------------------------------------------------------ #
# File: to_csv.py
# Date: 2026-04-01
# Author: Florentino
# Description: Write a DataFrame to CSV under EXCEL_PATH (to_csv).
# Explanation: It explains write a DataFrame to CSV under EXCEL_PATH and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from sample_data import sample_df
from settings import EXCEL_PATH

OUT = EXCEL_PATH / "pandas_basics_sample.csv"


def main() -> None:
    df = sample_df()
    df.to_csv(OUT, index=False)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
