from app.config.db.base_class import Base
from sqlalchemy import Integer, String, Column


class Movie(Base):
    id = Column(Integer, primary_key=True)
    movie_name = Column(String, nullable=False)

