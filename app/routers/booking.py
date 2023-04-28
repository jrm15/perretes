from fastapi import APIRouter, Depends, HTTPException, status
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.schemas.booking import BookingSchema, BookingCreate
from app.schemas.response import ResponseBase
from app.exceptions import ErrorAlterItemDB, NotExistItemBD


router = APIRouter(prefix="/booking", tags=["booking"], responses={404: {"description": "Not found"}})


@router.get("", response_model=list[BookingSchema])
async def get_all_characteristics(db: Session = Depends(get_db)):
    bookings = await Booking.get_all(db=db)
    return bookings


@router.get("/{id_booking}", response_model=BookingSchema)
async def get_characteristics(id_booking: int, db: Session = Depends(get_db)):
    try:
        bookings = await Booking.get_id(id=id_booking, db=db)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return bookings


@router.post("", response_model=BookingSchema)
async def create_characteristics(new_booking: BookingCreate, db: Session = Depends(get_db)):
    try:
        booking = await Booking.create(db=db, **new_booking.dict())
    except ErrorAlterItemDB as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return booking


@router.delete("/{id_booking}", response_model=ResponseBase)
async def delete_characteristics(id_booking: int, db: Session = Depends(get_db)):
    try:
        await Booking.remove_id(db=db, id=id_booking)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return ResponseBase(msg="Characteristics deleted")


@router.put("{/id_booking}", response_model=BookingSchema)
async def update_characteristics(id_booking: int, new_booking: BookingCreate, db: Session = Depends(get_db)):
    try:
        update_booking = await Booking.update_id(db=db, id=id_booking, data_change=new_booking.dict())
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return update_booking
