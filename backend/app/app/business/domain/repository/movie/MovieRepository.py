from sqlalchemy import Session
from typing import Any
from fastapi import Depends

class MovieRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def save(self, movie) -> Any:
        pass

