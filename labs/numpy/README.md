# NumPy Labs

One minimal script per operation (run any file with `python3 labs/numpy/<topic>/<name>.py` from the repo root). For scripts that import `settings` (`struct_npy.py`, `split_npy.py`), use `PYTHONPATH=.` from the repo root so `data/gen/` paths resolve.

| Folder | Topics |
| --- | --- |
| `arithmetic/` | Element-wise `+`, `-`, `*`, `/`, `**`, `%`, `sqrt`, `exp`, `sin`, `log`; topic scripts `inplace_uf`, `bool_mask`, `bcast`; drills `negate_between_3_8`, `expr_inplace_ab`, `integer_part_four_ways`, … |
| `aggregation/` | `sum`, `mean`, `median`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `percentile`; topic script `axis_agg`; drills `random_min_max`, `random_mean_30`, … |
| `shape/` | `reshape`, `transpose`, `flatten`, `concatenate`, `split`, `ravel`, `expand_dims`, `squeeze`, `vstack`, `hstack`; topic scripts `idx_flat`, `ravel_t`, `vhstack`, `view_copy`, `struct_npy`, `split_npy`; drills `rgba_dtype`, `print_all_values`, … |
| `linalg/` | `dot`, `det`, `eye`, `inv`, `matrix_rank`, `eigvals`, `solve`, `norm`, `trace`, `outer`; topic script `elem_matmul`; drills `identity_3`, `matmul_5x3_3x2`, `cauchy_matrix`, … |
| `datetime/` | `datetime64` / `timedelta64`: `yesterday_today_tomorrow`, `july_2016` |

Legacy entry: `basic_numpy.py` (tiny array + mean).

---

## Learning path

Short **topic scripts** mirror a classic NumPy tour: run them in order if you want a linear path. The **100-style drills** table below is separate bite-sized practice.

**Assumptions:** Python 3.10+ and NumPy installed.

### Concept map

| Area | Ideas |
| --- | --- |
| **Arithmetic** | Element-wise `+`, `-`, `*`, `/`, `**`; matrix product `@` / `dot` (not `*`) |
| **Updates** | In-place `+=`, `-=`; no C-style `++` / `--` |
| **ufuncs** | `np.sin`, `np.sqrt`, … on whole arrays |
| **Aggregation** | `sum`, `min`, `max`, … and `axis=` |
| **Indexing** | Slicing, fancy indexing, `flat` |
| **Boolean masks** | Comparisons, `a[mask]`, `a[cond] = …` |
| **Shape** | `reshape`, `ravel`, `T`, stack / split |
| **Views vs copies** | Slices often share memory; `.copy()` when you need isolation |
| **Broadcasting** | How different shapes combine (e.g. scalar + array) |
| **Structured arrays** | `dtype` with named fields |
| **I/O** | `.npy` / `.npz`; `loadtxt` / `genfromtxt` for text |

### Topic scripts (short names)

| Script | Folder | What it shows |
| --- | --- | --- |
| `elem_matmul.py` | `linalg/` | Vectors: `+`, `-`, `**`; matrices: `*` (element-wise) vs `@` (matmul) |
| `inplace_uf.py` | `arithmetic/` | `+=` / `-=`; `np.sin`, `np.sqrt` |
| `axis_agg.py` | `aggregation/` | Whole-array `sum` / `max` vs `sum(axis=0)` |
| `idx_flat.py` | `shape/` | Slices, slice assignment, `for row in arr`, `arr.flat` |
| `bool_mask.py` | `arithmetic/` | Boolean mask, filter, assign through mask |
| `ravel_t.py` | `shape/` | `reshape`, `ravel`, `.T` |
| `vhstack.py` | `shape/` | `np.vstack`, `np.hstack` |
| `view_copy.py` | `shape/` | View mutates base; `.copy()` does not |
| `bcast.py` | `arithmetic/` | `vector + scalar`, `matrix + row` |
| `struct_npy.py` | `shape/` | Structured array fields; `np.save` / `load` → `data/gen/struct_npy_rand.npy` |
| `split_npy.py` | `shape/` | `hsplit` / `vsplit`; `save`/`load`; `genfromtxt` from `StringIO` |

Related drills and one-offs: `linalg/dot.py`, `arithmetic/broadcast_multiply_rgb.py`, `shape/rgba_dtype.py`, `arithmetic/negate_between_3_8.py`, CSV-oriented work under `labs/files/`.

### Technical notes

- **Broadcasting:** trailing dimensions must match or be `1`.
- **`.npy` / `.npz`:** good for NumPy-native round-trips; compact and fast vs plain text.
- **Structured arrays:** handy for mixed dtypes inside NumPy; for large tables, pandas is often simpler.

```bash
# Topic path (from repo root)
PYTHONPATH=. python3 labs/numpy/linalg/elem_matmul.py
PYTHONPATH=. python3 labs/numpy/shape/struct_npy.py
PYTHONPATH=. python3 labs/numpy/shape/split_npy.py
python3 labs/numpy/arithmetic/inplace_uf.py
python3 labs/numpy/aggregation/axis_agg.py
```

