from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
