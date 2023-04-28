import enum
from sqlalchemy import Column, Integer, Boolean, Enum
from app.db import Base
from app.models.crud_base import CrudBase


class EnumSize(enum.Enum):
    pequeño = 1
    mediano = 2
    grande = 3


class EnumHair(enum.Enum):
    corto = 1
    largo = 2


class Characteristics(Base, CrudBase):
    __tablename__ = "characteristics"

    id = Column(Integer, primary_key=True)
    size = Column(Enum(EnumSize))
    hair = Column(Enum(EnumHair))
    behaviour = Column(Boolean)
    senior = Column(Boolean)

    # treatments = Relationship("Treatment", back_populates="characteristics")
