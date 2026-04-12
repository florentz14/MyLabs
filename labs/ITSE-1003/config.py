# Path helpers for labs/ITSE-1003 only (anchored to this file's directory).

from pathlib import Path

# labs/ITSE-1003
ITSE_ROOT = Path(__file__).resolve().parent
DATA_DIR = ITSE_ROOT / "data"
GENERATED_DIR = ITSE_ROOT / "generated"


def data_file(name: str) -> Path:
    """CSV or other file under this course's data/ folder."""
    return DATA_DIR / name
