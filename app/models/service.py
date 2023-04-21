from sqlalchemy import Column, Integer, String
from app.db import Base


class Service(Base):
    __tablename__ = "site"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    duration = Column(Integer)

    # id_characteristics = Column(Integer, ForeignKey("characteristics.id"))
    # bookings = Relationship("Booking", back_populates="service")
