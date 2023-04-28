from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    password: str


class UserCreate(UserBase):
    pass


class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
