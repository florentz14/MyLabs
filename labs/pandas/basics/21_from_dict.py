# ------------------------------------------------------------ #
# File: from_dict.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a DataFrame from a dictionary of lists.
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
