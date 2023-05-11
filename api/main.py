from fastapi import FastAPI
from api.db import Base, engine
from api.routers import user, characteristic, treatment, booking
import os

app = FastAPI()

if os.getenv("MODE") != "TEST":
    Base.metadata.create_all(bind=engine)

for router in [user.router, characteristic.router, treatment.router, booking.router]:
    app.include_router(router)
