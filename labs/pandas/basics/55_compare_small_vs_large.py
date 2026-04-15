# ------------------------------------------------------------ #
# File: 55_compare_small_vs_large.py
# Date: 2026-04-02
# Author: Florentino
# Description: Compare sample_df() vs sample_df_large() quickly.
# Explanation: It explains compare sample_df vs sample_df_large quickly and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

from sample_data import sample_df, sample_df_large


def main() -> None:
    small = sample_df()
    large = sample_df_large()

    print("=" * 65)
    print("COMPARE SAMPLE DATASETS")
    print("=" * 65)

    print("\nSmall dataset")
    print(f"Shape         : {small.shape}")
    print(f"Cities        : {small['City'].nunique()}")
    print(f"Missing score : {small['Score'].isna().sum()}")
    print(f"Mean score    : {small['Score'].mean():.2f}")

    print("\nLarge dataset")
    print(f"Shape         : {large.shape}")
    print(f"Cities        : {large['City'].nunique()}")
    print(f"Missing score : {large['Score'].isna().sum()}")
    print(f"Mean score    : {large['Score'].mean():.2f}")

    print("\nTop 3 city mean scores (large)")
    city_mean = large.groupby("City")["Score"].mean().sort_values(ascending=False)
    print(city_mean.head(3).round(2))


if __name__ == "__main__":
    main()
