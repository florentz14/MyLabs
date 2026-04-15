# ------------------------------------------------------------ #
# File: series_to_list.py
# Date: 2026-04-01
# Author: Florentino
# Description: Convert pandas Series to Python lists with tolist().
# Explanation: It explains convert pandas Series to Python lists with tolist and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    series = pd.Series([10, 20, 30, 40, 50])
    print("Original Series:")
    print(series)
    print(f"Type of Series : {type(series)}")
    print()

    converted_list = series.tolist()
    print("Converted Python List:")
    print(converted_list)
    print(f"Type of List   : {type(converted_list)}")
    print()

    float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
    float_list = float_series.tolist()
    print("Float Series to List:")
    print(f"  Series : {float_series.values}  ->  Type: {type(float_series)}")
    print(f"  List   : {float_list}  ->  Type: {type(float_list)}")
    print()

    str_series = pd.Series(["apple", "banana", "cherry", "date"])
    str_list = str_series.tolist()
    print("String Series to List:")
    print(f"  Series : {str_series.values}  ->  Type: {type(str_series)}")
    print(f"  List   : {str_list}  ->  Type: {type(str_list)}")
    print()

    indexed_series = pd.Series([100, 200, 300], index=["a", "b", "c"])
    indexed_list = indexed_series.tolist()
    print("Series with Custom Index to List:")
    print(f"  Series :\n{indexed_series}")
    print(f"  List   : {indexed_list}  ->  Type: {type(indexed_list)}")
    print()

    print("Element-wise type check (int Series -> list):")
    for index, value in enumerate(converted_list):
        print(f"  list[{index}] = {value}  ->  Type: {type(value)}")


if __name__ == "__main__":
    main()
