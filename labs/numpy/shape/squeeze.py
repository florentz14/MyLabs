# ------------------------------------------------------------ #
# File: squeeze.py
# Date: 2026-04-01
# Author: Florentino
# Description: Remove axes of length 1.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    print(np.squeeze(np.array([[1, 2]])))


if __name__ == "__main__":
    main()
