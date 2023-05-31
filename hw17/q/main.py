from fastapi import FastAPI, status, HTTPException, Body, Depends

from passlib.hash import pbkdf2_sha256
import uvicorn
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

posts = [
    {"id": 1, "title": "cheeze", "description": "cheeze descriptions"},
    {"id": 2, "title": "egg", "description": "egg descriptions"},
]
users = []

app = FastAPI()


# get for test
@app.get("/", tags=["greeting"])
def home():
    return {"message": "hello"}


# get posts
@app.get("/posts", tags=["post"])
def get_users():
    return {"all posts": posts}


# get post by id
@app.get("/posts/{id}", tags=["post"])
def get_user_by_id(id: int):
    post_lst = list(filter(lambda p: p["id"] == id, posts))
    if post_lst[0]:
        return {"post": post_lst[0]}
    else:
        raise {"message": "not found"}


# post add post
@app.post("/posts/add", dependencies=[Depends(jwtBearer())], tags=["post"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"message": "post added"}


# user add
@app.post("/users/signup", tags=["user"])
def user_signup(user: UserSchema):
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


@app.get("/users", tags=["user"])
def get_users():
    return {"users": users}


@app.get("/users/{id}", tags=["user"])
def get_user_by_id(id: int):
    user_lst = next((u for u in users if u["id"] == id), None)
    if user_lst[0]:
        return {"user": user_lst[0]}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.post("/users/login", tags=["user"])
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


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, host="127.0.0.1")
