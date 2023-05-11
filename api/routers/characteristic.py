from fastapi import APIRouter, Depends, HTTPException, status
from api.db import get_db
from sqlalchemy.orm import Session
from api.models.characteristic import Characteristic
from api.schemas.characteristic import CharacteristicSchema, CharacteristicCreate
from api.schemas.response import ResponseBase
from api.exceptions import ErrorAlterItemDB, NotExistItemBD


router = APIRouter(prefix="/characteristic", tags=["characteristic"], responses={404: {"description": "Not found"}})


@router.get("", response_model=list[CharacteristicSchema])
async def get_all_characteristics(db: Session = Depends(get_db)):
    characteristics = await Characteristic.get_all(db=db)
    return characteristics


@router.get("/{id}", response_model=CharacteristicSchema)
async def get_characteristics(id: int, db: Session = Depends(get_db)):
    try:
        characteristic = await Characteristic.get_id(id=id, db=db)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return characteristic


@router.post("", response_model=CharacteristicSchema)
async def create_characteristics(new_item: CharacteristicCreate, db: Session = Depends(get_db)):
    try:
        characteristic = await Characteristic.create(db=db, **new_item.dict())
    except ErrorAlterItemDB as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return characteristic


@router.delete("/{id}", response_model=ResponseBase)
async def delete_characteristics(id: int, db: Session = Depends(get_db)):
    try:
        await Characteristic.remove_id(db=db, id=id)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return ResponseBase(msg="Characteristic deleted")


@router.put("/{id}", response_model=CharacteristicSchema)
async def update_characteristics(id: int, new_item: CharacteristicCreate, db: Session = Depends(get_db)):
    try:
        update_data = await Characteristic.update_id(db=db, id=id, data_change=new_item.dict())
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return update_data
