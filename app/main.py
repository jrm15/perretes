from fastapi import FastAPI
from app.db import Base, engine
from app.routers import user, characteristics, treatment, booking
import os

app = FastAPI()

if os.getenv("MODE") != "TEST":
    Base.metadata.create_all(bind=engine)

for router in [user.router, characteristics.router, treatment.router, booking.router]:
    app.include_router(router)
