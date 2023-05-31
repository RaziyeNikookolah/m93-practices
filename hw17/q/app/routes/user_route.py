from fastapi import APIRouter, HTTPException, status, Body
from app.models.user_model import UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.data_storage import users
from passlib.hash import pbkdf2_sha256

# router for user endpoints
router = APIRouter(prefix="/users", tags=["user"])


# user add
@router.post("/")
def add_user(user: UserSchema):
    found_user = next((u for u in users if u["email"] == user.email), None)

    if found_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User exist with this email"
        )
    else:
        user.id = len(users) + 1
        user.password = pbkdf2_sha256.hash(user.password)
        users.append(user.dict())
        token = signJWT(user.email)
        return {"token": token["access token"], "message": "user added"}


@router.get("/")
def get_users():
    return {"users": users}


@router.get("/{id}")
def get_user_by_id(id: int):
    user_found = next((u for u in users if u["id"] == id), None)
    if user_found:
        return {"user": user_found}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/login")
def user_login(
    user: UserLoginSchema = Body(default=None),
):  # i think Body(default=None) is for set default value for object recieved
    found_user = next((u for u in users if u["email"] == user.email), None)

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username"
        )
    else:
        if not pbkdf2_sha256.verify(user.password, found_user["password"]):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
            )
        else:
            token = signJWT(user.email)
            return {"token": token["access token"], "message": "user logged in"}
