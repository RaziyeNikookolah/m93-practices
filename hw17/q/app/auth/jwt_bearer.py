# check the whether the request is authorized or not [verification of the protected request
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt_handler import decodeJwT


class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            jwtBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403,
                    detail="Invalid authentication scheme.",
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )

            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Envalid authorization code.")

    def verify_jwt(self, jwttoken: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = decodeJwT(jwttoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
