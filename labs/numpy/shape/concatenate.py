# ------------------------------------------------------------ #
# File: concatenate.py
# Date: 2026-04-01
# Author: Florentino
# Description: Join arrays along an axis (default: flattened 1-D).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    print(np.concatenate(([1, 2], [3, 4])))


if __name__ == "__main__":
    main()
