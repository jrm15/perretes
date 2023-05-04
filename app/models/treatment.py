from sqlalchemy import Column, Integer, String
from app.db import Base
from app.models.crud_base import CrudBase


class Treatment(Base, CrudBase):
    __tablename__ = "treatment"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    duration = Column(Integer)

    # id_characteristic = Column(Integer, ForeignKey("characteristic.id"))