---

## NumPy 100–style drills (items 6–15, 18–25, 33–53, 55–100)

Short exercises live **next to the topic** they illustrate (not in a separate `exercises/` folder).

| # | File | Folder | Description |
| --- | --- | --- | --- |
| 6 | `zeros_fifth_one.py` | `shape/` | Length-10 zeros, index 4 → 1 |
| 7 | `arange_10_49.py` | `shape/` | `np.arange(10, 50)` |
| 8 | `reverse_vector.py` | `shape/` | Reverse 1-D with `[::-1]` |
| 9 | `reshape_3x3_0_8.py` | `shape/` | 3×3 matrix 0…8 |
| 10 | `nonzero_indices.py` | `shape/` | `np.nonzero` on a small vector |
| 11 | `identity_3.py` | `linalg/` | 3×3 identity (`np.eye`) |
| 12 | `random_3cube.py` | `shape/` | Random 3×3×3 |
| 13 | `random_min_max.py` | `aggregation/` | 10×10 random, `min` / `max` |
| 14 | `random_mean_30.py` | `aggregation/` | Length-30 random, `mean` |
| 15 | `border_ones.py` | `shape/` | Ones on border, zeros inside |
| 18 | `subdiag_1_to_4.py` | `shape/` | 5×5, values 1…4 on first sub-diagonal |
| 19 | `checkerboard_8.py` | `shape/` | 8×8 checkerboard `(i+j)%2` |
| 20 | `unravel_100th.py` | `shape/` | `(x,y,z)` of 100th element in `(6,7,8)` (C order, index 99) |
| 21 | `checkerboard_tile_8.py` | `shape/` | 8×8 checkerboard with `np.tile` |
| 22 | `normalize_random_5x5.py` | `aggregation/` | Min–max normalize random 5×5 |
| 23 | `rgba_dtype.py` | `shape/` | RGBA as four `uint8` fields |
| 24 | `matmul_5x3_3x2.py` | `linalg/` | Matrix product 5×3 @ 3×2 |
| 25 | `negate_between_3_8.py` | `arithmetic/` | In-place negate for `3 < x < 8` |
| 33 | `yesterday_today_tomorrow.py` | `datetime/` | `datetime64` + 1 day |
| 34 | `july_2016.py` | `datetime/` | All days in July 2016 |
| 35 | `expr_inplace_ab.py` | `arithmetic/` | `((A+B)*(-A/2))` with `out=` |
| 36 | `integer_part_four_ways.py` | `arithmetic/` | Integer part: `floor`, `trunc`, `astype`, `modf` |
| 37 | `matrix_rows_0_to_4.py` | `shape/` | 5×5 rows `0…4` (`broadcast_to`) |
| 38 | `fromiter_generator.py` | `shape/` | `np.fromiter` + generator |
| 39 | `linspace_open_0_1.py` | `shape/` | 10 values strictly between 0 and 1 |
| 40 | `sort_random_vector.py` | `shape/` | Sort random length-10 vector |
| 41 | `add_reduce_sum.py` | `aggregation/` | `np.add.reduce` vs `sum` |
| 42 | `arrays_equal.py` | `shape/` | `array_equal` / `allclose` |
| 43 | `readonly_flags.py` | `shape/` | `flags.writeable = False` |
| 44 | `cartesian_to_polar.py` | `shape/` | `hypot`, `arctan2` |
| 45 | `replace_max_zero.py` | `shape/` | Replace max by 0 |
| 46 | `structured_grid_xy.py` | `shape/` | Structured `(x,y)` on `[0,1]²` grid |
| 47 | `cauchy_matrix.py` | `linalg/` | `1/(x_i - y_j)` |
| 48 | `iinfo_finfo_print.py` | `shape/` | `np.iinfo` / `np.finfo` |
| 49 | `print_all_values.py` | `shape/` | `set_printoptions(threshold=…)` |
| 50 | `closest_to_scalar.py` | `aggregation/` | Nearest value via `argmin` on `\|v-z\|` |
| 51 | `structured_xy_rgb.py` | `shape/` | Structured position + RGB |
| 52 | `pairwise_distances.py` | `shape/` | Consecutive distances on `(100,2)` |
| 53 | `float32_to_int32_inplace.py` | `shape/` | `astype` / `copyto` to int32 |

### Items 55–100

