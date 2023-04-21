from sqlalchemy import Column, Integer, String
from app.db import Base


class User(Base):
    __tablename__ = "site"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(60))
