# ------------------------------------------------------------ #
# File: dic.py
# Date: 2026-04-15
# Author: Florentino
# Description: Run countries and vehicles dictionary CSV demos.
# Explanation: It explains how to run both split dictionary demos from one entry point for convenience.
# ------------------------------------------------------------ #

from __future__ import annotations

from dic_countries import main as countries_main
from dic_vehicles import main as vehicles_main


def main() -> None:
    vehicles_main()
    print()
    countries_main()


if __name__ == "__main__":
    main()
