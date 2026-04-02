# ------------------------------------------------------------ #
# File: from_dict_scores.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a DataFrame from a dictionary of score columns.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    data = {
        "X": [78, 85, 96, 80, 86],
        "Y": [84, 94, 89, 83, 86],
        "Z": [86, 97, 96, 72, 83],
    }
    df = pd.DataFrame(data)
    print(df)


if __name__ == "__main__":
    main()
