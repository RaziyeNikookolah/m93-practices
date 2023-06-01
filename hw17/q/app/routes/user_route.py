from fastapi import APIRouter, HTTPException, status, Body
from app.models.user_model import UserSchema, UserLoginSchema, UserRole
from app.auth.jwt_handler import signJWT

# from passlib.context import CryptContext
from app.data_storage import users
from passlib.hash import pbkdf2_sha256

# router for user endpoints
router = APIRouter(prefix="/users", tags=["user"])
# mycontext = CryptContext(schemes=["sha256_crypt", "md5_crypt"])


# user add
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_user(user: UserSchema):
    if user.username in users.keys():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User exist with this username"
        )
    else:
        user.password = pbkdf2_sha256.hash(user.password)
        # user.password=mycontext.hash(user.password)
        users[user.username] = user
        # token = signJWT(user.username)
        # return {"token": token["access token"], "message": "user added"}
        return {"message": "user added"}


@router.get("/")
def get_users():
    return {"users": users}


@router.get("/{username}")
def get_user_by_username(username):
    user = users.get(username)

    if user:
        return {"user": user}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/admin/{username}")
def make_user_admin(username: str, user_new: UserSchema):
    user_old = users.get(username)
    if not user_old:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        user_new.role = UserRole.ADMIN
        users[user_new.username] = user_new
        return {"message": "User set as an admin"}


@router.put("/{username}")
def update_user(username: str, user_new: UserSchema):
    user_old = users.get(username)
    if not user_old:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        users[user_new.username] = user_new

        return {"message": "User updated"}


@router.delete("/{username}")
def delete_user(username: str):
    user = users.get(username)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        users.pop(username)
        return {"message": "user deleted"}


@router.post("/login")
def user_login(
    user: UserLoginSchema = Body(default=None),
):
    found_user = users.get(user.username)

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not existed.."
        )
    else:
        if not pbkdf2_sha256.verify(user.password, found_user.password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
            )
        else:
            token = signJWT(user.username)
            return {"token": token["access token"], "message": "user logged in"}
