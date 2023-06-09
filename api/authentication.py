from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status, Depends

from jose import JWTError, jwt
from passlib.context import CryptContext

from sqlalchemy.orm import Session


from api.schemas.token import TokenData
from api.settings import Settings

from fastapi.security import OAuth2PasswordBearer

from api.models.user import User

settings = Settings()


SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = Settings.token_expire
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/user/login")


# def get_password_hash(password):
#     return pwd_context.hash(password)

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)


async def authenticate_user(name: str, password: str, db) -> User:
    user = await User.get_name(name=name, db=db)
    if not user:
        return False
    # if not verify_password(password, user.password):
    #     return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#
#     user = get_user(username=token_data.username, db=db)
#     if user is None:
#         raise credentials_exception
#     return user

