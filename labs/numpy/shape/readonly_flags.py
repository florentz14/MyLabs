# ------------------------------------------------------------ #
# File: readonly_flags.py
# Date: 2026-04-02
# Author: Florentino
# Description: Make an array read-only via flags.writeable.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(4)
    a.flags.writeable = False
    print(a.flags.writeable)
    try:
        a[0] = 9
    except ValueError as e:
        print(type(e).__name__, e)


if __name__ == "__main__":
    main()
