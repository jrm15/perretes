from fastapi import APIRouter, Depends, HTTPException, status
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.characteristics import Characteristics
from app.schemas.characteristics import CharacteristicSchema, CharacteristicCreate
from app.schemas.response import ResponseBase
from app.exceptions import ErrorAlterItemDB, NotExistItemBD


router = APIRouter(prefix="/characteristics", tags=["characteristics"], responses={404: {"description": "Not found"}})


@router.get("", response_model=list[CharacteristicSchema])
async def get_all_characteristics(db: Session = Depends(get_db)):
    users = await Characteristics.get_all(db=db)
    return users


@router.get("/{id}", response_model=CharacteristicSchema)
async def get_characteristics(id: int, db: Session = Depends(get_db)):
    try:
        characteristics = await Characteristics.get_id(id=id, db=db)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return characteristics


@router.post("", response_model=CharacteristicSchema)
async def create_characteristics(new_item: CharacteristicCreate, db: Session = Depends(get_db)):
    try:
        characteristics = await Characteristics.create(db=db, **new_item.dict())
    except ErrorAlterItemDB as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return characteristics


@router.delete("/{id}", response_model=ResponseBase)
async def delete_characteristics(id: int, db: Session = Depends(get_db)):
    try:
        await Characteristics.remove_id(db=db, id=id)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return ResponseBase(msg="Characteristics deleted")


@router.put("{/id}", response_model=CharacteristicSchema)
async def update_characteristics(id: int, new_item: CharacteristicCreate, db: Session = Depends(get_db)):
    try:
        update_data = await Characteristics.update_id(db=db, id=id, data_change=new_item.dict())
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return update_data
