from typing import Any
from sqlalchemy import Column, Integer, String  # type: ignore

from project.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)

    def __init__(self, username: str, email: str, *args: Any, **kwargs: Any) -> None:
        self.username = username
        self.email = email
