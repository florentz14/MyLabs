# ------------------------------------------------------------ #
# File: columns.py
# Date: 2026-04-01
# Author: Florentino
# Description: Select and create columns in a DataFrame.
# Explanation: It explains select and create columns in a DataFrame and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "product": ["A", "B", "C"],
            "price": [10, 20, 15],
            "quantity": [2, 3, 1],
        }
    )

    df["total"] = df["price"] * df["quantity"]
    print("With total column:")
    print(df)

    df["double_price"] = df["price"].apply(lambda x: x * 2)
    print("\nWith apply:")
    print(df)

    mapping = {"A": "High", "B": "Medium", "C": "Low"}
    df["level"] = df["product"].map(mapping)
    print("\nWith map:")
    print(df)

    df = df.rename(columns={"total": "subtotal"})
    print("\nRenamed:")
    print(df)


if __name__ == "__main__":
    main()
