from sqlalchemy import Column, Integer, String, DateTime
from api.db import Base
from api.models.crud_base import CrudBase


class Booking(Base, CrudBase):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    name_dog = Column(String(100))
    telephone = Column(Integer)
    breed = Column(String(100))
    age = Column(Integer)
    observations = Column(String(100))
    date = Column(DateTime)

    # id_treatment = Column(Integer, ForeignKey("treatment.id"))
