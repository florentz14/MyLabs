from pathlib import Path
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm import DeclarativeBase, sessionmaker

BASE_DIR = Path(__file__).resolve().parent
# Always load project .env (not cwd-dependent)
load_dotenv(BASE_DIR / ".env")


def _resolve_sqlite_url_if_relative(url: str, base: Path) -> str:
    """SQLite file URLs relative to cwd become absolute under ``base`` (project root)."""
    parsed = make_url(url)
    if parsed.drivername != "sqlite":
        return url
    db = parsed.database
    if not db or db == ":memory:":
        return url
    path = Path(db)
    if path.is_absolute():
        return url
    resolved = (base / path).resolve()
    return f"sqlite:///{resolved}"


_raw_url = os.getenv("SQLALCHEMY_DATABASE_URL")
if not _raw_url or not _raw_url.strip():
    raise RuntimeError(
        "SQLALCHEMY_DATABASE_URL is not set. Add it to .env or the environment."
    )

SQLALCHEMY_DATABASE_URL = _resolve_sqlite_url_if_relative(_raw_url.strip(), BASE_DIR)

_engine_kwargs = {}
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    _engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(SQLALCHEMY_DATABASE_URL, **_engine_kwargs)

# SQLAlchemy 2.x: omit autocommit (deprecated on Session; use explicit transactions)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
