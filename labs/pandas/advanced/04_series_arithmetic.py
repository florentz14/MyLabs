# ------------------------------------------------------------ #
# File: 04_series_arithmetic.py
# Date: 2026-04-02
# Author: Florentino
# Description: Perform arithmetic operations between two pandas Series.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def build_series() -> tuple[pd.Series, pd.Series]:
    return pd.Series([2, 4, 6, 8, 10]), pd.Series([1, 3, 5, 7, 9])


def compute_ops(series1: pd.Series, series2: pd.Series) -> dict[str, pd.Series]:
    return {
        "add": series1 + series2,
        "sub": series1 - series2,
        "mul": series1 * series2,
        "div": series1 / series2,
        "floordiv": series1 // series2,
        "mod": series1 % series2,
        "pow": series1**series2,
    }


def print_ops(ops: dict[str, pd.Series]) -> None:
    labels = {
        "add": "+ Addition (Series1 + Series2):",
        "sub": "- Subtraction (Series1 - Series2):",
        "mul": "* Multiplication (Series1 * Series2):",
        "div": "/ Division (Series1 / Series2):",
        "floordiv": "// Floor Division (Series1 // Series2):",
        "mod": "% Modulus (Series1 % Series2):",
        "pow": "** Power (Series1 ** Series2):",
    }
    for key in ("add", "sub", "mul", "div", "floordiv", "mod", "pow"):
        print(f"\n{labels[key]}")
        print(ops[key].to_string())


def print_summary(series1: pd.Series, series2: pd.Series, ops: dict[str, pd.Series]) -> None:
    print("\n" + "=" * 60)
    print("                   SUMMARY TABLE")
    print("=" * 60)
    print(f"{'S1':>5} {'S2':>5} {'Add':>8} {'Sub':>8} {'Mul':>8} {'Div':>8} {'Mod':>5} {'Pow':>12}")
    print("-" * 60)
    for i in range(len(series1)):
        print(
            f"{series1[i]:>5} {series2[i]:>5} {ops['add'][i]:>8} {ops['sub'][i]:>8} "
            f"{ops['mul'][i]:>8} {ops['div'][i]:>8.2f} {ops['mod'][i]:>5} {ops['pow'][i]:>12}"
        )
    print("=" * 60)


def print_method_ops(series1: pd.Series, series2: pd.Series) -> None:
    print("\n-- Using Pandas Built-in Methods --")
    print(f"series1.add(series2)      : {series1.add(series2).tolist()}")
    print(f"series1.sub(series2)      : {series1.sub(series2).tolist()}")
    print(f"series1.mul(series2)      : {series1.mul(series2).tolist()}")
    print(f"series1.div(series2)      : {[round(x, 2) for x in series1.div(series2).tolist()]}")
    print(f"series1.floordiv(series2) : {series1.floordiv(series2).tolist()}")
    print(f"series1.mod(series2)      : {series1.mod(series2).tolist()}")
    print(f"series1.pow(series2)      : {series1.pow(series2).tolist()}")


def main() -> None:
    series1, series2 = build_series()
    ops = compute_ops(series1, series2)

    print("=" * 40)
    print("        SERIES ARITHMETIC")
    print("=" * 40)
    print(f"Series 1 : {series1.tolist()}")
    print(f"Series 2 : {series2.tolist()}")
    print("=" * 40)

    print_ops(ops)
    print_summary(series1, series2, ops)
    print_method_ops(series1, series2)


if __name__ == "__main__":
    main()
