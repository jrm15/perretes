from sqlalchemy.orm import Session
from api.exceptions import NotExistItemBD, ErrorAlterItemDB
from sqlalchemy.orm.exc import UnmappedInstanceError


class CrudBase:
    @classmethod
    async def get_all(cls, db: Session):
        return db.query(cls).all()

    @classmethod
    async def create(cls, db: Session, **kwargs):
        try:
            db_data = cls(**kwargs)
            db.add(db_data)
        except UnmappedInstanceError:
            raise ErrorAlterItemDB(f"{cls.__name__} cant create this item")
        db.commit()
        db.refresh(db_data)
        return db_data

    @classmethod
    async def get_id(cls, db: Session, id: int):
        item = db.query(cls).filter(cls.id == id).first()
        if item:
            return item
        else:
            raise NotExistItemBD(f"{cls.__name__} not found")

    @classmethod
    async def remove_id(cls, db: Session, id: int):
        item = await cls.get_id(db=db, id=id)
        try:
            db.query(cls).filter(cls.id == item.id).delete()
        except UnmappedInstanceError:
            raise ErrorAlterItemDB(f"{cls.__name__} cant delete this item")
        db.commit()

    @classmethod
    async def update_id(cls, db: Session, id: int, data_change: dict):
        item = await cls.get_id(db=db, id=id)
        try:
            db.query(cls).filter(cls.id == item.id).update(values=data_change)
        except UnmappedInstanceError:
            raise ErrorAlterItemDB(f"{cls.__name__} cant update this item")
        db.commit()
        return await cls.get_id(db=db, id=id)
