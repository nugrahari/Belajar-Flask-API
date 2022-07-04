from uuid import UUID
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from pydantic import BaseModel

from . import libs
from . import models as users_models


class JWTBearer(HTTPBearer):
    pass


security = JWTBearer()


class UserJWT(BaseModel):
    id: int
    role: Optional[users_models.RoleEnum]


class AuthUser:
    def __init__(self, token: HTTPAuthorizationCredentials = Depends(security)):
        try:
            current_jwt = libs.jwt_decode(token.credentials)
            self.user = UserJWT(**current_jwt.get('user'))
        except jwt.exceptions.DecodeError as err:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Invalid authentication credentials") from err


class AuthAdmin(AuthUser):
    def __init__(self, token: HTTPAuthorizationCredentials = Depends(security)):
        super().__init__(token)

        if self.user.role != users_models.RoleEnum.administrator:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not administrator")
