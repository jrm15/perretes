from sqlalchemy import Column, Integer, String
from app.db import Base
from app.models.crud_base import CrudBase


class User(Base, CrudBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(60))
