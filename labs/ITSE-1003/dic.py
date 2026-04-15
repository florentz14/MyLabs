# ------------------------------------------------------------ #
# File: dic.py
# Date: 2026-04-15
# Author: Florentino
# Description: DictWriter → CSV under data/; read back with DictReader.
# Explanation: It explains dictwriter → csv under data/; read back with dictreader and why it is useful in basic data analysis.
# ------------------------------------------------------------ #


from __future__ import annotations

import csv
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "data"

# Vehicle dictionary
vehicle_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "red",
    "price": 10000,
    "is_new": True,
    "is_used": False,
    "is_electric": False,
    "is_gasoline": True,
    "is_diesel": False,
    "is_hybrid": False,
}

# Country dictionary (values: country name or capital, as in the exercise)
country_dict = {
    "USA": "United States",
    "Canada": "Canada",
    "Mexico": "Mexico",
    "Brazil": "Brazil",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima",
    "Colombia": "Bogota",
    "Republica Dominicana": "Santo Domingo",
    "Ecuador": "Quito",
}


def write_vehicle_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(vehicle_dict.keys()))
        w.writeheader()
        w.writerow({k: str(v) if isinstance(v, bool) else v for k, v in vehicle_dict.items()})


def write_countries_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["country_key", "value"])
        for key, value in country_dict.items():
            w.writerow([key, value])


def read_vehicle_csv(path: Path) -> dict[str, object]:
    """One data row: first (and only) row from DictReader → dict."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row = next(reader)
    out: dict[str, object] = {}
    for key, raw in row.items():
        if key is None:
            continue
        if key in ("year", "price"):
            out[key] = int(raw)
        elif key.startswith("is_"):
            out[key] = raw == "True"
        else:
            out[key] = raw
    return out


def read_countries_csv(path: Path) -> dict[str, str]:
    """Each DictReader row → one entry country_key → value."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {r["country_key"]: r["value"] for r in reader}


def main() -> None:
    v_path = _DATA_DIR / "dic_vehicle.csv"
    c_path = _DATA_DIR / "dic_countries.csv"
    write_vehicle_csv(v_path)
    write_countries_csv(c_path)
    print("Wrote:", v_path)
    print("Wrote:", c_path)

    vehicle_from_csv = read_vehicle_csv(v_path)
    countries_from_csv = read_countries_csv(c_path)
    print("\nVehicle from DictReader:", vehicle_from_csv)
    print("Countries from DictReader:", countries_from_csv)


if __name__ == "__main__":
    main()
