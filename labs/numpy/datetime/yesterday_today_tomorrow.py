# ------------------------------------------------------------ #
# File: yesterday_today_tomorrow.py
# Date: 2026-04-02
# Author: Florentino
# Description: Yesterday, today, tomorrow with datetime64.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    today = np.datetime64("today")
    one = np.timedelta64(1, "D")
    print("yesterday", today - one)
    print("today    ", today)
    print("tomorrow ", today + one)


if __name__ == "__main__":
    main()
