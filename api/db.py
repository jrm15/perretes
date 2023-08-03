from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from api.settings import app_settings

Base = declarative_base()

if app_settings.DB_HOST:
    SQLALCHEMY_DATABASE_URL = URL.create("cockroachdb", username=app_settings.DB_USER,
                                         password=app_settings.DB_PASSWORD, host=app_settings.DB_HOST,
                                         port=app_settings.DB_PORT, database=app_settings.DB_NAME,
                                         query={"sslmode": "disable"})
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
