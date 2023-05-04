from sqlalchemy import Column, Integer, String
from app.db import Base
from app.models.crud_base import CrudBase
from sqlalchemy.orm import Session
from app.exceptions import NotExistItemBD


class User(Base, CrudBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(60))

    @classmethod
    async def get_name(cls, db: Session, name: str):
        item = db.query(cls).filter(cls.name == name).first()
        if item:
            return item
        else:
            raise NotExistItemBD(f"{cls.__name__} not found")

