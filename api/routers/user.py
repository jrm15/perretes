from fastapi import APIRouter, Depends, HTTPException, status
from api.db import get_db
from sqlalchemy.orm import Session
from api.models.user import User
from api.schemas.user import UserSchema, UserCreate
from api.schemas.response import ResponseBase
from api.exceptions import ErrorAlterItemDB, NotExistItemBD
from api import authentication
from fastapi.security import OAuth2PasswordRequestForm
from api.schemas.token import Token
from datetime import timedelta


router = APIRouter(prefix="/user", tags=["user"], responses={404: {"description": "Not found"}})

ACCESS_TOKEN_EXPIRE_MINUTES = 1440

@router.get("", response_model=list[UserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    users = await User.get_all(db=db)
    return users


@router.get("/id/{id_user}", response_model=UserSchema)
async def get_user_id(id_user: int, db: Session = Depends(get_db)):
    try:
        user = await User.get_id(db=db, id=id_user)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user


@router.get("/{name_user}", response_model=UserSchema)
async def get_user_name(name_user: str, db: Session = Depends(get_db)):
    try:
        user = await User.get_name(db=db, name=name_user)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user


@router.post("", response_model=UserSchema)
async def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = await User.create(db=db, **new_user.dict())
    except ErrorAlterItemDB as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    user = await authentication.authenticate_user(name=form_data.username, password=form_data.password, db=db)
    token = authentication.create_access_token(data={"sub": user.name}, expires_delta=access_token_expires)
    return Token(access_token=str(token), token_type="bearer")


@router.delete("/{id_user}", response_model=ResponseBase)
async def delete_user(id_user: int, db: Session = Depends(get_db)):
    try:
        await User.remove_id(id=id_user, db=db)
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return ResponseBase(msg="User deleted")


@router.put("/{id_user}", response_model=UserSchema)
async def update_user(id_user: int, new_user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_updated = await User.update_id(db=db, id=id_user, data_change=new_user.dict())
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user_updated

