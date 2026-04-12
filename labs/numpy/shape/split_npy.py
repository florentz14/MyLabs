# ------------------------------------------------------------ #
# File: split_npy.py
# Date: 2026-04-02
# Author: Florentino
# Description: `hsplit`/`vsplit`, small `.npy` I/O, `genfromtxt` via StringIO.
# ------------------------------------------------------------ #

from __future__ import annotations

import io

import numpy as np

from settings import GEN_PATH


def main() -> None:
    a = np.arange(12).reshape(3, 4)
    h1, h2 = np.hsplit(a, 2)
    v1, _v2, _v3 = np.vsplit(a, 3)
    print("Original:\n", a)
    print("vsplit first block:\n", v1)
    print("First hsplit part:\n", h1)

    GEN_PATH.mkdir(parents=True, exist_ok=True)
    out = GEN_PATH / "split_npy_1d.npy"
    np.save(out, np.array([1, 2, 3, 4, 5]))
    print("load:", np.load(out), "from", out)

    csv_text = io.StringIO("a,b\n1,2.5\n3,4.1\n")
    tab = np.genfromtxt(csv_text, delimiter=",", names=True)
    print("genfromtxt names:", tab.dtype.names)
    print("column a:", tab["a"])


if __name__ == "__main__":
    main()
