from sqlalchemy import Column, Integer, String, DATETIME
from app.db import Base


class Booking(Base):
    __tablename__ = "site"

    id = Column(Integer, primary_key=True)
    name_dog = Column(String(100))
    telephone = Column(Integer)
    breed = Column(String(100))
    age = Column(Integer)
    observations = Column(String(100))
    date = Column(DATETIME)

    # id_service = Column(Integer, ForeignKey("service.id"))
