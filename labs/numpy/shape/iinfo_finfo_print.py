# ------------------------------------------------------------ #
# File: iinfo_finfo_print.py
# Date: 2026-04-02
# Author: Florentino
# Description: Min/max for integer and float dtypes via iinfo/finfo.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    for t in (np.int8, np.int16, np.int32, np.int64, np.uint8, np.float16, np.float32, np.float64):
        if np.issubdtype(t, np.integer):
            info = np.iinfo(t)
            print(t.__name__, "min", info.min, "max", info.max)
        else:
            info = np.finfo(t)
            print(t.__name__, "min", info.min, "max", info.max)


if __name__ == "__main__":
    main()
