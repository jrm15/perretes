from fastapi import APIRouter, Depends, HTTPException, status
from api.db import get_db
from sqlalchemy.orm import Session
from api.models.treatment import Treatment
from api.schemas.treatment import TreatmentSchema, TreatmentCreate
from api.schemas.response import ResponseBase
from api.exceptions import ErrorAlterItemDB, NotExistItemBD
from api.authentication import verify_privilege

router = APIRouter(prefix="/treatment", tags=["treatment"], responses={404: {"description": "Not found"}})


@router.get("", response_model=list[TreatmentSchema])
async def get_all_treatments(db: Session = Depends(get_db),
                             dependencies=Depends(verify_privilege)):
    treatments = await Treatment.get_all(db=db)
    return treatments


@router.get("/{id_treatment}", response_model=TreatmentSchema)
async def get_treatment(id_treatment: int, db: Session = Depends(get_db),
                        dependencies=Depends(verify_privilege)):
    try:
        treatment = await Treatment.get_id(db=db, id=id_treatment)
    except NotExistItemBD as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return treatment


@router.post("", response_model=TreatmentSchema)
async def create_treatment(new_treatment: TreatmentCreate, db: Session = Depends(get_db),
                           dependencies=Depends(verify_privilege)):
    try:
        treatment = await Treatment.create(db=db, **new_treatment.dict())
    except ErrorAlterItemDB as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return treatment


@router.delete("/{id_treatment}", response_model=ResponseBase)
async def delete_treatment(id_treatment: int, db: Session = Depends(get_db),
                           dependencies=Depends(verify_privilege)):
    try:
        await Treatment.remove_id(id=id_treatment, db=db)
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return ResponseBase(msg="Service deleted")


@router.put("/{id_treatment}", response_model=TreatmentSchema)
async def update_treatment(id_treatment: int, new_treatment: TreatmentCreate, db: Session = Depends(get_db),
                           dependencies=Depends(verify_privilege)):
    try:
        treatment_updated = await Treatment.update_id(db=db, id=id_treatment, data_change=new_treatment.dict())
    except (ErrorAlterItemDB, NotExistItemBD) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return treatment_updated
