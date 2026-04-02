# ------------------------------------------------------------ #
# File: index_ops.py
# Date: 2026-04-01
# Author: Florentino
# Description: set_index, reset_index, index rename, and MultiIndex operations.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "country": ["USA", "USA", "UK", "UK"],
            "city": ["NYC", "LA", "London", "Manchester"],
            "pop": [8.4, 4.0, 9.0, 2.9],
        }
    )

    print("=== ORIGINAL ===")
    print(df)
    print()

    df_idx = df.set_index("country")
    print("=== set_index('country') ===")
    print(df_idx)
    print()

    df_reset = df_idx.reset_index()
    print("=== reset_index() ===")
    print(df_reset)
    print()

    df_idx2 = df.set_index("country", drop=False)
    print("=== set_index(drop=False) ===")
    print(df_idx2)
    print()

    df_idx_named = df.set_index("country")
    df_idx_named.index = df_idx_named.index.rename("nation")
    print("=== index.rename('nation') ===")
    print(df_idx_named)
    print()

    df_mi = df.set_index(["country", "city"])
    print("=== MultiIndex (country, city) ===")
    print(df_mi)
    print()

    df_mi_reset = df_mi.reset_index()
    print("=== reset_index() from MultiIndex ===")
    print(df_mi_reset)


if __name__ == "__main__":
    main()
