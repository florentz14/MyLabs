# ------------------------------------------------------------ #
# File: replace_name.py
# Date: 2026-04-01
# Author: Florentino
# Description: Replace one specific value in the name column.
# Explanation: It explains replace one specific value in the name column and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd

from settings import CSV_PATH

IN_CSV = CSV_PATH / "exam_data.csv"


def main() -> None:
    if not IN_CSV.is_file():
        raise FileNotFoundError(f"CSV not found: {IN_CSV}")

    df = pd.read_csv(IN_CSV, index_col="label")
    # Keep surname: e.g. "Sergio Gomez" -> "Suresh Gomez"
    df["name"] = df["name"].str.replace(r"^Sergio\b", "Suresh", regex=True)

    print("Change the name 'Sergio' to 'Suresh':")
    print(df)


if __name__ == "__main__":
    main()
