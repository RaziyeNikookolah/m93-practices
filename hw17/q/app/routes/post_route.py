from fastapi import APIRouter, Depends, status, HTTPException, Header
from ..models.post_model import PostSchema
from ..auth.jwt_bearer import jwtBearer
from ..data_storage import posts
from typing import List, Dict, Optional

# router for post endpoints
router = APIRouter(prefix="/posts", tags=["post"])


# get posts
@router.get("/")  # , response_model=Dict[str : List[PostSchema]])
def get_posts():
    return {"all posts": list(posts.values())}


# get post by id
@router.get("/{title}")  # , response_model=Dict[str:PostSchema])
def get_post_by_title(title: str):
    post = posts.get(title)

    if not post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="not found")
    else:
        return {"post": post}


@router.post("/getHeader")
def get_header(custom_header: Optional[List[str]] = Header(None)):
    print(custom_header)
    return {"header": custom_header}


# post add post
@router.post(
    "/", status_code=status.HTTP_201_CREATED, dependencies=[Depends(jwtBearer())]
)
def add_post(post: PostSchema):
    if post.title in posts:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, message="Post already exists"
        )
    else:
        posts[post.title] = post
        return {"message": "post added"}


@router.put("/{title}", dependencies=[Depends(jwtBearer())])
def update_post(title: str, post_new: PostSchema):
    post_old = posts.get(title)

    if not post_old:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, message="not found"
        )
    else:
        posts[post_new.title] = post_new

    return {"message": "post updated"}


@router.delete("/{title}", dependencies=[Depends(jwtBearer())])
def delete_post(title: str):
    post = posts.get(title)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, message="not found"
        )
    else:
        posts.pop(title)
        return {"message": "post deleted"}
