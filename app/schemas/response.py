from pydantic import BaseModel


class ResponseBase(BaseModel):
    msg: str