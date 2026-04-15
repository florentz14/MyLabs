# ------------------------------------------------------------ #
# File: index_labels.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a DataFrame with custom index labels.
# Explanation: It explains create a DataFrame with custom index labels and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    data = {
        "name": [
            "Aisha Hassan",
            "Mateo Rodriguez",
            "Hiroshi Tanaka",
            "Kwame Mensah",
            "Sofia Petrova",
            "Liam OConnor",
            "Fatima Alzahra",
            "Chen Wei",
            "Ananya Sharma",
            "Lucas Silva",
            "Noah Johnson",
            "Yuki Nakamura",
            "Zara Khan",
            "Victor Dubois",
        ],
        "score": [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0, 11.5, 17.3, 13.8, 15.2],
        "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1, 2, 2, 1, 3],
        "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes", "no", "yes", "yes", "yes"],
    }

    labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    df = pd.DataFrame(data, index=labels)
    print(df)


if __name__ == "__main__":
    main()
