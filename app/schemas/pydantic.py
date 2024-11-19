from pydantic import BaseModel, Field
from enum import Enum


class Movie(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=10, max_length=400)
    rating: float = Field(gt=1, lt=10)
    release_date: str
    poster: str

