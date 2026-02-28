from datetime import datetime
from datetime import timedelta
from typing import Annotated

import bcrypt
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.controller import UserController
from app.models.schemas import User
from app.settings import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Auth:
    @staticmethod
    async def get_password_hashed(password: str) -> str:
        password_bytes = password.encode("utf-8")
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    async def authenticate_user(email: str, password: str) -> User | None:
        user = await UserController.get_user(email=email)
        if not user:
            return None
        try:
            is_valid = bcrypt.checkpw(password.encode("utf-8"),
                                      user.password.encode("utf-8"))

            if is_valid:
                return user
            return None
        except Exception:
            return None

    @staticmethod
    async def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expiration = Settings.JWT_EXPIRY
        expiry_time = datetime.now() + timedelta(expiration)
        to_encode.update({"exp": expiry_time.timestamp()})

        encoded_jwt = jwt.encode(to_encode,
                                 Settings.JWT_KEY,
                                 algorithm=Settings.JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def get_user(token: Annotated[str, Depends(oauth2_scheme)]
                       ) -> User | None:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session has been expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, Settings.JWT_KEY,
                                 algorithms=[Settings.JWT_ALGORITHM])
            email = payload.get("sub")
            expiration = payload.get("exp")

            if email is None:
                raise credentials_exception

            if (expiration is None
                    or datetime.now().timestamp() > expiration):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )

        except Exception:
            raise credentials_exception
        user = await UserController.get_user(email=email)
        if user is None:
            raise credentials_exception
        return user
