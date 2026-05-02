"""
Misma tabla `people` que sqlalchemy_people.py, pero contra PostgreSQL.

Requiere un driver: `pip install psycopg[binary]` (recomendado) o `psycopg2-binary`.

Variables de entorno (opcionales, valores por defecto para desarrollo local):
  PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DATABASE
  O bien DATABASE_URL completa, por ejemplo:
  postgresql+psycopg://user:pass@localhost:5432/mydatabase
"""
from __future__ import annotations

import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.engine import URL

if os.environ.get("DATABASE_URL"):
    engine = create_engine(os.environ["DATABASE_URL"], echo=True)
else:
    url = URL.create(
        "postgresql+psycopg",
        username=os.environ.get("PG_USER", "postgres"),
        password=os.environ.get("PG_PASSWORD", "postgres"),
        host=os.environ.get("PG_HOST", "localhost"),
        port=int(os.environ.get("PG_PORT", "5432")),
        database=os.environ.get("PG_DATABASE", "mydatabase"),
    )
    engine = create_engine(url, echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", Integer),
)

meta.create_all(engine)
