# ------------------------------------------------------------ #
# File: float32_to_int32_inplace.py
# Date: 2026-04-02
# Author: Florentino
# Description: float32 → int32 truncation with copy=False / copyto.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([1.9, 2.1, -3.7, 42.0], dtype=np.float32)
    b = a.astype(np.int32, copy=False)
    print("float", a)
    print("int  ", b)
    out = np.empty_like(a, dtype=np.int32)
    np.copyto(out, a, casting="unsafe")
    print("copyto", out)


if __name__ == "__main__":
    main()
