# ------------------------------------------------------------ #
# File: models_music.py
# Date: 2026-04-19
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Pydantic v2 models for the music database (Artist for now; Genre/Album to follow).
# Explanation: Mirrors the `artists` table from music_database.py with validation (non-empty name, year range, trimmed strings) so application code can validate input before touching SQLite.
# ------------------------------------------------------------ #
# Requires: pip install pydantic

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Artist(BaseModel):
    """A music artist or band."""

    model_config = ConfigDict(
        str_strip_whitespace=True,  # trim leading/trailing whitespace on str fields
        extra="forbid",             # reject unknown fields when parsing
        from_attributes=True,       # allow Artist.model_validate(orm_or_row_obj)
        validate_assignment=True,   # re-validate on attribute set
    )

    id: Optional[int] = Field(
        default=None,
        ge=1,
        description="Primary key assigned by SQLite; None for new (unsaved) instances.",
    )
    name: Annotated[str, Field(min_length=1, max_length=200)]
    country: Optional[Annotated[str, Field(max_length=100)]] = None
    formed_year: Optional[Annotated[int, Field(ge=1800, le=2100)]] = None
    bio: Optional[str] = None
    created_at: Optional[datetime] = None

    @field_validator("name")
    @classmethod
    def _name_not_blank(cls, v: str) -> str:
        # Pydantic strips whitespace before validators run (per model_config),
        # so an all-whitespace input arrives empty and triggers min_length=1.
        if not v:
            raise ValueError("name must not be blank")
        return v

    @field_validator("country")
    @classmethod
    def _country_not_blank(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v:
            return None
        return v

    def to_db_row(self) -> tuple[str, Optional[str], Optional[int], Optional[str]]:
        """Tuple in the order expected by `INSERT INTO artists (name, country, formed_year, bio)`."""
        return (self.name, self.country, self.formed_year, self.bio)


__all__ = ["Artist"]


if __name__ == "__main__":
    sample = Artist(
        name="  Daft Punk  ",
        country="France",
        formed_year=1993,
        bio="French electronic music duo.",
    )
    print("Validated artist:")
    print(sample.model_dump_json(indent=2))
    print("DB row tuple:", sample.to_db_row())
