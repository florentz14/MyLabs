# ------------------------------------------------------------ #
# File: from_dict.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a DataFrame from a dictionary of lists.
# Explanation: It explains create a DataFrame from a dictionary of lists and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    data = {
        "name": ["Anna", "Louis", "Mary"],
        "age": [25, 30, 28],
        "city": ["Madrid", "Barcelona", "Valencia"],
    }
    df = pd.DataFrame(data)
    print(df)


if __name__ == "__main__":
    main()