| # | File | Folder | Description |
| --- | --- | --- | --- |
| 55 | `ndenumerate.py` | `shape/` | Walk N-D index + value pairs with `np.ndenumerate` |
| 56 | `gaussian_2d.py` | `shape/` | Build or sample a 2-D Gaussian bump / grid |
| 57 | `random_p_elements_2d.py` | `shape/` | Choose `p` distinct cells from a 2-D array |
| 58 | `row_subtract_mean.py` | `aggregation/` | Center each row by subtracting its mean |
| 59 | `sort_by_column.py` | `shape/` | Sort matrix rows using a chosen column as key |
| 60 | `has_null_columns.py` | `shape/` | Find columns that are all NaN (or “null”) |
| 61 | `nearest_value.py` | `aggregation/` | Nearest entry in an array to each query value |
| 62 | `nditer_sum_broadcast.py` | `shape/` | `np.nditer` with reduction and broadcasting |
| 63 | `named_ndarray.py` | `shape/` | Subclass `ndarray` with an extra name field |
| 64 | `add_at_repeated_indices.py` | `arithmetic/` | Accumulate with `np.add.at` at repeated indices |
| 65 | `accumulate_weights_by_index.py` | `aggregation/` | Sum weights bucketed by integer labels |
| 66 | `unique_rgb_colors.py` | `shape/` | Count distinct RGB tuples in an image-like array |
| 67 | `sum_axes_last_two.py` | `aggregation/` | Sum over the last two axes of an N-D array |
| 68 | `mean_by_subset_index.py` | `aggregation/` | Grouped mean using an index / label array |
| 69 | `dot_product_diagonal.py` | `linalg/` | Diagonal of `A @ B` via `einsum` (avoid full matmul) |
| 70 | `interleave_three_zeros.py` | `shape/` | Insert runs of zeros between blocks of data |
| 71 | `broadcast_multiply_rgb.py` | `arithmetic/` | Scale RGB planes with a broadcast 1×1×3 vector |
| 72 | `swap_rows.py` | `shape/` | Exchange two rows of a 2-D array in place |
| 73 | `triangle_edges_unique.py` | `shape/` | Unique undirected edges from integer triples |
| 74 | `inverse_bincount.py` | `shape/` | Rebuild a 1-D array from bin counts (inverse of `bincount`) |
| 75 | `sliding_mean.py` | `aggregation/` | Moving average with a 1-D sliding window |
| 76 | `sliding_window_matrix.py` | `shape/` | Slide a window over a 2-D array (stacked patches) |
| 77 | `inplace_negate_sign.py` | `arithmetic/` | Flip signs using `np.sign` / multiply by −1 in place |
| 78 | `point_to_line_distance.py` | `shape/` | Distance from points to a single line (geometry) |
| 79 | `points_to_lines_distance.py` | `shape/` | Distances from point set to several lines |
| 80 | `extract_centered_patch.py` | `shape/` | Crop a fixed-size window around a center index |
| 81 | `rolling_windows_1d.py` | `shape/` | 1-D signal → matrix of overlapping windows |
| 82 | `rank_low_vs_full.py` | `linalg/` | Compare rank of a product vs full matrix (see `matrix_rank.py`) |
| 83 | `mode_most_frequent.py` | `aggregation/` | Most frequent value in an array |
| 84 | `sliding_window_3x3.py` | `shape/` | 3×3 neighborhood operation on a grid |
| 85 | `symmetric_ndarray_subclass.py` | `shape/` | Enforce symmetry in a custom `ndarray` subclass |
| 86 | `batched_matvec_sum.py` | `linalg/` | Stack of matrix–vector products then sum |
| 87 | `block_sum_4x4.py` | `aggregation/` | Sum non-overlapping 4×4 tiles in a grid |
| 88 | `game_of_life.py` | `shape/` | One (or more) steps of Conway’s Game of Life |
| 89 | `n_largest.py` | `aggregation/` | Find the `n` largest elements (indices or values) |
| 90 | `cartesian_product_many.py` | `shape/` | Cartesian product of several 1-D coordinate arrays |
| 91 | `record_from_arrays.py` | `shape/` | Build structured / record array from column vectors |
| 92 | `cube_three_ways.py` | `arithmetic/` | Same 3-D cube built with three different NumPy idioms |
| 93 | `rows_containing_multiset.py` | `shape/` | Rows whose multiset of entries matches a target |
| 94 | `rows_not_all_equal.py` | `shape/` | Mask rows where values are not all the same |
| 95 | `int_to_binary_matrix.py` | `shape/` | Encode integers as rows of binary bits |
| 96 | `unique_rows_2d.py` | `shape/` | Unique rows of a 2-D array (order-preserving or sorted) |
| 97 | `einsum_inner_outer.py` | `shape/` | Inner and outer products via `np.einsum` |
| 98 | `equidistant_path_samples.py` | `shape/` | Evenly spaced samples along a piecewise-linear path |
| 99 | `multinomial_rows_select.py` | `shape/` | Multinomial draws then pick columns per row |
| 100 | `bootstrap_ci_mean.py` | `aggregation/` | Bootstrap confidence interval for the mean |

Example:

```bash
python3 labs/numpy/shape/zeros_fifth_one.py
python3 labs/numpy/aggregation/random_mean_30.py
python3 labs/numpy/datetime/july_2016.py
```
