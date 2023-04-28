from fastapi import APIRouter, Depends, HTTPException, status
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserSchema, UserCreate
from app.schemas.response import ResponseBase
from app.exceptions import ErrorAlterItemDB, NotExistItemBD


router = APIRouter(prefix="/user", tags=["user"], responses={404: {"description": "Not found"}})


@router.get("", response_model=list[UserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    users = await User.get_all(db=db)
    return users


@router.get("/{id_user}", response_model=UserSchema)
async def get_user(id_user: int, db: Session = Depends(get_db)):
    try:
        user = await User.get_id(db=db, id=id_user)
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
