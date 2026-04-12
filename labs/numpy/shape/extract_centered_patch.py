# ------------------------------------------------------------ #
# File: extract_centered_patch.py
# Date: 2026-04-02
# Author: Florentino
# Description: Fixed-shape subpatch centered on index; pad when needed.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def extract_patch(
    a: np.ndarray,
    cy: int,
    cx: int,
    ph: int,
    pw: int,
    fill: float = 0.0,
) -> np.ndarray:
    h, w = a.shape
    r0, r1 = cy - ph // 2, cy - ph // 2 + ph
    c0, c1 = cx - pw // 2, cx - pw // 2 + pw
    out = np.full((ph, pw), fill, dtype=a.dtype)
    sr0, sr1 = max(0, r0), min(h, r1)
    sc0, sc1 = max(0, c0), min(w, c1)
    dr0, dr1 = sr0 - r0, sr1 - r0
    dc0, dc1 = sc0 - c0, sc1 - c0
    out[dr0:dr1, dc0:dc1] = a[sr0:sr1, sc0:sc1]
    return out


def main() -> None:
    a = np.arange(100).reshape(10, 10)
    print(extract_patch(a, 0, 0, 3, 3, fill=-1))


if __name__ == "__main__":
    main()
