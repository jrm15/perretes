from pydantic import BaseModel
from datetime import datetime


class BookingBase(BaseModel):
    name_dog: str
    breed: str
    telephone: int
    age: int
    observations: str
    date: datetime
    # id_treatment = Column(Integer, ForeignKey("treatment.id"))
    # treatments = Relationship("Treatments", back_populates="booking")


class BookingCreate(BookingBase):
    pass


class BookingSchema(BookingBase):
    id: int

    class Config:
        orm_mode = True
