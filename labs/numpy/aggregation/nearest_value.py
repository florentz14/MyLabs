# ------------------------------------------------------------ #
# File: nearest_value.py
# Date: 2026-04-02
# Author: Florentino
# Description: Nearest array element to a scalar. See `closest_to_scalar.py`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.linspace(0.0, 1.0, 11)
    v = 0.33
    print(z[np.argmin(np.abs(z - v))])


if __name__ == "__main__":
    main()
