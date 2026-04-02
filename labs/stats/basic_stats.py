# ------------------------------------------------------------ #
# File: basic_stats.py
# Date: 2026-04-01
# Author: Florentino
# Description: Starter descriptive stats with the standard library statistics module.
# ------------------------------------------------------------ #

from __future__ import annotations

import statistics


def main() -> None:
    values = [10, 20, 30, 40, 50]
    print("Data:", values)
    print("Mean:", statistics.mean(values))
    print("Median:", statistics.median(values))
    print("Stdev (sample):", round(statistics.stdev(values), 4))


if __name__ == "__main__":
    main()
