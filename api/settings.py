import os
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    DB_HOST: str = None
    DB_USER: str = None
    DB_PASSWORD: str = None
    DB_PORT: str = None
    DB_NAME: str = None

app_settings = Settings()
