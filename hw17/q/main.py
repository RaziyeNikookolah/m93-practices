# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}


from fastapi import FastAPI
from app.routes.user_route import router as user_router
from app.routes.post_route import router as post_router
import uvicorn


app = FastAPI()
app.include_router(user_router)
app.include_router(post_router)


# get for test
@app.get("/", tags=["greeting"])
def home():
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, host="127.0.0.1")


# print("Adding an Item:")
# import requests

# print(requests.get("").json())
