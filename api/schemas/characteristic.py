from pydantic import BaseModel
from api.models.characteristic import EnumSize, EnumHair


class CharacteristicBase(BaseModel):
    size: EnumSize
    hair: EnumHair
    behaviour: bool
    senior: bool


class CharacteristicCreate(CharacteristicBase):
    pass


class CharacteristicSchema(CharacteristicBase):
    id: int

    class Config:
        orm_mode = True
