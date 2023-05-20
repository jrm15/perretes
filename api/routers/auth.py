from fastapi import APIRouter, Depends, HTTPException, status
from api.db import get_db
from sqlalchemy.orm import Session
from api import authentication
from fastapi.security import OAuth2PasswordRequestForm
from api.schemas.token import Token

router = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not found"}})


@router.post("", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await authentication.authenticate_user(name=form_data.username, password=form_data.password, db=db)
    if user:
        token = authentication.create_access_token(data={"sub": str(user.id)})
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or password incorrect")
    return Token(access_token=str(token), token_type="bearer")