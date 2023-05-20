from fastapi import APIRouter, Depends, HTTPException, status
from api.db import get_db
from sqlalchemy.orm import Session
from api.models.user import User
from api.schemas.user import UserSchema, UserCreate
from api.schemas.response import ResponseBase
from api.exceptions import ErrorAlterItemDB, NotExistItemBD
from api.authentication import get_password_hash, get_current_user, verify_privilege


router = APIRouter(prefix="/user", tags=["user"], responses={404: {"description": "Not found"}})


@router.get("", response_model=list[UserSchema])
async def get_all_users(db: Session = Depends(get_db), dependencies=Depends(verify_privilege)):
    users = await User.get_all(db=db)
    return users


@router.get("/id/{id_user}", response_model=UserSchema)
async def get_user_id(id_user: int, db: Session = Depends(get_db), dependencies=Depends(verify_privilege)):
    try:
        user = await User.get_id(db=db, id=id_user)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user


@router.get("/{name_user}", response_model=UserSchema)
async def get_user_name(name_user: str, db: Session = Depends(get_db), dependencies=Depends(verify_privilege)):
    try:
        user = await User.get_name(db=db, name=name_user)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user


@router.post("", response_model=UserSchema)
async def create_user(new_user: UserCreate, db: Session = Depends(get_db), dependencies=Depends(verify_privilege)):
    try:
        new_user.password = get_password_hash(new_user.password)
        user = await User.create(db=db, **new_user.dict())
    except ErrorAlterItemDB as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user


@router.delete("/{id_user}", response_model=ResponseBase)
async def delete_user(id_user: int, db: Session = Depends(get_db), dependencies=Depends(verify_privilege)):
    try:
        await User.remove_id(id=id_user, db=db)
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return ResponseBase(msg="User deleted")


@router.put("/{id_user}", response_model=UserSchema)
async def update_user(id_user: int, new_user: UserCreate, db: Session = Depends(get_db),
                      dependencies=Depends(verify_privilege)):
    try:
        user_updated = await User.update_id(db=db, id=id_user, data_change=new_user.dict())
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return user_updated


@router.get("/me", response_model=UserSchema)
async def get_user_me(current_user: User = Depends(get_current_user)):
    return current_user
