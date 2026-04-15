# ------------------------------------------------------------ #
# File: dic_vehicles.py
# Date: 2026-04-15
# Author: Florentino
# Description: Write/read vehicle CSV using DictWriter/DictReader.
# Explanation: It explains vehicle CSV write/read with type parsing and validation for basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import csv
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "data"

# Vehicles with id/code to support richer CSV exercises.
vehicle_rows = [
    {"vehicle_id": 1, "vehicle_code": "FOR-MUS-1964", "brand": "Ford", "model": "Mustang", "year": 1964, "color": "red", "price": 10000, "is_new": True, "is_used": False, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 2, "vehicle_code": "TOY-COR-2020", "brand": "Toyota", "model": "Corolla", "year": 2020, "color": "white", "price": 18000, "is_new": False, "is_used": True, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 3, "vehicle_code": "TES-M3-2023", "brand": "Tesla", "model": "Model 3", "year": 2023, "color": "black", "price": 42000, "is_new": True, "is_used": False, "is_electric": True, "is_gasoline": False, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 4, "vehicle_code": "HON-CIV-2018", "brand": "Honda", "model": "Civic", "year": 2018, "color": "blue", "price": 16000, "is_new": False, "is_used": True, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 5, "vehicle_code": "CHE-SIL-2021", "brand": "Chevrolet", "model": "Silverado", "year": 2021, "color": "gray", "price": 35000, "is_new": False, "is_used": True, "is_electric": False, "is_gasoline": True, "is_diesel": True, "is_hybrid": False},
    {"vehicle_id": 6, "vehicle_code": "HYU-ELA-2022", "brand": "Hyundai", "model": "Elantra", "year": 2022, "color": "silver", "price": 21000, "is_new": True, "is_used": False, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 7, "vehicle_code": "KIA-NIR-2024", "brand": "Kia", "model": "Niro", "year": 2024, "color": "green", "price": 29000, "is_new": True, "is_used": False, "is_electric": False, "is_gasoline": False, "is_diesel": False, "is_hybrid": True},
    {"vehicle_id": 8, "vehicle_code": "NIS-LEA-2019", "brand": "Nissan", "model": "Leaf", "year": 2019, "color": "white", "price": 17000, "is_new": False, "is_used": True, "is_electric": True, "is_gasoline": False, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 9, "vehicle_code": "BMW-X5-2017", "brand": "BMW", "model": "X5", "year": 2017, "color": "black", "price": 33000, "is_new": False, "is_used": True, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 10, "vehicle_code": "AUD-A4-2016", "brand": "Audi", "model": "A4", "year": 2016, "color": "red", "price": 24000, "is_new": False, "is_used": True, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
    {"vehicle_id": 11, "vehicle_code": "VOL-GOL-2015", "brand": "Volkswagen", "model": "Golf", "year": 2015, "color": "blue", "price": 14000, "is_new": False, "is_used": True, "is_electric": False, "is_gasoline": True, "is_diesel": False, "is_hybrid": False},
]


def write_vehicle_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(vehicle_rows[0].keys()))
        w.writeheader()
        w.writerows(
            [{k: str(v) if isinstance(v, bool) else v for k, v in row.items()} for row in vehicle_rows]
        )


def read_vehicle_csv(path: Path) -> dict[str, object]:
    """One data row: first (and only) row from DictReader -> dict."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader, None)
    if row is None:
        raise ValueError(f"Vehicle CSV has no data rows: {path}")
    out: dict[str, object] = {}
    for key, raw in row.items():
        if key is None:
            continue
        if key in ("vehicle_id", "year", "price"):
            if raw is None or raw == "":
                raise ValueError(f"Missing numeric value for '{key}' in {path}")
            try:
                out[key] = int(raw)
            except ValueError as exc:
                raise ValueError(
                    f"Invalid integer for '{key}' in {path}: {raw!r}"
                ) from exc
        elif key.startswith("is_"):
            out[key] = raw == "True"
        else:
            out[key] = raw
    return out


def main() -> None:
    v_path = _DATA_DIR / "dic_vehicle.csv"
    write_vehicle_csv(v_path)
    print("Wrote:", v_path)

    vehicle_from_csv = read_vehicle_csv(v_path)
    print("Vehicle from DictReader:", vehicle_from_csv)


if __name__ == "__main__":
    main()
