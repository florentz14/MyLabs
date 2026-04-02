# ------------------------------------------------------------ #
# File: insert_color.py
# Date: 2026-04-01
# Author: Florentino
# Description: Insert a new color column into the DataFrame.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")

    base_colors = ["Red", "Blue", "Orange", "Red", "White", "White", "Blue", "Green", "Green", "Red"]
    repeats = (len(df) // len(base_colors)) + 1
    colors = (base_colors * repeats)[: len(df)]
    df["color"] = colors

    print("New DataFrame after inserting the 'color' column:")
    print(df)


if __name__ == "__main__":
    main()
