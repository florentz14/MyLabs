# ------------------------------------------------------------ #
# File: 53_rename_columns.py
# Date: 2026-04-01
# Author: Florentino
# Description: Rename multiple DataFrame columns in one rename() call.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})

    print("original DataFrame")
    print(df)

    df = df.rename(
        columns={"col1": "Column1", "col2": "Column2", "col3": "Column3"}
    )
    print("\nnew DataFrame after renaming columns:")
    print(df)


if __name__ == "__main__":
    main()
