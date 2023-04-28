from pydantic import BaseModel


class TreatmentBase(BaseModel):
    name: str
    duration: int


class TreatmentCreate(TreatmentBase):
    pass


class TreatmentSchema(TreatmentBase):
    id: int

    class Config:
        orm_mode = True
