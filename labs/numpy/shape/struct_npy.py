# ------------------------------------------------------------ #
# File: struct_npy.py
# Date: 2026-04-02
# Author: Florentino
# Description: Structured dtype + `np.save`/`load` → `data/gen/struct_npy_rand.npy`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np

from settings import GEN_PATH


def main() -> None:
    dtype = [("name", "U10"), ("age", "i4"), ("weight", "f4")]
    users = np.array([("Ann", 25, 55.5), ("John", 30, 85.0)], dtype=dtype)
    print("names:", users["name"])
    print("age > 28:\n", users[users["age"] > 28])

    GEN_PATH.mkdir(parents=True, exist_ok=True)
    path = GEN_PATH / "struct_npy_rand.npy"
    data = np.random.default_rng(0).random((10, 10))
    np.save(path, data)
    loaded = np.load(path)
    print("saved and loaded shape:", loaded.shape, "path:", path)


if __name__ == "__main__":
    main()
