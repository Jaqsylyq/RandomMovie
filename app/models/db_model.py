from sqlalchemy import Column
from sqlalchemy.orm import DeclarativeBase

class Model(DeclarativeBase):
    pass

class Movie(Model):
    __tablename__ = "movies"

    id: int = Column(primary_key=True)
    title: str = Column(nullable=False)
    description: str = Column(nullable=False)
    rating: float = Column(nullable=False)
    release_date: str = Column(nullable=False)
    poster: str = Column(nullable=False)
